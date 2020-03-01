"""
给出两个有序的链表L1,L2 .
在不创建新的链表的基础上将两个链表合并为一个
要求合并后的链表仍为有序
"""

from day01.linklist import *

# 创建两个链表,初始化数值
L1 = LinkList()
L2 = LinkList()

L1.init_list([1,5,7,8,10,12,13,19])
L2.init_list([0,3,4,8,14,21,22])

L1.show()
print("=========================")
L2.show()

def merge(L1,L2):
    # 将L2向L1中合并
    p = L1.head
    q = L2.head.next
    while p.next is not None:
        if p.next.val < q.val:
            p = p.next
        else:
            tmp = p.next
            p.next = q
            p = p.next
            q = tmp

    p.next = q


merge(L1,L2)
print("=================================")
L1.show()






