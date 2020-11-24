import matplotlib.pyplot as plt
import numpy as np
import string

# points a, b and c
a, b, c, d = (0,0,0), (0,1,1), (1,1,1), (1,0,1)

# matrix with row vectors of points
A = np.array([a, b, c, d])
theta = np.pi/5
cs = np.cos(theta)
ss = np.sin(theta)
sh = 2
tx = 3
ty = 5 
I = np.eye(3)
T_s = np.array([[2,0,0], [0,2,0], [0,0,1]])
T_r = np.array([[cs,ss,0], [-ss,cs,0], [0,0,1]])
T_tl = np.array([[1,0,tx], [0,1,ty], [0,0,1]])
T_shh = np.array([[1,sh,0], [0,1,0], [0,0,1]])
T_shv = np.array([[1,0,0], [sh,1,0], [0,0,1]])

color_lut = 'rgbc'
fig = plt.figure()
ax = plt.gca()
xs = []
ys = []
xs_s = []
ys_s = []

ci = 0
for row in A:
    output_row = T_r @ row
    print(output_row)
    x, y, i = row
    x_s, y_s, i_s = output_row
    xs_s.append(x_s)
    ys_s.append(y_s)
    xs.append(x)
    ys.append(y)
    i, i_s = int(i), int(i_s)
    c, c_s = color_lut[i], color_lut[i_s]
    plt.scatter(x, y, color = c)
    plt.scatter(x_s, y_s, color = c_s)
    plt.text(x+0.15, y, f"{string.ascii_letters[int(i_s)]}")
    plt.text(x_s+0.15, y_s, f"{string.ascii_letters[int(i_s)]}")
    ci+=1

xs.append(xs[0])
ys.append(ys[0])
xs_s.append(xs_s[0])
ys_s.append(ys_s[0])

plt.plot(xs, ys, color = "gray", linestyle = "dotted")
ax.set_xticks(np.arange(-2.5, 3, 0.5))
ax.set_yticks(np.arange(-2.5, 3, 0.5))
plt.grid()
plt.show()