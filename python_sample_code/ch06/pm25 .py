import sqlite3,ast,hashlib,os,requests
from bs4 import BeautifulSoup

conn = sqlite3.connect('DataBasePM25.sqlite') # 建立数据库连接
cursor = conn.cursor() # 建立 cursor 对象

# 建立一个数据表
sqlstr='''
CREATE TABLE IF NOT EXISTS TablePM25 ("no" INTEGER PRIMARY KEY AUTOINCREMENT 
NOT NULL UNIQUE ,"SiteName" TEXT NOT NULL ,"PM25" INTEGER)
'''
cursor.execute(sqlstr)

url = "http://api.help.bj.cn/apis/aqilist/"
html=requests.get(url).text.encode('utf-8-sig')  # 读取网页原始码
# 判断网页是否更新
md5 = hashlib.md5(html).hexdigest()
old_md5 = ""

if os.path.exists('old_md5-.txt'):
    with open('old_md5-.txt', 'r') as f:
        old_md5 = f.read()
with open('old_md5-.txt', 'w') as f:
        f.write(md5)
print("old_md5="+old_md5+";"+"md5="+md5)  #显示新老md5码进行观察
if md5 != old_md5:
    print('数据已更新...')    
    sp=BeautifulSoup(html,'html.parser')   #解析网页内容
    jsondata = ast.literal_eval(sp.text)  #此时jscondata取到的是字典类型数据
    # 删除数据表内容
    js1=jsondata.get("aqidata")     #取出字典数据中的aqidata项的值（值是列表）
    conn.execute("delete from TablePM25")
    conn.commit()
    n=1
    for city in js1:   #city此时是列表js1中的第一条字典数据
        CityName=city["city"]  #取出city字典数据中的值为"city"的key
        PM25=0 if city["pm2_5"] == "" else int(city["pm2_5"])  #如果city字典中的key对应的value为空，则PM25=0,否则，把PM25=value   
        print("城市:{}   PM2.5={}".format(CityName,PM25))   #显示城市对应的名称与PM2.5值
        # 新增一笔记录
        sqlstr="insert into TablePM25 values({},'{}',{})" .format(n,CityName,PM25)
        cursor.execute(sqlstr)
        n+=1
        conn.commit() # 主动更新 
else:
    print('数据未更新，从数据库读取...') 
    cursor=conn.execute("select *  from TablePM25")
    rows=cursor.fetchall()
    for row in rows:
        print("城市:{}   PM2.5={}".format(row[1],row[2]))    

conn.close()  # 关闭数据库连  