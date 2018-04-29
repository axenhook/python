def CkeckKey(no):
    key_id=""
    if datas != None:
        for key in datas:
            if no==key: # 读取键名
                key_id = key
                break  
    return key_id
        
### 主程序从这里开始 ###
        
from firebase import firebase

url = 'https://chiouapp01-74bde.firebaseio.com/English_adv/'
fb = firebase.FirebaseApplication(url, None)
datas=fb.get(url, None)

with open('eword_less.csv','r', encoding = 'gbk') as f:
    for line in f:
        eword,cword = line.rstrip('\n').split(',')
        if CkeckKey(eword) == "":      # 判断键是否存在
            fb.put(url,data=cword,name=eword)
            print(eword,":",cword)
    print("\n转换完毕!")         