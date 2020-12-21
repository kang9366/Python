import numpy as np

a = np.zeros(5)
b = np.ones(5)
print(a)
print(b)

c = np.empty((2,3), dtype=int)
print(c)
print(c.shape)
print("row : ", c.shape[0])
print('col : ', c.shape[1])

c1 = c.reshape(3,2)
print(c1)

#0부터 3까지의 배열 만들기
array1 = np.arange(4)
print(array1)

array2 = np.zeros((4, 4), dtype = float)
print(array2)

#0부터 9까지 랜덤으로 초기화된 배열 만들기
array4 = np.random.randint(0, 200, (3, 3))
print(array4)

array_np = np.array([1, 2, 3, 4])
array_reshape = array_np.reshape((2, 2))
print(array_reshape)

#등차 수열 만들기 (start : 시작지점, stop : 끝지점, num = 만들 원소의 개수, endpoint : 끝지점을 포함할지의 여부, retstep : 간격을 리턴할지의 여부)
array_5 = np.linspace(start=0, stop=50, num=10, endpoint=True, retstep=True)
print(array_5)

#난수 발생
#유한 모집단에서 표본 추출
d = [i for i in range(100)]
e = np.random.choice(d, 10)
print(e)

#일양분포 --> [0, 1) 구간에서 난수 발생
x = np.random.random(10)
print(x)

#정규분포
y = np.random.randn(2, 10)
print(y)