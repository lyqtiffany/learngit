
'''
目标：读取excel数据
方案：
#xlrd---xls
#openpyxl ---xlsx
    1 通过指定的行号列号去获取对应的用例数据 for 循环行号去读取数据
        -缺点 ： 如果测试人员对测试用例进行修改，导致代码报错
    2-智能读取--模糊匹配
'''
import xlrd
import json
from xlutils.copy import copy

def get_excel_data(sheetName, caseName):
    """
    :param sheetName: the sheet name which need to read data
    :param caseName: the caseName
    :return: [request body, expected result], indexList
    """
    resList = []  #存放从测试用例中读取出来的请求体和期望结果
    indexList = [] #存放
    execFile = '../data/delivery_testcase_a.xls'

    workBook = xlrd.open_workbook(execFile)
    workSheet = workBook.sheet_by_name(sheetName)

    # 获取一列数据
    # for i in range(len(workSheet.col_values(0))):
    #     print(workSheet.col_values(0)[i])

    caseNameData = workSheet.col_values(0) #第0列包含所有的case名字

    for one in caseNameData:
        if caseName in one:
            bodyData = workSheet.cell(caseNameData.index(one),9).value
            expData = workSheet.cell(caseNameData.index(one),11).value #str
            resList.append((json.loads(bodyData),json.loads(expData)))  #json.loads() #转换成为字典
            indexList.append(caseNameData.index(one))
    return resList,indexList


def set_excelData(sheetIndex, indexList, actual_result_List, status_List):
    """
    :param sheetIndex:
    :param indexList: List contains valid case row number
    :param actual_result_List: List contains actual result
    :param status_List: List contains status for each test case's status
    :return: write result to excel file
    """
    # 1原始测试用例excel表路径
    excelDir = '../data/delivery_testcase_a.xls'
    #2 打开excel 对象
    workBook = xlrd.open_workbook(excelDir,formatting_info=True)
    workBookNew = copy(workBook) #复制一个新excel文件对象
    workSheetNew = workBookNew.get_sheet(sheetIndex) #取出复制出来的新excel 文件对象的第一个子表,只能用下标

    for i in range(len(indexList)):
        workSheetNew.write(indexList[i], 12, actual_result_List[i])
        workSheetNew.write(indexList[i], 13, status_List[i])

    workBookNew.save('../data/resD.xls')




if __name__ == '__main__':
    res = get_excel_data('登录模块',"Login")
    for one in res:
        print(one)

