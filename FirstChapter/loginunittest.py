import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys



class TestLoginClass(unittest.TestCase):  # 创建测试类

    @classmethod  # 类方法，只执行一次，但必须要加注解@classmethod,且名字固定为setUpClass
    def setUpClass(cls):
        # cls.activeweb = ActiveWeb()  # 实例化
        # cls.loginpage = LoginPage()  # 实例化
        #
        # url = "%s/nereus/agent/v/#/login" % WEB_URL_TITLE  # 代理商后台
        # # url = "https://m-mbmpay.ahdipay.com/nereus/agent/index"   #现网
        # cls.activeweb.getUrl(url)  # 打开网址
        pass

    @classmethod  # 类方法，只执行一次，但必须要加注解@classmethod,且名字固定为tearDownClass
    def tearDownClass(cls):
        # cls.activeweb.closeBrowse()
        pass

    def setUp(self):  # 每条用例执行测试之前都要执行此方法
        # #谷歌浏览器
        # path = r"%s/driver/chromedriver.exe" % str(os.path.dirname(os.path.abspath(__file__))) # 配置驱动路径
        # print("path:%s" % path)
        # option = webdriver.ChromeOptions()
        # option.add_argument('--user-data-dir=C:\\Users\\Administrator\\Local\\Google\\Chrome\\User Data\\Default')  # 设置成用户自己的数据目录# 浏览器输入chrome://version 下个人资料路径就是自己的数据目录
        # driver = webdriver.Chrome(executable_path=path, chrome_options=option)

        # 火狐浏览器
        self.driver = webdriver.Firefox()
        self.driver.get("https://bjw.halodigit.com:9060/nereus/merchant/index#/login")
        print("driver.title:%s" % self.driver.title)
        assert "QRindo Merchant" in self.driver.title

        pass


    def tearDown(self):  # 每条用例执行测试之后都要执行此方法
        self.driver.close()
        pass

    # @unittest.skip('testLoginSuccess')
    def testLoginSuccess(self):
        elem = self.driver.find_element_by_name("login.loginName")
        elem.clear()
        elem.send_keys("81122336666")
        elem.send_keys(Keys.TAB)  # 按tab键
        elem = self.driver.find_element_by_name("loginPwd")
        elem.clear()
        elem.send_keys("abc123456")

        elem = self.driver.find_element_by_xpath('//*[@id="login-holder"]/div[4]/form/div/div[2]/a/span')
        elem.click()
        time.sleep(5)
        time.sleep(5)
        print("driver.page_source:%s" % self.driver.page_source)
        assert "Applications list" in self.driver.page_source

    @unittest.skip('testLoginFail')
    def testLoginFail(self):
        elem = self.driver.find_element_by_name("login.loginName")
        elem.clear()
        elem.send_keys("83344567832")
        elem.send_keys(Keys.TAB)  # 按tab键
        elem = self.driver.find_element_by_name("loginPwd")
        elem.clear()
        elem.send_keys("abc123456")

        elem = self.driver.find_element_by_xpath('//*[@id="login-holder"]/div[4]/form/div/div[2]/a/span')
        elem.click()
        time.sleep(5)
        time.sleep(5)

        print("driver.page_source:%s" % self.driver.page_source)
        assert "Incorrect account or password" in self.driver.page_source


print("loginunittest文件中的__name__：%s"%__name__)

if __name__ == '__main__':
    print("hello world")
    unittest.main()










