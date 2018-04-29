import hashlib,os,requests 

url = "http://opendata.epa.gov.tw/ws/Data/REWXQA/?\
$orderby=SiteName&$skip=0&$top=1000&format=json"

# 读取网页原始码
html=requests.get(url).text.encode('utf-8-sig')
# 判断网页是否更新
md5 = hashlib.md5(html).hexdigest()
if os.path.exists('old_md5.txt'):
    with open('old_md5.txt', 'r') as f:
        old_md5 = f.read()
    with open('old_md5.txt', 'w') as f:
        f.write(md5)
else:
    with open('old_md5.txt', 'w') as f:
        f.write(md5)

if md5 != old_md5:
    print('数据已更新...') 
else:
    print('数据未更新，从数据库读取...')
