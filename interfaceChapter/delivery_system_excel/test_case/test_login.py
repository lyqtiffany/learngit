from interfaceChapter.delivery_system_excel.libs.login import Login
from interfaceChapter.delivery_system_excel.tools.excelControl import get_excel_data,set_excelData

import json


# http://121.41.14.39:8082/doc.html#/default/  swagger接口文档

excelData, indexList = get_excel_data('登录模块', 'Login')

actual_result_List = []
status_List = []


for one in range(len(excelData)):

    res = Login().login(excelData[one][0])  #0是body, 1是期望结果

    actual_result_List.append(str(res))   # 每个res是字典,需要转成str

    if res['msg'] == excelData[one][1]['msg']:
        status = 'pass'
    else:
        status = 'fail'
    status_List.append(status)


# 4 写入结果
set_excelData(0, indexList, actual_result_List, status_List) #0是登录模块的sheet下标



