import pandas as pd
import numpy as np


rng = np.random.default_rng(12345)
diffs = rng.normal(0, 1, size=100)
cumulative = np.add.accumulate(diffs)
data_frame = pd.DataFrame({
    "diffs": diffs,
    "cumulative": cumulative
})
print(data_frame)

# store the data in this DataFrame object into the `sample.csv` file
# use the `index=False` keyword argument
# so that the index is not stored in the CSV file
data_frame.to_csv("sample.csv", index=False)

# read the `sample.csv` file into a new DataFrame object
df = pd.read_csv("sample.csv", index_col=False)
print(df)