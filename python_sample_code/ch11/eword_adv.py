def menu():
    os.system("cls")
    print("英 汉 词 典")
    print("-------------------------")
    print("1. 翻  译  单  词")
    print("2. 输  入  单  词")
    print("3. 显  示  单  词")
    print("4. 修  改  单  词")
    print("5. 删  除  单  词")
    print("0. 结  束  程  序")
    print("-------------------------")
    
def CkeckKey(no):
    key_id=""
    if datas != None:
        for key,value in datas.items():
            if no==key: # 读取键名
                key_id = key
                break  
    return key_id   
    
def input_data():  
    global datas      
    while True:
        eword =input("请输入英文单字(Enter==>停止输入)")
        if eword=="": break
        key_id = CkeckKey(eword)   
        if key_id != "":      # 判断键是否存在
            print("{} 单词已存在!".format(datas.get(key_id)))
            continue
        cword=input("请输入中文翻译：")
        fb.put(url, data=cword,name=eword)
        time.sleep(2)
        if datas == None: datas = dict()
        datas[eword]=cword
        print(eword,":",cword," 已存储完毕!")

def disp_data():
    global datas
    datas=fb.get(url, None)
    if datas != None:
        dc_sort = sorted(datas.items(),key = operator.itemgetter(0))
        n,page=0,15
        for item in dc_sort:
            if n % page ==0:
                  print("单词\t中文翻译")
                  print("======================")
            key=item[0]      
            print("{}\t{}".format(key,item[1]))
            n+=1
            if n == page:
                c=input("请按 Enter 显示下一页，Q 键返回主菜单") 
                if c.upper() == "Q":return
                n=0
        c=input("请按任意键返回主菜单")         
       
def search_data():
    while True:
        eword =input("请输入要翻译的英文单词(Enter==>停止输入)")
        if eword=="": break
        key_id = CkeckKey(eword)
        if key_id != "":      # 判断键是否存在
            print("中文翻译：{}".format(datas[key_id]))
        else:
            print("{}单词不存在!\n".format(eword))  
        input("请按任意键继续翻译…")    
        
def edit_data():
    while True:
        eword =input("请输入要修改的英文单词(Enter==>停止输入)")
        if eword=="": break
        key_id = CkeckKey(eword)
        if key_id != "":      # 判断键是否存在
            print("原来中文翻译：{}".format(datas[key_id]))  
            cword=input("请输入中文翻译：")
            datas[key_id]=cword 
            fb.put(url + '/', data=cword, name=key_id)       
            time.sleep(2)
            print(eword,":",cword," 已修改完毕!\n")         
        else:
            print("{} 单词不存在!\n".format(eword)) 

def delete_data():
    while True:
        eword =input("请输入要删除的英文单词(Enter==>停止输入)")
        if eword=="": break
        key_id = CkeckKey(eword)   
        if key_id != "":      # 判断键是否存在
            print("确定删除 {} 的数据!".format(datas[key_id]),end="")
            yn=input("(Y/N)?")
            if (yn=="Y" or yn=="y"):
                fb.delete(url + '/' + key_id,None)
                datas.pop(key_id)
                print("数据删除完毕\n")
        else:
            print("{} 单词不存在!\n".format(eword)) 


### 主程序从这里开始 ###

import time,os
from firebase import firebase
import operator

url = 'https://chiouapp01-dedce.firebaseio.com/English_adv'
fb = firebase.FirebaseApplication(url, None)
datas=fb.get(url, None)

while True:
    menu()
    choice = input("请输入您的选择：")
    try:
        choice = int(choice)
        print()
        if choice==1:
            search_data()
        elif choice==2:
            input_data()
        elif choice==3:
            disp_data()
        elif choice==4:
            edit_data()
        elif choice==5:
            delete_data()
        else:
            break
    except:    
        print("非常按键!")
        time.sleep(1)
print("程序执行完毕！")
