#
#
# import re
import time
from selenium import webdriver
#
#实力化一个浏览器
driver = webdriver.Chrome()
#driver = webdriver.PhantomJS()
#
# #发送请求
driver.get("http://www.baidu.com")

#元素定位
driver.find_element_by_id("kw").send_keys("python")
time.sleep(5)
driver.find_element_by_id("su").click()

#p-js进行页面截屏
driver.save_screenshot("./baidu.png")

'''
cookies = driver.get_cookies()
print(cookies)
print("*"*100)
只获取cookies中的name,value,用字典推倒式
cookie = {i['name']:i['value'] for i in cookies}
print(cookie)

'''

time.sleep(10)
#退出浏览器
driver.quit()



