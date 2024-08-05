
#获取cookie
import requests

requests.post(url=url_login,data=data_login)
#获取接口的cookie信息，一般通过登录接口返回
print(response.cookies)
#获取cookie，以字典类型返回
cookie = requests.utils.dict_from_cookiejar(response.cookies)
print(cookie)


#后续接口怎么使用cookie信息来验证登录状态
url = ''
header ={''}
res = requests.get(url=url,cookies=cookie)
print(res.text)



