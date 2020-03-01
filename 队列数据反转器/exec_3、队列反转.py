"""
创建一个顺序队列, 队列中入队一组值
将队列中的值反转过来(值的个数不确定).
比如:[1,2,3,4,5]-->[5,4,3,2,1]
"""

from squeue import *
from lstack import *

sq = SQueue()
for i in range(8):
    sq.enqueue(i)

# 完成队列反转
ls = LStack()
# 出队 入栈
while not sq.is_empty():
    ls.push(sq.dequeue())

# 出栈 入队
while not ls.is_empty():
    sq.enqueue(ls.pop())

while not sq.is_empty():
    print(sq.dequeue())

