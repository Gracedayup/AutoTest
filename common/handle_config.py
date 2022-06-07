"""
获取config文件的内容：
1.获取文件中的所有区域section
2.根据指定section获取key集合
3.根据指定section和指定option获取对应value
"""
import configparser
from common import project_path
import os


class GetConfig(object):
    def __init__(self):
        self.cf = configparser.ConfigParser()
        self.config_dir = project_path.config_dir

    def get_value(self, filename, section, option):
        config_name = os.path.join(self.config_dir, filename)
        print(config_name)
        self.cf.read(config_name, encoding="utf8")
        try:
            value = self.cf.get(section, option)
        except Exception as e:
            print("输入的区域或者选项错误")
            raise e
        return value



