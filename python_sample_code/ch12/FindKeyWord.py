import os
cur_path=os.path.dirname(__file__) # 取得当前路径
sample_tree=os.walk(cur_path)
keyword="shutil"

for dirname,subdir,files in sample_tree:
   allfiles=[]   
   for file in files:  # 取得所有 .py .txt 文件，存入 allfiles 列表中
      ext=file.split('.')[-1]
      if ext=="py" or ext=="txt": 
         allfiles.append(dirname +'/'+file)
         
   if len(allfiles)>0:  
      for file in allfiles:  # 读取 allfiles 列表所有文件  
         try:
            fp = open(file, "r", encoding = 'UTF-8')
            article = fp.readlines()
            fp.close 
            line=0            
            for row in article:
               line+=1
               if keyword in row:
                   print("在 {}，第 {} 行找到{}。".format(file,line,keyword))
         except:
            print("{} 无法读取..." .format(file)) 
     
print("完成...")
