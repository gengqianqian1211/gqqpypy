import yaml
import os

#导入设置模块中的字典--路径
#from configs.setting import FILE_PATH



#读取yanl文件封装
def read_yaml(yaml_path):
    """
     读取yaml文件数据
    :param yaml_payh:
    :return:
    """
    try:
        #读取yaml文件
        with open(yaml_path,'r',encoding='utf-8') as file:
            #打开yaml文件
            data = yaml.safe_load(file)
            return data

    except UnicodeDecodeError:
        print(f'{yaml_path} 文件编码格式错误，--尝试使用utf-8去解码YAML文件发生错误，请确保yaml文件是utf-8格式')

        #读取yaml文件异常
    except yaml.YAMLError as e:
        print(f'Error:读取yaml文件失败，请检查yaml文件格式 -{yaml_path},{e}')

    except Exception as e:
        print(f'读取{yaml_path} 文件时出现异常，原因：{e}')




if __name__ == '__main__':
    #读取yaml文件所在的路径   ./ 当前文件目录    ../当前文件的上一级目录    添加需要读取文件的路径
    res = read_yaml('../data/login.yaml')
    print(res)
