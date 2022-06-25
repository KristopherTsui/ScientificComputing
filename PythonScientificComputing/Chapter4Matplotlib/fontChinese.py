import numpy as np
from matplotlib import pyplot as plt
from matplotlib.font_manager import FontProperties


font = FontProperties(fname="C:\\windows\\fonts\\simsun.ttc", size=14)
t = np.linspace(0, 10, 1000)
y = np.sin(t)
plt.close("all")
plt.plot(t, y)
plt.xlabel(u"时间", fontproperties="simsun", fontsize=22)
plt.ylabel(u"振幅", fontproperties=font)
plt.title(u"正弦波", fontproperties="simhei", fontsize=22)
plt.show()