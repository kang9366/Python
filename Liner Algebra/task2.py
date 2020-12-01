import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import string
import turtle as t

# 3D figure 
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d') # Axe3D object
xrange=[-7, 7]
yrange=[-7, 7]
zrange=[-7, 7]
ax.set_xlim(xrange)
ax.set_ylim(yrange)
ax.set_zlim(zrange)

# points a, b and, c
a1, a2, a3, a4, a5 = (0,0,5), (2,0,5), (2,3,5), (0,3,5), (0,0,5)
b1, b2, b3, b4, b5 = (0,0,3), (2,0,3), (2,3,3), (0,3,3), (0,0,3)
c1, c2, c3, c4, c5 = (0,0,4), (2,0,4), (2,0,3), (0,0,3), (0,0,4)
d1, d2, d3, d4, d5 = (2,3,4), (0,3,4), (0,3,3), (2,3,3), (2,3,4)

# matrix with row vectors of points
A = np.array([a1, a2, a3, a4, a5])
Anew=np.zeros((A.shape[0],A.shape[1]+1))
AT=np.zeros((A.shape[0],A.shape[1]))
Ac=np.ones((1,A.shape[0]))
Anew[:,:-1]=A
Anew[:,-1]=Ac

B = np.array([b1, b2, b3, b4, b5])
Bnew=np.zeros((B.shape[0],B.shape[1]+1))
BT=np.zeros((B.shape[0],B.shape[1]))
Bc=np.ones((1,B.shape[0]))
Bnew[:,:-1]=B
Bnew[:,-1]=Bc

C = np.array([c1, c2, c3, c4, c5])
Cnew=np.zeros((C.shape[0],C.shape[1]+1))
CT=np.zeros((C.shape[0],C.shape[1]))
Cc=np.ones((1,C.shape[0]))
Cnew[:,:-1]=C
Cnew[:,-1]=Cc

D = np.array([d1, d2, d3, d4, d5])
Dnew=np.zeros((D.shape[0],D.shape[1]+1))
DT=np.zeros((D.shape[0],D.shape[1]))
Dc=np.ones((1,D.shape[0]))
Dnew[:,:-1]=D
Dnew[:,-1]=Dc

ax.plot(A[:,0], A[:,1], A[:,2], color='k', alpha=0.6, marker='o')
ax.plot(B[:,0], B[:,1], B[:,2], color='k', alpha=0.6, marker='o')
ax.plot(C[:,0], C[:,1], C[:,2], color='k', alpha=0.6, marker='o')
ax.plot(D[:,0], D[:,1], D[:,2], color='k', alpha=0.6, marker='o')
print(A[:,0])
print(A[:,1])
print(A[:,2])
plt.show()