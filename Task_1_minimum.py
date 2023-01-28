import numpy as np
from matplotlib import pyplot as plt
import numdifftools as ndt
from matplotlib.pyplot import cm

plt.close("all")


def f(x, y):
    return -(((x-2.0)**3.0)*np.cos(((3.0*(y-0.2))/2.0)-((x-0.1)/2.0))*(np.cos((3.0*(y-0.2)/2.0)+((x-0.1)/2.0)))*((y-2.0)**2.0))/25.0


xwpoczątowe = -4
xwkoncowe = 2
Nxw = 100
xw = np.linspace(xwpoczątowe, xwkoncowe, Nxw)

ywpoczatkowe = -4
ywkoncowe = 2
Nyw = 100
yw = np.linspace(ywpoczatkowe, ywkoncowe, Nyw)

XksoweW, YgrekoweW = np.meshgrid(xw, yw)

ZetoweW = f(XksoweW, YgrekoweW)


fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
c = ax1.contour(XksoweW, YgrekoweW, ZetoweW, 30,
                cmap=cm.spring, linewidths=0.5)
plt.clabel(c, fmt="%.2f")

ax1.set_xlabel("x")
ax1.set_ylabel("y")


xksowe = 1
ygrekowe = -1
krok = 1
fw = f(xksowe, ygrekowe)


def fw(punkt):
    return f(punkt[0], punkt[1])


punkt = np.array([xksowe, ygrekowe])
gra = ndt.Gradient(fw)
grd = gra(punkt)

i = 0
while (np.sqrt(grd[0]**2+grd[1]**2) > 1e-6):
    if (f(punkt[0], punkt[1]) < f(punkt[0]-krok*grd[0], punkt[1]-krok*grd[1])):
        krok = krok/2
        punkt = punkt - krok*grd
        grd = gra(punkt)
        i += 1
    else:
        punkt = punkt - krok*grd
        grd = gra(punkt)
        i += 1
    ax1.plot(punkt[0], punkt[1], '*k')
    plt.text(punkt[0], punkt[1], i)

ax1.plot(xksowe, ygrekowe, 'or')
plt.text(xksowe, ygrekowe, "({},{})".format(xksowe, ygrekowe), size=7)

print("Minimum lokalne funkcji znajduje się w punkcie ({},{}), znalezione mininum lokalne po wykonaniu {} kroków. Wartość funkcji f = {} znajduje się w punkcie ({},{}). Gradient wynosi: ({},{})".format(
    xksowe, ygrekowe, i, f(punkt[0], punkt[1]), punkt[0], punkt[0], grd[0], grd[1]))


fig1 = plt.figure()
ax0 = fig1.add_subplot(111, projection='3d', elev=10, azim=-45)
ax0.plot_surface(XksoweW, YgrekoweW, ZetoweW, cmap=cm.spring)
ax0.set_xlabel("x")
ax0.set_ylabel("y")
ax0.set_zlabel("z")

plt.show()
