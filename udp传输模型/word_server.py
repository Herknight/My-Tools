"""
使用udp完成，从客户端输入单词，得到单词解释
客户端可以循环输入单词
"""

from socket import *


# 打开文件 'r'
f = open('dict.txt')

def find_word(word):
    f.seek(0) # 每次查找前先将位置定位到开头
    # 每次获取一行
    for line in f:
        w = line.split(' ')[0]
        # 如果遍历到的单词已经大于目标,就结束查找
        if w > word:
            break
        elif w == word:
            return line
    return "没有找到单词"


# 创建套接字
sockfd = socket(AF_INET,SOCK_DGRAM)
sockfd.bind(('0.0.0.0',8888))

# 循环接受单词返回单词解释
while True:
    word,addr = sockfd.recvfrom(1024)
    # 调用查单词
    result = find_word(word.decode())
    sockfd.sendto(result.encode(),addr)

f.close()
sockfd.close()