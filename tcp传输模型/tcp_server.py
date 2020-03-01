"""
tcp_server.py  tcp套接字服务端功能流程
重点代码

注意 ： 注意流程和函数使用
"""

import socket
from time import sleep

# 创建TCP套接字
sockfd = socket.socket(socket.AF_INET,
                       socket.SOCK_STREAM)

# 绑定地址
sockfd.bind(('0.0.0.0',8889))

# 设置监听
sockfd.listen(5)

# 阻塞等待客户端连接
while True:
    print("Waiting for connect...")
    try:
        connfd,addr = sockfd.accept()
        print("Connect from",addr)  # 打印连接的客户端
    except KeyboardInterrupt:
        print("服务端退出")
        break
    except Exception as e:
        print(e)
        continue


    # 收发消息
    while True:
        data = connfd.recv(5)
        # 连接的客户端退出，recv会立即返回空字符串
        if not data:
            break
        print(data.decode())
        sleep(0.1)
        n = connfd.send(b"Thanks#")
        print("Send %d bytes"%n)
    connfd.close()


# 关闭套接字
sockfd.close()











