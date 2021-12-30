"""
        ------ 分 式 ------

"""

"""
        案例一百四十二 案例化Fraction类

"""
print(f'{"案例一百四十二 案例化Fraction类" :^30s}' + "\n")

import fractions
fac1 = fractions.Fraction('5/9')
print(f' 用字符串初始化: {fac1}')
fac2 = fractions.Fraction(3.5)
print(f' 用浮点数初始化: {fac2}')
fac3 = fractions.Fraction(2,5)
print(f' 用分子与分母初始化: {fac3}')

import decimal
dcm = decimal.Decimal(0.4)
fac4 = fractions.Fraction(dcm)
print(f' 用Decimal对象来初始化: {fac4}')

fac5 = fractions.Fraction(fractions.Fraction(1,3),fractions.Fraction(2,7))
print(f' 用其他Fraction对象初始化: {fac5}')

fac6 = fractions.Fraction(-3,-11)
print(f' 分子和分母都是负值: {fac6}')
fac7 = fractions.Fraction(4,-9)
print(f' 分子是正值,分母是负值: {fac7}')
fac8 = fractions.Fraction(-3,5)
print(f' 分子是负值,分母是正值: {fac8}')

print("="*36)

"""
        案例一百四十三 限制分母的大小

"""
print(f'{"案例一百四十三 限制分母的大小" :^30s}' + "\n")

floats = 0.2,1.25,0.875,1.2,8.5
for n in floats:
    print(f'浮点数: {n}')
    fac = fractions.Fraction(n)
    print(f'产生的分式: {fac}')
    print(f'限制分母大小后: {fac.limit_denominator()}\n')

print("="*36)

"""
        案例一百四十四 常见的分式运算

"""
print(f'{"案例一百四十四 常见的分式运算" :^30s}' + "\n")

a = fractions.Fraction('1/5')
b = fractions.Fraction('2/3')
r = a + b
print(f' {a} + {b} = {r}')

a = fractions.Fraction('4/11')
b = fractions.Fraction('2/15')
r = a - b
print(f' {a} - {b} = {r}')

a = fractions.Fraction('3/8')
b = fractions.Fraction('7/12')
r = a * b
print(f' {a} * {b} = {r}')

a = fractions.Fraction('3/10')
b = fractions.Fraction('1/2')
r = a / b
print(f' {a} / {b} = {r}')

a = fractions.Fraction('6/25')
b = fractions.Fraction('1/3')
r = a % b
print(f' {a} % {b} = {r}')

a = fractions.Fraction(-7,13)
r = abs(a)
print(f' |{a}| = {r}')

print("="*36)