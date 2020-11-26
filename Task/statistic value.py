def sum1(arr):
    sumVar = 0
    for a in arr:
        sumVar += a
    return sumVar

def sum2(arr):
    i, sum = 0, 0
    while i < len(arr):
        sum += arr[i] ** 2
        i += 1
    return sum

def isodd(num):
    return num % 2 == 1

def median(isOdd, arr):
    half = int(len(arr)/2) 
    arr.sort()
    return arr[half] if isOdd else ((arr[half] + arr[half-1])/2)

x1 = [x for x in range(1, 21) if x % 2 == 0]
x2 = [x for x in range(1, 101) if x % 3 == 0]

print("**** x1 결과물 ****")
x1Avg = sum1(x1) / len(x1)
print("x1 평균 :", x1Avg)
print("x1 분산 :", (sum2(x1) - (len(x1) * x1Avg ** 2)) / (len(x1)-1))
print("x1 중앙값 :", median(isodd(len(x1)), x1))


print("**** x2 결과물 ****")
x2Avg = sum1(x2) / len(x2)
print("x2 평균 :", x2Avg)
print("x2 분산 :", (sum2(x2) - (len(x2) * x2Avg ** 2)) / (len(x2)-1))
print("x2 중앙값 :", median(isodd(len(x2)), x2))