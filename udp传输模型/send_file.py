from socket import *
from time import sleep

s = socket()
s.connect(('127.0.0.1',8888))

# 读取文件，循环发送
f = open('timg.jpg','rb')
while True:
    # 边读取边发送
    data = f.read(1024)
    if not data:
        sleep(0.5)
        s.send(b'##')
        break
    s.send(data)

sleep(0.5)
s.send(b'send over')

f.close()
s.close()
