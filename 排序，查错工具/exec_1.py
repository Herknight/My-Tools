"""
编写一个接口程序,要求判断一段文字中括号匹配是否正确,
如果正确则打印"匹配正确",如果不正确则打印出哪里出错(只需要找出第一个错误即可)

出错情况 : 少前括号,少后括号,括号不匹配
"""
from lstack import *

text = "When an Open Data (standard) is created and promoted, it’s [important ]to think why - what change is th=is {trying (to] drive}? What will people do with this data that they couldn’t do before?"

ls = LStack()  # 初始化一个栈 用来存储左括号

# 先定义好验证条件
parens = "()[]{}"  # 关注字符
left_parens = "([{"  # 入栈的字符
opposite = {')':'(',']':'[','}':'{'}  # 匹配原则

# 编写生成器,用来遍历字符串,不断的提供括号及位置
def parent(text):
    # 通过开两个变量记录字符和字符位置
    i,text_len = 0,len(text)

    # 开始遍历字符串
    while True:
        while i < text_len and text[i] not in parens:
            i += 1

        # 判定因为什么结束上一个循环
        if i >= text_len:
            return
        else:
            yield i,text[i]  # 提供位置和括号字符
            i += 1


# 验证过程封装位函数
def ver():
    for i, c in parent(text):
        if c in left_parens:
            ls.push((i,c))  # 入栈一个元组
        # 遇到了右括号
        elif ls.is_empty() or ls.pop()[1] != opposite[c]:
            print("Unmatch is found at %d for %s"%(i,c))
            break
    else:
        if ls.is_empty():
            print("All parens is matched")
        else:
            # 左括号多了 (i,c)
            print("Unmatch is found at %d for %s"%ls.pop())


ver()















