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
url = 'https://chiouapp01-dedce.firebaseio.com'
fb = firebase.FirebaseApplication(url, None)
datas=fb.get('/students', None)

while True:
#    datas=fb.get('/students', None)
    no = input("请输入序号(Enter==>停止输入)")
    if no=="": break
    key_id = CkeckKey(int(no))   
    if key_id != "":    # 判断键是否存在
        print("确定要删除{}的数据？".format(datas[key_id]["name"]))
        yn=input("(Y/N)?")
        if (yn=="Y" or yn=="y"):
            fb.delete('/students/'+key_id,None)
            datas.pop(key_id)
            print("数据删除完毕\n")         
    else:
        print("{} 对应的数据不存在!\n".format(no))
