"""
squeue.py  队列的顺序存储
思路 :
1. 基于列表完成数据存储
2. 对列表功能进行封装
3. 列表的头部作为队头,尾部作为队尾
功能: 入队(enqueue),出队(dequeue),判断队列为空
"""

# 自定义异常
class QueueError(Exception):
    pass

class SQueue:
    # 设置空列表作为队列存储空间
    def __init__(self):
        self.__elems = []

    # 判断队列是否为空
    def is_empty(self):
        return self.__elems == []

    # 入队
    def enqueue(self,val):
        self.__elems.append(val)

    # 出对
    def dequeue(self):
        if not self.__elems:
            raise QueueError("Queue is empty")
        return self.__elems.pop(0)

if __name__ == '__main__':
    sq = SQueue()

    sq.enqueue(10)
    sq.enqueue(20)
    sq.enqueue(30)

    while not sq.is_empty():
        print(sq.dequeue())

