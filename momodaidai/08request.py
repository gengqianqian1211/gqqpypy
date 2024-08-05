import requests



#####################################
#发送get请求
url = 'http://10.0.5.159:8881/complaints/pc/main/login.do?'
req_data = {
   'strAccount' : '18300000001',
    'strPasswd' :'123@Qwe',
    'Qwe&strApp': 'hexi'
}
res = requests.get(url=url, params=req_data, headers=header)

#响应结果默认返回接口的一个状态码
print(res.status_code)
#获取接口响应内容（文本）
print(res.text)

#获取接口响应内容（json格式）
print(res.json())

#####################################
#post请求  表单提交
url_login = ''
header_login ={'Content-Type':'application/x-www-formurlencoded;charset=UTF-8'}
data_login = {
    " ":" ",
    " ":" "
}
res_login = requests.post(url=url_login, data=data_login)

#响应结果
print(res_login.status_code)
#响应结果text格式
print(res_login.text)
#响应结果json格式
print(res_login.json())
#返回的值需要转码 \\u767b格式时
print(res_login.text.encode().decode('unicode_escape'))

#####################################
#post请求 json格式提交
url_detail = ''
header_detail = {'Content-Type':'application/json;charset=UTF-8'}
data_detail = {
    "pro_id" : "44444",
    "size":20
}
res_datail = requests.post(url=url_detail,json=data_detail,headers=header_detail)
#
print(res_datail.status_code)


#####################################
#创建一个会话
session = requests.Session()

#发起请求操作
res = session.get(url=url, params=req_data)
print(res.text)

res_2 = session.post(url=url_detail,json=data_detail,headers=heard_detail)
print(res_2.text)


#####################################
#直接调用request方法发起接口调用
method = 'post'
res = requests.request(method=method,url=url,json=data_detail,headers=header_detail)
print(res.text)

