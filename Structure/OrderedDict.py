import collections as cln

d1 = {}
d1['x'] = 100
d1['l'] = 500
d1['y'] = 200
d1['z'] = 300

for k, v in d1.items():
    print(k, v)

print("===============================")

d2 = cln.OrderedDict()
d2['x'] = 100
d2['l'] = 200
d2['z'] = 300
d2['y'] = 500
for k, v in d2.items():
    print(k, v)

def sort_by_key(mydict):
    return mydict[0]

def sort_by_value(mydict):
    return mydict[1]

d = {}
d['l'] = 100
d['x'] = 200
d['y'] = 300
d['z'] = 500
print("key에 의한 정렬")
for k, v in cln.OrderedDict(sorted(d.items(), key = sort_by_key, reverse=False)).items():
    print(k, v)

print("\nvalue에 의한 정렬")
for k, v in cln.OrderedDict(sorted(d.items(), key = sort_by_value, reverse=True)).items():
    print(k, v)

