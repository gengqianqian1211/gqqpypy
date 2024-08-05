

import requests

url = 'https://parkcqszxc.esint.com.cn/#/login'

data={
'namespaceId':	27830275,
'userIdentifie':	18000000002,
'password':	'abc123!',
'regionCode':	86,
'logonSceneType':	'desk'
}

res = requests.post(url=url,json=data)
print(res.text)