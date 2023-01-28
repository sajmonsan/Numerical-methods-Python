import numpy as np
import matplotlib.pyplot as plt


def f(t, y):
    return np.sin(t*y**2)+np.cos(t*y**2)


def rk4(f, t0, y0, h, n):
    t = np.zeros(n+1)
    y = np.zeros(n+1)
    t[0] = t0
    y[0] = y0
    for i in range(n):
        k1 = h*f(t[i], y[i])
        k2 = h*f(t[i] + h/2, y[i] + k1/2)
        k3 = h*f(t[i] + h/2, y[i] + k2/2)
        k4 = h*f(t[i] + h, y[i] + k3)
        y[i+1] = y[i] + (k1 + 2*k2 + 2*k3 + k4)/6
        t[i+1] = t[i] + h
    return t, y


t0 = 0
y0 = 1
h = 0.1
n = 1000000
t, y = rk4(f, t0, y0, h, n)
plt.plot(t, y)
plt.show()
