c_code = {'Korea' : 82, 'US' : 1, 'China' : 86, 'Germany' : 81}
print(c_code['Korea']) #value값 출력
print(c_code.keys())
print(c_code.values())
print(c_code.items())

for k, v in c_code.items():
    print("key : ", k, "value : ", v)

if 'Korea' in c_code.keys():
    print("Korea is exist")
else:
    print('Korea is not exist')

    