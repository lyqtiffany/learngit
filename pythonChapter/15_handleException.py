#异常
#一个抓取异常的语句中至少要有try 和至少一个except,还可以加else语句和finally语句

# try:
#     a = int(input('please input a number'))
#     print(1/a)
# except ZeroDivisionError: #捕获0作为分母的异常
#     print('0不能作为分母')
# except ValueError: #捕获值异常
#     print('not number entered')
# except:  #捕获以上异常之外的所有异常
#     print('程序有错误')
# else: #如果程序正常运行，没有报错，才会执行else
#     print('没有出现异常')
# finally:  #一定会执行
#     print('程序运行完毕')

#常见的异常
# NameError #没有定义的变量
#IndexError #下标越界
#IOError #输入输出异常
#FileNotFoundError #文件不存在的异常

#所有的异常都是Exception的子类，或者子类的子类
# print(NameError.__bases__) #(<class 'Exception'>,)


#手动抛出异常
# try:
#     raise IOError  #raise，方便调试程序能否正常抛出异常
# except IOError:
#     print('文件读写错误')


#断言
# assert 1==2 #当结果为真时，断言不做事情，当结果为假时，断言生效

#日志模块
# import logging  #日志模块
# import time #时间m模块
# import traceback #导入异常信息显示模块
# logging.basicConfig(level='DEBUG',filename='d:/pythonCourse/alog1.log', filemode='a') #调整打印日志的级别
# logging.debug('debug')
# logging.info('info')
# logging.warning('warning') #默认显示warning及以上的级别
# logging.error('error')
# logging.critical(time.strftime('%y-%m-%d %H-%M-%S')+'critical error')
#
# try:
#     a = int(input('please input a number'))
#     print(1/a)
# except ZeroDivisionError: #捕获0作为分母的异常
#     logging.error(time.strftime('%y-%m-%d %H-%M-%S')+traceback.format_exc()) #把异常记录到日志文件里面
# except ValueError: #捕获值异常
#     logging.error(time.strftime('%y-%m-%d %H-%M-%S')+traceback.format_exc())

#打印200以内的质数
for i in range(2, 200):
    count = 0
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i)
        # print(i, end = ',') #print默认换行，现在是用逗号隔开




