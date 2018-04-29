def CkeckKey(no):
    key_id=""
    if datas != None:
        for key in datas:
            if no==datas[key]["no"]: # 如果找到键名,则...
                key_id = key
                break
    return key_id 

### 主程序从这里开始 ###        
        
from firebase import firebase

students = [{'no':1 ,'name':'李天龙'},
{'no':2,'name':'高一人'},
{'no':3,'name':'洪大同'}]

url = 'https://chiouapp01-74bde.firebaseio.com'
fb = firebase.FirebaseApplication(url, None)

datas=fb.get('/students', None)

for student in students:
    no=student["no"] # 读取键名称  
    if CkeckKey(no) == "":      # 判断键是否存在
        fb.post('/students', student)
        print("{} 储存完毕".format(student))
