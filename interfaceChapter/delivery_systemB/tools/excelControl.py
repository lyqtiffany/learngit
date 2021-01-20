
'''
目标：读取excel数据
方案：
#xlrd---xls
#openpyxl ---xlsx
    1 通过指定的行号列号去获取对应的用例数据 for 循环行号去读取数据
        -缺点 ： 如果测试人员对测试用例进行修改，导致代码报错
    2-智能读取--模糊匹配
'''
import xlrd,xlwt
import json
from xlutils.copy import copy

def get_excel_data(sheetName, caseName):

    resList = []  # 存放excel读取结果

    #1 获取excel路径
    excelFile = '../data/delivery_testcaseB.xls'
    #2 需要把excel加载到内存---open, formatting_info=True保持原来的样式
    workBook = xlrd.open_workbook(excelFile, formatting_info=True)
    #3- 获取对应的sheet
    #print(workBook.sheet_names()) #获取所有的sheet名称
    workSheet = workBook.sheet_by_name(sheetName)
    #获取一行数据
    #print(workSheet.row_values(0))  #excel编号的下标从0开始
    #获取一列数据
    #print(workSheet.col_values(0))
    #print(workSheet.cell(1,9).value) #workSheet.cell(行号，列号).value

    #遍历第0列
    index = 0  #遍历变量
    for one in workSheet.col_values(0): #遍历第0列，caseName
        if caseName in one:  #如果需要的用例名字在里面
            reqBodyData = workSheet.cell(index, 9).value #请求体--字符串
            # print(reqBodyData, type(reqBodyData))
            respData = workSheet.cell(index, 11).value #响应体
            #接口需要传递的是字典格式，excel读取出来是str,需要转换 json.loads()
            resList.append((json.loads(reqBodyData), json.loads(respData))) #[(请求体1，响应体1)，(请求体2，响应体2)]
        index += 1
    return resList


def get_excel_rowNum(sheetName, caseName):

    numList = []  # 存放excel需要的行号,sheet里面可能有多个模块的用例，比如我们只需要登陆用例

    #1 获取excel路径
    excelFile = '../data/delivery_testcaseB.xls'
    #2 需要把excel加载到内存---open, formatting_info=True保持原来的样式
    workBook = xlrd.open_workbook(excelFile, formatting_info=True)
    #3- 获取对应的sheet

    workSheet = workBook.sheet_by_name(sheetName)
    index = 0  # 遍历变量
    for one in workSheet.col_values(0):  # 遍历第0列，caseName
        if caseName in one:  # 如果需要的用例名字在里面
            numList.append(index)  #
        index += 1
    return numList

def set_excelData():
    #1-excel表路径
    excelDir = '../data/delivery_testcaseB.xls'
    #2- 打开excel对象--formatting_info=True  保持样式
    workBook = xlrd.open_workbook(excelDir,formatting_info=True)
    workBookNew = copy(workBook)#复制一个新excel文件对象
    workSheetNew = workBookNew.get_sheet(0)#取复制出来的新excel文件对象的第一个子表,只能用下标
    return workBookNew,workSheetNew#复制出来的excel对象，复制出来excel对象的第一个子表

if __name__ == '__main__':
     res = get_excel_data('登录模块',"Login")
     for one in res:
        print(one)

