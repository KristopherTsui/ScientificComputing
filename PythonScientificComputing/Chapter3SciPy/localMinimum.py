import numpy as np
from scipy import optimize as opt
from matplotlib import pyplot as plt


def target_function(x, y):
    return (1 - x)**2 + 100 * (y - x**2)**2


class TargetFunction(object):
    def __init__(self):
        self.f_points = []
        self.fprime_points = []
        self.fhess_points = []

    def f(self, p):
        x, y = p.tolist()
        z = target_function(x, y)
        self.f_points.append((x, y))
        return z

    def fprime(self, p):
        x, y = p.tolist()
        self.fprime_points.append((x, y))
        dx = -2 + 2 * x - 400 * x * (y - x**2)
        dy = 200 * y - 200 * x**2
        return np.array([dx, dy])

    def fhess(self, p):
        x, y = p.tolist()
        self.fhess_points.append((x, y))
        return np.array([
            [2 * (600 * x**2 - 200 * y + 1), -400 * x],
            [-400 * x, 200]
        ])

    
def fmin_demo(method):
    target = TargetFunction()
    init_point = (-1, -1)
    res = opt.minimize(target.f, init_point, method=method,
                        jac=target.fprime, hess=target.fhess)
    return res, [np.array(points) for points in (target.f_points, target.fprime_points, target.fhess_points)]


methods = ("Nelder-Mead", "Powell", "CG", "BFGS", "Newton-CG", "L-BFGS-B")
for method in methods:
    res, (f_points, fprime_points, fhess_points) = fmin_demo(method)
    print(f'{method:12s}: min={float(res["fun"]):12g}, f count={len(f_points):3d}, fprime count={len(fprime_points):3d}, fhess count={len(fhess_points):3d}')