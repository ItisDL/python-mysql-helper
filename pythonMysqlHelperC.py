# -*- coding: utf-8 -*-
# by dl
import pymysql
import traceback
from config import conf


class pythonMysqlHepler:
    def __init__(self, host=conf.my_host,
                 user=conf.my_user,
                 password=conf.my_password,
                 db=conf.my_db,
                 port=conf.my_port,
                 charset=conf.my_charset,
                 dict=1):
        self.host = host
        self.user = user
        self.password = password
        self.db = db
        self.port=port
        self.charset=charset
        self.con = pymysql.connect(host=self.host,
                                   user=self.user,
                                   password=self.password,
                                   db=self.db,
                                   port=self.db,
                                   charset = self.charset
                                   )
    # @staticmethod
    def update(self,table,data,where):
        cur = self.con.cursor()
        # set项
        setStr = ''
        for _ in data:
            setStr += _ + '=%s,'
        setStr = setStr[:-1]
        # print(setStr)
        # where项
        whereStr = where
        # whereStr = ' where '
        # for _ in where:
        # whereStr += _ + '=' + where
        # 拼接
        sql = 'update ' + table + ' set ' + setStr + whereStr
        print(sql)
        params = list(data.values())
        results = cur.execute(sql, params)
        self.con.commit()
        return results

if __name__ == '__main__':
    # 没有实例化直接用会报错 实例化 可以直接在类名后面加一个()
    res = pythonMysqlHepler().update(table='user_shop',data={'name':'DLTest'},where='id = 1')
    print(res)
