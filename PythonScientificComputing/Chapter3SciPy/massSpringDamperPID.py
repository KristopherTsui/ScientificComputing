import numpy as np
from scipy import integrate
from scipy import optimize as opt
from matplotlib import pyplot as plt


class MassSpringDamper(object):

    def __init__(self, m, k, b, F) -> None:
        self.m, self.k, self.b, self.F = m, k, b, F

    def f(self, t, xu):
        x, u = xu.tolist()
        dx = u
        du = (self.F - self.k * x - self.b * u ) / self.m
        return [dx, du]


class PID(object):

    def __init__(self, kp, ki, kd, dt):
        self.kp, self.ki, self.kd, self.dt = kp, ki, kd, dt
        self.last_error = None
        self.status = 0.0

    def update(self, error):
        p = self.kp * error
        i = self.ki * self.status
        if self.last_error is None:
            d = 0.0
        else:
            d = self.kd * (error - self.last_error) / self.dt
        self.status += error * self.dt
        self.last_error = error
        return p + i + d


def pid_control_system(kp, ki, kd, dt, target=1.0):
    m, b, k = 1.0, 10.0, 20.0
    system = MassSpringDamper(m=m, k=k, b=b, F=0.0)
    pid = PID(kp, ki, kd, dt)
    init_status = 0.0, 0.0

    r = integrate.ode(system.f)
    r.set_integrator('vode', method='bdf')
    r.set_initial_value(init_status, 0)

    t = [0]
    result = [init_status]
    F_arr = [0]

    while r.successful() and r.t + dt < 2.0:
        r.integrate(r.t + dt)
        err = target - r.y[0]
        F = pid.update(err)
        system.F = F
        t.append(r.t)
        result.append(r.y)
        F_arr.append(F)
    
    result = np.array(result)
    t = np.array(t)
    F_arr = np.array(F_arr)
    return t, F_arr, result


def eval_func(k):
    kp, ki, kd = k
    _, _, result = pid_control_system(kp, ki, kd, 0.01)
    return np.sum(np.abs(result[:, 0] - 1.0))


if __name__ == '__main__':
    t, F_arr, result = pid_control_system(50.0, 100.0, 10.0, 0.001)
    print("Final value of contral force:", F_arr[-1])

    kwargs = {
        "method": "L-BFGS-B",   # "Powell" or "Nelder-Mead"
        "bounds": [(10.0, 200.0), (10.0, 100.0), (1.0, 100.0)],
    }
    opt_k = opt.basinhopping(eval_func, (10.0, 10.0, 10.0),
                            niter=10, minimizer_kwargs=kwargs)
    print(opt_k.x)
    kp, ki, kd = opt_k.x
    t, F_arr, result = pid_control_system(kp, ki, kd, 0.01)
    idx = np.argmin(np.abs(t - 0.5))
    x, u = result[idx]
    print(f"t={t[idx]}, x={x:g}, u={u:g}")

    fig = plt.figure()
    ax1, ax2, ax3 = fig.subplots(3, 1)
    ax1.plot(t, result[:, 0], label="Displacement")
    ax1.set_xlim(0, 2)
    ax1.legend()
    ax2.plot(t, result[:, 1], label="Velocity")
    ax2.set_xlim(0, 2)
    ax2.legend()
    ax3.plot(t, F_arr, label="Control Force")
    ax3.set_xlim(0, 2)
    ax3.legend()
    plt.show()