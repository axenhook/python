import matplotlib.pyplot as plt   #导入绘图模块，重命名为plt
import requests    #导入网页内容抓取包
from bs4 import BeautifulSoup as bs  #导入网页解析模块，重命名为bs
from pylab import *   #导入pylab包
rcParams['font.sans-serif'] = ['SimHei']  #让matplotlib支持简体中文

year = []    #横坐标列表
gdp = []   #纵坐标列表
url = "http://value500.com/M2GDP.html"   #设置要在哪个网页抓数据
content = requests.get(url)   #获取网页内容
content.encoding='utf-8'    #转为utf-8编码
content1=content.text  #取得网页内容的text部分
parse = bs(content1,"html.parser") #进行html解析
data1 = parse.find_all("table")  #获取所有表元素
rows = data1[19].find_all("tr") #取出包含所需数据的表（网页第20个表）
i=0                             #为了不读取表头数据，设置此控制变量
for row in rows:
    cols = row.find_all("td")  #把每一行表数据存入cols变量
    if(len(cols) > 0 and i==0):  #如果是第一行，则控制变量加1
        i+=1
    else:                       #如果不是第一行，则写入绘图列表
        year.append(cols[0].text[:-2])  #取得年份数据（数据的最后两个字符不是数据需去除）并写入图形的year轴
        gdp.append(cols[2].text)     #把gdp值存入gdp轴
plt.plot(year, gdp, linewidth=2.0)   #绘制图形，线宽为2
plt.title("1990~2016年度我国GDP")   #设置图形标题
plt.xlabel("年度")    #设置x轴标题
plt.ylabel("GDP(亿元)")  #设置y轴标题
plt.show()    #显示所绘图形