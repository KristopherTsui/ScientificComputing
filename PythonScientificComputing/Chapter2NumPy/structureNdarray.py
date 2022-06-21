import numpy as np

# create dtype object
persontype = np.dtype({
    'names': ['name', 'age', 'weight'],
    'formats': ['S30', 'i', 'f']    # 30 bytes string, int, float
}, align=True)

# create array of structures
a = np.array([("Zhang", 32, 75.5), ("Wang", 24, 65.2)], dtype=persontype)
print(a)

# save a to binary file
a.tofile("a.bin")

# read data a from binary file a.bin
b = np.fromfile("a.bin", dtype=persontype)
print(b)