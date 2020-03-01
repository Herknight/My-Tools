#定义一次交换，排序前的准备
def su_sort(l,low,high):
    #选定基准数
    x = l[low]
    while low<high:
        #比基准数小的往前放
        while l[high] > x and low < high:
            high -=1
        l[low]=l[high]  # 将比基准小的数的索引和基准数交换位置，放到前面
        #比基准数大的往后放
        while l[low] <= x and high > low:
            low += 1
        l[high]=l[low]  # 将比基准大的数的索引和基准数交换位置，放到后面
    l[low] = x # 将基准数插入
    return low

#开始快排循环
def quick(l,low,high):
    if low < high:
        key = su_sort(l,low,high)
        #key-1做上限，左边一半新列表继续
        quick(l,low,key - 1)
        #key+1做下限，右边一半新列表继续
        quick(l,key + 1,high)

# l = [4,9,3,1,2,5,8,4]
# quick(l,0,len(l)-1)
# print(l)

l = [4,9,3,1,2,5,8,4]
quick(l,0,len(l)-1)
print(l)
print("你好！")
