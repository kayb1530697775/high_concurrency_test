# -*- coding:utf-8 -*-
# @author: kayb
# @file: mysql_db.py
# @time: 2021/4/17 下午9:22


from pymysql import Connection, cursors


class HCdb(object):
    def __init__(self):
        self.host = "127.0.0.1"
        self.user = "root"
        self.passwd = "123"
        self.database = "high_concurrency_db"
        self.port = 3306

    def __enter__(self):
        self.connection =  Connection(
            host=self.host,
            user=self.user,
            passwd=self.passwd,
            database=self.database,
            port=self.port,
            cursorclass=cursors.DictCursor
        )

        self.cs = self.connection.cursor()

        return self.cs

    def __exit__(self, exc_type, exc_val, exc_tb):

        self.cs.close()
        self.connection.close()


def get_db_data():
    sql_text = """
    select * from goods;

    """

    with HCdb() as cs:
        cs.execute(sql_text)
        all_datas = cs.fetchall()

    return all_datas


if __name__ == '__main__':
    db_datas = get_db_data()
    print(db_datas)








