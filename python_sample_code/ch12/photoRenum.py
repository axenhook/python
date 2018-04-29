import os,shutil
cur_path=os.path.dirname(__file__) # 取得当前路径
sample_tree=os.walk(cur_path)
output_dir = 'output2'

for dirname,subdir,files in sample_tree:
   allfiles=[]
   basename= os.path.basename(dirname)
   if basename == output_dir:  # output2 目录不再重复处理
      continue

   for file in files:  # 读取所有 jpg 文件名，存入 allfiles 列表中
      ext=file.split('.')[-1]
      if ext=="jpg": # 读取 *.jpg to allfiles
         allfiles.append(file)       

   if len(allfiles)>0: # 将 jpg 存入 output2 目录中
      target_dir = dirname + '/' + output_dir
      if not os.path.exists(target_dir):
         os.mkdir(target_dir)      

      counter=0
      for file in allfiles:  
         filename=file.split('.')[0] #取主文件名 
         ext=file.split('.')[1]      #取扩展文件名
         m_filename = "p" + str(counter)    #重新给主文件名进行编号命名
         destfile = "{}.{}".format(target_dir+'/'+m_filename, ext) # 加上完整路径
         srcfile=dirname + "/" + file
         print(destfile)
         shutil.copy(srcfile,destfile); # 复制文件
         counter +=1
     
print("完成...")
