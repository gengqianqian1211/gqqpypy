'''
从yaml文件读取参数
--------------------------
1. 在 unit_tools---handle_data--- 文件夹下创建 yaml_handler.py

--------------------------
2.创建文件夹 data --用于存放yaml文件，创建yaml文件 login.yaml
--------------------------
3.在yaml_handler.py文件 编写代码
#读取yanl文件封装

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

--------------------------
4.



4.


接口之间参数传递 --写入yaml文件，读取yaml文件
1.
2.创建工具文件夹 unit_tools --创建子文件夹handle_data--存放封装读取yaml文件的方法
3.创建配置文件configs，创建py配置文件setting 编写读取yaml文件路径方法，在根目录中创建文件 extract ，方便setting文件读取数据
4.编写写入yaml文件的脚本

'''