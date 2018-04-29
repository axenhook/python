with open('file2.txt','r',encoding ='UTF-8') as f:
    doc=f.readlines() 
    print(doc)    # 输出所有文件内容  
    
f=open('file2.txt','r',encoding ='UTF-8')
str1=f.read(5)
print(str1)  # 只输出文件前5个字符
f.close()