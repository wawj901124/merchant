import itertools as its   #导入itertools，重名为ite

#迭代器
words = "1234567890"
r = its.product(words,repeat=5)   #生成一个3位数的密码本   10个中取3个排列组合

#将生成的数据保存在文件中
dic = open("密码本.txt","a")   #以追加的方式
for i in r:
    dic.write("".join(i))   #以空格做连接符连接各个内容
    dic.write("".join("\n"))   #加一个换行符
dic.close()   #关闭文件
