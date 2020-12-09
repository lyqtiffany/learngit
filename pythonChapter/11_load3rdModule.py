#加载第三方库
# import time
# print(time.strftime("%Y-%m-%d %H:%M:%S")) #按照年月日时分秒打印当前时间
# print(time.time()) #当前时间距离1970年1月1日经过了多少秒

# import os #加载操作系统模块
# os.system("calc")
# # os.system("cmd")

# import sys #加载系统模块
# # print(sys.path) #打印python的标准路径
# for one in sys.path:
#     print(one)
#打印出来第一个路径是当前路径
#第二个路径是工程路径

#把某个路径加入Python的标准路径
# sys.path.append('d:/pythonCourse')
#import modulename #不要用from pythonCourse import modulename

#所有第三方库全部安装在python安装目录下的lib\site-packages里
# C:\Users\Administrator\AppData\Local\Programs\Python\Python38\lib\site-packages

#cmd中执行安装第三方的命令
#pip install selenium #这样是从官网直接下载安装，可能网速慢，可以考虑使用国内的镜像网站
#pip install selenium -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com #豆瓣源
#pip install selenium -i https://pypi.tuna.tsinghua.edu.cn/simple/ ;--trusted-host pypi.tuna.tsinghua.edu.cn  #清华源

#安装xlwt, xlrd, pytest,selenium

#pip list #查看目前安装了哪些库，cmd执行pip list
#虚拟环境和真实环境，在创建项目的时候可以选择，尽量用真实环境

# pip show selenium #展示selenium的模块信息

#卸载第三方库
# pip uninstall module name

#安装指定版本的第三方库
#pip install selenium == 3.0.2 #指定安装3.0.2版本
#pip install selenium >= 3.0.2 #指定安装不低于3.0.2版本


#更新
# pip install selenium -u

#install ,windows的批处理文件安装第三方库

# 永久添加标准路径,
#在python安装目录下的lib\site-packages里新建一个.pth文件，里面放入要添加的路径， D:\pythonCourse


#思考题，猜数字，随机生成一个0-100之间的数字，用户猜，猜对了，游戏结束
#猜错了，提示值过大或者过小

from random import randint
result = randint(0,100)
userInput = int(input('please input a int'))
if userInput == result:
    print('correct')
elif userInput > result:
    print('>')
else:
    print('<')