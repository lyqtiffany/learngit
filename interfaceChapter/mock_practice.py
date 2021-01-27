
import time
#1 - 写服务器端-- mock ---xxx.json
#2- 测试代码

#提交申请接口
HOST = "http://127.0.0.1:9999"
import requests
def create_order():
    url = f"{HOST}/api/order/create/a"
    payload = {"user_id":"001","goods_id":"1234","num":"1","amount":"100.8"}
    resp = requests.post(url, json=payload)

    return resp.json()['order_id']

#查询:
#概念，频率+超时
def query_order(orderID, interval = 3, timeout=20):
    """
    :param orderID: 订单id
    :param interval: 频率3s一次
    :param timeout: 20s超时
    :return: 查询结果
    """
    url = f'{HOST}/api/order/get_result'
    payload = {"order_id":orderID}
    #1-查询开始计时—
    start_time = time.time() #阻塞模式

    #2结束时间
    end_time = start_time+timeout
    while time.time()<end_time:
        resp = requests.get(url,params=payload)
        if resp.text:  # 如果在超时的范围内，提前有值返回，就退出
            break
        time.sleep(interval)
    return resp.json()

import threading #多线程模块
if __name__ == '__main__':
    id =create_order()
    print(id)
    # res = query_order(id)
    # print(res)

   # # threading.Thread(target=希望哪个函数做子线程，就写这个函数名，args=函数需要的参数，写成元组)
   #  t1 = threading.Thread(target=query_order,args=(id,))
   #  # 2 守护线程
   #  t1.setDaemon(True)
   #  #3 启动进程
   #  t1.start()
   #
   #  for i in range(5):
   #      time.sleep(1)
   #      print("我正在执行其他模块的用例",i)

#多线程做  /协程、协程加进程，异步框架xdist
#需求点 希望提高自动化执行效率
#希望等待查询结果的时候，可以去执行其他的自动化测试操作
"""
可以把查询接口做成子线程
"""



