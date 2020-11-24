import numpy as np

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