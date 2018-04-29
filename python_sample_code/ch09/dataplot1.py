import pandas as pd
from pylab import *
rcParams['font.sans-serif'] = ['SimHei']   #设置中文显示
datas = [[65,92,78,83,70], [90,72,76,93,56], [81,85,91,89,77], [79,53,47,94,80]]
indexs = ["林大明", "陈聪明", "黄美丽", "熊小娟"]
columns = ["语文", "数学", "英文", "自然", "社会"]
df = pd.DataFrame(datas, columns=columns,  index=indexs)
df.plot()
