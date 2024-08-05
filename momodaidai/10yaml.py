# 读取yaml文件

import yaml

with open('10data.yaml','r',encoding='utf-8') as f:
    data = yaml.safe_load(f)
    print(data)

