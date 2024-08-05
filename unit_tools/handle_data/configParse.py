import configparser
#导入配置文件
from configs.setting import FILE_PATH


class ConfigParse:
    """
    解析.ini后缀的配置文件
    """
    def __init__(self,file_path = FILE_PATH['ini']):

        #取默认值
        self.file_path = file_path

        #调用读取方法
        self.config = configparser.ConfigParser()

        # 默认方法调用
        self.read_config()

        # 读取yaml路径
        def read_config(self):
            self.config.read(self.file_path)

        # 读取yaml参数
        def get_value(self,section,option):
            """
            获取配置文件的值
            :param self:
            :param section: 头参数
            :param option:下级参数key值
            :return:
            """
            try:
            #利用参数发请求
                return self.config.get(section,option)
            except Exception as e:
                #异常处理
                 print(f'解析配置文件出现异常，原因{e}')



        #调用文件取host值
        def get_host(self,option):
            """
            专门获取接口的服务器ip地址信息
            :param self:
            :param option:
            :return:
            """
            return self.get_value('Host',option)

        #读取mysql的数据
        def get_mysql_conf(self,option):
            """
            获取mysql 数据库的配置参数值
            :param self:
            :param option:
            :return:
            """
            return self.get_value('MYSQL',option)




if __name__ == '__main__':
    conf = ConfigParse()
    res = conf.get_host('host')
    res1 = conf.get_mysql('port')
    print(res)
    print(res1)