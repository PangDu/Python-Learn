"""
        ------ 随机数 ------

"""

"""
        案例一百一十一 产生一个随机整数

"""
print(f'{"案例一百一十一 产生一个随机整数" :^30s}' + "\n")
import random
n = 20
while n > 0:
    x = random.randrange(100,999) # x >= 100 && x < 999
    print(x,end=' ')
    n -= 1

print('\n')

n = 20
while n > 0:
    x = random.randint(100,999) # x >= 100 && x<= 999
    print(x,end=' ')
    n -= 1
print('\n')
print("="*36)

"""
        案例一百一十二 从序列中随即取出一个元素

"""
print(f'{"案例一百一十二 从序列中随即取出一个元素" :^30s}' + "\n")
fruit = ('grape','banana','carambola','plum','cherry','pitaya','durian','haw','bennet')
for i in range(1,7):
    item = random.choice(fruit)
    print(f' 第{i}轮: {item}')
print("="*36)

"""
        案例一百一十三 生成0~1的随机数

"""
print(f'{"案例一百一十三 生成0~1的随机数" :^30s}' + "\n")
lists = [random.random() for x in range(0,30)]
for n in lists:
    print(n)
print("="*36)

"""
        案例一百一十四 从原序列中选取随机样本组成新序列

"""
print(f'{"案例一百一十四 从原序列中选取随机样本组成新序列" :^30s}' + "\n")
src = (56,34,345,12,999,888,77777,6666,900000)
new_list1 =random.sample(src,5)
print(f' 原序列: {src}\n')
print(f' 随机生成的新序列: {new_list1}\n')
new_list2 = random.sample(range(1000),10)
print(new_list2)
print("="*36)

"""
        案例一百一十五 打乱列表中的元素顺序

"""
print(f'{"案例一百一十五 打乱列表中的元素顺序" :^30s}' + "\n")
nums = [99,88,66,777,555555,4444444,33333333333]
random.shuffle(nums)
print(f' 第一次打乱顺序: {nums}')
random.shuffle(nums)
print(f' 第二次打乱顺序: {nums}')
random.shuffle(nums)
print(f' 第三次打乱顺序: {nums}')
print("="*36)
