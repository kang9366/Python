import numpy as np
import matplotlib.pyplot as plt

x1 = np.linspace(5, 10)
x2 = np.linspace(10, 20)
x3 = np.linspace(20, 25)

l1 = 0.5*(x1**2)
l2 = 0.05*(x2**3) - x2**2 + 15*x2 - 50
l3 = 0.0025*(x3**4) - 0.15*(x3**3) + 135*x3 - 1650

v1 = x1
v2 = 0.15*(x2**2) - 2*x2 +15
v3 = 0.01*(x3**3) - 0.45*(x3**2) + 135

a1 = x1/x1
a2 = 0.3*x2 - 2
a3 = 0.03*(x3**2) - 0.9*x3

def l(t):
    if 0<=t and t<=10:
        return 0.5*t*t
    elif 10<=t and t<=20:
        return 0.05*(t**3) - t**2 + 15*t - 50
    else:
        return 0.0025*(t**4) - 0.15*(t**3) + 135*t - 1650

def v(t):
    if 0<=t and t<=10:
        return t
    elif 10<=t and t<=20:
        return 0.15*(t**2) - 2*t +15
    else:
        return 0.01*(t**3) - 0.45*(t**2) + 135

def a(t):
    if 0<=t and t<=10:
        return t/t
    elif 10<=t and t<=20:
        return 0.3*t - 2
    else:
        return 0.03*(t**2) - 0.9*t

print("----------위치----------")
for i in np.arange(5, 25, 0.3):
    num = round(float(i), 1)
    print(l(num))

print("\n----------속도----------")
for i in np.arange(5, 25, 0.3):
    num = round(float(i), 1)
    print(v(num))

print("\n----------가속도----------")
for i in np.arange(5, 25, 0.3):
    num = round(float(i), 1)
    print(a(num))

plt.plot(x1, l1, 'g')
plt.plot(x2, l2, 'g')
plt.plot(x3, l3, 'g')

plt.plot(x1, v1, 'k')
plt.plot(x2, v2, 'k')
plt.plot(x3, v3, 'k')

plt.plot(x1, a1, 'r')
plt.plot(x2, a2, 'r')
plt.plot(x3, a3, 'r')

plt.show()