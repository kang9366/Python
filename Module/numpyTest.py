import numpy as np
import matplotlib.pyplot as plt
import statistics

# x = np.linspace(1, 30, 30, endpoint=True)
# n = len(x)
# y = 2 + 3*x + np.random.normal(size=n, loc=0, scale=10)
# print(y)

# t = np.linspace(1, 20, 20, endpoint=True)
# print(t)

# print(np.arange(2, 10))

x = np.linspace(1, 30, 30, endpoint=True)
n = len(x)
y = 2+3*x + np.random.normal(size=n, loc = 0, scale=10)
mx = statistics.mean(x)
my = statistics.mean(y)
b1 = (sum(x*y) - n*mx*my) / (sum(x**2) - n*mx**2)
b0 = my - b1 * mx
yhat = b0 + b1 * x
b0 = round(b0, 3)
b1 = round(b1, 3)
print("회귀식은 : y = {0} + {1} x 입니다.".format(b0, b1))

plt.plot(x, y, '*')
plt.plot(x, yhat)
plt.xlim(-0.5, 30.5)
plt.show()