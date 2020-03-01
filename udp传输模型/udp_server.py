"""
udp_server.py udp服务端
重点代码
"""

from socket import *

# 创建UDP套接字
sockfd = socket(AF_INET,SOCK_DGRAM)

# 绑定地址
server_addr = ('0.0.0.0',8888)
sockfd.bind(server_addr)

# 循环收发
while True:
    data,addr = sockfd.recvfrom(1024)
    print("收到的消息:",data.decode())
    sockfd.sendto(b'Thanks',addr)

# 关闭套接字
sockfd.close()