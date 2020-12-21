# f = open("/Users/kangseunggu/Desktop/BTS_Dynamite_lyrics.txt", "r")
# fw = open("dynamite1.txt", "w")

# counter= 0
# for line in f:
#     lcounter = line.lower().count("dynamite")
#     if(lcounter != 0):
#         print(line)
#         fw.write(line)
#     counter += lcounter

# f.close()
# fw.close()

date_info = {'year' : '1998', 'month' : '08', 'date' : '17'}
file_name = "{year} - {month} - {date}.txt".format(**date_info)
print(file_name)