from socket import *
import sys
import getpass


def main():
    if len(sys.argv) < 3:
        print('argv is error')
        return
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
    s = socket()
    s.connect((HOST,PORT))

    while True:
        print('''
            ==========Welcome=========
            --1.注册   2.登录   3.退出--
            ==========================
            ''')
        try:
            cmd = int(input("输入选项(1, 2 or 3)>>>"))
        except Exception:
            print("命令错误")
            continue
        if cmd not in [1, 2, 3]:
            print("请输入正确选项")
            #清除标准输入
            sys.stdin.flush() 
            continue
        elif cmd == 1:
            name = do_register(s)
            if name != 1:
                print('注册成功!,直接登录!')
                login(s,name)
            else:
                print('注册失败!')
        elif cmd == 2:
            name = do_login(s)
            if name != 1:
                print('登录成功')
                login(s, name)
            else:
                print('登录失败')
        elif cmd ==3:
            s.send(b"E")
            sys.exit('谢谢使用')

#注册
def do_register(s):
    while True:
        name = input('请输入用户名:')
        passwd = getpass.getpass('请输入密码:')
        passwd1 = getpass.getpass('请确认密码:')
        if (' ' in name) or (' ' in passwd):
            print('用户名或密码不能用空格')
            continue
        if passwd != passwd1:
            print('密码不一致')
            continue
        msg = 'R {} {}'.format(name, passwd)
        s.send(msg.encode())
        data = s.recv(1024).decode()
        if data == 'OK':
            return name
        elif data == 'EXIT':
            print('用户已存在')
            return 1
        else:
            return 1

#登陆
def do_login(s):
    while True:
        print('''\n
                ===============查询界面==================
                1.查询           2. 历史记录        3.退出
                ========================================
                ''')
        try:
            cmd = int(input('输入选项>>>'))
        except Exception:
            print('命令错误')
            continue
        if cmd not in [1,2,3]:
            print('没有该命令')
            sys.stdin.flush()#清除输入
            continue
        elif cmd ==1:
            do_query(s, name)
        elif cmd ==2:
            do_history(s,name)
        elif cmd == 3:
            return




if __name__ == '__main__':
    main()