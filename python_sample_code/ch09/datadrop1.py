import pandas as pd
datas = [[65,92,78,83,70], [90,72,76,93,56], [81,85,91,89,77], [79,53,47,94,80]]
indexs = ["林大明", "陈聪明", "黄美丽", "熊小娟"]
columns = ["语文", "数学", "英文", "自然", "社会"]
df = pd.DataFrame(datas, columns=columns,  index=indexs)
print('删除陈聪明成绩 ->')
df1 = df.drop("陈聪明")
print(df1)
print()
print('删除数学成绩 ->')
df2 = df.drop("数学", axis=1)
print(df2)
print()
print('删除数学及自然成绩 ->')
df3 = df.drop(["数学", "自然"], axis=1)
print(df3)
print()
print('删除从陈聪明到熊小娟成绩 ->')
df4 = df.drop(df.index[1:4])
print(df4)
print()
print('删除从数学到自然的成绩 ->')
df5 = df.drop(df.columns[1:4], axis=1)
print(df5)
print()


