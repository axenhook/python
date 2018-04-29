import pandas as pd
dt = pd.read_html("http://www.86pm25.com/city/beijing.html")
data=dt[0]
print(data)