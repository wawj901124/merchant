import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from ThreeChapter.MyDefinePageObject.GlobalConfig.GlobalConfig import *
from ThreeChapter.MyDefinePageObject.MyUtil.my_log import mylog


class MyBaseFunction(object):
    def __init__(self):
        if WEBDRIVERCONFIG == "1":
            self.driver = webdriver.Firefox()
        elif WEBDRIVERCONFIG == "2":
            self.driver = webdriver.Chrome()
        elif WEBDRIVERCONFIG == "3":
            self.driver = webdriver.Ie()

    def PrintLog(self,context):
        mylog.printDebugLog(context)

    def PrintErrorLog(self,context):
        mylog.printErrorLog(context)

    def OpenUrl(self,url):
        self.driver.get(url)
        self.PrintLog("打开网址：%s.\n" % url)

    def DelayTime(self,delayTime):
        time.sleep(int(delayTime))
        self.PrintLog("等待%s秒...\n" % delayTime)

    def FindElementByXpath(self,xpath):
        try:
            ele = self.driver.find_element_by_xpath(xpath)
            self.PrintLog("定位到xpath为：%s的元素.\n" % xpath)
        except Exception as e:
            self.PrintErrorLog("出现异常，问题原因：%s.\n" % e)
        return ele

    def FindElementByName(self,name):
        try:
            ele = self.driver.find_element_by_name(name)
            self.PrintLog("定位到name为：%s的元素.\n" % name)
        except Exception as e:
            self.printErrorLog("出现异常，问题原因：%s.\n" % e)
        return ele

    def ElementClick(self,ele):
        ele.click()
        self.PrintLog("点击该元素.\n")
        self.DelayTime(3)

    def ElementInput(self,ele,inputtext):
        ele.clear()
        self.PrintLog("清除该元素中的内容.\n")
        ele.send_keys(inputtext)
        self.PrintLog("往该元素中输入：%s.\n"% inputtext)
    

    def AssertSomethingInPageSource(self,asserttext):
        assert asserttext in self.driver.page_source
        self.PrintLog("页面中存在：%s\n" % asserttext)

    def AssertSomethingNotInPageSource(self,asserttext):
        assert asserttext not in self.driver.page_source
        self.PrintLog("页面中不存在：%s\n" % asserttext)












