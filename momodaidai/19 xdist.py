
#多线程执行测试用例

import pytest
from time import sleep

class TestLogin:
    def test_login_success(self):
        sleep(3)
        print('登录成功场景')

    def test_login_success(self):
        sleep(3)
        print('登录失败场景')

    def test_login_success(self):
        sleep(3)
        print('登录错误场景')

if __name__ == '__main__':
    pytest.main(['-s','-v','-n=3'])



