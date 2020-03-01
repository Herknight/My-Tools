"""
编写一个程序，向一个文件写入如下内容

          1. 2019-1-1  18:18:18
          2. 2019-1-1  18:18:20


       每隔2秒写入一次，每条占一行。
       ctrl-c/红点 结束程序，下次启动后序号要跟之前的连续
       需要可以在编辑器中实时看到文件写入情况
"""

import time

f = open('log.txt','ab+')

# 文件偏移量定位到开头
f.seek(0)
n = 0
# 获取有多少行
for line in f:
    n += 1


# f.seek(-29,2) # 移动到最后一行开头
# data = f.readline().decode()
# n = int(data.split('.')[0]) # 获取行号

while True:
    n += 1
    time.sleep(2)
    s = "%d. %s\n"%(n,time.ctime())
    f.write(s.encode())
    f.flush()   # 随时查看




