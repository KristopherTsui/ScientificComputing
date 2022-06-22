import pandas as pd
import numpy as np


def transform_function(row):
    if row["four"]:
        return 0.5 * row["two"]
    return row["one"] * row["two"]


rng = np.random.default_rng(12345)
three = rng.uniform(-0.2, 1.0, size=100)
three[three < 0] = np.nan

data_frame = pd.DataFrame({
    "one": rng.random(size=100),
    "two": np.add.accumulate(rng.normal(0, 1, size=100)),
    "three": three
})
data_frame["four"] = data_frame["one"] > 0.5
# use the `axis=1` keyword argument to apply the function to each row
data_frame["five"] = data_frame.apply(transform_function, axis=1)
print(data_frame)

# filter out the rows in the DataFrame that contain a Not a Number(NaN) value
df = data_frame.dropna()
print(df)