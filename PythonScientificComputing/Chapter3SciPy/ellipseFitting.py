import numpy as np
from scipy import linalg
from matplotlib import pyplot as plt


def f(x, y, p):
    """
    General Equation of Ellipse.
    """
    a, b, c, d, e, f = p
    return a * x**2 + b * x * y + c * y**2 + d * x + e * y + f


np.random.seed(42)
t = np.random.uniform(0, 2 * np.pi, 60)
a, b, alpha = 0.5, 1.0, 0.4
x = 1.0 + a * np.cos(t) * np.cos(alpha) - b * np.sin(t) * np.sin(alpha)
y = 1.0 + a * np.cos(t) * np.sin(alpha) - b * np.sin(t) * np.cos(alpha)
x += np.random.normal(0, 0.05, size=len(x))
y += np.random.normal(0, 0.05, size=len(y))

D = np.c_[x**2, x * y, y**2, x, y, np.ones_like(x)]
A = np.dot(D.T, D)
C = np.zeros((6, 6))
eigvals, eigvecs = linalg.eig(A, C)
eigvecs = np.real(eigvecs)
err = np.mean(np.dot(D, eigvecs)**2, 0)
p = eigvecs[:, np.argmin(err)]
print(p)

X, Y = np.mgrid[0:2:500j, 0:2:500j]
Z = f(X, Y, p)
fig = plt.figure()
plt.plot(x, y, 'ro')
plt.contour(X, Y, Z, 0)
plt.xlim(0, 2)
plt.ylim(0, 2)
plt.show()