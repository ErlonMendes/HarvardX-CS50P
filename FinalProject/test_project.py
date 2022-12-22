from project import mesh_creation, pde_solution, plot_creation
import numpy as np


def test_mesh():
    mesh_creation(200, 100, 1000, 1)
    assert True


def test_solution():
    pde_solution(1, 0.125, 0.5, 8000, 200, 25, 100, 0)
    assert True


def test_plot():
    t = np.linspace(0, 10, 50)
    x = np.linspace(0, 10, 50)
    t, x = np.meshgrid(t, x)
    u = np.zeros([50, 50])
    plot_creation(t, x, u)
    assert True

# Executar pytest test_project.py no Terminal
