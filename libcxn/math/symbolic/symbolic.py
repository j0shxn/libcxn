import sympy as sp
from typing import Sequence, Union

class PrettyPrint:
    """Callable expressive and pretty printing class"""
    def __init__(self, is_active:bool=True):
        self.is_active = is_active

    def __call__(self, symvarname:str, symvar, desc:str=""):
        """
        Pretty-print a sympy variable with its name and type.

        Parameters
        ----------
        symvarname : str
            The name of the variable (for display).
        symvar : any
            The sympy object to pretty-print.
        desc : str
            Descriptor string.
        """
        if self.is_active:
            print("\n"+"-"*70)
            print(f"{symvarname}::{type(symvar)}")
            if desc !="": print(f"description:{desc}")
            sp.pprint(symvar)
            print("\n"+"-"*70)

def rodri(k:sp.Matrix,
          ang: Union[float, sp.Basic]) -> sp.Matrix:
    """
    Compute the Rodrigues rotation matrix for a given axis and angle.

    Parameters
    ----------
    k : sequence of float or sympy.Basic
        The axis vector (length 3).
    ang : float or sympy.Basic
        The rotation angle in radians.

    Returns
    -------
    sympy.Matrix
        The 3x3 rotation matrix.

    Example
    -------
    >>> k = [sp.Symbol('kx'), sp.Symbol('ky'), sp.Symbol('kz')]
    >>> ang = sp.Symbol('theta')
    >>> rodri(k, ang)
    Matrix([...])
    """
    K = sp.Matrix([
        [0,    -k[2],  k[1]],
        [k[2],  0,    -k[0]],
        [-k[1], k[0],   0 ]
    ])
    return sp.eye(3) + sp.sin(ang)*K + (1-sp.cos(ang))*K**2

def cartesian_to_azel(vec):
    """
    Convert cartesian coordinates to a AZEL vector.

    Parameters
    ---
    vec : sympy.Matrix or sequence

    Returns
    ---
    sympy.Matrix
        3D Cartesian vector
    """
    norm = sp.sqrt(vec.dot(vec))
    nvec = vec/norm
    az = -sp.atan2(vec[1], vec[0])
    el = sp.asin(vec[2])
    return sp.Matrix([az, el, norm])

def cartesian_to_spherical(vec):
    """
    Convert cartesian coordinates to a spherical vector.

    Parameters
    ---
    vec : sympy.Matrix or sequence

    Returns
    ---
    sympy.Matrix
        3D Cartesian vector
    """
    norm = sp.sqrt(vec.dot(vec))
    nvec = vec/norm
    az = sp.atan2(vec[1], vec[0])
    el = sp.asin(vec[2])
    return sp.Matrix([az, el, norm])

def spherical_to_cartesian(vec):
    """
    Convert spherical coordinates to a 3D Cartesian vector.

    Parameters
    ---
    vec : sympy.Matrix or sequence
        [azimuthal (rad), elevation (rad), radius]

    Returns
    ---
    sympy.Matrix
        3D Cartesian vector
    """
    cart = sp.Matrix([\
        vec[2]*sp.cos(vec[1])*sp.cos(vec[0]),
        vec[2]*sp.cos(vec[1])*sp.sin(vec[0]),
        vec[2]*sp.sin(vec[1])])
    return cart

