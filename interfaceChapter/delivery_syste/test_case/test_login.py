
# 1 获取excel对应的数据
# 2 调用封装好的接口库代码
#3 调试运行
from interfaceChapter.delivery_syste.tools.excelControl import get_excel_data, set_excelData,get_excel_rowNum
from interfaceChapter.delivery_syste.libs.login import Login


#http://121.41.14.39:8082/doc.html#/home  swagger 接口文档

# res = get_excel_data('登录模块','Login')
# print(res)

workBookNew,workSheetNew = set_excelData()#元组
excelData = get_excel_data('登录模块','Login')
numList = get_excel_rowNum('登录模块','Login')

for one in range(len(excelData)):
    # print(one)
    bodyData = one[0] #请求头
    respData = one[1] #响应体
    # bodyData, respData = one #合成一个步骤

    res = Login().login(bodyData)
    #print(res)

    if one in numList:
        #断言
        if res['msg'] == respData['msg']:
            info = 'pass'

            workSheetNew.write(excelData.index(one) + 1, 12, info)  # (行号，列号，字符串内容)
        else:
            info = 'fail'

            workSheetNew.write(excelData.index(one) + 1, 12, info)
        #print(info)
workBookNew.save('../data/res.xls')
 # 4 写入结果





