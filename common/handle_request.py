import requests


class HandleRequest(object):
    def request(self, method, url, data=None, headers=None):
        res = None
        if method.lower() == "get":
            res = requests.get(url=url, params=eval(data), headers=headers)
        elif method.lower() == "post":
            res = requests.post(url=url, json=eval(data), headers=headers)
        elif method.lower() == "put":
            res = requests.put(url=url, json=eval(data), headers=headers)
        elif method.lower() == "delete":
            res = requests.delete(url=url, json=eval(data), headers=headers)
        else:
            print("传入的方法%s不正确" % method.lower())
        return res


if __name__ == '__main__':
    data1 = HandleRequest()





