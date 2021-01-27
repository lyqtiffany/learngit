
# 日志的配置设置
import logging
import datetime

def logger(name=__name__): #执行的模块名字
    #1 日志的名称： 路径+名字(进程名字/日期)+后缀
    logname = f"../logs/{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.log"

    #2 创建日志文件对象
    loggerObject = logging.getLogger(name) #

    #3 日志级别
    loggerObject.setLevel(logging.INFO)

    #4 日志文件的属性，mode =a 就是追加方式，只有一个文件
    rHandle = logging.FileHandler(logname,mode='w', encoding="utf-8")

    # 5 日志内容的格式
    #
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s[%(lineno)d]: %(message)s  " )
    rHandle.setFormatter(formatter)
    loggerObject.addHandler(rHandle)

    return loggerObject

if __name__ == '__main__':
    log = logger()













