def power(x):
    return x**2

num = [i for i in range(4)]

result = map(power, num)
print(list(result))