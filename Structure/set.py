s1 = {1,2,3,4,4}
s1.add(10)
s1.remove(1)
s1.discard(3)
s1.update([4,5,6,7])

s3 = {1,3,5,7,9}
print("합집합 : " + str(s1.union(s3)))
print("교집합 : " + str(s1.intersection(s3)))
print("차집합 : " + str(s1.difference(s3)))

print("합집합 : " + str(s1 | s3))
print("교집합 : " + str(s1 & s3))
print("차집합 : " + str(s1 - s3))