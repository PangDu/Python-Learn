"""
    稳定排序算法: 冒泡、插入、归并、基数
    不稳定排序算法: 快速、希尔、堆
"""
print("------------插入排序------------")
# 直接插入排序
"""
    将要排序的数据逐次放在有序的新列表中,新列表就是排序后的结果.
"""
# Python 性能分析
import cProfile
list = [23,14,55,778,22,23,1,4]
list_result = []
print('------以下为直接插入排序结果------')
def insertSortDirectly():
    for i in list:
        if len(list_result) == 0:
            list_result.append(i) 
        else:
            index = 0
            while index < len(list_result):
                if list_result[index] < i :
                    index += 1
                else:
                    list_result.insert(index,i)
                    break
            if index == len(list_result):
                list_result.append(i)
        print(list_result)
cProfile.run('insertSortDirectly()')

# 折半插入排序 [1, 4, 14, 22, 23, 23, 55, 778]
listBinary = [23,14,55,778,22,23,1,4]
listBinary_result = []
print('------以下为折半插入排序结果------')
def binaryInsertionSort():
    for i in listBinary:
        if len(listBinary_result) == 0:
            listBinary_result.append(i)
        else:
            index = int(len(listBinary_result) / 2)
            if listBinary_result[index] < i:
                while index < len(listBinary_result):
                    # 查找右边
                    if listBinary_result[index] < i:
                        index += 1
                    else:
                        listBinary_result.insert(index,i)
                        break
                if index == len(listBinary_result):
                    listBinary_result.append(i)
            elif listBinary_result[index] > i:
                while index >= 0:
                    if listBinary_result[index] > i:
                        index -= 1
                    else:
                        if index == 0:
                            index += 1
                            listBinary_result.insert(index,i)
                            break
                if index == -1:
                    listBinary_result.insert(0,i)
            print(listBinary_result)
cProfile.run('binaryInsertionSort()')


# 冒泡排序
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
