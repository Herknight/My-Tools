# 发送请求，得到结果

from socket import *

# 服务器地址
ADDR = ('127.0.0.1',8888)

# 创建套接字
sockfd = socket(AF_INET,SOCK_DGRAM)

# 循环发送消息
while True:
    data = input("Word:")
    if not data:
        break
    sockfd.sendto(data.encode(),ADDR)
    msg,addr = sockfd.recvfrom(1024)
    print(msg.decode())

sockfd.close()