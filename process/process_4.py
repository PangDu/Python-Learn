"""
        案例六十九 最简单的流程

"""
print(f'{"案例六十九 最简单的流程" :^30s}' + "\n")
print('circle')
print('rectangle')
print('ellipse')
print('path')
print('rhombus')
print("="*36)

"""
        案例七十 声明阶段与调用阶段

"""
print(f'{"案例七十 声明阶段与调用阶段" :^30s}' + "\n")
a : int
b : int
c = 0.1

def test(x):
    print(x.__class__)

class G:
    val = 'na'

class F:
    other = G()

print("="*36)

"""
        案例七十一 单路分支

"""
print(f'{"案例七十一 单路分支" :^30s}' + "\n")
def checklen(s):
    if len(s) < 5:
        return " 至少需要5个字符!"
    return " 字符串长度符合要求!"

print(checklen("uieewwq"))
print(checklen("qwe"))
print("="*36)

"""
        案例七十二 双路分支

"""
print(f'{"案例七十二 双路分支" :^30s}' + "\n")
def inputChar(c):
    if (c % 3) == 0:
        print(f' {c} 可以被3整除!')
    else:
        print(f' {c}不可以被3整除!')
inputChar(12)
inputChar(43)
print("="*36)

"""
        案例七十三 更复杂的分支语句

"""
print(f'{"案例七十三 更复杂的分支语句" :^30s}' + "\n")
import random
nums = []
while len(nums) < 50:
    n = random.randint(1,100)
    if n in nums:
        continue
    nums.append(n)

c_0to30 = 0
c_30to50 = 0
c_50to80 = 0
c_other = 0

for x in nums:
    if 0 <= x < 30:
        c_0to30 += 1
    elif 30 <= x < 50:
        c_30to50 += 1
    elif 50 <= x < 60:
        c_50to80 += 1
    else:
        c_other += 1
print(f' 生成的整数列表: {nums}')
print(f' 大于或等于0小于30的整数有 {c_0to30} 个')
print(f' 大于或等于30小于50的整数有 {c_30to50} 个')
print(f' 大于或等于50小于80的整数有 {c_50to80} 个')
print(f' 未统计 {c_other} 个')
print("="*36)

"""
        案例七十四 分支语句的嵌套使用

"""
print(f'{"案例七十四 分支语句的嵌套使用" :^30s}' + "\n")
def factor(n):
    if n >= 2:
        x = 2
        print(f' {n} = ',end= '')
        while x <= n:
            if (n % x) ==0:
                n = n//x
                if n!= 1:
                    print(f'{x} × ',end = '')
                else:
                    print(f'{x}',end= '\n')
                    break
            else:
                x += 1

factor(16)
factor(100)
factor(67)
factor(1200)
print("="*36)

"""
        案例七十五 输出从1到10各个整数的平方根

"""
print(f'{"案例七十五 输出从1到10各个整数的平方根" :^30s}' + "\n")
import math

n = 10
i = 1
while i <= n :
    res = math.sqrt(i)
    print(f' {i}平方根: {res}')
    i += 1
print("="*36)

"""
        案例七十六 使用for循环

"""
print(f'{"案例七十六 使用for循环" :^30s}' + "\n")
import random
x = 0
numbers = []
while x < 10:
    numbers.append(random.random() * 100)
    x += 1

for n in numbers:
    print(f' n = {n}')
print("="*36)

"""
        案例七十七 for循环与range函数

"""
print(f'{"案例七十七 for循环与range函数" :^30s}' + "\n")
for n in range(10):
    print(n,end=' ')
print('\n')
for n in range(0,50,3):
    print(n,end=' ')
print('\n')
for a in range(60,30,-5):
    print(a,end=' ')
print('\n')
print("="*36)

"""
        案例七十八 组成每个数位均不同的三位数

"""
print(f'{"案例七十八 组成每个数位均不同的三位数" :^30s}' + "\n")
results = []
for a in range(1,9):
    for b in range(1,9):
        for c in range(1,9):
            if a != b and b !=c and a != c:
                results.append(a *100 + b *10 + c)
c = 0
for n in results:
    c += 1
    print(n,end = ' ')
    if (c % 20) == 0:
        print('\n')
print('\n')
print("="*36)

"""
        案例七十九 求"水仙花数"

"""
str =  '案例七十九 求' + '"水仙花数"'
print(f'{str:^30s}' + "\n")
nums = range(100,1000)
result = []
for n in nums:
    a = n //100
    b = n //10 % 10
    c = n % 10

    if n == (a ** 3 + b **3 + c**3):
        result.append(n)
for n in result:
    print(n,end = ' ')
print('\n')
print("="*36)