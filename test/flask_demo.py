"""
@Time : 2022/6/6 16:55
@Author : sunny cao
@File : flask_demo.py
"""
from flask import Flask,request,jsonify

app = Flask(__name__)
class Flask_demo(object):

    def __success(self, data= None):
        if not data:
            data = []
        return jsonify({'success': True, 'msg': '', 'data': data})

    @app.route('/getContent', methods=['POST'])
    def get_content(self):
        print("welcome to flask")
        return Flask_demo().__success()


if __name__ == '__main__':
    app.run(host='127.0.0.1', port='8181')