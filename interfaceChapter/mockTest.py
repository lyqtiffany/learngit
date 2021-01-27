HOST = "http://127.0.0.1:9999"
import requests

url = f'{HOST}/xintian_sq'
#payload = {"key1":"abc"}  #queries里面的内容
# resp = requests.post(url, data=payload)
resp = requests.get(url)
print(resp.text)

print(resp)


#配置不同的请求
#修改完json文件需要保持


#约定URI

# #约定请求参数-form
# payload_form = {"key1":"abc"}
# url_form = f'{HOST}/abc5'
# resp_form = requests.post(url_form, data=payload)  #表单用data
#
# #约定请求参数 json
# payload_json = {"key1":"value1", "key2":"value2"}
# url_json = f'{HOST}/abc6'
# resp_json = requests.post(url_form, json=payload)  #表单用data
#约定方法
#约定头

#约定请求体参数

#uri-startsWith匹配，模糊匹配
# uri startsWith /sqa 只要url是/sqa, 或者/sqa开头，都可以访问

#返回状态码
#返回json格式的数据



