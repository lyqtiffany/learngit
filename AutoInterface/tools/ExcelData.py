#1获取excel数据, body, 请求体，预期结果
#2传入接口代码  #请求体
#3写入测试结果，pass/fail 预期结果与实际结果对比

import xlrd
from xlutils.copy import copy
import json

#字典--存储结构
#json字符串


#1获取excel数据, body, 请求体，预期结果
def get_excel_data(sheetName, caseName):
    '''
    :param sheetName: 表名
    :param caseName: 用例名
    :return: 一个列表嵌套元组[(请求头1),(期望数据1)，(请求头2),(期望数据2) ]
    '''
    resList = [] #存结果
    excelDir = '../data/在线考试系统接口测试用例-v1.3.xls'
    #1打开excel对象 ---formatting_info=True  保持样式
    workBook = xlrd.open_workbook(excelDir, formatting_info=True)
    #2对某一个sheet操作
    workSheet = workBook.sheet_by_name(sheetName)
    #3 获取值 第6列，第8列
    print(workSheet.col_values(0)) #打印第0列的内容

    #获取数据
    idx = 0 #从第0行开始操作-也可以从第1行（根据实际sheet）
    for one in workSheet.col_values(0): #每一行遍历，检查要执行的case是否在第0列的某一行
        if caseName in one: #如果需要执行的case名称在这一行， 说明这条用例是我们需要的
            #请求体--单元格数据--cell(行号，列号，行号从0开始，列号从1开始)
            reqBody = workSheet.cell(idx, 6).value
            respData = workSheet.cell(idx, 8).value  #期望数据'
            #每一行数据增加返回list里
            #字符串--转化--字典 dict= json.loads(json数据)
            resList.append((json.loads(reqBody),json.loads(respData))) #字符串格式,转化为字典，字典打印是单引号，json是双引号
        idx += 1 #每次遍历一次，就准备操作下一行
    return resList

if __name__ == '__main__':
    res = get_excel_data('1-登录模块','login')
    for one in res:
        print(one)


