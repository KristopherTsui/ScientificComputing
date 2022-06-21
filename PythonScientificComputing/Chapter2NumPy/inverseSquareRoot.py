import numpy as np


def InvSqrt(number: np.ndarray) -> np.ndarray:
    y = number.astype(np.float32)
    x2 = y * 0.5
    i = y.view(np.int32)
    i[:] = 0x5f3759df - (i >> 1)
    y = y * (1.5 - x2 * y * y)
    return y


if __name__ == '__main__':
    number = np.linspace(0.1, 10, 100)
    y = InvSqrt(number)
    print(np.max(np.abs(1 / np.sqrt(number)) - y))