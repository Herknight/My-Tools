"""
tcp_client.py  tcp客户端流程
重点代码
"""

from socket import *

# 创建tcp套接字
sockfd = socket()  # 默认参数-->tcp套接字

# 连接服务端程序
server_addr = ('172.40.91.143',8889)
sockfd.connect(server_addr)

# 发送接收消息
while True:
    data = input("Msg:")
    # data为空退出循环
    if not data:
        break
    sockfd.send(data.encode()) # 发送字节串
    data = sockfd.recv(1024)
    print("Server:",data.decode())

# 关闭套接字
sockfd.close()









