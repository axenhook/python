import pandas as pd
tables = pd.read_html("http://value500.com/M2GDP.html")
n = 1
for table in tables:
    print("第 " + str(n) + " 个表格：")
    print(table.head())
    print()
    n += 1
