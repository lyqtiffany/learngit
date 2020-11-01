#增加留言
import requests
from AutoInterface.configs.config import HOST
from AutoInterface.lib.apiLib.login import Login

#1--封装类
class Msg:
    def add_msg(self, inToken, inData):#增加留言
        '''
        :param inToken: 登录接口获取的token
        :param inData: 留言新增的body
        :return: 响应体
        '''
        url = f'{HOST}/api/message'
        #请求头--需要带token,  --格式是字典{键：值}
        header = {'X-AUTH-TOKEN': inToken, 'content-type': 'application/json'}
        payload = inData
        resp = requests.post(url, json=payload, headers=header)
        return resp.json()
if __name__ == '__main__':
    #1-登陆操作-获取token
    token = Login().login({'username': '20154084', 'password': '123456'}, getToken=True)
    #新增留言接口
    info = {'title': '留言标题sq', 'content': '留言内容'}
    res = Msg().add_msg(token, info)
    print(res) #留言id可以作为后续的删除，回复操作

