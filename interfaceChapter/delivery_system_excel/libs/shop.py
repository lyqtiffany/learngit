import requests

from interfaceChapter.delivery_system_excel.configs.config import HOST
from interfaceChapter.delivery_system_excel.libs.login import Login
from interfaceChapter.delivery_system_excel.tools.excelControl import get_excel_data,set_excelData


class Shop:
    # 操作店铺，需要token
    def __init__(self,inToken):
        self.header = {'Authorization': inToken} #请求头

    #列出商铺
    def shop_list(self, inData):

        payload = inData
        url = f'{HOST}/shopping/myShop'
        resp = requests.get(url,headers = self.header, params=payload)
        # print(resp.json())
        return resp.json()

if __name__ == '__main__':
    token = Login().login({'username': 'sq0777', 'password': 'xintian'}, getToken=True)
    # print(token)

    inData, indexList = get_excel_data('我的商铺','listshopping')
    for i in range(len(inData)):
        bodyData = inData[i][0]
        expData = inData[i][1]




