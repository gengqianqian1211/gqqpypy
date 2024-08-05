import random
import pytest

class Testlogin:
    # reruns 失败重跑的次数设置
    # reruns_delay：失败重跑的时间间隔设置

    #单个测试用例失败重跑设置
    @pytest.mark.P1
    def test_login_sucess(self):
        assert random.choice([True,False]),'测试失败'
        print('登录成功场景')