import pandas as pd
tables = pd.read_html("http://value500.com/M2GDP.html")
table = tables[18]
table = table.drop(table.index[0:1])
table.columns = ["年份", "M2指标", "GDP绝对额", "M2/GDP"]
table.index = range(len(table.index))
print(table)