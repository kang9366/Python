#ㄱ - 합 반환함수 def sum1(arr): sum = 0
for i in arr:
sum += i return sum

#ㄴ - 제곱합 반환함수
def sum2(arr): 
    sum = 0
i = 0 
while(True):
sum += arr[i]*arr[i] i += 1
if i == len(arr): break
return sum

#ㄷ - 짝수,홀수 판별함수
def isodd(num):
if num % 2 != 0: return True
else:
return False

#ㄹ-x1
x1 = []
for i in range(1,21):
    if(not(isodd(i))):
        x1.append(i)
x1.sort()

#ㄹ-x2
x2 = []
n = 0
for i in range(1, 101): 
    if(i % 3 == 0):
        x2.insert(n, i)
        n += 1
x2.sort()

#평균
def mean(x):
    return sum1(x)/len(x)

#중앙값
def median(x):
    temp = []
    x.sort()
    n = int(len(x)/2)
    if isodd(len(x)):
        return x[n]
    else:
        temp = [x[n-1], x[n]]
        return mean(temp)

#분산
def var(x):
    n = len(x)
    return (sum2(x) - (n*mean(x)*mean(x)))/(n-1)

print("---------------------------------------------------")
print("x1 리스트 : " + str(x1))
print("x2 리스트 : " + str(x2))
print("---------------------------------------------------")
print("x1 평균 : " + str(mean(x1)))
print("x2 평균 : " + str(mean(x2)))
print("---------------------------------------------------")
print("x1 중앙값 : " + str(median(x1)))
print("x2 중앙값 : " + str(median(x2)))
print("---------------------------------------------------")
print("x1 분산 : " + str(var(x1)))
print("x2 분산 : " + str(var(x2)))
print("---------------------------------------------------")
