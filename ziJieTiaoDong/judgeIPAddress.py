# 判断是否是合法的IP地址
def isIpVsAddrLegal(ipStr):

    if '.' not in ipStr:  #判断字符串里面有没有.
        return False

    #用.切割ip地址为一个列表
    ip_split_list = ipStr.strip().split('.')

    if len(ip_split_list) != 4: # 切割后列表必须要有四个元素
        return False

    for i in range(4):
        try:
            ip_split_list[i] = int(ip_split_list[i])
        except:
            print("IP invalid for not number: "+ ipStr)  #每个参数必须为数字，否则校验失败
            exit()  #退出，不再判断后续的字符串

        if ip_split_list[i] <= 255 and ip_split_list[i] >= 0:  #每个参数值必须在0-255之间
            pass
        else:
            print("IP invalid: " + ipStr)
            return False

    if int(ip_split_list[0] == 0):  #first 参数 is not 0
        print("ip format wrong")
        exit() #退出，不再判断后续的字符串

    return True

if __name__ == '__main__':
    testIP = 'a.b.c.d'
    #print(isIpVsAddrLegal(testIP))

    ip_list=['', '.', '12.2.', '11.31.137.251', '100.10.0.1000','1.1.1.1','12.23.13','aa.12.1.2','12345678','289043jdhjkbh']
    for one_str in ip_list:
        if isIpVsAddrLegal(one_str):  #字符串方法
            print('{0} is a legal ip address!'.format(one_str))


'''
IPy库是一个处理IP比较强大的第三方库。涉及到计算大量的IP地址，包括网段、网络掩码、广播地址、子网数、IP类型等别担心，Ipy模块拯救你。
Ipy模块可以很好的辅助我们高效的完成IP的规划工作。


正则表达式判定法
最简单的实现方法是构造一个正则表达式。判断用户的输入与正则表达式是否匹配。若匹配则是正确的IP地址，否则不是正确的IP地址。
下面给出相对应的验证ip的正则表达式：
^(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|[1-9])\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)$

\d表示0~9的任何一个数字
{2}表示正好出现两次
[0-4]表示0~4的任何一个数字
| 的意思是或者
1\d{2}的意思就是100~199之间的任意一个数字
2[0-4]\d的意思是200~249之间的任意一个数字
25[0-5]的意思是250~255之间的任意一个数字
[1-9]\d的意思是10~99之间的任意一个数字
[1-9])的意思是1~9之间的任意一个数字
.的意思是.点要转义（特殊字符类似，@都要加\转义）
代码如下：

import re
def check_ip(ipAddr):
    compile_ip=re.compile('^(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|[1-9])\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)$')
    if compile_ip.match(ipAddr):
        return True
    else:
        return False'''


