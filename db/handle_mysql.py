"""
description:mysql操作
"""
import pymysql


class HandleMysql(object):
    def __init__(self, host, user, password, database, charset='uft8'):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.charset = charset
        con = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
        self.cursor = con.cursor()

    def get_description(self):
        key = self.cursor.description
        return key

    def query_data(self, sql):
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        # 封装为list
        result_list = zip(self.get_description(), result)
        return result_list


if __name__ == '__main__':
    query_project = HandleMysql(host="124.221.190.245", user="root", password="123456", database="project")
    query_project_sql = "SELECT PROJECTID,PROJECTNAME FROM common_project"
    print("查询出来的数据为：", query_project.query_data(query_project_sql))
    print("查询出来的数据类型为：", type(query_project.query_data(query_project_sql)))



