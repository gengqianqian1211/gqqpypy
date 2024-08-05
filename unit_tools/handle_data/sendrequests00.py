# 请求封装

from unit_tools.handle_data.yaml_handler import read_yaml
import requests
# 导入cookie组件
from requests import utils
# 导入返回值编码模块
import re
import yaml


class SendRequests:
    def __init__(self):
        pass

    # 解决接口返回编码格式为\\u767b的函数
    res_text = None

    def _text_encode(cls, res_text):
        """
        处理接口返回出现 unicode编码时，如：\\u767b
        :param res_text:
        :return:
        """

    match = re.search(r'\\u[0-9a-fA-F]{4}', res_text)
    if match:
        result = res_text.encode().decode('unicode_escape')
    else:
        result = res_text
    return result

    # 封装request方法
    def send_rerquest(self, **kwargs):
        # 创建一个会话
        session = requests.Session()
        response = None
        try:
            # 请求
            response = session.request(**kwargs)
            # 获取返回值的cookie
            set_cookie = requests.utils.dict_from_cookiejar(response.cookies)
            if set_cookie:
                # print(f'获取到cookie：{set_cookie}')
                #将cookie写入全局变量中
                write_yaml({'Cookie':set_cookie})


            # 返回值转码
            res = self._text_encode(response.text)
            print(res)


        except requests.exceptions.ConnectionError:
            print("接口请求异常，可能是request的连接数过多或者速度过快导致程序报错")
        except requests.exceptions.RequesyException as e:
            print("请求异常，请检查系统或数据是否正常")

        return response

    # 封装执行请求
    def execute_api_request(self, api_name, url, method, header, case_name, cookie=None, file=None, **kwargs):
        # 此种注释的打印方式，按住shift，再按三次双引号键
        """
        :param api_name:接口名称
        :param url:接口地址
        :param method:请求方法
        :param header:请求头
        :param case_name:测试用例名称
        :param cookie:cookie
        :param file:文件上传
        :param kwargs:未知数量关键字参数
        :return:
        """
        # 调用封装的方法    verify 参数忽略https证书校验
        response = self.send_request(method=method,
                                     url=url,
                                     headers=header,
                                     cookies=cookie,
                                     files=file,
                                     timeout=10,
                                     verify=False,
                                     **kwargs
                                     )


if __name__ == '__main__':
    ''' 
    url_login = ''
    header_login = {'Content-Type': 'application/x-www-formurlencoded;charset=UTF-8'}
    data_login = {
        " ": " ",
        " ": " "
    }
    send = SendRequests()
    res = send.execute_api_request(api_name=None, url=url_login, method='post', header=None, case_name=None,
                                   data=data_login)
'''
    #读取yaml文件的路径和数据
    url = 'http://127.0.0.1:87878'+data['baseInfo']['url']
    #读取yaml文件字典内容
    method = data['baseInfo']['method']
    header = data['baseInfo']['header']
    #取值yaml文件列表内容
    req_data = data['testCase'][0]['data']



    #修改请求为读取yaml文件内容
    send = SendRequests()
    res = send.execute_api_request(api_name=None, url=url, method=method, header=None, case_name=None,
                                   data=req_data)
    print(res.text)


   #将返回结果转成json格式 并写入yaml
   res_json = res.json()
   token = res.json['token']
   user_id = res_json['userId']
   write_yaml({'token':token,'userId':user_id})

#在请求中调用host
    from unit_tools.handle_data.configParse import ConfigParse
    host = ConfigParse().get_host('host')
    data = read_yaml('.././data/login.yaml')[0]
    url = host + data['baseInfo']['url']
    method = data['baseInfo']['method']
    header = data['baseInfo']['header']
    req_data = data['testCase'][0]['data']
