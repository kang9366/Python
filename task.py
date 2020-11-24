#######################################3
while(True):
    #근무시간을 실수로 입력받기
    hour = float(input("근무 시간을 입력해주세요 : "))
    #근무시간이 0시간 초과 40시간 이하이면 시급은 만원
    if hour > 0 and hour <= 40:
        wage = int(hour * 10000)
        print(f'{wage:,}')
    
    #근무시간이 40시간 초과 52시간 미만이면 40시간까지는 시급이 만원 그 이후에는 15000원
    elif hour > 40 and hour < 52:
        wage = int((40 * 10000) + (hour-40)*15000)
        print(f'{wage:,}')
    
    #근무시간이 0시간 미만이거나 52시간 초과이면 good bye 출력 후 프로그램 종료
    elif hour < 0 or hour > 52:
        print("Good bye")
        break

#########################################4
score = [73, 62, 46, 46, 79, 11, 61, 63, 76, 81, 63, 57, 73, 49, 60, 75, 61, 60, 92, 24]

def p(i, grade):
    print(str(i) + " : " + grade + " 입니다.")

for i in score:
    if i > 95:
        p(i, 'A+')
    elif i <= 95 and i > 90:
        p(i, 'A')
    elif i <= 90 and i > 85:
        p(i, 'B+')
    elif i <= 85 and i > 80:
        p(i, 'B')
    elif i <= 80 and i > 75:
        p(i, 'C+')
    elif i <= 75 and i > 70:
        p(i, 'C')
    elif i <= 70 and i > 65:
        p(i, 'D+')
    elif i <= 65 and i > 60:
        p(i, 'D')
    elif i <= 60:
        p(i, 'F')

########################################5
#ㄱ - 합 반환함수
def sum1(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum

#ㄴ - 제곱합 반환함수
def sum2(arr):
    sum = 0
    i = 0
    while(True):
        sum += arr[i]*arr[i]
        i += 1
        if i == len(arr):
            break
    return sum

#ㄷ - 짝수,홀수 판별함수
def isodd(num):
    if num % 2 != 0:
        return True
    else:
        return False

#ㄹ-x1
x1 = []
for i in range(1,21):
    if(not(isodd(i))):
        x1.append(i)

#ㄹ-x2
x2 = []
for i in range(1, 101):
    if(i % 3 == 0):
        x2.append(i)

#평균
def mean(x):
    return sum1(x)/len(x)

#중앙값
def median(x):
    temp = []
    n = int(len(x)/2)
    if isodd(len(x)%2):
        return x[n]
    else:
        temp = [x[n], x[n+1]]
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
print("x1 중앙값 : " + str(median(x2)))
print("---------------------------------------------------")
print("x1 분산 : " + str(var(x1)))
print("x2 분산 : " + str(var(x2)))
print("---------------------------------------------------")