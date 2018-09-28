import pymysql

db = pymysql.connect('localhost', 'root', '123456',)

def main():
    #创建游标对象
    cursor = db.cursor()
    cursor.execute('create database Dictionary \
                    character set utf8;')
    cursor.execute('use Dictionary;')
    # sql = "create table words (id int auto_increment primary key,\
    #         word varchar(64), interpret text);"
    # cursor.execute(sql)
    #查询历史
    sql1 = "create table hist (id int auto_increment primary key,\
            name varchar(32) not null,\
            word varchar(64), chinese varchar(64));"
    cursor.execute(sql1)
    #用户信息
    sql2 = "create table users (id int auto_increment primary key,\
            addr varchar(64),name varchar(32) not null,\
            passwd varchar(64) not null default '000000');"
    cursor.execute(sql2)
if __name__ == '__main__':
    main()
    # for line in f:
    #     try:
    #         l = re.split('[ ]+', line)
    #     except:
    #         pass

    #     sql3 = "insert into words (word, interpret) \
    #             values ('%s', '%s')"%(l[0], ' '.join(l[1:]))
    #     try:
    #         cursor.execute(sql3)
    #         db.commit()
    #     except:
    #         db.rollback()

    # f.close()