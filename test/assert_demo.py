"""
学习assertpy的方法
"""
import assertpy


"""
assertpy的使用
"""


def assert_match_string():
    a = None
    result = assertpy.assert_that(a).is_not_none()
    print(result)


def assert_demo():
    assert 1+3 == 5, "1+3应该等于4"


if __name__ == '__main__':
    # assert_match_string()
    assert_demo()
