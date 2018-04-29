with open('file1.txt','r') as f:
    content=f.readlines() 
    print(type(content))   # 显示返回值的数据类型
    print(content)     #显示文件内容