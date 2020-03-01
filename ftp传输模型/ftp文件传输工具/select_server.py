"""
select tcp 服务
重点代码

思路分析:
1. 将关注的ＩＯ放入监控列表
2. 当ＩＯ就绪时通知ｓｅｌｅｃｔ返回
3. 遍历返回值列表，处理就绪的ＩＯ
"""

from socket import *
from select import select

#　创建监听套接字
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',8888))
s.listen(5)

#　设置关注的ＩＯ列表
rlist = [s]  #　ｓ　用于等待处理连接
wlist = []
xlist = []

#　循环ＩＯ监控
while True:
    # print("++++",rlist)
    rs,ws,xs = select(rlist,wlist,xlist)
    # print('----',rs)
    # 遍历返回值列表，判断哪个ＩＯ就绪
    for r in rs:
        if r is s:
            c,addr = r.accept()
            print("Connect from",addr)
            rlist.append(c) #　增加新的关注的ＩＯ
        else:
            #　表明有客户端发送消息
            data = r.recv(1024).decode()
            print(data)
            r.send(b'OK')

    for w in ws:
        pass

    for x in xs:
        pass
