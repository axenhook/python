import os,docx
cur_path=os.path.dirname(__file__) # 取得当前路径
sample_tree=os.walk(cur_path)

keyword="篮球"
print("查找字符串：{}" .format(keyword))

for dirname,subdir,files in sample_tree:
   allfiles=[]   
   for file in files:  # 取得所有.docx文件并存入 allfiles 列表中
      ext=file.split('.')[-1]
      if ext=="docx": # get *.docx to allfiles 
         allfiles.append(dirname +'/'+file)
         
   for file in allfiles:
      print("正在查找{}文件...".format(file))
      try:
         doc = docx.Document(file)
         line=0
         for p in doc.paragraphs:
             line+=1
             if keyword in p.text:
                 print("...在第 {} 段文字中找到{}\n {}。".format(line,keyword,p.text))  
      except:
         print("无法读取 {} 文件..." .format(file))  
     
print("\n查找完毕...")
