def CkeckKey(no):
    key_id=""
    if datas != None:
        for key in datas:
            if no==datas[key]["no"]: # 如果找到键名，则......
                key_id = key
                break
    return key_id 

### 主程序从这里开始 ###
        
from firebase import firebase
import time

url = 'https://chiouapp01-74bde.firebaseio.com'
fb = firebase.FirebaseApplication(url, None)
datas=fb.get('/students', None)

while True:
    no = input("请输入编号(Enter==>停止输入)")
    if no=="": break
    key_id = CkeckKey(int(no))   
    if key_id != "":      # 判断键是否存在
        print("原来姓名：{}".format(datas[key_id]["name"]))  
        name=input("请输入姓名：")
        data = {"no":int(no),"name":name} 
        datas[key_id]=data 
        fb.put(url + '/students/', data=data, name=key_id)       
        time.sleep(2)
        print("{} 已修改完毕\n".format(data))         
    else:
        print("{} 对应的数据不存在!\n".format(no))
