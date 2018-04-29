def getrandom2(n1, n2):  #取得2个不重复的随机值
    while True:
        r1 = random.randint(n1, n2)
        r2 = random.randint(n1, n2)
        if r1 != r2:  #如果两数不相等就跳出，相等则继续取
            break
    return r1, r2

import os, random
from win32com import client
from win32com.client import constants
word = client.gencache.EnsureDispatch('Word.Application')
word.Visible = 1
word.DisplayAlerts = 0  #不显示警告
doc = word.Documents.Add()
range1 = doc.Range(0,0)  #文件开头
range1.Style.Font.Size = "16"  #字体大小
title = "明星小学营养午餐菜单"
year1 = "2017年8月"
week = ["一","二","三","四","五"]
teacher = ["欧阳怡","翟定国","陈碧山","陈丽娟","郑怡衡","林邓超","朱健政","刘伟明","刘维基","梁银燕"]
rice = ["糙米饭","白米饭","拌面"]
vegetable = ["毛豆白菜","豆芽菜","蛋香时瓜","高丽菜","佛手瓜","酸菜豆包","冬瓜","萝卜海带结","茄汁洋芋","家常豆腐","鲜菇花椰","豆皮三丝","伍彩雪莲","干香根丝","茄汁豆腐","香炒花椰","芹香粉丝","红萝卜","洋葱","青椒"]
meat = ["糖醋排骨","美味大鸡腿","椒盐鱼条","香菇肉燥","宫保鸡丁","香卤腿排","梅干绞肉","香酥鱼丁","条瓜烧鸡","时瓜肉丝","海结卤肉","葱烧鸡","柳叶鱼","咖哩绞肉","笋香鸡","沙茶猪柳","五香棒腿","三杯鸡丁","海结猪柳","茄汁鸡丁"]
soup = ["蛋香木须汤","味噌海芽汤","绿豆汤","榨菜肉丝汤","姜丝海芽汤","枸杞爱玉汤","冬菜蛋花汤","冬瓜西米露","紫菜蛋花汤","蛋香木须汤"]
date1= 1  #开始日期为1日
weekday = 2  #开始日期为星期六

while weekday < 6 and date1 < 31:  #周一到周五及30日前才制作菜单
    range1.InsertAfter(title + "\n")
    range1.InsertAfter("日期：" + year1 + str(date1) + "日 (星期" + week[weekday-1] + ")\n")
    range1.InsertAfter("制作者：" + teacher[random.randint(0,9)] + "老师\n")    #10位老师中随机选一位
    range1.InsertAfter("今日菜单：\n")
    range1.InsertAfter("一、" + rice[random.randint(0,2)] + "\n")  #取1个随机数作为主食列表下标
    rand1, rand2 = getrandom2(0,19)  #取得两个随机数，作为菜品列表下标
    range1.InsertAfter("二、" + vegetable[rand1] + "\n")
    range1.InsertAfter("三、" + vegetable[rand2] + "\n")
    rand1, rand2 = getrandom2(0,19)    #重取两个随机数，作为肉品列表下标
    range1.InsertAfter("四、" + meat[rand1] + "\n")
    range1.InsertAfter("五、" + meat[rand2] + "\n")
    range1.InsertAfter("六、" + soup[random.randint(0,9)] + "\n")    #取一个随机数，作为汤品列表下标
    range1.Collapse(constants.wdCollapseEnd)  #移到range尾
    range1.InsertBreak(constants.wdSectionBreakNextPage)  #换页
    weekday += 1  #星期加1
    date1 += 1  #日期加1
    if weekday == 6:  #如果是星期六
        weekday = 1  #设为星期一
        date1 += 2  #日期加2(星期六及星期日)
    
cpath=os.path.dirname(__file__)
doc.SaveAs(cpath + "\\media\\food.docx")  #获取文件保存路径并把文件保存为food.docx
#doc.Close()    
#word.Quit()
