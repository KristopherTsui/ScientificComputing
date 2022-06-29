import numpy as np
from matplotlib import pyplot as plt
from scipy import optimize


SIZE = 100
rng = np.random.default_rng(12345)
x_data = rng.uniform(-3.0, 3.0, size=SIZE)
noise = rng.normal(0.0, 0.8, size=SIZE)
y_data = 2.0*x_data**2 - 4*x_data + noise

fig, ax = plt.subplots()
ax.scatter(x_data, y_data)
ax.set(xlabel="x", ylabel="y", title="Scatter plot of sample data")


def func(x, a, b, c):
    return a*x**2 + b*x + c


coeffs, _ = optimize.curve_fit(func, x_data, y_data)
print(coeffs)

x = np.linspace(-3.0, 3.0, SIZE)
y = func(x, coeffs[0], coeffs[1], coeffs[2])
ax.plot(x, y, "k--")
plt.show()