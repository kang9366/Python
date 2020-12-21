#list comprehension
x = [i for i in range(9)]
print(x)

#if문
y = [i for i in range(9) if i%2==0]
print(y)

#if else문
z = [i if i%2==0 else 3 for i in range(9)]
print(z)

#반복문 중첩
l = [i+j for i in range(3) for j in range(4)]
print(l)

