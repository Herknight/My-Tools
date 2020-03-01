#快排

def search(l,val):
    low,high = 0,len(l) - 1 # 查找范围的开始和结束索引位
    # 循环查找,每次去除一半
    while low <= high:
        mid = (low + high) // 2  # 中间数索引
        if l[mid] < val:
            low = mid + 1
        elif l[mid] > val:
            high = mid - 1
        else:
            return mid


l = [1,2,3,4,5,6,7,8,9,10]
print("Key index:",search(l,6))