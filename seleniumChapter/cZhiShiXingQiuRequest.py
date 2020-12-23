

import requests
requests.packages.urllib3.disable_warnings()
headers = {'Cookie': 'abtest_env=product; zsxq_access_token=461215D4-8DC5-08B3-256C-7B98FCD01E1D_D45F32F6C8265C04'}
resp = requests.get('https://wx.zsxq.com/dweb2/index/group/init', headers=headers, verify=False)

# resp = requests.get('https://api.zsxq.com/v1.10/groups/5448528884/topics/sticky?count=3', headers=headers, verify=False)

resp.encoding = resp.apparent_encoding
print(resp.text)