def rbCity():  #单击区县按钮的处理函数
    global sitelist, listradio
    sitelist.clear()  #清除原有监测站点列表
    for r in listradio:  #删除原有监测站点按钮
        r.destroy()
    n=0
    for c1 in data["区╱县"]:  #逐一取出所选区县市的监测站点
        if(c1 == city.get()):
            sitelist.append(data.ix[n, 1])
        n += 1    
    sitemake()  #生成测站点按钮
    rbSite()  #显示PM2.5数值

def rbSite():  #单击监测站按钮后的处理函数
    n = 0
    for s in data.ix[:,1]:  #逐一取得监测站点
        if(s == site.get()):  #如果某监测站点名称与选中的监测站点相同，则
            pm = data.ix[n][ "PM2.5浓度"]  #取得该站点的PM2.5数值
            pm=pm[:-5]    #去除数据后面的5位单位字符
            pm=int(pm)  #把PM2.5的字符型数据转为整型
            if(pd.isnull(pm)):  #如果没有数据，则
                result1.set(s + "站的 PM2.5 值当前无数据！")   #显示无数据
            else:  #如果有数据，则
                if(pm <= 35):  #转换为空气质量等级
                    grade1 = "优秀"
                elif(pm <= 53):
                    grade1 = "良好"
                elif(pm <= 70):
                    grade1 = "中等"
                else:
                    grade1 = "差"
                result1.set(s + "站的 PM2.5 值为" + str(pm) + ";" + grade1 )
            break  #找到选中的监测站点的数据后就跳出循环
        n += 1
    
def clickRefresh():  #重新读取数据
    global data
    df = pd.read_html("http://www.86pm25.com/city/beijing.html")
    data=df[0]
    rbSite()  #更新监测站点的数据

def sitemake():  #建立监测站点按钮
    global sitelist, listradio
    for c1 in sitelist:  #逐一建立按钮
        rbtem = tk.Radiobutton(frame2, text=c1, variable=site, value=c1, command=rbSite)  #建立单选按钮
        listradio.append(rbtem)  #插入至按钮列表
        if(c1==sitelist[0]):  #默认选取第1个按钮         
            rbtem.select()
        rbtem.pack(side="left")  #靠左对齐

import tkinter as tk
import pandas as pd
df = pd.read_html("http://www.86pm25.com/city/beijing.html")
data=df[0]
win=tk.Tk()
win.geometry("640x270")
win.title("PM2.5 实时监测")
city = tk.StringVar()  #区县名称变量
site = tk.StringVar()  #监测站点名称变量
result1 = tk.StringVar()  #显示信息变量
citylist = []  #区县列表
sitelist = []  #监测站点列表
listradio = []  #区县按钮列表
#建立区县列表
for c1 in data["区╱县"]:  
    if(c1 not in citylist):  #如果列表中不存在该县区就将该县区名称插入列表
        citylist.append(c1)
#建立第1个区县的监测站点列表
count = 0
for c1 in data["区╱县"]:  
    if(c1 ==  citylist[0]):  #如果是第1个区县，则
        sitelist.append(data.ix[count, 1])  #把该区县的所有监测站点插入到监测站点列表
    count += 1
label1 = tk.Label(win, text="区县：", pady=6, fg="blue", font=("新细明体", 12))
label1.pack()
frame1 = tk.Frame(win)  #区县容器
frame1.pack()
for i in range(0,2):  #按钮分2行
    for j in range(0,8):  #每行8个
        n = i * 8 + j  #第n个按钮
        if(n < len(citylist)):
            city1 = citylist[n]  #取得区县名称
            rbtem = tk.Radiobutton(frame1, text=city1, variable=city, value=city1, command=rbCity)  #建立单选按钮
            rbtem.grid(row=i, column=j)  #设置按钮的位置
            if(n==0):  #选取第1个区县
                rbtem.select()
label2 = tk.Label(win, text="监测站点：", pady=6, fg="blue", font=("新细明体", 12))
label2.pack()
frame2 = tk.Frame(win)  #监测站点容器
frame2.pack()
sitemake()
btnDown = tk.Button(win, text="更新数据", font=("新细明体", 12), command=clickRefresh)
btnDown.pack(pady=6)
lblResult1 = tk.Label(win, textvariable=result1, fg="red", font=("新细明体", 16))
lblResult1.pack(pady=6)
rbSite()  #显示测站讯息
win.mainloop()