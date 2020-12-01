import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import string
import turtle as t

# 3D figure 
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d') # Axe3D object
xrange=[-15, 15]
yrange=[-15, 15]
zrange=[-30, 10]
ax.set_xlim(xrange)
ax.set_ylim(yrange)
ax.set_zlim(zrange)

# head
a1, a2, a3, a4, a5 = (0,0,7), (3,0,7), (3,3,7), (0,3,7), (0,0,7)
b1, b2, b3, b4, b5 = (0,0,2), (3,0,2), (3,3,2), (0,3,2), (0,0,2)
c1, c2, c3, c4, c5 = (0,0,2), (3,0,2), (3,0,7), (0,0,7), (0,0,2)
d1, d2, d3, d4, d5 = (0,3,2), (3,3,2), (3,3,7), (0,3,7), (0,3,2)

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

ax.plot(A[:,0], A[:,1], A[:,2], color='k', alpha=0.6)
ax.plot(B[:,0], B[:,1], B[:,2], color='k', alpha=0.6)
ax.plot(C[:,0], C[:,1], C[:,2], color='k', alpha=0.6)
ax.plot(D[:,0], D[:,1], D[:,2], color='k', alpha=0.6)
print(A[:,0])
print(A[:,1])
print(A[:,2])

#neck
a1, a2, a3, a4, a5 = (1,1,2), (2,1,2), (2,2,2), (1,2,2), (1,1,2)
b1, b2, b3, b4, b5 = (1,1,-1), (2,1,-1), (2,2,-1), (1,2,-1), (1,1,-1)
c1, c2, c3, c4, c5 = (1,1,-1), (2,1,-1), (2,1,2), (1,1,2), (1,1,-1)
d1, d2, d3, d4, d5 = (1,2,-1), (2,2,-1), (2,2,2), (1,2,2), (1,2,-1)

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

ax.plot(A[:,0], A[:,1], A[:,2], color='k', alpha=0.6)
ax.plot(B[:,0], B[:,1], B[:,2], color='k', alpha=0.6)
ax.plot(C[:,0], C[:,1], C[:,2], color='k', alpha=0.6)
ax.plot(D[:,0], D[:,1], D[:,2], color='k', alpha=0.6)

#body
a1, a2, a3, a4, a5 = (-2,-3,-1), (5,-3,-1), (5,6,-1), (-2,6,-1), (-2,-3,-1)
b1, b2, b3, b4, b5 = (-2,-3,-13), (5,-3,-13), (5,6,-13), (-2,6,-13), (-2,-3,-13)
c1, c2, c3, c4, c5 = (-2,-3,-13), (5,-3,-13), (5,-3,-1), (-2,-3,-1), (-2,-3,-13)
d1, d2, d3, d4, d5 = (-2,6,-13), (5,6,-13), (5,6,-1), (-2,6,-1), (-2,6,-13)

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

ax.plot(A[:,0], A[:,1], A[:,2], color='k', alpha=0.6)
ax.plot(B[:,0], B[:,1], B[:,2], color='k', alpha=0.6)
ax.plot(C[:,0], C[:,1], C[:,2], color='k', alpha=0.6)
ax.plot(D[:,0], D[:,1], D[:,2], color='k', alpha=0.6)

#left leg
a1, a2, a3, a4, a5 = (0.5,-1.5,-13), (2.5,-1.5,-13), (2.5,0.5,-13), (0.5,0.5,-13), (0.5,-1.5,-13)
b1, b2, b3, b4, b5 = (0.5,-1.5,-28), (2.5,-1.5,-28), (2.5,0.5,-28), (0.5,0.5,-28), (0.5,-1.5,-28)
c1, c2, c3, c4, c5 = (0.5,-1.5,-28), (2.5,-1.5,-28), (2.5,-1.5,-13), (0.5,-1.5,-13), (0.5,-1.5,-28)
d1, d2, d3, d4, d5 = (0.5,0.5,-28), (2.5,0.5,-28), (2.5,0.5,-13), (0.5,0.5,-13), (0.5,0.5,-28)

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

ax.plot(A[:,0], A[:,1], A[:,2], color='k', alpha=0.6)
ax.plot(B[:,0], B[:,1], B[:,2], color='k', alpha=0.6)
ax.plot(C[:,0], C[:,1], C[:,2], color='k', alpha=0.6)
ax.plot(D[:,0], D[:,1], D[:,2], color='k', alpha=0.6)

#right leg
a1, a2, a3, a4, a5 = (0.5,2.5,-13), (2.5,2.5,-13), (2.5,4.5,-13), (0.5,4.5,-13), (0.5,2.5,-13)
b1, b2, b3, b4, b5 = (0.5,2.5,-28), (2.5,2.5,-28), (2.5,4.5,-28), (0.5,4.5,-28), (0.5,2.5,-28)
c1, c2, c3, c4, c5 = (0.5,2.5,-28), (2.5,2.5,-28), (2.5,2.5,-13), (0.5,2.5,-13), (0.5,2.5,-28)
d1, d2, d3, d4, d5 = (0.5,4.5,-28), (2.5,4.5,-28), (2.5,4.5,-13), (0.5,4.5,-13), (0.5,4.5,-28)

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

ax.plot(A[:,0], A[:,1], A[:,2], color='k', alpha=0.6)
ax.plot(B[:,0], B[:,1], B[:,2], color='k', alpha=0.6)
ax.plot(C[:,0], C[:,1], C[:,2], color='k', alpha=0.6)
ax.plot(D[:,0], D[:,1], D[:,2], color='k', alpha=0.6)

#left foot
a1, a2, a3, a4, a5 = (0.5,-1.5,-28), (4,-1.5,-28), (4,0.5,-28), (0.5,0.5,-28), (0.5,-1.5,-28)
b1, b2, b3, b4, b5 = (0.5,-1.5,-30), (4,-1.5,-30), (4,0.5,-30), (0.5,0.5,-30), (0.5,-1.5,-30)
c1, c2, c3, c4, c5 = (0.5,-1.5,-30), (4,-1.5,-30), (4,-1.5,-28), (0.5,-1.5,-28), (0.5,-1.5,-30)
d1, d2, d3, d4, d5 = (0.5,0.5,-30), (4,0.5,-30), (4,0.5,-28), (0.5,0.5,-28), (0.5,0.5,-30)

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

ax.plot(A[:,0], A[:,1], A[:,2], color='k', alpha=0.6)
ax.plot(B[:,0], B[:,1], B[:,2], color='k', alpha=0.6)
ax.plot(C[:,0], C[:,1], C[:,2], color='k', alpha=0.6)
ax.plot(D[:,0], D[:,1], D[:,2], color='k', alpha=0.6)

#right foot
a1, a2, a3, a4, a5 = (0.5,2.5,-28), (4,2.5,-28), (4,4.5,-28), (0.5,4.5,-28), (0.5,2.5,-28)
b1, b2, b3, b4, b5 = (0.5,2.5,-30), (4,2.5,-30), (4,4.5,-30), (0.5,4.5,-30), (0.5,2.5,-30)
c1, c2, c3, c4, c5 = (0.5,2.5,-30), (4,2.5,-30), (4,2.5,-28), (0.5,2.5,-28), (0.5,2.5,-30)
d1, d2, d3, d4, d5 = (0.5,4.5,-30), (4,4.5,-30), (4,4.5,-28), (0.5,4.5,-28), (0.5,4.5,-30)

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

ax.plot(A[:,0], A[:,1], A[:,2], color='k', alpha=0.6)
ax.plot(B[:,0], B[:,1], B[:,2], color='k', alpha=0.6)
ax.plot(C[:,0], C[:,1], C[:,2], color='k', alpha=0.6)
ax.plot(D[:,0], D[:,1], D[:,2], color='k', alpha=0.6)

#left arm
a1, a2, a3, a4, a5 = (0.5,-5,-5), (2.5,-5,-5), (2.5,-3,-5), (0.5,-3,-5), (0.5,-5,-5)
b1, b2, b3, b4, b5 = (0.5,-5,-18), (2.5,-5,-18), (2.5,-3,-18), (0.5,-3,-18), (0.5,-5,-18)
c1, c2, c3, c4, c5 = (0.5,-5,-18), (2.5,-5,-18), (2.5,-5,-5), (0.5,-5,-5), (0.5,-5,-18)
d1, d2, d3, d4, d5 = (0.5,-3,-18), (2.5,-3,-18), (2.5,-3,-5), (0.5,-3,-5), (0.5,-3,-18)

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

ax.plot(A[:,0], A[:,1], A[:,2], color='k', alpha=0.6)
ax.plot(B[:,0], B[:,1], B[:,2], color='k', alpha=0.6)
ax.plot(C[:,0], C[:,1], C[:,2], color='k', alpha=0.6)
ax.plot(D[:,0], D[:,1], D[:,2], color='k', alpha=0.6)

#rigth arm
a1, a2, a3, a4, a5 = (0.5,6,-5), (2.5,6,-5), (2.5,8,-5), (0.5,8,-5), (0.5,6,-5)
b1, b2, b3, b4, b5 = (0.5,6,-18), (2.5,6,-18), (2.5,8,-18), (0.5,8,-18), (0.5,6,-18)
c1, c2, c3, c4, c5 = (0.5,6,-18), (2.5,6,-18), (2.5,6,-5), (0.5,6,-5), (0.5,6,-18)
d1, d2, d3, d4, d5 = (0.5,8,-18), (2.5,8,-18), (2.5,8,-5), (0.5,8,-5), (0.5,8,-18)

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

ax.plot(A[:,0], A[:,1], A[:,2], color='k', alpha=0.6)
ax.plot(B[:,0], B[:,1], B[:,2], color='k', alpha=0.6)
ax.plot(C[:,0], C[:,1], C[:,2], color='k', alpha=0.6)
ax.plot(D[:,0], D[:,1], D[:,2], color='k', alpha=0.6)

#bar1
a1, a2, a3, a4, a5 = (-4,1,-6), (-2,1,-6), (-2,2,-6), (-4,2,-6), (-4,1,-6)
b1, b2, b3, b4, b5 = (-4,1,-7), (-2,1,-7), (-2,2,-7), (-4,2,-7), (-4,1,-7)
c1, c2, c3, c4, c5 = (-4,1,-7), (-2,1,-7), (-2,1,-6), (-4,1,-6), (-4,1,-7)
d1, d2, d3, d4, d5 = (-4,2,-7), (-2,2,-7), (-2,2,-6), (-4,2,-6), (-4,2,-7)

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

ax.plot(A[:,0], A[:,1], A[:,2], color='k', alpha=0.6)
ax.plot(B[:,0], B[:,1], B[:,2], color='k', alpha=0.6)
ax.plot(C[:,0], C[:,1], C[:,2], color='k', alpha=0.6)
ax.plot(D[:,0], D[:,1], D[:,2], color='k', alpha=0.6)

#bar2
a1, a2, a3, a4, a5 = (-5,-2,-6), (-4,-2,-6), (-4,5,-6), (-5,5,-6), (-5,-2,-6)
b1, b2, b3, b4, b5 = (-5,-2,-7), (-4,-2,-7), (-4,5,-7), (-5,5,-7), (-5,-2,-7)
c1, c2, c3, c4, c5 = (-5,-2,-7), (-4,-2,-7), (-4,-2,-6), (-5,-2,-6), (-5,-2,-7)
d1, d2, d3, d4, d5 = (-5,5,-7), (-4,5,-7), (-4,5,-6), (-5,5,-6), (-5,5,-7)

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

ax.plot(A[:,0], A[:,1], A[:,2], color='k', alpha=0.6)
ax.plot(B[:,0], B[:,1], B[:,2], color='k', alpha=0.6)
ax.plot(C[:,0], C[:,1], C[:,2], color='k', alpha=0.6)
ax.plot(D[:,0], D[:,1], D[:,2], color='k', alpha=0.6)

#bar3
a1, a2, a3, a4, a5 = (-5,1,-3), (-4,1,-3), (-4,2,-3), (-5,2,-3), (-5,1,-3)
b1, b2, b3, b4, b5 = (-5,1,-10), (-4,1,-10), (-4,2,-10), (-5,2,-10), (-5,1,-10)
c1, c2, c3, c4, c5 = (-5,1,-10), (-4,1,-10), (-4,1,-3), (-5,1,-3), (-5,1,-10)
d1, d2, d3, d4, d5 = (-5,2,-10), (-4,2,-10), (-4,2,-3), (-5,2,-3), (-5,2,-10)

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

ax.plot(A[:,0], A[:,1], A[:,2], color='k', alpha=0.6)
ax.plot(B[:,0], B[:,1], B[:,2], color='k', alpha=0.6)
ax.plot(C[:,0], C[:,1], C[:,2], color='k', alpha=0.6)
ax.plot(D[:,0], D[:,1], D[:,2], color='k', alpha=0.6)


plt.show()