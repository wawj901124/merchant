import unittest

from SecondChapter.htmltest import HTMLTestRunner_my as HTMLTestRunner
from SecondChapter.logindefinefunction import TestLoginClass
from SecondChapter.myemail.send_attach_email import SendEmail



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
result = runner.run(mySuite)
# print("Result:%s" % result)
# print("Result_success:%s" % result.success_count)
# print("Result_failure:%s" % result.failure_count)
# print("Result_error:%s" % result.error_count)

fp.close()

# 发送report至邮箱
send_e = SendEmail()
user_list = ['xiangkaizheng@iapppay.com']
emailtitle = u'商户后台登录 自动化测试_测试报告'
send_e.send_main_result_num(result.success_count, result.failure_count,result.error_count,filename,user_list,emailtitle)