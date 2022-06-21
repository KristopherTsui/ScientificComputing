import numpy as np
import time

def triangle_wave(x: float, c: float, c0: float, hc: float) -> float:
    # The period of the triangle wave is 1,
    # so only the fractional part of the x coordinate is taken for calculation
    x = x - int(x)
    if x >= c:
        r = 0.0
    elif x < c0:
        r = x / c0 * hc
    else:
        r = (c - x) / (c - c0) * hc
    return r


def triangle_wave_where(x: np.ndarray, c: float, c0: float, hc: float) -> np.ndarray:
    x = x - x.astype(int)
    return np.where(x >= c, 0, np.where(x < c0, x / c0 * hc, (c - x) / (c - c0 * hc)))


def triangle_wave_select(x: np.ndarray, c: float, c0: float, hc: float) -> np.ndarray:
    x = x - x.astype(int)
    return np.select(condlist=[x >= c, x < c0, True],
                    choicelist=[0, x / c0 * hc, (c - x) / (c - c0) * hc])
    # An array of candidate values by the default parameter
    # when none of the conditions specified value are met 
    # return np.select([x >= c, x < c0], [0, x/ c0 * hc], default=(c - x) / (c - c0) * hc)


def triangle_wave_piecewise(x: np.ndarray, c: float, c0: float, hc: float) -> np.ndarray:
    x = x - x.astype(int)
    return np.piecewise(x, condlist=[x >= c, x < c0], funclist=[
        0,                                  # x >= c
        lambda x: x / c0 * hc,              # x < c0
        lambda x: (c - x) / (c - c0) * hc   # else
    ])


# convert a function that calculates a single value
# into a ufunc function that calculates each element of the array
# by frompyfunc()
triangle_ufunc1 = np.frompyfunc(triangle_wave, 4, 1)
# vectorize() can achieve similar functions as frompyfunc()
triangle_ufunc2 = np.vectorize(triangle_wave, otypes=[float])

x = np.linspace(0, 2, 1000000)
start = time.process_time()
y1 = np.array([triangle_wave(t, 0.6, 0.4, 1.0) for t in x])
print("The total time of iteration is ", time.process_time() - start)
start = time.process_time()
y2 = triangle_ufunc1(x, 0.6, 0.4, 1.0)
print("The total time of frompyfunc is ", time.process_time() - start)
start = time.process_time()
y3 = triangle_ufunc2(x, 0.6, 0.4, 1.0)
print("The total time of vectorize is ", time.process_time() - start)
start = time.process_time()
y4 = triangle_wave_where(x, 0.6, 0.4, 1.0)
print("The total time of where is ", time.process_time() - start)
start = time.process_time()
y5 = triangle_wave_select(x, 0.6, 0.4, 1.0)
print("The total time of select is ", time.process_time() - start)
start = time.process_time()
y6 = triangle_wave_piecewise(x, 0.6, 0.4, 1.0)
print("The total time of piecewise is ", time.process_time() - start)