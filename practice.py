#tuple packing : 우변의 객체들을 좌변에 있는 변수 하나에 할당하는 것
t = 1, 2, 3
print(t)

#tuple unpacking : 우변의 패킹한 튜플 변수에서 여러개의 값을 좌변으로 꺼내오는 것
a, b, c = t
print(a, b, c)

#dictionary  : {key1 : mappig value1, key2 : mapping value2, ....}
dic = {'c' : 'a', 2 : 'b', 3 : 'c'}
#key로 사용할 수 있는 자료형 : int, float, str, tuple, frozenset (list, dict, set는 사용 불가)
#mapping value에는 모든 종류의 자료형이 올 수 있다.
#index가 아닌 key value로 mapping value를 추출할 수 있다.
print(dic['c'])
#dict에 새로운 키 추가방법 : dict_name['key value'] = mapping value
#객체 삭제 방법 : del함수로 key값을 삭제
del dic['c']
#membership 연산자 : dictionary에 key값이 있는지 boolean형으로 확인
print(2 in dic)
#mapping값의 여부 확인
print('b' in dic.values())
#method about dictionary
dic_copy = dic.copy()
print(dic_copy)

