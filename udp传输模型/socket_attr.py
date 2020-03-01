"""
套接字属性介绍
"""

from socket import *

# 创建套接字对象
s = socket(AF_INET,SOCK_STREAM)

# 设置端口立即重用
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

s.bind(('172.40.91.143',8888))
s.listen(3)
c,addr = s.accept()

print(s.type)  # 套接字类型
print(s.family) # 地址类型
print(s.getsockname()) # 绑定的地址
print(s.fileno()) # 文件描述符
print(c.getpeername())  # 获取连接端的地址

c.recv(1024)





