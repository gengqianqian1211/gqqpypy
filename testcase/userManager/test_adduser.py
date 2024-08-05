import pytest


class TestAddUser:
    '''
    @pytest.mark.run(order=3)
    def test_add_user_01(self):
        print('新增用户01')

    @pytest.mark.run(order=2)
    def test_add_user_02(self):
        print('新增用户02')

    @pytest.mark.run(order=1)
    def test_add_user_03(self):
        print('新增用户03')

'''

    @pytest.mark.last
    def test_add_user_01(self):
        print('新增用户01')

    @pytest.mark.P1
    def test_add_user_02(self):
        print('新增用户02')

    @pytest.mark.first
    def test_add_user_03(self):
        print('新增用户03')

if __name__ == '__main__':
    pytest.main(['-vs','-k','test_adduser'])