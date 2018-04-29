from selenium import webdriver #导入webdriver
url='http://www.wsbookshow.com/bookshow/jc/bk/cxsj/12442.html'  #以此链接为例
browser=webdriver.Chrome()  #生成Chrome浏览器对象(结果是打开Chrome浏览器)
browser.get(url)    #在浏览器中打开url
login_form=browser.find_element_by_id("menu_1")   ##查找id="menu_1"的元素
print(login_form.text)   #显示元素内容
browser.quit()   #退出浏览器，退出驱动程序
username=browser.find_element_by_name("username")   #查找name="username"的元素
password=browser.find_element_by_name("pwd")  #查找name="pwd"的元素
login_form=browser.find_element_by_xpath("//input[@name='arcID']")
login_form=browser.find_element_by_xpath("//div[@id='feedback_userbox']")
continue_link=browser.find_element_by_link_text('新概念英语')
continue_link=browser.find_element_by_link_text('英语')
heading1=browser.find_element_by_tag_name('h1')
content=browser.find_elements_by_class_name('topbanner')
content=browser.find_elements_by_css_selector('.topsearch')
#print(content.get_property)
browser.quit()   #退出浏览器，退出驱动程序