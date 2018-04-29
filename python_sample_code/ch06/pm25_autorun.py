import sqlite3,ast,requests,os
from bs4 import BeautifulSoup

cur_path=os.path.dirname(__file__) # 取得目前路径
print(cur_path)
conn = sqlite3.connect(cur_path + '/' + 'DataBasePM25.sqlite') # 建立数据库连接
cursor = conn.cursor() # 建立 cursor 对象

# 建立一个数据表
sqlstr='''
CREATE TABLE IF NOT EXISTS TablePM25 ("no" INTEGER PRIMARY KEY AUTOINCREMENT 
NOT NULL UNIQUE ,"SiteName" TEXT NOT NULL ,"PM25" INTEGER)
'''
cursor.execute(sqlstr)

url = "http://api.help.bj.cn/apis/aqilist/"
# 读取网页原始码
html=requests.get(url).text.encode('utf-8-sig')

print('数据已更新...')    
sp=BeautifulSoup(html,'html.parser')    #sp是bs4.Beautifulsoup类
# 将网页内转换为 list,list 中的元素是 dict 
jsondata = ast.literal_eval(sp.text)   #把sp.text字符串转为dict类型
js=jsondata.get("aqidata")  #从jasondata中取出值为"aqidata"的key对应的value的列表

# 删除数据表内容
conn.execute("delete from TablePM25")
conn.commit()

#把抓到的数据逐条存到数据库
n=1
for city in js:
    CityName=city["city"]
    PM25=0 if city["pm2_5"] == "" else int(city["pm2_5"])     
    print("城市:{}   PM2.5={}".format(CityName,PM25))
    # 新增一条记录
    sqlstr="insert into TablePM25 values({},'{}',{})" .format(n,CityName,PM25)
    cursor.execute(sqlstr)
    n+=1
    conn.commit() # 主动更新  
conn.close()  # 关闭数据库连  