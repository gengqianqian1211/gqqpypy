import pytest
import random

class TestAssertResult:
    #相等断言，判断两个值是相等的
    def test_assert_eq(self):
        assert  1==1,'断言失败他们不相等'

    #不等断言
    def test_assert_eq_02(self):
        #预期结果
        exp = {'msg':'登录成功'}
        #返回结果
        response = {'msg':'登录成功'}
        assert exp !=response,'断言失败他们相等'

    #真假断言
    def test_assert_bool(self):
        assert random.choice([True,False]),'真假断言失败'

    #成员关系断言
    def test_assert_contains(self):
        contains = 'pytest'
        contains_list = ['pytest','unittest','python']
        assert contains in contains_list

    #集合断言
    def test_assert_set(self):
        set_a ={1,2,3,4,5}
        set_b ={5,4,3,2,1}
        assert set_a == set_b

if __name__ == '__main__':
    pytest.main(['-vs','-k','test_assert_result'])