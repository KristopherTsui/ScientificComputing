import numpy as np
from matplotlib import pyplot as plt


def f(x, y):
    return x * np.exp(-x**2 - y**2)


def vec_field(f, x, y, dx=1e-6, dy=1e-6):
    x2 = x + dx
    y2 = y + dy
    v = f(x, y)
    vx = (f(x2, y) - v) / dx
    vy = (f(x, y2) - v) / dy
    return vx, vy


X, Y = np.mgrid[-2:2:20j, -2:2:20j]
C = f(X, Y)
U, V = vec_field(f, X, Y)

plt.quiver(X, Y, U, V, C)
plt.colorbar()
plt.gca().set_aspect("equal")
plt.show()