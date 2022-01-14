"""
        lambda表达式

"""
#匿名函数
"""
        案例一百六十四 打印满足条件的数字

"""
print(f'{"案例一百六十四 打印满足条件的数字" :^30s}' + "\n")

def print_with_cond(iterable,condi=lambda i:True):
    for x in iterable:
        if condi(x):
            print(x,end=' ')
numbers = [7,78,54,23,123,578]
con1 = lambda n:(n % 3) == 0
print_with_cond(numbers,con1)
print('\n')
con2 = lambda n:(n % 2) == 0
print_with_cond(numbers,con2)
print('\n')

print("="*36)

"""
        案例一百六十五 按数字的绝对值大小排序

"""
print(f'{"案例一百六十五 按数字的绝对值大小排序" :^30s}' + "\n")

nums = -5,2,-3,8,-7,12,-10
result = sorted(nums,key=lambda n: abs(n))
print(f' 原序列: {nums}')
print(f' 排序后: {result}')

print("="*36)
