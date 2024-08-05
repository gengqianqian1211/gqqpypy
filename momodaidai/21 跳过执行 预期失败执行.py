import random
import pytest

class Testlogin:

    @pytest.mark.skip
    def test_login_sucess(self):
        print('登录成功场景')


    num = 3
    @pytest.mark.skipif(num == 3,reason='符合表达式条件，所以次用例跳过')
    def test_login_sucess1(self):
        print('登录失败场景')

    num = 5
    @pytest.mark.skipif(num == 3, reason='符合表达式条件，所以次用例跳过')
    def test_login_sucess1(self):
        print('登录失败场景222')

    @pytest.mark.xfail
    def test_login_sucess5(self):
        assert 1 ==2
        print('登录失败场景222')


if __name__ == '__main__':
    pytest.main(['-s', '-v', '-k','test_skip_case'])