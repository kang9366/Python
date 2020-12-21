import pandas as pd

mylist1 = [1, 2, 5, 0, 0]
df1 = pd.DataFrame(mylist1)
print(df1)

df2 = pd.DataFrame([[1, 2, 3, 5],
[2, 3, 2, 1],
[2, 6, 2, 8]])
print(df2)

print("\n------------------\n")
df3 = pd.DataFrame({
    "var1" : [1, 2, 3, 4, 5],
    "var2" : [2, 4, 1, 5, 7],
    "var3" : ['g', 'd', 'd', 'w', 'd']},
    index = [1, 2, 3, 4, 5])
print(df3)
print(df3.iloc[0, 2])