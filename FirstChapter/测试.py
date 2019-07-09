# -*- coding: UTF-8 -*-
import unittest

class testclass(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("---------类开始-----------")




    def testcase_1(cls):
        print("测试开始：1111")

    @classmethod
    def tearDownClass(cls):
        print("--------类结束------------")



if __name__==("__main__"):
    unittest.main(verbosity=2)