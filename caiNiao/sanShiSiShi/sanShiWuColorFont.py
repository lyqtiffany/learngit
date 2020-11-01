#35题目：文本颜色设置

# !/usr/bin/python
# -*- coding: UTF-8 -*-
# 转义序列是以ESC开头,即用\033来完成（ESC的ASCII码用十进制表示是27，用八进制表示就是033）。
#格式：\033[显示方式;前景色;背景色m
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[4;93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


print(bcolors.WARNING + "警告的颜色字体?" + bcolors.ENDC)