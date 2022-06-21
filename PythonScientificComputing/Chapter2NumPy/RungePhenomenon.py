import numpy as np
from numpy import polynomial as npp
import matplotlib.pyplot as plt


def f(x):
    return 1 / (1 + 25 * x**2)


n = 11
# Take n sampling points equidistantly on the [-1,1] interval
x1 = np.linspace(-1, 1, n)
# Use the roots of the nth-order Chebyshev polynomial as sampling points
x2 = npp.Chebyshev.basis(n).roots()

xd = np.linspace(-1, 1, 200)
# Polynomial interpolation of f(x) using two sample points separately
c1 = npp.Chebyshev.fit(x1, f(x1), n - 1, domain=[-1, 1])
c2 = npp.Chebyshev.fit(x2, f(x2), n - 1, domain=[-1, 1])

print("Maximum error of interpolating polynomial:")
print("Equidistant sampling points:", abs(c1(xd) - f(xd)).max())
print("Chebyshev points:", abs(c2(xd) - f(xd)).max())


fig = plt.figure()
ax1, ax2 = fig.subplots(1, 2)

ax1.plot(xd, f(xd), 'b--', label=r"$f(x)$")
ax1.scatter(x1, f(x1), color='red', label="Interpolation points")
ax1.plot(xd, c1(xd), color='purple', label="interpolating Polynomials")
ax1.set_xlim(-1, 1)
ax1.set_ylim(-0.5, 2)

ax2.plot(xd, f(xd), 'b--')
ax2.scatter(x2, f(x2), color='red')
ax2.plot(xd, c2(xd), color='purple')
ax2.set_xlim(-1, 1)
ax2.set_ylim(-0.2, 1.0)

fig.legend(loc='upper center')
plt.show()
plt.savefig("Runge.pdf")