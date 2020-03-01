"""
使用udp，从客户端录入学生信息，在服务端将学生信息写入文件
要求每个学生信息占一行
ID  NAME  AGE  SCORE
"""

from socket import *
import struct

# 定义数据传输格式
st = struct.Struct('i28sif')

# 创建套接字接受内容
s = socket(AF_INET,SOCK_DGRAM)
s.bind(('0.0.0.0',8888))

# 打开文件
f = open('student.txt','a')

while True:
    data,addr = s.recvfrom(1024)

    # 将信息转换位元组数据 (1,b'lily',13,89.5)
    data = st.unpack(data)
    info = "%d  %-10s  %d  %.1f\n"%data
    f.write(info)
    f.flush()

f.close()
s.close()









