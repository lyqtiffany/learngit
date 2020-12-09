#一个.py文件就是一个模块
#组织存放模块的目录，我们称之为包，可能是文件夹
#文件夹和包的区别，如果文件夹下面有一个__init__.py文件，这个文件夹就称为包
#当加载某个包时，里面的__init__.py文件会自动执行一次

#模块起名时，按规范应该是用字母开头，首位不应该是数字
#from 包 import 模块
# from pythonChapter import aabbcc

# 模块化的其他好处
# 用库的形式封装功能，方便给别的代码调用
# 避免变量名冲突（包括函数名）
#   每个模块中的变量名作用域只在本模块中



#内置函数，不需要额外加载，直接使用的， print()
#python标准库，指加载之后就能使用的   import this #加载<python之禅> #python标准库
#第三方库，需要先安装后才能使用的 , e.g. selenium

#加载模块值需要模块名字，不需要.py

# 模块的使用
# 导入模块的几种方式
# import aabbcc #加载aabbcc模块， aabbcc模块在同一个包、目录下面
# print(aabbcc.fuc1(2, 3)) #调用aabbcc模块里面的fuc1函数
#对于同一个目录下的模块，如果有红色波浪线，可以右键此目录，选择mark directory as-->source root,将其加入到标准路径
#如果是灰色波浪线，选择右下角的小侦探图标，将进度条向左移动，就可以取消

#from 包 import 模块
# from pythonChapter import aabbcc
# print(aabbcc.fun1(3,4))

#from 包.模块 import 函数 #直接从指定模块里面导入函数
# from pythonChapter.aabbcc import fun1
# print(fun1(5,6))

# from 模块 import 函数  #同目录下，加载指定函数，省时省空间
# from aabbcc import fun1
# print(fun1(11,12))

# from 模块 import * #加载模块下的所有内容

#通过起别名来区分不同模块的同名函数
# from aabbcc import fun1 as s1
# from qqddcc import fun1 as s2

#同时导入多个模块，中间用逗号隔开
# if __name__ == '__main__': #main下面的语句只在本模块内部执行,主要用来调试
# import aabbcc
# print(aabbcc.__name__) #打印这个模块的文件名,
