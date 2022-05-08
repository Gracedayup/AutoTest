import hashlib


class ConvertData(object):
    @staticmethod
    def convert_md5(self, data):
        md = hashlib.md5()
        md.update(data.encode("utf-8"))
        data = md.hexdigest()
        return data