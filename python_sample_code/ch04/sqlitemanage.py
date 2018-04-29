def menu():
    os.system("cls")
    print("账号、密码管理系统")
    print("-------------------------")
    print("1. 输入账号、密码")
    print("2. 显示账号、密码")
    print("3. 修  改  密  码")
    print("4. 删除账号、密码")
    print("0. 结  束  程  序")
    print("-------------------------")
        
def disp_data():
    cursor = conn.execute('select * from password')
    print("账号\t密码")
    print("================")
    for row in cursor:
        print("{}\t{}".format(row[0],row[1]))
    input("按任意键返回主菜单")        
    
def input_data():       
    while True:
        name =input("请输入账号(Enter==>停止输入)")
        if name=="": break
        sqlstr="select * from password where name='{}'" .format(name)
        cursor=conn.execute(sqlstr) 
        row = cursor.fetchone()
        if not row==None:
            print("{} 账号已存在!".format(name))
            continue
        password=input("请输入密码：")        
        sqlstr="insert into password values('{}','{}');".format(name,password)
        conn.execute(sqlstr)
        conn.commit()  
        print("{} 已保存完毕".format(name))    
    
def edit_data():
    while True:
        name =input("请输入要修改的账号(Enter==>停止输入)")
        if name=="": break
        sqlstr="select * from password where name='{}'" .format(name)
        cursor=conn.execute(sqlstr) 
        row = cursor.fetchone()
        print(row)
        if row==None:
            print("{} 账号不存在!".format(name))
            continue
        print("原来密码为：{}".format(row[1]))
        password=input("请输入新密码：")
        sqlstr = "update password set pass='{}' where name='{}'".format(password, name)
        conn.execute(sqlstr)
        conn.commit()        
        input("密码更改完毕，请按任意键返回主菜单") 
        break      
    
def delete_data():
    while True:
        name =input("请输入要删除的账号(Enter==>停止输入)")
        if name=="": break
        sqlstr="select * from password where name='{}'" .format(name)
        cursor=conn.execute(sqlstr) 
        row = cursor.fetchone()
        if row==None:
            print("{} 账号不存在!".format(name))
            continue
        print("确定删除{}的数据!：".format(name))
        yn=input("(Y/N)?")
        if (yn=="Y" or yn=="y"):
            sqlstr = "delete from password where name='{}'".format(name)
            conn.execute(sqlstr)
            conn.commit()
            input("已删除完毕，请按任意键返回主菜单") 
            break

### 主程序从这里开始 ###

import os,sqlite3

conn = sqlite3.connect('Sqlite01.sqlite')
while True:
    menu()
    choice = int(input("请输入您的选择："))
    print()
    if choice==1:
        input_data()
    elif choice==2:
        disp_data()
    elif choice==3:
        edit_data()
    elif choice==4:
        delete_data()
    else:
        break    

conn.close()
print("程序执行完毕！")
