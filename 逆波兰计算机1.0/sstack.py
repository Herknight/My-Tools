"""
sstack.py  栈模型的顺序存
重点代码

思路 :
1. 顺序存储可以使用列表实现,但是列表功能丰富,不符合栈模型要求
2. 将列表功能封装,实现顺序栈的类,只提供栈的操作功能

功能: 出栈, 入栈,判断栈空,查看栈顶元素
"""

# 自定义异常
class StackError(Exception):
    pass

# 顺序栈
class SStack:
    def __init__(self):
        # 空列表就是栈的存储空间
        # 列表的最后一个元素作为栈顶元素
        self.__elems = []

    # 入栈
    def push(self,val):
        self.__elems.append(val)

    # 判断栈空
    def is_empty(self):
        return self.__elems == []

    # 出栈
    def pop(self):
        if self.is_empty():
            raise StackError("pop from empty stack")
        return self.__elems.pop()

    # 查看栈顶
    def top(self):
        if self.is_empty():
            raise StackError("pop from empty stack")
        return self.__elems[-1]



if __name__ == '__main__':
    st = SStack()
    st.push(10)
    st.push(20)
    st.push(30)
    while not st.is_empty():
        print(st.pop())
    st.pop()