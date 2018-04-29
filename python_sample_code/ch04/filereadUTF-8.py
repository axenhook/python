f=open('file2.txt','r',encoding ='UTF-8')
for line in f:
    print(line,end="")
f.close()