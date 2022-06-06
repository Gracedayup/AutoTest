"""
@Time : 2022/6/6 16:03
@Author : sunny cao
@File : verification_code1.py
"""
import requests


class VerificationCode(object):
    access_token = ''

    def baidu_auth_api(self, ak, sk):
        """
        :param ak: 百度ai平台的api key
        :param sk:百度ai平台的secret key
        :return: None
        """
        auth_url = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&' \
            'client_id='+ak+'&' \
            'client_secret='+ sk
        response = requests.get(auth_url)
        VerificationCode.access_token = response.json()['access_token']
        print(VerificationCode.access_token)

    def baidu_ocr_api(self, img_base64):
        """
        :param img_base64: 图片base64编码
        :return:None
        """
        ocr_url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic'
        request_url = ocr_url+"?access_token=" + VerificationCode.access_token
        params = {"image": img_base64}
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        response = requests.post(request_url, data=params, headers=headers)
        code = response.json()
        print(code)


if __name__ == '__main__':
    api = VerificationCode()
    api.baidu_auth_api('xCPIGQRetI3iqDIcBWw7l9g6', 'jH5AoA8B4ep4IdHkzdONBwgCMwMNI7Vl')
    b64_data = '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'
    api.baidu_ocr_api(b64_data)
