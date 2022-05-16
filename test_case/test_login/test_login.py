# encoding:utf-8

import pytest
from common.yaml_util import YamlUtil
import os
import requests
import json
import allure
import assertpy
from common.handle_excel import HandleExcel
from common.handle_request import HandleRequest


class TestLogin:
    @allure.feature('Jugo-Account')
    @allure.story('登录')
    @allure.step('步骤：测试登录功能')
    @pytest.mark.p0
    @pytest.mark.parametrize("args", YamlUtil(os.getcwd()+"/test_case/test_login/login.yaml").read_yaml())
    #@pytest.mark.flaky(reruns=2, reruns_delay=5)
    def test_login(self, args):
        print("请求参数为：", args)
        # 处理请求参数
        url = args['login']['url']
        param = json.dumps(args['login']['params'])
        header = args['login']['headers']
        method = args['login']['method']
        result = HandleRequest().request(method=method, url=url, data=param, headers=header)
        # 对响应结果断言
        print("返回结果为：", result.json())
        assert result.json()['code'] == args['login']['code']
        assert result.json()['codeRemark'] == "成功"
        assert assertpy.assert_that(result.json()['codeRemark']).is_type_of(str)

if __name__ == '__main__':
    pytest.main(['-s'])
