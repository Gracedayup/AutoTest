# encoding:utf-8
import pytest
from common.handle_request import HandleRequest
from common.yaml_util import YamlUtil


class Testlogin(object):

    def test_login(self):
        url = "/thirdparty/user/auth"
        method = "post"
        headers = {"Content-Type": "application/json"}
        data = {
                "orignService": "jugo-flow",
                "password": "admin123456",
                "username": "admin"
                }
        res = HandleRequest("\\config\\config.yaml", "base", "base_account_url").send_request(method=method, url=url, json=data, headers=headers)
        extract_data = {"token": res.json()['data']['token']}
        YamlUtil().write_extract_file("\\extract.yaml", extract_data)

