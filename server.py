from socket import *
import os
import signal
import time
from pymysql import connect
import sys
import traceback
import requests
import warnings

class DictServer(object):
    def __init__(self):
        self.baseurl = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
        self.headers = {"User-Agent":"Mozilla5.0"}
        self.proxies = {"HTTP":"http://309435365:szayclhp@114.67.228.126:16819"}
        #创建数据库连接
        self.db = connect('localhost','root','123456')
        #创建游标
        self.cursor = self.db.cursor()


    def do_child(self,c,db):
            #循环接受请求
        while True:
            data = self.c.recv(128).decode()
            print("Request:",data)
            #退出
            if (not data) or data[0] == 'E':
                c.close()
                sys.exit(0)
            #注册
            elif data[0] == 'R':
                do_register(c,data)
            #登陆
            elif data[0] == 'L':
                do_login(c,data)
            #查词
            elif data[0] == 'Q':
                do_query(c,data)
            #历史记录
            elif data[0] == 'H':
                do_history(c,data)
            #小游戏
            elif data[0] == 'C':
                do_playgame(c,data)

    #注册        
    def do_register(self,c,data):
        l = data.split(' ')
        name = l[1]
        passwd = l[2]

        cursor = db.cursor()
        sql = "select * from user where name= '%s'"%name
        cursor.execute(sql)
        r = cursor.fetchone()
        if r != None:   
            c.send(b'EXISTS')
            return

        sql = "insert into user (name, passwd) \
            values ('%s','%s')"%(name, passwd)
        try:
            cursor.execute(sql)
            db.commit()
            c.send(b'OK')
        except:
            db.rollback()
            c.send(b'FALL')
            return
        else:
            print('%s 注册成功'%name)


    #登陆
    def do_login(c,data):
        l = data.split(' ')
        name = l[1]
        passwd = l[2]
        cursor = db.cursor()

        sql = "select * from user \
            where name= '%s' and passwd='%s'"%(name, passwd)

        cursor.execute(sql)
        r = cursor.fetchone()
        if r == None:
            c.send('用户名或密码不正确'.encode())
        else:
            c.send(b'OK')

    #查词
    def do_query(c,data):

        #爬虫
        do_word(word)
        pass

    #爬虫查词
    def do_word(word):
        pass

    #历史记录
    def do_history(c,data):
        pass

    #小游戏
    def do_playgame(c,data):
        pass



    #主流程控制
    def main(self,ADDR):
        #创建套接字
        s = socket()
        s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
        s.bind(ADDR)
        s.listen(5)

        #忽略子进程退出
        signal.signal(signal.SIGCHLD,signal.SIG_IGN)
        db = pymysql.connect('localhost', 'root', '123456', 'Dictionary')


        while True:
            try:
                c,addr = s.accept()
                print("Connect from",addr)
            except KeyboardInterrupt:
                s.close()
                sys.exit("服务端退出")
            except Exception:
                traceback.print_exc()
                continue

        #创建子进程
        pid = os.fork()
        if pid < 0:
            print("create process failed")
            c.close()
        elif pid == 0:
            s.close()
            do_child(c,db) 
        else:
            c.close()

        

if __name__ == "__main__":
    DICT_TEXT = './dict.txt'
    HOST = '0.0.0.0'
    PORT = 8888
    ADDR = (HOST,PORT)

    server = DictServer()
    server.main(ADDR)
