import numpy as np
from matplotlib import pyplot as plt
from matplotlib import transforms


fig, ax = plt.subplots()
x = np.arange(0, 2, 0.01)
y = np.sin(2 * np.pi * x)

N = 7   # the number of shadow
for i in range(N, 0, -1):
    offset = transforms.ScaledTranslation(i, -i, transforms.IdentityTransform())
    shadow_trans = plt.gca().transData + offset
    ax.plot(x, y, linewidth=4, color="black",
            transform=shadow_trans, alpha=(N - i) / 2.0 / N)

ax.plot(x, y, linewidth=4, color="black")
ax.set_ylim(-1.5, 1.5)
plt.show()