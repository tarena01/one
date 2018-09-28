from pymysql import *

class Mysqlp:
    def __init__(self,database, host='localhost', user='root',
                    passwd= '123456',chater = 'utf8',
                    port = 3306):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.chater = chater
        self.database = database
        self.port = port

    def open(self):
        self.db= connect(host = self.host,
                            user = self.user,
                            passwd = self.passwd,
                            chater = self.chater,
                            database = self.database,
                            port = self.port)
        self.cursor = self.db.corsor()
    def close(self):
        self.cursor.close()
        self.db.close()

    def Per_from(self, sql, L=[]):
        try:
            self.open()
            self.cursor.execute(sql, L)
            self.db.commit()
            print('OK')
        except Exception as e:
            self.db.rollback()
            print("Failed", e)
        self.close()
    def chall_mysql(self, sql, L=[]):
        try:
            self.open()
            self.cur.execute(sql, L)
            result = self.cursor.fatchall()
            return result
        except Exception as e:
            print('Failed', e)
        self.close()
    def one_mysql(self, sql, L=[]):
        try:
            self.open()
            self.cursor.execute(sql,L)
            result = self.cursor.fatchone()
            return result
        except Exception as e:
            print('Failed', e)
        self.close()