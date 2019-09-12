# -*- coding: utf-8 -*-
# by dl
import pymysql
import sys
from config import conf


class pythonMysqlHepler:
    def __init__(self, host=conf.my_host,
                 user=conf.my_user,
                 password=conf.my_password,
                 db=conf.my_db,
                 port=conf.my_port,
                 charset=conf.my_charset):
        self.host = host
        self.user = user
        self.password = password
        self.db = db
        self.port = port
        self.charset = charset
        self.con = pymysql.connect(host=self.host,
                                   user=self.user,
                                   password=self.password,
                                   db=self.db,
                                   port=self.port,
                                   charset=self.charset
                                   )

    def createCur(self, funcName=''):
        if funcName in ['getOne', 'getCol']:
            self.cur = self.con.cursor()
        else:
            self.cur = self.con.cursor(cursor=pymysql.cursors.DictCursor)

    def executeSql(self, sql, params):
        if params:
            result = self.cur.execute(sql, params)
        else:
            result = self.cur.execute(sql)
        return result

    def getOne(self, sql, params=()):
        self.createCur(sys._getframe().f_code.co_name)
        self.executeSql(sql + ' limit 1', params)
        results = self.cur.fetchone()
        if results:
            return results[0]
        else:
            return results

    def getRow(self, sql, params=()):
        self.createCur(sys._getframe().f_code.co_name)
        self.executeSql(sql + ' limit 1', params)
        results = self.cur.fetchone()
        return results

    def getCol(self, sql, params=()):
        self.createCur(sys._getframe().f_code.co_name)
        self.cur.execute(sql, params)
        results = self.cur.fetchall()
        if results:
            return [x[0] for x in results]
        else:
            return results

    def getAll(self, sql, params=()):
        self.createCur(sys._getframe().f_code.co_name)
        self.executeSql(sql, params)
        results = self.cur.fetchall()
        return results

    def exec(self, sql, params=()):
        self.createCur(sys._getframe().f_code.co_name)
        result = self.executeSql(sql, params)
        return result

    def insert(self, table, data):
        self.createCur(sys._getframe().f_code.co_name)
        colStr = '(' + ','.join(data.keys()) + ')'
        vDataStr = ''
        for _ in data.keys():
            vDataStr += '%s,'
        vDataStr = vDataStr[:-1]
        vDataStr = '(' + vDataStr + ')'
        sql = 'insert into ' + table + colStr + ' values ' + vDataStr
        params = list(data.values())
        results = self.cur.execute(sql, params)
        self.con.commit()
        return results

    def update(self, table, data, where):
        self.createCur(sys._getframe().f_code.co_name)
        setStr = ''
        for _ in data:
            setStr += _ + ' = %s,'
        setStr = setStr[:-1]
        whereStr = ' where ' + where
        sql = 'update ' + table + ' set ' + setStr + whereStr
        params = list(data.values())
        results = self.cur.execute(sql, params)
        self.con.commit()
        return results


if __name__ == '__main__':
    # res = pythonMysqlHepler().insert(table='user_shop', data={'name': 'DLInsert'})
    # print(res)
    # 没有实例化直接用会报错 不想实例化可以直接在类名后面加一个()
    # res = pythonMysqlHepler().update(table='user_shop', data={'name': 'DLTest'}, where='id = 2')
    # print(res)
    # res = pythonMysqlHepler().exec(sql='delete from user_shop where id = 1')
    # print(res)
    # res = pythonMysqlHepler().getAll(sql='select * from user_shop')
    # print(res)
    # res = pythonMysqlHepler().getOne(sql='select id from user_shop where id =2')
    # print(res)
    # res = pythonMysqlHepler().getRow(sql='select * from user_shop')
    # print(res)
    # res = pythonMysqlHepler().getCol(sql='select name from user_shop')
    # print(res)
    pass
