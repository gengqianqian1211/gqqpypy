import pytest
from unit_tools.handle_data.yaml_handler import read_yaml

class TestParameter:

    @pytest.mark.parametrize('api_info',read_yaml('../data/adduser.yaml'))
    def test_04(self,api_info):
        print(f'获取的接口信息：{api_info}')



if __name__ == '__main__':
    pytest.main(['-vs','-k','test_parameter'])