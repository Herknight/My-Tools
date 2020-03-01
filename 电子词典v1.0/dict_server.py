"""
dict 服务端
功能: 业务逻辑处理
模型: Process 多进程 tcp 并发
"""

from socket import *
from multiprocessing import Process
import os,signal
from dict_db import Database
from time import sleep

HOST = '0.0.0.0'
PORT = 8888
ADDR = (HOST,PORT)

#　数据库操作对象
db = Database()

#　处理注册
def do_register(c,data):
    tmp = data.split(' ')
    name = tmp[1]
    passwd = tmp[2]
    if db.register(name,passwd):
        c.send(b'OK')
    else:
        c.send(b'Fail')

#　处理登录
def do_login(c,data):
    tmp = data.split(' ')
    name = tmp[1]
    passwd = tmp[2]
    if db.login(name,passwd):
        c.send(b'OK')
    else:
        c.send(b'Fail')

#　查询单词
def do_query(c,data):
    tmp = data.split(' ')
    name = tmp[1]
    word = tmp[2]

    #　插入历史记录
    db.insert_history(name,word)

    #　通过数据库找到单词 (找到返回解释，找不到None)
    mean = db.query(word)
    if mean:
        msg = "%s : %s"%(word,mean)
    else:
        msg = "没有找到该单词"
    c.send(msg.encode())

#　历史记录
def do_hist(c,data):
    name = data.split(' ')[1]
    r = db.history(name)
    for i in r:
        #　ｉ -->(name  word  time)
        msg = "%s　%-16s  %s"%i
        sleep(0.1)
        c.send(msg.encode())
    sleep(0.1)
    c.send(b"##")

# 客户端处理函数,循环收发消息
def handle(c):
    while True:
        data = c.recv(1024).decode()
        if not data or data[0] == 'E':
            os._exit(0)
        elif data[0] == 'R':
            do_register(c,data)
        elif data[0] == 'L':
            do_login(c,data)
        elif data[0] == 'Q':
            do_query(c,data)
        elif data[0] == 'H':
            do_hist(c, data)


# 程序的启动入口
def main():
    # 创建监听套接字
    s = socket()
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind(ADDR)
    s.listen(5)

    signal.signal(signal.SIGCHLD,signal.SIG_IGN)
    print("Listen the port 8888....")

    while True:
        # 循环等待客户端连接
        try:
            c,addr = s.accept()
            print("Connect from",addr)
        except KeyboardInterrupt:
            db.close() #　关闭数据库连接
            os._exit(0)
        except Exception as e:
            print(e)
            continue

        # 创建新的进程处理请求
        client = Process(target=handle,args=(c,))
        client.daemon = True
        client.start()

if __name__ == '__main__':
    main()