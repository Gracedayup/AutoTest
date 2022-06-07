import requests
from common.yaml_util import YamlUtil


class HandleRequest(object):
    session = requests.session()
    def __init__(self, file, base, base_url):
        """

        :param file: yaml文件路径
        :param base:
        :param base_url:
        """
        self.base_url = YamlUtil().read_config_file(file, base, base_url)

    def send_request(self, method, url, **kwargs):
        # 处理method
        method = str(method).lower()
        # 处理基础路径
        self.base_url = self.base_url + url
        res = HandleRequest.session.request(method=method, url=self.base_url, **kwargs)
        return res

    # def request(self, method, url, data=None, headers=None):
    #     res = None
    #     if method.lower() == "get":
    #         res = requests.get(url=url, params=eval(data), headers=headers)
    #     elif method.lower() == "post":
    #         res = requests.post(url=url, json=eval(data), headers=headers)
    #     elif method.lower() == "put":
    #         res = requests.put(url=url, json=eval(data), headers=headers)
    #     elif method.lower() == "delete":
    #         res = requests.delete(url=url, json=eval(data), headers=headers)
    #     else:
    #         print("传入的方法%s不正确" % method.lower())
    #     return res


if __name__ == '__main__':
    data1 = HandleRequest()





