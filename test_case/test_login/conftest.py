"""
pytest.fixture中sope作用域：function
"""
import pytest

@pytest.fixture(scope="function", autouse="True")
def start_fuc():
    print("开始执行测试用例")
    yield
    print("测试用例执行结束")


