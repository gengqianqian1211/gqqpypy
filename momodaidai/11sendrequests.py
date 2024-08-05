# 请求封装

import requests
# 导入cookie组件
from requests import utils
import re


class SendRequests:
    def __init__(self):
        pass


    # 解决接口返回编码格式为\\u767b的函数
    res_text = None
    @classmethod
    def _text_encode(cls, res_text):
        """
        处理接口返回出现 unicode编码时，如：\\u767b
        :param res_text:
        :return:
        """

        match = re.search(r'\\u[0-9a-fA-F]{4}', res_text)
        if match:
             res = res_text.encode().decode('unicode_escape')
        else:
             res = res_text

        return res

    # 封装request方法
    def send_request(self, **kwargs):
        # 创建一个会话
        session = requests.Session()
        response = None
        try:
            # 请求
            response = session.request(**kwargs)

            # 获取返回值的cookie
            set_cookie = requests.utils.dict_from_cookiejar(response.cookies)
            if set_cookie:
                print(f'获取到cookie：{set_cookie}')

            # 返回值转码
            res = self._text_encode(response.text)
            print(res)

        except requests.exceptions.ConnectionError:
            print("接口请求异常，可能是request的连接数过多或者速度过快导致程序报错")
        except requests.exceptions.RequestException as e:
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
        return response


if __name__ == '__main__':
    # ---post请求

    url_detail = 'http://10.0.5.45:8080/pmd/work_log/list.do'
    header_detail = {'Content-Type': 'application/x-www-form-urlencoded',
                     'Cookie': 'JSESSIONID=01947628C86164484FEC1825002371C0'}
    data_detail = {"NUMBERING_AND_NAME": "电力智", "lastStart": "2024-01-01", "lastEnd": "2024-12-31"}

    send = SendRequests()

    res_cms_login = send.execute_api_request(api_name=None, url=url_detail, method='post', header=header_detail,
                                             case_name=None,
                                             data=data_detail)
    print(res_cms_login.text)

# ---get请求

url_login = 'http://10.0.5.159:8881/complaints/pc/main/login.do?strAccount=18300000001&strPasswd=123@Qwe&strApp=hexi'

method_login = 'get'

send = SendRequests()
res = send.execute_api_request(api_name=None, url=url_login, method=method_login, header=None,
                               case_name=None)
print(res.text)
print((res))
