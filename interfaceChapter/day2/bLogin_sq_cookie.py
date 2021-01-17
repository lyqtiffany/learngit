# cookie关联操作

fiddler_proxies = {       #fiddler 抓Python脚本的请求
    'http':'http://127.0.0.1:8888',
    'https':'https://127.0.0.1:8888'
}

import requests

# requests.packages.urllib3.disable_warnings() #处理HTTPS警告
#resp = requests.post(url, data= payload, verify =False) #verify=False表示不使用SSL

def login():
    url = 'http://120.55.190.222:7080/api/mgr/loginReq'
    # url = 'http://127.0.0.1/api/mgr/loginReq'

    payload = {'username': 'auto', 'password': 'sdfsdfsdf'}
    resp = requests.post(url, data= payload)
    #return resp.text
    #return resp.cookies #方案1， 直接关联原始cookie

    #如果项目需求，需要定制化cookies: sessionid+token--需要自己封装cookies
    #cookies里面就是sessionID--直接取出sessionID
    return resp.cookies['sessionid'] #方案2

    # 查看课程
def lesson_list(inData, inCookie):
    url = 'http://120.55.190.222/api/mgr/sq_mgr/'
    #url = 'http://127.0.0.1/api/mgr/sq_mgr'
    #user_cookie = inCookie #原始的值cookie #方案1
    user_cookie = {'sessionid':inCookie, 'token': 'sq'} #方案2：自己封装
    payload = inData
    resp = requests.get(url, params=payload, cookies=user_cookie)
    # header = {'Cookie': 'sessionid=5j2b2p669zuxurjy7oapdzm3tml9hmzi;token= sq'}

    #如果响应体出现编码，不是我们需要的中文，设置响应编码
    resp.encoding='unicode_escape'
    return resp.text


if __name__ == '__main__':
    res = login()
    print(res)

    # 列出课程操作
    print(lesson_list({'action': 'list_course', 'pagenum': 1, 'pagesize': 20},res))





