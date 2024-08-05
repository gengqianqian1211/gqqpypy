import yaml
import os

#导入设置模块中的字典--路径
from configs.setting import FILE_PATH



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


#读取根目录下文件函数，如果文件不存在则创建一个文件
def write_yaml(value):
    """
    yaml文件数据写入
    :param value:
    :return:
    """
    file_path = FILE_PATH['extract']
    print(file_path)

    if not os.path.exists(file_path):
        with open(file_path,'w'):
            pass

    # 在yaml文件中写入内容
    file = None
    try:
        #参数 a为追加写入，  参数w为清空写入
        file = open(file_path,'a',encoding='utf-8')
        if isinstance(value,dict):
            #参数 allow_unicaode为true 允许写入中文    sort_keys是否按顺序写入
            write_data = yaml.dump(value,allow_unicaode = True,sort_keys = False)
            file.write(write_data)
        else:
            print('导入的类型也必须为字典类型')

    except Exception as e:
        print(f'写入yaml文件时出现异常,原因：{e}')

    finally:
        #写入后关闭文件
        file.close()

#清空yaml文件的方法
def clear_yaml():
    '''
    清空extract.yaml文件的数据
    :return:
    '''
    with open(FILE_PATH['extract'],'w') as f:
        f.truncate()

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


if __name__ == '__main__':
    #读取yaml文件所在的路径   ./ 当前文件目录    ../当前文件的上一级目录
    res = read_yaml('../../data/login.yaml')
    print(res)
    clear_yaml()


    #验证写入yaml文件的类型必须为字典类型
    res = write_yaml({'name':'xiaoming'})





