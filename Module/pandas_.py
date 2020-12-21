import pandas as pd
import statistics as st
from tkinter import filedialog, Tk

mylist1 = [1, 2, 5, 0, 0]
df1 = pd.DataFrame(mylist1)
print(df1)

df2 = pd.DataFrame([[1, 2, 3, 5],
[2, 3, 2, 1],
[2, 6, 2, 8]])
print(df2)

df3 = pd.DataFrame({
    "var1" : [1, 2, 3, 4, 5],
    "var2" : [2, 4, 1, 5, 7],
    "var3" : ['g', 'd', 'd', 'w', 'd']},
    index = [1, 2, 3, 4, 5])
print(df3)
print(df3.iloc[0, 2])

url ="http://jupiter.hallym.ac.kr/ftpdata/data/bmi.txt"
mydf1 = pd.read_csv(url, names = ['ht', 'wt', 'year', 'religon', 'gender', 'marriage'],
                    header = None, sep = '\s+')

print("Read from web : ", mydf1.shape)
print(mydf1.head())
print(mydf1.describe())

data = list(mydf1['ht'])

mydf1.to_csv("bmi.csv")
qidx = mydf1.wt / (mydf1.ht/100) **2
print("\n----------------\n")
mydf1['bmi'] = qidx
del mydf1['bmi']
mydf1.insert(2, 'bmi', qidx)
print(mydf1.head())

# root = Tk()
# mydf2 = pd.read_csv(filedialog.askopenfilename(parent=root), header = 0, encoding='utf-8')
# root.withdraw()
# print(mydf2)