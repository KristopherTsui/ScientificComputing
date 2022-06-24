import numpy as np
from scipy import optimize as opt
from matplotlib import pyplot as plt


def func(x, p):
    """
    The function A * sin(2 * pi * k * x + theta) used to fit the data.
    """
    A, k, theta = p
    return A * np.sin(2 * np.pi * k * x + theta)


def residuals(p, y, x):
    """
    The difference between the experimental data x, y and the fitting function, 
    p is the coefficient to be found for the fitting
    """
    return y - func(x, p)


x = np.linspace(0, 2 * np.pi, 100)
A, k, theta = 10, 0.34, np.pi / 6   # function arguments for real data
y0 = func(x, [A, k, theta])         # real data
# Experimental data after adding noise
np.random.seed(0)
y1 = y0 + 2 * np.random.randn(len(x))

p0 = [7, 0.40, 0]                   # First guess function fit parameters

# Call leastsq for data fitting
# residuals is the function of calculating the error
# p0 is the initial value of the fitting parameter
# args is the experimental data to be fitted
plsq = opt.leastsq(residuals, p0, args=(y1, x))

print("Real Parameters:", [A, k, theta])
print("Fitting Parameters:", plsq[0])

plt.figure()
plt.plot(x, y1, "o", label="Experimental data with noise")
plt.plot(x, y0, label="Real data")
plt.plot(x, func(x, plsq[0]), label=u"Fitting data")
plt.xlim((0, 7))
plt.ylim((-15, 15))
plt.legend(loc="best")
plt.show()