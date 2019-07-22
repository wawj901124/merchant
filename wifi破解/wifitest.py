import pywifi   #导入pywifi
from pywifi import const   #引用一些常量

#判断是否已经连接到wifi环境
def gic():
    #创建一个无线的对象
    wifi = pywifi.PyWiFi()
    print(wifi)
    #获取到第一个无线网卡
    ifaces = wifi.interfaces()[0]
    #列表
    print(ifaces)
    #打印网卡的名称
    print(ifaces.name())
    #打印网卡的连接状态: 0表示未连接到wifi环境  4表示连接到
    print(ifaces.status())
    #IFACE_CONNECTED表示连接状态， connect 连接
    print(const.IFACE_CONNECTED)
    if ifaces.status() == const.IFACE_CONNECTED:
        print("已连接")
    else:
        print("未连接")

gic()


#扫描附近的wifi
def bies():
    #创建一个无线的对象
    wifi = pywifi.PyWiFi()
    #获取wifi的第一个网卡（一般的笔记本电脑也就一个网卡）
    iface = wifi.interfaces()[0]
    #扫描wifi
    iface.scan()
    #获取扫描结果
    result = iface.scan_results()
    #打印获取到的结果
    print(result)
    #获取扫描结果wifi的名称
    for data in result:
        #打印wifi的名称，ssid:shi
        print(data.ssid)

bies()
