import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


#谷歌浏览器
path = r"%s/driver/chromedriver.exe" % str(os.path.dirname(os.path.abspath(__file__))) # 配置驱动路径
print("path:%s" % path)
option = webdriver.ChromeOptions()
option.add_argument('--user-data-dir=C:\\Users\\Administrator\\Local\\Google\\Chrome\\User Data\\Default')  # 设置成用户自己的数据目录# 浏览器输入chrome://version 下个人资料路径就是自己的数据目录
driver = webdriver.Chrome(executable_path=path, chrome_options=option)

# #火狐浏览器
# driver = webdriver.Firefox()
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
print("driver.page_source:%s" % driver.page_source)
assert "No results found." not in driver.page_source
driver.close()