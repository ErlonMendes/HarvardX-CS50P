import math
import numpy as np  # Need numpy install
import matplotlib.pyplot as plt  # Need matplotlib install
from matplotlib import cm  # Need matplotlib install


def main():
    time = int(input("Simulation time [Enter for 1000]: ") or "1000")
    length = int(input("Bar length [Enter for 100]: ") or "100")
    alpha = int(input("Thermal diffusivity alpha [Enter for 1]: ") or "1")
    u0 = int(input("Initial temperature (°C) [Enter for 25]: ") or "25")
    ul = int(input("Left temperature (°C) [Enter for 100]: ") or "100")
    ur = int(input("Right temperature (°C) [Enter for 0]: ") or "0")
    nx = int(input("Number of nodes in the bar [Enter for 200]: ") or "200")
    t, x, deltat, deltax, nt = mesh_creation(nx, length, time, alpha)
    u = pde_solution(alpha, deltat, deltax, nt, nx, u0, ul, ur)
    plot_creation(t, x, u)


def mesh_creation(nx, length, time, alpha):
    deltax = length/nx
    deltat = 1/2*deltax**2/alpha  # positivity criterion
    nt = math.floor(time/deltat)
    t = np.linspace(0, time, nt)
    x = np.linspace(0, length, nx)
    t, x = np.meshgrid(t, x)
    return t, x, deltat, deltax, nt


def pde_solution(alpha, deltat, deltax, nt, nx, u0, ul, ur):
    rx = alpha * deltat / deltax ** 2
    u = np.empty([nx, nt])
    u[:, :] = u0
    u[0, :] = ul
    u[nx-1, :] = ur
    for n in range(nt - 1):
        for i in range(1, nx - 1):
            u[i, n + 1] = rx * (u[i + 1, n] + u[i - 1, n]) + (1 - 2 * rx) * u[i, n]
    return u


def plot_creation(t, x, u):
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    ax.plot_surface(t, x, u, cmap=cm.jet)
    ax.set(xlabel='time', ylabel='length', zlabel='temperature (°C)')
    ax.view_init(20, -140, 0)
    plt.show()


if __name__ == "__main__":
    main()
