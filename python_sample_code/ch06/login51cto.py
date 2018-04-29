from selenium import webdriver
from time import sleep

url = 'http://www.51cto.com/'

browser = webdriver.Chrome()
browser.maximize_window
browser.get(url)

browser.find_element_by_xpath('//*[@id="login_status"]/a[1]').click() #获取“登录”元素
broser.find_element_by_xpath('//*[@id="loginform-username"]').clear()#清空输入框
browser.find_element_by_xpath('//*[@id="loginform-username"]').send_keys('oomms') #填写用户名
broser.find_element_by_xpath('//*[@id="loginform-password"]').clear() #清空输入框
browser.find_element_by_xpath('//*[@id="loginform-password"]').send_keys('abc123') #填写密码
sleep(3)  #加入等待
browser.find_element_by_xpath('//*[@id="login-form"]/div[3]/input').click()  #单击“登录”按钮