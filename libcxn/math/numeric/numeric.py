# -*- coding: utf-8 -*-
# Copyright (c) 2025 Bugra Coskun
# License: GPLv3
# [ libcxn.math.numeric ]
import numpy as np

class Gaussian2DIsotropic:
    """
    2D isotropic Gaussian with peak value 1 at the mean.
    
    f(x, y) = exp(-((x - mu_x)^2 + (y - mu_y)^2) / (2*sigma^2))
    
    Parameters
    ----------
    mu : tuple of float
        (mu_x, mu_y) center of the Gaussian.
    sigma : float
        Standard deviation (spread) in both directions.
    """
    def __init__(self, mu=(0.0, 0.0), sigma=1.0):
        if sigma <= 0:
            raise ValueError("sigma must be positive.")
        self.mu_x, self.mu_y = mu
        self.sigma = float(sigma)
        self.inv_two_sigma2 = 1.0 / (2.0 * self.sigma**2)

    def __call__(self, x: float, y: float) -> float:
        dx = x - self.mu_x
        dy = y - self.mu_y
        r2 = dx*dx + dy*dy
        return np.exp(- r2 * self.inv_two_sigma2)

def auto_align(A:np.ndarray, B:np.ndarray, max_lag:int=200):
    """
    Aligns array `b` to array `a` by finding the lag 
    that minimizes their difference.

    Parameters:
    ---
    A (numpy.ndarray): Reference array (1D)
    B (numpy.ndarray): Target array (1D)
    max_lag (int): Maximum number of sample points shifted

    Returns:
    ---
    a_out (numpy.ndarray): best aligned array a
    b_out (numpy.ndarray): best aligned array b
    lag (int): number of samples shifted

    lag > 0: a is shifted up and b is shifted down
    lag < 0: a is shifted down and b is shifted up
    """

    n = min(len(A), len(B))
    a = A[:n]
    b = B[:n]

    MSE_min = 1e+100
    lag = 0
    lag0 = 0
    n = len(a)

    for lag0 in range(0,max_lag):

        c = a[lag0:] - b[:n-lag0] # slide a "up" and slide b "down"
        nc = a[:n-lag0] - b[lag0:] # slide b "up" and slide a "down"

        mse = np.mean(np.square(c)) # sum_i((c_i)^2)/n
        nmse = np.mean(np.square(nc)) # sum_i((c_i)^2)/n

        if mse < nmse: 
            MSE = mse
            lag1 = lag0

        else: 
            MSE = nmse
            lag1 = -lag0

        if MSE_min > MSE:
            MSE_min = MSE
            lag = lag1

    if lag > 0:
        a_out = a[lag:]
        b_out = b[:n-lag]

    else: # lag is negative
        a_out = a[:n+lag]
        b_out = b[-lag:]

    return a_out, b_out, lag 

def butterworth(data, cutoff=5, fs=100, order=4):
    nyq = 0.5 * fs
    norm_cutoff = cutoff / nyq
    b, a = butter(order, norm_cutoff, btype='low', analog=False)
    return filtfilt(b, a, data)
