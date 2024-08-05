

'''
#yaml测试用例文件动态解析
1. +++++++++++++++++++
创建用户文件adduser.yaml 文件 存放接口数据
接口数据中读取之前存储的token

token: ${get_extratc_data()}

2. +++++++++++++++++++
在 sendrequests.py 文件中 将cookie写入全局变量中
write_yaml({'Cookie':set_cookie})

3. +++++++++++++++++++
在 yaml_handler.py  文件中 添加读取yaml文件路径的异常
        #读取yaml文件异常
    except yaml.YAMLError as e:
        print(f'Error:读取yaml文件失败，请检查yaml文件格式 -{yaml_path},{e}')

4. +++++++++++++++++++
在 yaml_handler.py  文件中 读取全局yaml文件函数格式

#读取yaml文件函数 格式
def get_extract_yaml(node_name,sub_node_name=None):
    """
    用于获取yaml文件的数据
    :param node_name: 第一级key
    :param sub_node_name: 下一级key
    :return:
    """
    file_path = FILE_PATH['extract']
    try:
        pass
    except yaml.YAMLError as e:
        print(f'Error:读取yaml文件失败，请检查 -{file_path}，{e}')
    except Exception as e:
        print(f'Error:未知异常 - {e}')

'''