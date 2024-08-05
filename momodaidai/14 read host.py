


'''
1.++++++++++
在文件 configs 文件下创建config.ini 文件  在config.ini文件中添加host信息

服务器信息
[Host]
host = http://127.0.0.1:8787


[MySQL]
host = localhost
port = 3306
username = root
password = 123456
databass = db

2.++++++++++
在文件 configs 文件下创建 setting 将配置文件写入setting中

    #将创建的config.ini中的内容写入 setting
    'ini':os.path.join(DIR_PATH,'configs','config.ini')

3.++++++++++
创建文件 configParse.py
编写读取ini文件的方法
读取host的方法
读取mysql的方法

4.++++++++++
在文件夹 sendrequests.py 中添加 调用配置文件的host 和配置文件的参数






'''

