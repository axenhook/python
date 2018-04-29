import requests
url = 'http://www.wsbookshow.com/'
html = requests.get(url)
html.encoding="gbk"

htmllist = html.text.splitlines()
n=0
for row in htmllist:
    if "新概念" in row: n+=1
print("找到 {} 次!".format(n))