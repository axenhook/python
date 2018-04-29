import requests,os
from bs4 import BeautifulSoup
from urllib.request import urlopen

url = 'http://www.tooopen.com/img/87.aspx'

html = requests.get(url)
html.encoding="utf-8"

sp = BeautifulSoup(html.text, 'html.parser')

# 建立images目录保存图片
images_dir="images/"
if not os.path.exists(images_dir):
    os.mkdir(images_dir)
    
# 取得所有 <a> 和 <img> 标签
all_links=sp.find_all(['a','img']) 
for link in all_links:
    # 读取 src 和　href 属性内容
    src=link.get('src')
    href = link.get('href')
    attrs=[src,src]
    for attr in attrs:
        # 读取　.jpg 和　.png 檔
        if attr != None and ('.jpg' in attr or '.png' in attr):
            # 设置图片文件完整路径
            full_path = attr            
            filename = full_path.split('/')[-1]  # 取得图片名
            ext = filename.split('.')[-1]  #取得扩展名
            filename = filename.split('.')[-2] #取得主文件名
            if 'jpg' in ext: filename = filename + '.jpg'
            else:            filename = filename + '.png'
            print(attr)
            # 保存图片
            try:
                image = urlopen(full_path)
                f = open(os.path.join(images_dir,filename),'wb')
                f.write(image.read())
                f.close()
            except:
                print("{} 无法读取!".format(filename))


