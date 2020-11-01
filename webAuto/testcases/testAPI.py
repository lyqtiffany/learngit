from webAuto.lib.ShowapiRequest import ShowapiRequest

r = ShowapiRequest("http://route.showapi.com/184-4", "404646", "2237bfbf1ea3472fbe4b8b69fc6b9a00")
#r = ShowapiRequest("http://route.showapi.com/184-4","272526","a924d4e982ae404b8a068b4d1c7784f2")

r.addFilePara("image", "test.png") #抠图后的图
r.addBodyPara("typeId", "34")
r.addBodyPara("convert_to_jpg", "0")
r.addBodyPara("needMorePrecise", "0")
res = r.post()
print(res.text) # 返回信息
body = res.json()['showapi_res_body']
print(body['Result'])