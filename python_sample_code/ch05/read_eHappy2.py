import requests
url = 'http://www.wsbookshow.com/'
html = requests.get(url)
html.encoding="gbk"
htmllist = html.text.splitlines()
for row in htmllist:
   print(row)
