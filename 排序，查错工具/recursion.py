"""
求一个数的阶乘  n!
"""

def fun(n):
    result = 1
    for i in range(1,n + 1):
        result *= i
    return  result

def recursion(n):
    if n <= 1:
        return 1
    return n * recursion(n - 1)

print(recursion(5))














