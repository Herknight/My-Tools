"""
http请求过程演示
"""

from  socket import *

# tcp套接字 （http-->tcp）
s = socket()
s.bind(('0.0.0.0',8000))
s.listen(3)

c,addr = s.accept()
print("Connect from",addr)
# 获取请求
data = c.recv(4096)
print(data)

# 返回响应
response = """HTTP/1.1 200 OK
Content-Type:text/html

Hello World
"""

c.send(response.encode())


c.close()
s.close()