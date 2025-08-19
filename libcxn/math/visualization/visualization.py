# -*- coding: utf-8 -*-
# Copyright (c) 2025 Bugra Coskun
# License: GPLv3
# [ libcxn.math.visualization]
import matplotlib.pyplot as plt

def scatter3d(X, Y, Z, xlabel="X", ylabel="Y", zlabel="Z=f(X,Y)",
              title="3D Scatter of Z",
              filename="figure.png",
              def_az=45, def_el=30, def_size=(8,8), def_dpi=150):

    fig = plt.figure(figsize=def_size, dpi=def_dpi)
    ax = fig.add_subplot(111, projection="3d")
    ax.view_init(elev=def_el, azim=def_az)
    sc = ax.scatter(X, Y, Z, c=Z, cmap="viridis", s=10)

    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_zlabel(zlabel)
    ax.set_title(title)

    fig.colorbar(sc, ax=ax, shrink=0.6, label=zlabel)
    fig.savefig(filename, dpi=def_dpi, bbox_inches="tight")
    plt.show()
