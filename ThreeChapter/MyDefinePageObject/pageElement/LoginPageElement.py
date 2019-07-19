from ThreeChapter.MyDefinePageObject.GlobalConfig.GlobalConfig import *

class LoginPage(object):
    if IS_ONLINE:
        PageUrl = "%s/nereus/merchant/index#/login" % ONLINE_DOMAIN_NAME
    else:
        PageUrl = "%s/nereus/merchant/index#/login" % TEST_DOMAIN_NAME

    Account = ""
    AccountInput = ""
    AccountInputName = "login.loginName"
    AccountInputTip = ""
    Password = ""
    PasswordInput = ""
    PasswordInputName = "loginPwd"
    PasswordInputTip = ""

    LoginButton = ""
    LoginButtonXpath = '//*[@id="login-holder"]/div[4]/form/div/div[2]/a/span'
    LoginButtonTip = ""



loginpage = LoginPage()

