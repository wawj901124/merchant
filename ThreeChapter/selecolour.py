from selenium.webdriver.support.color import Color
from SecondChapter.my_log import MyLog

uselog = MyLog(Color.from_string('#00ff33').rgba)

uselog.printLog()
print(Color.from_string('rgb(1, 255, 3)').hex)
print(Color.from_string('blue').rgba)