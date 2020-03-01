# 一轮交换
def sub_sort(l,low,high):
    # 选定基准
    x = l[low]
    while low < high:
        # 后面的数向前甩
        while l[high] > x and high > low:
            high -= 1
        l[low] = l[high]  # 将基准数放到前面
        # 前面的数往后甩
        while l[low] <= x and low < high:
            low += 1
        l[high] = l[low] # 将基准数放到后面
    l[low] = x # 将基准数插入
    return low

# 快速排序
def quick(l,low,high):
    if low < high:
        #将一轮交换后的基准数赋值给key
        key = sub_sort(l,low,high)
        #key-1为上限，列表左边形成新列表递归一次
        quick(l,low,key - 1)
        #key+1为下限，列表右边形成新列表递归一次
        quick(l,key+1,high)    

l = [4,9,3,1,5]
quick(l,0,len(l)-1)
print(l)
print("你好！")

