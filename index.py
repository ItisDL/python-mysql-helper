# -*- coding: utf-8 -*-
# by dl
import pymysql
import traceback
from config import conf
def pm_db(sql='', act='select', dict=1, params=(), table='', data=(), where=''):
    db = pymysql.connect(host=conf.my_host, user=conf.my_user, password=conf.my_password, db=conf.my_db,
                         port=conf.my_port,
                         charset=conf.my_charset)
    if dict == 1 and not (act == 'getOne' or act == 'getCol'):
        cur = db.cursor(cursor=pymysql.cursors.DictCursor)
    else:
        cur = db.cursor()
    try:
        if act == 'select':
            cur.execute(sql, params)  
            results = cur.fetchall()  
            return results
        elif act == 'insert':
            # 插入项
            colStr = '(' + ','.join(data.keys()) + ')'
            # 虚拟列
            vDataStr = ''
            for _ in data.keys():
                vDataStr += '%s,'
            # 去除尾部
            vDataStr = '(' + vDataStr + ')'
            # # 插入值
            # dataValues = ["'" + x + "'" for x in data.values()]
            # dataStr = '(' + ','.join(dataValues) + ')'
            # 拼接
            sql = 'insert into ' + table + colStr + ' values ' + vDataStr
            # 传入参数
            params = list(data.values())
            # print(sql)
            results = cur.execute(sql, params)
            db.commit()
            return results
        elif act == 'update':
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
            params = list(data.values())
            results = cur.execute(sql, params)
            db.commit()
            return results
        elif act == 'exec':
            results = cur.execute(sql, params)
            db.commit()
            return results
        elif act == 'getOne':
            cur.execute(sql + ' limit 1', params)  
            results = cur.fetchall()  
            if results:
                return results[0][0]
            else:
                return results
        elif act == 'getRow':
            cur.execute(sql + ' limit 1', params)  
            results = cur.fetchall()  
            if results:
                return results[0]
            else:
                return results
        elif act == 'getCol':
            cur.execute(sql, params)  
            results = cur.fetchall()  
            if results:
                return [x[0] for x in results]
            else:
                return results
    except:
        traceback.print_exc()
    finally:
        cur.close()  # 关闭游标
        db.close()  # 关闭连接

if __name__ =='__main__':
    sql = "select * from user_shop"
    print(pm_db(sql))