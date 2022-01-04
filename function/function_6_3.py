"""
        可变参数

"""

"""
        案例一百五十五 可变参数的位置参数

"""
print(f'{"案例一百五十五 可变参数的位置参数" :^30s}' + "\n")

def run_funtion(*args):
    print(' {} 函数被调用'.format(run_funtion.__name__))
    print(f' 参数: {args}')
    print(f' 参数个数: {len(args)}\n')
run_funtion(1,5,8,9,19)
run_funtion()
run_funtion('hello','world','!')
run_funtion(999,'tick',0.0000001)

ps = [2,'eerd',0.99,b'c']
run_funtion(*ps)

print("="*36)

"""
        案例一百五十六 可变的关键字参数

"""
print(f'{"案例一百五十六 可变的关键字参数" :^30s}' + "\n")

def demo_fun(**kwargs):
    print(' {}函数被调用'.format(demo_fun.__name__))
    print(f' 参数:',end='')
    for k,v in kwargs.items():
        print(f' {k} = {v} ', end= '')
    print('\n')
demo_fun(a='dedc',b = 888, c= 0.09)
demo_fun()
demo_fun(f = 1000.1)

pars = {'title' : 888,'content' : 'do some work'}
demo_fun(**pars)

print("="*36)

"""
        案例一百五十七 可变参数的混合使用

"""
print(f'{"案例一百五十七 可变参数的混合使用" :^30s}' + "\n")

def demo_func_1(*psargs, **kwargs):
    print(' {}函数被调用'.format(demo_func_1.__name__))
    print(f' 位置参数: {psargs}')
    print(f' 关键字参数: {kwargs}\n')
demo_func_1()
demo_func_1(f = 0.08, y = 'xyz')
demo_func_1(20,88,'run')
demo_func_1('x','y',z = 1)

print("="*36)

"""
        案例一百五十八 可变参数与非可变参数的混合使用

"""
print(f'{"案例一百五十八 可变参数与非可变参数的混合使用" :^30s}' + "\n")
#若可变的位置参数后出现非可变参数,函数调用时,可变位置参数后的参数必须按关键字传值
#若可变位置参数在非可变参数后,非可变参数必须按位置传参
#若函数的参数列表同时出现可变的关键字参数与非可变参数,可变关键字参数必须位于参数列表末尾
def demo_fun2(*args,x,y):
    print(' {}函数被调用'.format(demo_fun2.__name__))
    print(' 参数:')
    print(f' args = {args}, x = {x}, y = {y} \n')
demo_fun2(2,3,4,5,x='b',y=99)

def demo_fun3(s,t,*args):
    print(' {}函数被调用'.format(demo_fun3.__name__))
    print(' 参数:')
    print(f' s = {s}, t = {t}, args = {args}\n')
demo_fun3(3,5,88,999,9999)

def demo_fun4(f,e,**kw):
    print(' {}函数被调用'.format(demo_fun4.__name__))
    print(' 参数:')
    print(f' f = {f}, e = {e}, kw = {kw}\n')
demo_fun4(1,2,a=3,b='b')

print("="*36)
