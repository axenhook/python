def CkeckKey(no):
    key_id=""
    if datas != None:
        for key in datas:
            if no==datas[key]["eword"]: # 读取键名
                key_id = key 
                break
    return key_id
        
### 主程序从这里开始 ###
 
from firebase import firebase

url = 'https://chiouapp01-74bde.firebaseio.com/English'
fb = firebase.FirebaseApplication(url, None)
datas=fb.get(url, None)

with open('eword.csv','r', encoding = 'gbk') as f:
    for line in f:
        eword,cword = line.rstrip('\n').split(',')
        word={'eword':eword,'cword':cword}
        if CkeckKey(eword) == "":      # 判断键是否存在
            fb.post(url, word)  
            print(word)
    print("\n转换完毕!")         
