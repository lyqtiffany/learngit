from interfaceChapter.delivery_system_excel.libs.login import Login
from interfaceChapter.delivery_system_excel.tools.excelControl import get_excel_data, set_excelData
from interfaceChapter.delivery_system_excel.libs.shop import Shop
import pprint

token = Login().login({'username': 'sq0777', 'password': 'xintian'}, getToken=True)

#获取用例中的请求体和期望结果，获取有效用例的行数
inData, indexList = get_excel_data('我的商铺', 'listshopping')

actual_result_List = []
status_List = []

# for i in range(1):
for i in range(len(inData)):
    bodyData = inData[i][0]
    expData = inData[i][1]

    shop = Shop(token)

    res = shop.shop_list(bodyData) #列出商品的返回结果

    actual_result_List.append(str(res)) #保存返回结果

    if 'code' in res:
        if res['code'] == expData['code']:
            status = 'pass'
        else:
            status = 'fail'
    elif 'error' in res:
        if res['error'] == expData['error']:
            status = 'pass'
        else:
            status = 'fail'
    else:
        status = 'fail'
    status_List.append(status) #保存状态结果

set_excelData(1, indexList, actual_result_List, status_List) # 1是登录模块的sheet下标



