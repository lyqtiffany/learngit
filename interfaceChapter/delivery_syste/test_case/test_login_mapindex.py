
# 1 获取excel对应的数据
# 2 调用封装好的接口库代码
#3 调试运行
from interfaceChapter.delivery_syste.tools.excelControl import get_excel_data, set_excelData,get_excel_rowNum
from interfaceChapter.delivery_syste.libs.login import Login

#http://121.41.14.39:8082/doc.html#/home  swagger 接口文档


workBookNew,workSheetNew = set_excelData()#元组

# 1、读取excel数据,请求体和期望结果,有效用例的行数
resList,indexList = get_excel_data('登录模块','Login')  #返回请求体，期望结果，行数
# print(resList)
# print(indexList)

#2- 把excel读取的数据关联到请求代码里
for one in range(len(resList)):

    res = Login().login(resList[one][0])#传入对应行的body,0处是body, 1处是期望结果

    #3-实际与预期相对比，结果写入测试结果到excel----做判断--断言
    if res['msg'] == resList[one][1]['msg']: #
    # 写入成功！
        workSheetNew.write(indexList[one],12,str(res))#workSheetNew.write(行号，列号，值),#每个res是字典
        workSheetNew.write(indexList[one], 13, 'pass')
    else:
    # 写入没有成功！
        workSheetNew.write(indexList[one], 12, str(res))  # workSheetNew.write(行号，列号，值)
        workSheetNew.write(indexList[one], 13, 'fail')
 # 4 写入结果
workBookNew.save('../data/res.xls')






