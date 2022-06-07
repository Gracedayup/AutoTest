import yaml
import os


class YamlUtil(object):
    def get_object_path(self):
        """

        :return:返回父级目录路径
        """
        return os.path.abspath(os.getcwd())

    def read_config_file(self, file, one_node, two_node):
        """

        :param file: 文件绝对路径
        :param one_node:父节点
        :param two_node:子节点
        :return:子节点的值
        """
        file_path = YamlUtil().get_object_path() + file
        with open(file_path, encoding='utf-8') as f:
            value = yaml.load(stream=f, Loader=yaml.FullLoader)
            return value[one_node][two_node]

    # 读取extract.yml文件
    def read_extract_file(self, file, node_name):
        """
        读取yaml文件中的数据
        :param file:文件名
        :param node_name:读取的key
        :return:
        """
        file_path = YamlUtil().get_object_path() + file
        with open(file_path, encoding='utf-8') as f:
            value = yaml.load(stream=f, Loader=yaml.FullLoader)
            return value[node_name]

    def write_extract_file(self, file, data):
        """
        写入全局变量至yaml文件
        :param file: 文件名
        :param data: 写入的数据
        :return: None
        """
        file_path = YamlUtil().get_object_path() + file
        with open(file_path, encoding='utf-8', mode='a') as f:
            yaml.dump(data, stream=f, allow_unicode=True)

    def clear_extract_file(self, file, data):
        """
        清除yaml文件内容
        :param file:
        :param data:
        :return:None
        """
        file_path = YamlUtil().get_object_path() + file
        with open(file_path, encoding='utf-8', mode='w') as f:
            f.truncate()


if __name__ == '__main__':
    result = YamlUtil().read_config_file(f"\\test_case\\test_login\\login.yaml", 'login', 'name')
    print(result)

