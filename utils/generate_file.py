"""
生成大小、任意格式的文件
param:

"""
import os
import string
import random

class GenerateFile(object):

    def __init__(self, file_size, file_size_unit, file_format):
        """
        初始化参数
        :param file_size: 文件大小
        :param file_size_unit:文件单位，GB、MB、KB、B
        """
        self.file_size = file_size
        self.file_size_unit = file_size_unit
        self.file_format = file_format

    def gen_file(self):
        """
        自动生成任意大小、任意格式的文件
        :return:
        """
        file_size = self.file_size
        # 生成文件名，如：1MB_file.txt
        file_name = str(self.file_size) + str(self.file_size_unit) + "_file" + "." + str(self.file_format)
        # 生成随机字符
        rand_str = string.ascii_letters
        if "gb" in str(self.file_size_unit).lower():
            file_size = float(file_size)*1024*1024*1024
        elif "mb" in str(self.file_size_unit).lower():
            file_size = float(file_size)*1024*1024
        elif "kb" in str(self.file_size_unit).lower():
            file_size = float(file_size)*1024
        elif "b" in str(self.file_size_unit).lower():
            file_size = float(file_size)

        with open(file_name, 'w') as fs:
            for i in range(int(file_size)):
                fs.write(random.choice(rand_str))
        return file_name


if __name__ == '__main__':
    file = GenerateFile("5", "MB", "pdf")
    file_name = file.gen_file()
    print(f"文件路径为:", os.path.join(os.path.dirname(os.path.realpath(__file__)), file_name))
