
# 1 获取excel对应的数据
# 2 调用封装好的接口库代码
#3 调试运行
from interfaceChapter.delivery_syste.tools.excelControl import get_excel_data, set_excelData,get_excel_rowNum
from interfaceChapter.delivery_syste.libs.login import Login

#http://121.41.14.39:8082/doc.html#/home  swagger 接口文档


workBookNew,workSheetNew = set_excelData()#元组

# 1、读取excel数据,请求体和期望结果
resList = get_excel_data('登录模块','Login')

# 1、读取excel数据，有效用例的行数
indexList = get_excel_rowNum('登录模块', "Login") #取到下标1,2,3,4,5,6


#2- 把excel读取的数据关联到请求代码里

for one in range(0,len(resList)):#0,1,2,3,4,5

    res = Login().login(resList[one][0])#传入对应行的body,0处是body, 1处是期望结果

    if one+1 in indexList:#判断是否是有效数据

    #3-实际与预期相对比，结果写入测试结果到excel----做判断--断言
        if res['msg'] == resList[one][1]['msg']:
            # 写入成功！
            workSheetNew.write(one+1,12,'pass')#workSheetNew.write(行号，列号，值)
        else:
            # 写入没有成功！
            workSheetNew.write(one+1, 12, 'fail')  # workSheetNew.write(行号，列号，值)
workBookNew.save('../data/res.xls')
 # 4 写入结果





