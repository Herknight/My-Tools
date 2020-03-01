"""
sort.py  排序方法训练
"""

def bubble(l):
    n = len(l)
    # 外层循环来确定比较多少轮
    for i in range(n - 1):
        # 内存循环确定每轮两两比较多少次
        for j in range(n - 1 - i):
            if l[j] > l[j + 1]:
                l[j],l[j+1]=l[j+1],l[j]


# 一轮交换
def sub_sort(l,low,high):
    # 选定基准
    x = l[low]
    while low < high:
        # 后面的数向前甩
        while l[high] > x and high > low:
            high -= 1
        l[low] = l[high]  # 将比基准小的数放到前面
        # 前面的数往后甩
        while l[low] <= x and low < high:
            low += 1
        l[high] = l[low] # 将比基准大的数放到后面
    l[low] = x # 将基准数插入
    return low

# 快速排序
def quick(l,low,high):
    if low < high:
        key = sub_sort(l,low,high)
        quick(l,low,key - 1)
        quick(l,key+1,high)



l = [4,9,3,1,2,5,8,4]
# bubble(l)
quick(l,0,len(l)-1)
print(l)  # 有序