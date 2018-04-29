import requests
from bs4 import BeautifulSoup
url = 'http://www.baidu.com'
html = requests.get(url)
sp = BeautifulSoup(html.text, 'html.parser')