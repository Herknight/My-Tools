"""
逆波兰表达式实现
"""

from sstack import *

st = SStack()

while True:
    exp = input()
    tmp = exp.split(' ')  # 按照空格切割字符串
    for i in tmp:
        if i not in ['+','-','*','/','p']:
            st.push(float(i))
        elif i == '+':
            y = st.pop()
            x = st.pop()
            st.push(x + y)
        elif i == '-':
            y = st.pop()
            x = st.pop()
            st.push(x - y)
        elif i == '*':
            y = st.pop()
            x = st.pop()
            st.push(x * y)
        elif i == '/':
            y = st.pop()
            x = st.pop()
            st.push(x / y)
        elif i == 'p':
            print(st.top())








