"""
        函数的定义与调用

"""

"""
        案例一百四十八 定义函数

"""
print(f'{"案例一百四十八 定义函数" :^30s}' + "\n")

def func_1(a,b):
    print(f' 函数的参数值:\n a:{a}\n b:{b}\n')

def func_2():
    print(' 函数是无参的\n')

def func_3(n):
    print(f' 参数值:\n n:{n}')
    print(' 函数有返回值!')
    return n * 10

func_1(66,88)
func_2()
func_3(8)

print("="*36)

"""
        案例一百四十九 函数的调用方法

"""
print(f'{"案例一百四十九 函数的调用方法" :^30s}' + "\n")

def set_data(x,y):
    print(f' {set_data.__name__}函数被调用')
    print(' 参数:\n x:{},y:{}\n'.format(x,y))

def other_fun():
    print(' {}函数被调用,此函数无参数\n'.format(other_fun.__name__))

def get_a_num():
    from random import randint
    return randint(1,200)

set_data(88,99)
other_fun()
print(f' {get_a_num.__name__}函数返回的数值: {get_a_num()}\n')

print("="*36)

"""
        案例一百五十 函数的定义顺序

"""
print(f'{"案例一百五十 函数的定义顺序" :^30s}' + "\n")

def fun_a():
    return fun_b() + ' morning'

def fun_b():
    return 'Good'
res = fun_a()
print(f' 函数调用结果: {res}')

print("="*36)

"""
        案例一百五十一 如何更改函数的引用名称

"""
print(f'{"案例一百五十一 如何更改函数的引用名称" :^30s}' + "\n")

def __do_something(s):
    print(' 函数执行,参数为: {}'.format(s))
do_working = __do_something
del __do_something
do_working(100)

print("="*36)
