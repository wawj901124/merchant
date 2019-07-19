import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://bjw.halodigit.com:9060/nereus/merchant/index#/login")
        print("driver.title:%s" % self.driver.title)
        assert "QRindo Merchant" in self.driver.title

    def test_search_in_python_org(self):
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

    def test_fail(self):
        elem = self.driver.find_element_by_name("login.loginName")
        elem.clear()
        elem.send_keys("8112233666")
        elem.send_keys(Keys.TAB)  # 按tab键
        elem = self.driver.find_element_by_name("loginPwd")
        elem.clear()
        elem.send_keys("abc123456")
        elem = self.driver.find_element_by_xpath('//*[@id="login-holder"]/div[4]/form/div/div[2]/a/span')
        elem.click()
        time.sleep(5)
        time.sleep(5)
        print("driver.page_source:%s" % self.driver.page_source)
        assert "LOGIN" in self.driver.page_source

    def test_shibai(self):
        self.assertTrue(False)



    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()