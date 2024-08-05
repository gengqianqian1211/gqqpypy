import pytest

class TestParameter:


    #传递多个参数，通过列表的类型的可迭代对象实现参数化
    @pytest.mark.parametrize('user_name,password',
                             [('test01','admin123'),('test02','admin122'),('test03','admin121')])
    def test_login(self,user_name,password):
        print(user_name)
        print('正确的用户名和密码登录')

    #传递一个参数
    @pytest.mark.parametrize('user_name',
                             ['test01', 'test02',  'test03'])
    def test_login2(self, user_name):
        print(user_name)
        print('正确的用户名和密码登录2')

    #通过元祖类型的可迭代对象实现参数化
    @pytest.mark.parametrize('user_name',
                             ('test01', 'test02',  'test03'))
    def test_login3(self, user_name):
        print(user_name)
        print('正确的用户名和密码登录3')

    #通过字典类型的可迭代对象实现参数化
    @pytest.mark.parametrize('user_name',
                             {'user_name':'test01', 'user_name':'test02',  'user_name':'test03'})
    def test_login4(self, user_name):
        print(user_name)
        print('正确的用户名和密码登录4')


if __name__ == '__main__':
    pytest.main(['-vs','-k','test_parameter'])