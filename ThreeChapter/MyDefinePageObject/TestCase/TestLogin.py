import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from ddt import ddt,data,unpack

from ThreeChapter.MyDefinePageObject.BaseFunction.MyBaseFuction import MyBaseFunction
from ThreeChapter.MyDefinePageObject.pageElement.LoginPageElement import loginpage


@ddt
class TestLoginClass(unittest.TestCase):  # 创建测试类

    @classmethod  # 类方法，只执行一次，但必须要加注解@classmethod,且名字固定为setUpClass
    def setUpClass(cls):
        pass

    @classmethod  # 类方法，只执行一次，但必须要加注解@classmethod,且名字固定为tearDownClass
    def tearDownClass(cls):
        pass

    def setUp(self):  # 每条用例执行测试之前都要执行此方法

        # 火狐浏览器
        self.mybasefunction  = MyBaseFunction()
        self.driver = self.mybasefunction.driver
        self.mybasefunction.OpenUrl(loginpage.PageUrl)
        # self.driver.get("https://bjw.halodigit.com:9060/nereus/merchant/index#/login")
        # print("driver.title:%s" % self.driver.title)
        # assert "QRindo Merchant" in self.driver.title
        pass


    def tearDown(self):  # 每条用例执行测试之后都要执行此方法
        self.driver.quit()
        pass


    def definelogin(self,account, password, asserttext):
        self.mybasefunction.AssertSomethingNotInPageSource(asserttext)
        ele = self.mybasefunction.FindElementByName(loginpage.AccountInputName)
        self.mybasefunction.ElementInput(ele,account)
        ele = self.mybasefunction.FindElementByName(loginpage.PasswordInputName)
        self.mybasefunction.ElementInput(ele,password)
        ele = self.mybasefunction.FindElementByXpath(loginpage.LoginButtonXpath)
        self.mybasefunction.ElementClick(ele)
        self.mybasefunction.DelayTime(10)
        self.mybasefunction.AssertSomethingInPageSource(asserttext)

    # 下面的(("81122336666","abc123456", "Applications list"),
    #           ("83344567832","abc123456","Incorrect account or password")
    #           )代表我们传入的参数,每次传入三个值
    @data(("81122336666","abc123456", "Applications list"),
          ("83344567832","abc123456","Incorrect account or password")
          )
    # 告诉我们的测试用例传入的是两个以上的值
    @unpack
    # 定义三个参数用于接收我们传入的参数
    def test(self,account, password, asserttext):
        self.definelogin(account, password, asserttext)


if __name__ == '__main__':
    print("hello world")
    unittest.main()










