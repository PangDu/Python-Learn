#冒泡排序
def bubble_sort(alist):
    n = len(alist)
    for j in range(n-1):
        for i in range(n-1-j):
            if alist[i] > alist[i+1]:
                alist[i],alist[i+1] = alist[i+1],alist[i]
            
if __name__ == '__main__':
    numList = [33,12,66,6,68,233,890,1]
    print(f'排序前: {numList}')
    bubble_sort(numList)
    print(f'排序后: {numList}')
#枚举算法
