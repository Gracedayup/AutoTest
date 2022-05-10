"""
生成大小、任意格式的文件
param:
"""
import os

class GenerateFile(object):
    def __init__(self, file_path, file_size):
        self.file_path = file_path
        self.file_size = file_size

    def gen_file(self):
        with open(self.file_path, 'w') as file:
            file.seek(1024*1024*int(self.file_size)-2)
            file.write('001')

if __name__ == '__main__':
    file = GenerateFile("test.pdf", "1")
    file.gen_file()