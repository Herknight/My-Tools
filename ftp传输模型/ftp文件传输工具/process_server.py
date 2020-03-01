"""
process_server.py 基于Process进程并发
"""

from socket import *
from multiprocessing import Process
import os,signal

ADDR = ('0.0.0.0',8888)

# 客户端处理函数,循环收发消息
def handle(c):
    while True:
        data = c.recv(1024).decode()
        if not data:
            break
        print(data)
        c.send(b'OK')

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
        os._exit(0)
    except Exception as e:
        print(e)
        continue

    # 创建新的进程处理请求
    client = Process(target=handle,args=(c,))
    client.daemon = True
    client.start()


