import numpy as np
from matplotlib import pyplot as plt


x = np.linspace(-1, 1, 10)
y = x**2

fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(x, y)

for i, (_x, _y) in enumerate(zip(x, y)):
    ax.text(_x, _y, str(i), color="red", fontsize=i+10)
    
ax.text(0.5, 0.8, u"子图坐标系中的文字", color="blue", ha="center", transform=ax.transAxes, fontproperties="simhei")
plt.figtext(0.1, 0.92, u"图表坐标系中的文字", color="green", fontproperties="simhei")

plt.show()