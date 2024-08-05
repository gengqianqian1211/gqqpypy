
# sendrequests 文件中添加 读取yaml文件的方法
from unit_tools.handle_data.yaml_handler import read_yaml

# 读取yaml文件的路径和数据
url = 'http://127.0.0.1:87878' + data['baseInfo']['url']
# 读取yaml文件字典内容
method = data['baseInfo']['method']
header = data['baseInfo']['header']
# 取值yaml文件列表内容
req_data = data['testCase'][0]['data']

# 修改请求为读取yaml文件内容
send = SendRequests()
res = send.execute_api_request(api_name=None, url=url, method=method, header=None, case_name=None,
                               data=req_data)
print(res.text)

# 将返回结果转成json格式 并写入yanl
res_json = res.json()
token = res.json['token']
user_id = res_json['userId']
write_yaml({'token': token, 'userId': user_id})