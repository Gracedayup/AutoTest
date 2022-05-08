import yaml
import os


class YamlUtil(object):
    def __init__(self, yaml_file):
        self.yaml_file = yaml_file

    def read_yaml(self):
        with open(self.yaml_file, encoding='utf-8') as f:
            value = yaml.load(f, Loader=yaml.FullLoader)
            return value


if __name__ == '__main__':
    login_yamlurl = os.path.dirname(os.getcwd())+"/test_case/test_login/login.yaml"
    login_yaml = YamlUtil(login_yamlurl)
    login_yaml.read_yaml()
