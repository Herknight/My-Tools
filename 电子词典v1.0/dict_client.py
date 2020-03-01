"""
dict 客户端

功能: 根据用户输入,发送请求,得到结果
结构 : 一级界面 --> 注册,登录,退出
      二级界面 --> 查单词  历史记录   注销
请求类型: 注册R　登录L　查单词Q　历史记录H　退出E
"""

from socket import *
import sys
from getpass import getpass

#　服务器地址
ADDR = ('127.0.0.1',8888)

# 套接字全局变量
s = socket()
s.connect(ADDR)

#　注册用户
def do_register():
    while True:
        name = input("User:")
        passwd = getpass()
        passwd1 = getpass("Again:")

        if passwd != passwd1:
            print("两次密码不一致")
            continue

        if (' ' in name) or (' ' in passwd):
            print("用户名密码不可以有空格")
            continue

        #　请求类型
        msg = "R %s %s"%(name,passwd)
        s.send(msg.encode()) #　发送请求
        data = s.recv(128).decode()
        if data == 'OK':
            print("注册成功")
            login(name) #　二级界面
        else:
            print("注册失败")
        return

#　登录
def do_login():
    name = input("User:")
    passwd = getpass()
    msg = "L %s %s"%(name,passwd)
    s.send(msg.encode()) #　发送请求
    data = s.recv(128).decode()
    if data == 'OK':
        print("登录成功")
        login(name)  #　二级界面
    else:
        print("登录失败")

#　查单词
def do_query(name):
    while True:
        word = input("单词:")
        if word == '##':
            #　结束查询
            break
        msg = "Q %s %s"%(name,word)
        s.send(msg.encode())
        #　直接打印回复结果
        data = s.recv(2048).decode()
        print(data)

#　历史记录
def do_hist(name):
    msg = "H "+name
    s.send(msg.encode())
    #　循环接受历史记录
    while True:
        data = s.recv(1024).decode()
        if data == '##':
            break
        print(data)


#　二级界面
def login(name):
    while True:
        print("""
        =============Query===============
        1. 查单词　　2.历史记录　　3.注销
        =================================
        """)
        cmd = input("输入选项:")
        if cmd == '1':
            do_query(name)
        elif cmd == '2':
            do_hist(name)
        elif cmd == '3':
            return
        else:
            print("请输入正确选项")

#　启动函数
def main():
    while True:
        print("""
        =============Welcome===========
        1. 注册　　　2.　登录　　3. 退出
        ===============================
        """)
        cmd = input("输入选项:")
        if cmd == '1':
            do_register()
        elif cmd == '2':
            do_login()
        elif cmd == '3':
            s.send(b'E')
            sys.exit("谢谢使用")
        else:
            print("请输入正确选项")


if __name__ == '__main__':
    main()





