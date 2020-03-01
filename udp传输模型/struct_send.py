from socket import *
import struct

# 定义数据传输格式
st = struct.Struct('i28sif')

# 创建套接字接受内容
s = socket(AF_INET,SOCK_DGRAM)

# 服务端地址
ADDR = ('127.0.0.1',8888)

while True:
    print("================================")
    id = int(input("ID:"))
    name = input("Name:").encode()
    age = int(input("Age:"))
    score = float(input("Score:"))
    #数据打包
    data = st.pack(id,name,age,score)
    s.sendto(data,ADDR)