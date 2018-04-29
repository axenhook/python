import pandas as pd
datas = [[65,92,78,83,70], [90,72,76,93,56], [81,85,91,89,77], [79,53,47,94,80]]
indexs = ["林大明", "陈聪明", "黄美丽", "熊小娟"]
columns = ["语文", "数学", "英文", "自然", "社会"]
df = pd.DataFrame(datas, columns=columns,  index=indexs)
print('df.ix["陈聪明"]["数学"] (原始)：' + str(df.loc["陈聪明"]["数学"]))
df.ix["陈聪明"]["数学"] = 91
print('df.ix["陈聪明"]["数学"] (修改)：' + str(df.loc["陈聪明"]["数学"]))
print()
print('df.ix["陈聪明", :] ->')
df.ix["陈聪明", :] = 80
print(df.ix["陈聪明", :])
