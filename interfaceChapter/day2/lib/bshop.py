
import requests

from interfaceChapter.day2.config.config import HOST
from interfaceChapter.day2.lib.bLogin_token import Login
#token的关联
#店铺的模块
class Shop: #每一个店铺的实例，都只需要鉴权一次
    def __init__(self, inToken):
        self.header = {'Authorization': inToken} #列出店铺必须要带的一个header: authorization

    # 1 列出店铺
    def shop_list(self, inData):
        url = f'{HOST}/shopping/myShop'

        #get请求，参数在url?后面
        payload = inData
        # 发请求
        # params 会把数据拼接到url后面
        resp = requests.get(url, params=payload, headers=self.header)
        print(resp.request.url)
        return resp.text

if __name__ == '__main__':
    #1 登陆
    token = Login().login({'username': 'sq0777', 'password': 'xintian'}, getToken=True)
    #列出商铺的接口调用
    res = Shop(token).shop_list({'page':1,'limit':20})
    print(res)



