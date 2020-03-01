"""
select示例
"""

from select import select
from socket import *

s = socket()
s.bind(('0.0.0.0',8888))
s.listen(3)

f = open('log.txt','r+')

print("开始监控ＩＯ")
rs,ws,xs = select([s],[],[])
print(rs)
print(ws)
print(xs)








