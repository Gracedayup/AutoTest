import requests
from common.yaml_util import YamlUtil
import os
import json


class Test(object):
    def test01(self, url, param, header):
        result = requests.post(url=url, data=param, headers=header)
        return result


if __name__ == '__main__':
    values = YamlUtil(os.path.dirname(os.getcwd())+"/test_case/test_login/login.yaml").read_yaml()
    login_url = values['login']['url']
    login_param = values['login']['params']
    login_header = values['login']['headers']
    print("请求url：", login_url)
    print("请求参数：", login_param)
    login_result = Test().test01(url=login_url, param=json.dumps(login_param), header=login_header)


