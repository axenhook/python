from selenium import webdriver
from time import sleep

urls = ['http://www.baidu.com',
        'http://www.wsbookshow.com',
        'http://news.sina.com.cn/']

browser = webdriver.Chrome()
browser.maximize_window
for url in urls:
    browser.get(url) 
    sleep(3)

browser.quit()