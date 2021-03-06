import os,docx,sys

if len(sys.argv) == 1:
    keyword="shutil" 
    print("语法：python FindKeyWord3.py 查找字符串\n")
else:
    keyword=sys.argv[1]  
 
#cur_path=os.path.dirname(__file__) # 取得当前路径
cur_path=os.getcwd()
sample_tree=os.walk(cur_path)
print(cur_path)

for dirname,subdir,files in sample_tree:
   allfiles=[]   
   for file in files:  # 取得所有 .py .txt .docx文件，存入allfiles列表中
      ext=file.split('.')[-1]
      if ext=="py" or ext=="txt" or ext=="docx": 
          allfiles.append(dirname +'/'+file)
         
   if len(allfiles)>0:  
      for file in allfiles:  # 读取 allfiles 列表所有文件  
         try:
            if file.split('.')[-1]=="docx": # .docx
                doc = docx.Document(file)
                line=0
                for p in doc.paragraphs:
                    line+=1
                    if keyword in p.text:
                        print("...在第 {} 段文字中找到{}\n {}。".format(line,keyword,p.text))  
            else:  # .py or .txt             
                fp = open(file, "r", encoding = 'UTF-8')
                article = fp.readlines()
                fp.close 
                line=0            
                for row in article:
                   line+=1
                   if keyword in row:
                       print("在 {}，第 {} 行找到 {} 。".format(file,line,keyword))
         except:
            print("{} 无法读取..." .format(file)) 
     
print("完成...")
