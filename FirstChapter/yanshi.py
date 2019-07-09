from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()   #启动浏览器
driver.get("https://bjw.halodigit.com:9060/nereus/merchant/index#/login")  #加载网址
print(driver.title)
assert "QRindo Merchant" in driver.title  #断言title
print(driver.page_source)
# print(driver.title)
elem = driver.find_element_by_name("login.loginName")  #输入账号
elem.clear()
elem.send_keys("81122336666")
elem = driver.find_element_by_name("loginPwd")  #输入密码
elem.clear()
elem.send_keys("abc123456")
elem.send_keys(Keys.RETURN)

time.sleep(5)
time.sleep(5)
# print(driver.page_source)
assert "Search"  in driver.page_source
driver.close()