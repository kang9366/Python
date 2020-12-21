import collections as cln

mytext = 'collections'
lmytext = list(mytext)
print(lmytext)
freq = cln.Counter(lmytext)
print(freq)

cc = cln.Counter({'red' : 4, 'blue' : 3})
print("cc : ", list(cc.elements()))

dd = cln.Counter(red=3, blue=4)
print("dd : ", list(dd.elements()))

ee = dd + cc
print("dd + cc : ", dd + cc)
print("dd - cc", dd - cc)

ee.subtract(dd)
print(ee)