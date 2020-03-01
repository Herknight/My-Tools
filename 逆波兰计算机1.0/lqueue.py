"""
lqueue.py 链式队列
重点代码

思路:
1. 基于链表构建队列模型
2. 链表的开端作为队头, 结尾作为队尾
3. 对头队尾分别添加标记,避免每次插入数据都遍历链表
4. 队头和队尾重叠时认为队列为空
"""

# 自定义异常
class QueueError(Exception):
    pass

# 节点类
class Node:
    def __init__(self,val,next = None):
        self.val = val
        self.next = next

# 队列操作
class LQueue:
    def __init__(self):
        # 定义队头,队尾
        self.front = self.rear = Node(None)

    def is_empty(self):
        return self.front == self.rear

    # 如队  rear动
    def enqueue(self,val):
        self.rear.next = Node(val)
        self.rear = self.rear.next

    # 出队  front动
    def dequeue(self):
        if self.front == self.rear:
            raise QueueError("Queue is empty")

        # front移动到的节点已经出队
        self.front = self.front.next
        return self.front.val

if __name__ == '__main__':
    lq = LQueue()
    lq.enqueue(10)
    lq.enqueue(20)
    lq.enqueue(30)
    print(lq.dequeue())









