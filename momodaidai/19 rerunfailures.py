#测试用例执行失败后重跑


import random
import pytest

class Testlogin:
    # reruns 失败重跑的次数设置
    # reruns_delay：失败重跑的时间间隔设置

    #单个测试用例失败重跑设置
    # @pytest.mark.flaky(reruns=3,reruns_delay=2)
    def test_login_sucess(self):
        assert random.chhoice([True,False]),'测试失败'
        print('登录成功场景')

    def test_login_sucess(self):
        assert random.chhoice([True, False]), '测试失败'
        print('登录失败场景')
if __name__ == '__main__':
    pytest.main(['-s', '-v', '-k','19 rerunfailures'])