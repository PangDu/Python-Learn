"""
        ------ input 与print函数 ------

"""
import time
from sys import stdout

"""
    案例六 接收键盘输入

"""
content = input('请输入你想输入的内容:')
print(f'你输入的内容是:{content}')

"""
    案例七 打印屏幕消息

"""
"print(*objects,sep='',end='\n',file=sys.stdout,flush=False)"

a = 3900            #整型
b = 1.29            #浮点型
c = "erwqert"       #字符串
print(a,b,c)

r = "红色"
g = "绿色"
b = "蓝色" 
w = "白色"
print(r,g,b,w,sep='、')

"""
    案例八 打印进度条

"""
tasks = range(1,31)
progress_width = 25
for n in tasks:
    #延时0.5秒，模拟耗时操作
    time.sleep(0.5)
    #计算当前进度的百分比
    curr_ps = n / len(tasks)
    #生成进度条文本,用”>“符号表示进度值
    #ljust方法:字符串左对齐,剩下的空间用’-‘去填充
    progress_str = '{0:s}'.format(int(progress_width * curr_ps) * '>').ljust(progress_width,'-')
    #.0%:把浮点数值转换成百分比(乘以100,在后边加上符号%)，.0:去掉小数位部分
    msg_str = '【{0:.0%}】'.format(curr_ps)
    print(f'\r{progress_str}{msg_str}',end = '')

"""
    案例九 将文本打印到文件中

"""
with open('test.txt',mode = 'wt', encoding='UTF-8') as my_file:
    print("__weak修饰的对象被Block引用," +
    "不会影响对象的释放,而__strong在Block内部修饰的对象,会保证,在使用这个对象在scope内," +
    "这个对象都不会被释放,出了scope,引用计数就会-1," +
    "且__strong主要是用在多线程运用中,若果只使用单线程,只需要使用__weak即可",file= my_file)

"""
    案例十 打印文本时使用分隔符

"""
print('\n')
print('abc','xyz',sep='#')
print('line1','line2','line3',sep='\n')
print('第一步','第二步','第三步','完成',sep='->')
print('\n')
"""
    案例十一 使用sys.stdout打印文本

"""
stdout.write('第一行文本\n')
stdout.write('第二行文本\n')
stdout.write('第三行文本'.center(50,'*'))
stdout.write('\n')

"""
    案例十二 
"""
