import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


rng = np.random.default_rng(12345)
uniform = rng.uniform(1, 5, size=100)
normal = rng.normal(1, 2.5, size=100)
bimodal = np.concatenate([rng.normal(0, 1, size=50), rng.normal(6, 1, size=50)])
df = pd.DataFrame({
    "uniform": uniform,
    "normal": normal,
    "bimodal": bimodal
})

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, tight_layout=True)
df["uniform"].plot(kind="hist", title="Uniform", ax=ax1)
df["normal"].plot(kind="hist", title="Normal", ax=ax2)
df["bimodal"].plot(kind="hist", title="Bimodal", ax=ax3, bins=20)

# the `describe` method creates a new DataFrame
descriptive = df.describe()
descriptive.loc["kurtosis"] = df.kurtosis()
print(descriptive)

# add vertical lines to the histograms to illustrate the value of the mean
uniform_mean = descriptive.loc["mean", "uniform"]
normal_mean = descriptive.loc["mean", "normal"]
bimodal_mean = descriptive.loc["mean", "bimodal"]
ax1.vlines(uniform_mean, 0, 20)
ax2.vlines(normal_mean, 0, 25)
ax3.vlines(bimodal_mean, 0, 12)
plt.show()