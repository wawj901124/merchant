from SecondChapter.htmltest import HTMLTestRunner_my as HTMLTestRunner
import unittest
from SecondChapter.logindefinefunction import TestLoginClass


mySuite= unittest.TestSuite()
mySuite.addTest(unittest.makeSuite(TestLoginClass))

filename = './myreports/report.html'
fp = open(filename, 'wb')

# 定义测试报告
runner = HTMLTestRunner.HTMLTestRunner(
    stream=fp,
    title=u'商户后台登录 自动化测试_测试报告',
    description=u'用例执行情况：',
    verbosity=2)  # verbosity=2,输出测试用例中打印的信息
runner.run(mySuite)
fp.close()