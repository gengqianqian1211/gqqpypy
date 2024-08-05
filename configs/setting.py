import os
import sys

#读取上一层目录
DIR_PATH1 = os.path.dirname(__file__)

#读取项目跟目录
DIR_PATH = os.path.dirname(os.path.dirname(__file__))
print(DIR_PATH)
#将根目录添加到系统中
sys.path.append(DIR_PATH)


#在根目录下创建文件extract，方便setting文件读取
FILE_PATH = {
    #在根目录下创建文件extract
    'extract':os.path.join(DIR_PATH,'extract.yaml'),
    #将创建的config.ini中的内容写入 setting
    'ini':os.path.join(DIR_PATH,'configs','config.ini')
}
print(FILE_PATH['extract'])


