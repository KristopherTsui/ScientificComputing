import numpy as np
from matplotlib import pyplot as plt


levels = [4, 5, 3, 2]
x = np.linspace(0, 1, len(levels))

for i in range(len(levels) - 1):
    j = i + 1
    n1, n2 = levels[i], levels[j]
    y1, y2 = np.mgrid[0:1:n1*1j, 0:1:n2*1j]
    x1 = np.full_like(y1, x[i])
    x2 = np.full_like(y2, x[j])
    plt.quiver(x1, y1, x2 - x1, y2 - y1, angles="xy", units="dots", scale_units="xy", scale=1, width=1, headlength=10, headaxislength=10, headwidth=5)

yp = np.concatenate([np.linspace(0, 1, n) for n in levels])
xp = np.repeat(x, levels)
plt.plot(xp, yp, linestyle="none", marker="o", markersize=10)
plt.gca().axis("off")
plt.margins(0.1, 0.1)
plt.show()