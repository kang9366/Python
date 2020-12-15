import numpy as np
from scipy import linalg

#A 행렬 입력 받기ㅠ
print("-----A 행렬-----")
n = int(input("행 개수 입력 : "))

#입력받은 행 개수로 정방영행렬을 만든뒤 반복문으로 값을 하나씩 입력받는다
A = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        num = int(input(str(i+1) + "행, " + str(j+1) + "열 : "))
        A[i, j] = num

#B행렬은 A행렬의 전치행렬
B = np.transpose(A)

print(A)

print("\n-----B 행렬-----")
print(B)

#A의 행과 열의 개수와 동일하게 정방영행렬인 C행렬을 만들고 반복문을 이용해 값을 하나씩 입력받는다
print("\n-----C 행렬-----")
C = np.zeros((n,n))
for i in range(n):
    for j in range(n):
        num = int(input(str(i+1) + "행, " + str(j+1) + "열 : "))
        C[i, j] = num

#X구하기
X = linalg.solve_continuous_lyapunov(A, C)

print("\n-----X-----")
print(X)

print("\n-----test----")
print("A@X + X@B")
print(A@X + X@B)
print("C")
print(C)

if (A@X + X@B) == C:
    print("true")
else:
    print("false")