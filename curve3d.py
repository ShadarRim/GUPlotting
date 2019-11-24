import numpy as np
import matplotlib.pyplot as plt
import math
import pylab
from mpl_toolkits.mplot3d import Axes3D

def par_plane_draw(a = 1, b = 1, c = 1, d = 1):
    x = np.arange(-10, 10, 0.1)
    y = np.arange(-10, 10, 0.1)

    x_grid, y_grid = np.meshgrid(x, y)

    z_grid = (-d - a*x_grid - b*y_grid)/c

    z_grid2 = (-d+10 - a*x_grid - b*y_grid)/c

    fig = pylab.figure()
    axes = Axes3D(fig)

    axes.plot_surface(x_grid, y_grid, z_grid)
    axes.plot_surface(x_grid, y_grid, z_grid2)
    pylab.show()

def parab_draw(x_cent = 1, y_cent = 1, z_cent = 1, a = 1, b = 1):
    x = np.arange(-10, 10, 0.1)
    y = np.arange(-10, 10, 0.1)

    x_grid, y_grid = np.meshgrid(x, y)

    z_grid = (x_grid**2/a**2 + y_grid**2/ b**2)

    fig = pylab.figure()
    axes = Axes3D(fig)

    axes.plot_surface(x_grid, y_grid, z_grid)
    pylab.show()

def elipt_parab_draw(a = 1, b = 1):
    x = np.arange(-10, 10, 0.1)
    y = np.arange(-10, 10, 0.1)

    x_grid, y_grid = np.meshgrid(x, y)

    z_grid = (x_grid**2/a**2 + y_grid**2/ b**2)

    fig = pylab.figure()
    axes = Axes3D(fig)

    axes.plot_surface(x_grid, y_grid, z_grid)
    pylab.show()

def hypp_parab_draw(a = 1, b = 1):
    x = np.arange(-10, 10, 0.1)
    y = np.arange(-10, 10, 0.1)

    x_grid, y_grid = np.meshgrid(x, y)

    z_grid = (x_grid**2/a**2 - y_grid**2/ b**2)

    fig = pylab.figure()
    axes = Axes3D(fig)

    axes.plot_surface(x_grid, y_grid, z_grid)
    pylab.show()


if __name__ == "__main__":
    par_plane_draw()
    elipt_parab_draw()
    hypp_parab_draw()
