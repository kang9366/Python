# date_info = {'year' : "1998", 'month' : '08', 'day' : '17'}
# file_name = "{year}-{month}-{day}.txt".format(**date_info)

f = open("/Users/kangseunggu/Desktop/BTS_Dynamite_lyrics.txt")
contents = f.readlines()
f.close()
print(contents)