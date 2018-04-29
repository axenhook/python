import pandas as pd
datas = [[65,92,78,83,70], [90,72,76,93,56], [81,85,91,89,77], [79,53,47,94,80]]
indexs = ["林大明", "陈聪明", "黄美丽", "熊小娟"]
columns = ["语文", "数学", "英文", "自然", "社会"]
df = pd.DataFrame(datas, columns=columns,  index=indexs)
print('按照数学成绩降序排序 ->')
df1 = df.sort_values(by="数学", ascending=False)
print(df1)
print()
print('按照列标题升序排序 ->')
df2 = df.sort_index(axis=0)
print(df2)
print()

