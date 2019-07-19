#!/usr/bin/python3
# -*- coding:utf-8 -*-
from selenium import webdriver
import time
import unittest
from ddt import ddt,data,unpack



a=1
print(a)
@ddt
class test_merchant(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("-----------测试开始-------------")

    @classmethod
    def tearDownClass(cls):
        print("------------测试结束-------------")

    def setUp(self):
        self.browser=webdriver.firefox()
        self.browser.get('https://bjw.halodigit.com:9060/nereus/merchant/index#/login')
        self.browser.maximize_window()
        time.sleep(3)

    def tearDown(self):
        self.browser.quit()

    @data(['loginname','password'],)
    @unpack
    def test(self,loginname,password):
        browser = self.browser
        browser.find_element_by_id('loginName').send_keys(loginname)
        browser.find_element_by_id('loginPwd').send_keys(password)
        browser.find_elements_by_css_selector('.btn')[2].click()
        assert 'The length cannot be less than10' in browser.page_source
        errormsg = browser.find_elements_by_css_selector('.w5c-error')[0].text
        print(errormsg)


if __name__ == '__main__':
    unittest.main()
else:
    print(2)
