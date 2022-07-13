import numpy as np
import numpy.linalg as nl
import scipy as sc
import scipy.linalg as sl

import matplotlib.pyplot as plt
import seaborn as sns

T1 = 10
T2 = 20
T3 = 30
T4 = 40
n = 9

s = n*n
A = np.zeros((s, s))
B = np.zeros(s)

for i in range(s):
    if i == 0:
        A[i,i] = 4
        A[i, i+1] = -1
        A[i, i+n] = -1
        B[i] = T1 + T3
    elif i < n-1:
        A[i, i-1] = -1
        A[i, i] = 4
        A[i, i+1] = -1
        A[i, i+n] = -1
        B[i] = T3
    elif i == n-1:
        A[i, i] = 4
        A[i, i-1] = -1
        A[i, i+n] = -1
        B[i] = T2 + T3
    elif i == (s-n):
        A[i, i] = 4
        A[i, i+1] = -1
        A[i, i-n] = -1
        B[i] = T1 + T4
    elif (s-1) > i > s-n:
        A[i, i] = 4
        A[i, i-1] = -1
        A[i, i+1] = -1
        A[i, i-n] = -1
        B[i] = T4
    elif i == (s-1):
        A[i, i] = 4
        A[i, i-1] = -1
        A[i, i-n] = -1
        B[i] = T2 + T4
    else:
        A[i, i] = 4
        A[i, i-1] = -1
        A[i, i+1] = -1
        A[i, i-n] = -1
        A[i, i+n] = -1
        B[i] = 0

print("--------------A--------------")
print(A)

print("\n--------------B--------------")
print(B)

print("\n--------------선형방정식--------------")
num = np.zeros((n,n))
for i in range(n):
    for j in range(n):
        num[i,j] = str(i+1) + str(j+1)
num = num.reshape((1,s))

for i in range(s):
    for j in range(s):
        if A[i,j] > 0:
            if i==0:
                print(str(A[i, j]) + "*X" + str(int(num[0][j])), end="")
            else:
                print(" + " + str(A[i, j]) + "*X" + str(int(num[0][j])), end="")

        elif A[i,j] < 0:
            print(" " + str(A[i, j]) + "*X" + str(int(num[0][j])), end="")
    print(" = " + str(B[i]))

print("\n--------------역행렬을 이용해 구한 해--------------")
x = nl.inv(A)@B
x = x.reshape((n,n))
print(x)
num = num.reshape((n,n))

for i in range(n):
    for j in range(n):
        print("X" + str(int(num[i,j])) + " = " + str(x[i,j]))

print("\n--------------LU 분해를 이용한 해--------------")
P, L, U = sl.lu(A)
y = nl.inv(L)@B
x1 = nl.inv(U)@y
x1 = x1.reshape((n,n))
print(x1)

for i in range(n):
    for j in range(n):
        print("X" + str(int(num[i,j])) + " = " + str(x1[i,j]))

# sns.heatmap(A)
# plt.show()     

# sns.heatmap(A, cmap='coolwarm')
# plt.show()     

# sns.heatmap(A, annot=True) #숫자 출력
# plt.show()   

# sns.heatmap(x)
# plt.show()     

# sns.heatmap(x, cmap='coolwarm')
# plt.show()     

# sns.heatmap(x, annot=True) #숫자 출력
# plt.show()   