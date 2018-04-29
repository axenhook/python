import pandas as pd
datas = [[65,92,78,83,70], [90,72,76,93,56], [81,85,91,89,77], [79,53,47,94,80]]
indexs = ["林大明", "陈聪明", "黄美丽", "熊小娟"]
columns = ["语文", "数学", "英文", "自然", "社会"]
df = pd.DataFrame(datas, columns=columns,  index=indexs)
print('df["自然"] ->')
print(df["自然"])
print()
print('df[["国文", "数学", "自然"] ->')
print(df[["国文", "数学", "自然"]])
print()
print('df[df.数学>=80] ->')
print(df[df.数学 >= 80])

