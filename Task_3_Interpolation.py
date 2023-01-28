import numpy as np
import scipy as sp
from matplotlib import pyplot as plt
plt.close('all')


def f(x):
    return np.sin(x)


# Pierwsza część (punkty)
xksowep = -5
xksowek = 4
Nxksowe = 11

X = np.linspace(xksowep, xksowek, Nxksowe)
Y = np.zeros(Nxksowe)

for i in range(Nxksowe):
    Y[i] = f(X[i])

nxksowe = len(X)

x = sp.poly1d([0], r=True)

Lagrange = 0
for i in range(nxksowe):
    pom = 1
    for j in np.hstack((np.arange(i), np.arange(i+1, nxksowe))):
        pom *= (x-X[j])/(X[i] - X[j])
    Lagrange += pom*Y[i]

# Druga część (czebyszew)
xksowelp = -5
xksowelk = 4
Nlk = 30
xksowel = np.linspace(xksowelp, xksowelk, Nlk)
ygrekowel = Lagrange(xksowel)

a = -5
b = 4
Nc = 11
XC = np.zeros(Nc)
YC = np.zeros(Nc)
for i in range(Nc):
    XC[i] = (a+b)/2+(b-a)/2*np.cos((2*(i+1)-1)*np.pi/(2*Nc))
    YC[i] = f(XC[i])

nxksowec = len(XC)

xksowec = sp.poly1d([0], r=True)

Lagrangec = 0
for i in range(nxksowec):
    pom = 1
    for j in np.hstack((np.arange(i), np.arange(i+1, nxksowe))):
        pom *= (xksowec-XC[j])/(XC[i] - XC[j])
    Lagrangec += pom*YC[i]

# trzecia część (błedy)
xksowelpc = -5
xksowelkc = 4
Nlkc = 30
xksowelc = np.linspace(xksowelpc, xksowelkc, Nlkc)
ygrekowelc = Lagrangec(xksowelc)

ygrekowef = f(xksowel)
b = (ygrekowef-ygrekowel)/ygrekowef

ygrekowefc = f(xksowelc)
bc = (ygrekowefc-ygrekowelc)/ygrekowefc

# rysowanie wykresów
fig = plt.figure()
ax = fig.add_subplot(211)
ax.plot([-4, 4], [-4, 4], ',w')

ax.plot(X, Y, '.m', label="Punkty rozłożone równomierne", )
ax.plot(xksowel, ygrekowel, '-k')

ax2 = fig.add_subplot(212)
ax2.plot(XC, YC, '.m', label="Punkty Czebyszewa")
ax2.plot(xksowelc, ygrekowelc, '-k')

fig3 = plt.figure()
ax3 = fig3.add_subplot(211)
ax3.plot(xksowelc, bc, 'orange',
         label="Błędy wynikające z punktów rozłożonych równomiernie")

ax4 = fig3.add_subplot(212)
ax4.plot(xksowel, b, 'purple', label="Błędy wynikające z punktów Czebyszewa")


ax.set_ylim([-1.1, 1.1])
ax.legend(loc='lower right')
ax2.legend(loc='lower right')
ax3.legend(loc='upper right')
ax4.legend(loc='upper right')
plt.show()
