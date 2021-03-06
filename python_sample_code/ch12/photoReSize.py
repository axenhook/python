import os
from PIL import Image

image_dir = 'resized_photo'
image_width = 800

cur_path=os.path.dirname(__file__) # 取得当前路径
sample_tree=os.walk(cur_path)

for dirname,subdir,files in sample_tree:
    allfiles=[] 
    basename= os.path.basename(dirname)
    if basename == image_dir:  # resized_photo 目录不再重复处理
        continue  
    for file in files:  # 取得所有 .png .jpg 文件，存入 allfiles 列表中
        ext=file.split('.')[-1]
        if ext=="png" or ext=="jpg":
            allfiles.append(dirname +'/'+file)
         
    if len(allfiles)>0: 
        target_dir = dirname + '/' + image_dir
        if not os.path.exists(target_dir):
            os.mkdir(target_dir)
        for file in allfiles:
            pathname,filename = os.path.split(file)
            img = Image.open(file)
            w,h = img.size
            img = img.resize((image_width,int(image_width/float(w)*h)))
            img.save(target_dir+'/'+filename)
            print("<{}> 复制完成!".format(target_dir+'/'+filename))
            img.close()
            
print("完成...")  
