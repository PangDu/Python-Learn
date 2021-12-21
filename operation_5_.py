"""
        案例九十六 二进制的逻辑运算

"""
print(f'{"案例九十六 二进制的逻辑运算" :^30s}' + "\n")
x,y = 12, 9
print(f'{x:b} & {y:b} = {x & y :04b}')
print(f'{x:b} | {y:b} = {x | y :04b}')
print(f'{x:b} ^ {y:b} = {x ^ y :04b}')
print("="*36)

"""
        案例九十七 移动二进制位

"""
print(f'{"案例九十七 移动二进制位" :^30s}' + "\n")
n = int('01011011',base=2)
c1 = n << 4
c2 = n >> 3
print(f' 原数值:{n :08b}')
#左边0忽略
print(f' 二进制位向左移动4位后:{c1:08b}')
#右边0忽略
print(f' 二进制向右移动3位后:{c2:08b}')
print("="*36)

"""
        案例九十八 查找同时包含a、e两个字母的单词

"""
print(f'{"案例九十八 查找同时包含a、e两个字母的单词" :^30s}' + "\n")
words = ('amount','wisdom','perfect','learn','daedal')
results = []
for n in words:
    if n.count('a') and n.count('e'):
        results.append(n)
print(f'results: {results}')
print("="*36)

"""
        案例九十九 or运算符

"""
print(f'{"案例九十九 or运算符" :^30s}' + "\n")
results = []
for num in range(1,200):
    if (num % 12 == 0) or (num % 15 == 0):
        results.append(num)
print(f'results: {results}')
print("="*36)

"""
        案例一百 自定义布尔运算

"""
#检测对象是否存在__bool__方法,若找到调用该方法运算结果
#若__bool__方法找不到,查找__len__方法,该方法返回非0值视为True、返回0视为False
#以上二个方法都找不到则布尔运算结果总是True
#bool类从int类派生,对于整数值非0即为Ture;浮点型数值也是,因为float类实现了__bool__方法
print(f'{"案例一百 自定义布尔运算" :^30s}' + "\n")
class Demo100:
    def __bool__(self):
        if len(self.__dict__):
            return True
        return False

x = Demo100()
if x:
    print(' x中设置了动态属性!')
else:
    print(' x中未设置动态属性!')

y = Demo100()
y.test1 = 5
y.test2 = 10
if y:
    print(' y中设置了动态属性!')
else:
    print(' y中未设置动态属性!')
print("="*36)
