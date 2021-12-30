"""
        ------ 统计学函数 ------

"""

"""
        案例一百三十三 求和函数

"""
print(f'{"案例一百三十三 求和函数" :^30s}' + "\n")

elems = (50,80,20,30,60)
result = sum(elems)
print(f' {elems}求和后: {result}')

elems = [0.0001,0.002,4.513,0.888,0.0003]
result = sum(elems)
print(f' {elems}求和后: {result}')

elems = ['x','y','z']
result = ''.join(elems)
print(f' {elems}串联后: {result}')
print("="*36)

"""
        案例一百三十四 算术平均数

"""
print(f'{" 案例一百三十四 算术平均数" :^30s}' + "\n")

import statistics
sample = [15,70,28,19,65,46,23]
M = statistics.mean(sample)
print(f' 数据样本:\n {sample}\n 算术平均值: {M}\n')

print("="*36)

"""
        案例一百三十五 求字符串样本的平均长度

"""
print(f'{" 案例一百三十五 求字符串样本的平均长度" :^30s}' + "\n")

sample = '桃李春风','act','may','山河','tomato','九里山河古战场,牧童拾得旧刀枪','diskspace'
samplepoints = [len(x) for x in sample]
M = statistics.mean(samplepoints)
print(' 数据样本:',sample,sep='\n')
print(f' 平均长度: {M}')

print("="*36)

"""
        案例一百三十六 调和平均数

"""
print(f'{" 案例一百三十六 调和平均数" :^30s}' + "\n")

sample = [56.7,98.6,44.12,55,16,8,37.23]
M = statistics.harmonic_mean(sample)
print(' 数据样本:',sample,sep='\n')
print(f' 调和平均值: {M}')

print("="*36)

"""
        案例一百三十七 中位数

"""
print(f'{" 案例一百三十七 中位数" :^30s}' + "\n")

sample = [5,9,3,6,7]
m1 = statistics.median(sample)
print(' 样本:',sample)
print(' 中位数:',m1)

sample = [20,12,8,16,14,6]
#中间两项的平均值
m2 = statistics.median(sample)
#中间两个数中取出较大的一个
m3 = statistics.median_high(sample)
#中间两个数中取出较小的一个
m4 = statistics.median_low(sample)
print(' 样本:',sample)
print(' 中位数(均值):',m2)
print(' 中位数(较大):',m3)
print(' 中位数(较小):',m4)

print("="*36)

"""
        案例一百三十八 从分组数据中求中位数

"""
print(f'{" 案例一百三十八 从分组数据中求中位数" :^30s}' + "\n")

sample = [25,40,80,40,25,36,40]
interval = 1
mg = statistics.median_grouped(sample)
print(f' 样本:\n {sample}')
print(f' 组距: {interval}')
print(f' 分组中位数: {mg} \n')

sample = [7,27,27,27,65,85,85,85]
interval = 2
mg = statistics.median_grouped(sample)
print(f' 样本:\n {sample}')
print(f' 组距: {interval}')
print(f' 分组中位数: {mg}')

sample = [55,57,52,53,61,62]
mg = statistics.median_grouped(sample)
print(f' 样本:\n {sample}')
print(f' 当样本不存在重复变量时,分组中位数为: {mg}')

print("="*36)

"""
        案例一百三十九 众 数

"""
print(f'{" 案例一百三十九 众数" :^30s}' + "\n")

sample = 1,5,6,6,5,5,5,6
print(f' 样本: {sample}')
c = statistics.mode(sample)
print(f' 众数: {c}')

sample = 51,2,10,7,4,11
print(f' 无重复项的样本: {sample}')
try:
    d = statistics.mode(sample)
except:
    d = '<发生错误>'
print(f' 众数: {d}')

print("="*36)

"""
        案例一百四十 方 差

"""
print(f'{" 案例一百四十 方 差" :^30s}' + "\n")

sample1 = 37.1,36.89,37.2,37.22,37.01,37.12,36.92,36.99,37.03,36.98
sample2 = 37.23,37.012,37.31,36.84,37.01,36.91,37.35,36.97,37.04,37.11
print(f' 样本1:\n {sample1}')
print(f' 样本方差: {statistics.variance(sample1)}')
print(f' 总体方差: {statistics.pvariance(sample1)}\n')

print(f' 样本2:\n {sample2}')
print(f' 样本方差: {statistics.variance(sample2)}')
print(f' 总体方差: {statistics.pvariance(sample2)}')

print("="*36)

"""
        案例一百四十一 标 准 差

"""
print(f'{" 案例一百四十一 标 准 差" :^30s}' + "\n")

data1 = 2966,3002,2980
data2 = 3500,3325,3490
s1 = statistics.stdev(data1)
s2 = statistics.stdev(data2)
print(f'第一组样本:\n {data1}')
print(f'标准差: {s1}\n')
print(f'第二组样本:\n {data2}')
print(f'标准差: {s2}\n')

print("="*36)