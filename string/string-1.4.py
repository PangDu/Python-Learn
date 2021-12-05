import datetime
import string
from sys import prefix
import textwrap

"""
        ------ 格式化字符串 ------

"""
"""
        案例12 输出十六进制字符串

"""
print(f'{"输出十六进制字符串" :^30s}' + "\n")
numbers = [6500,112,180,1030]
for a in numbers:
        #d:十进制
        #x:十六进制
        #f'':格式字符串
        #: :6d生成字符宽度6个字符，不足用空格填充
        #: #生成十六进制数前面加上0x
        print(f'{a:6d} ==> {a:#8x}') 
print("="*36)

"""
        案例十三 设置字符串的对其方式

"""
print(f'{"设置字符串的对其方式" :^30s}' + "\n")
print(f'{"左对齐" :<30s}')
print(f'{"居中对齐" :^30s}')
print(f'{"右对齐" :>30s}')
print('\n')

sample = "测试文本"
# *：表示用该字符去填充剩余空间
#左对齐
print(f'{sample :*<30s}')
#居中对齐
print(f'{sample :*^30s}')
#右对齐
print(f'{sample :*>30s}')
print('\n')

# =:将数值的符号左边对齐,数值部分右边对齐,中间空余用空格或0填充
# #:呈现十六进制前面加上0x或0X;呈现八进制前面加上0o;呈现二进制前面加上0b
#十六进制两端对齐
print(f'{128 :=#20x}')
#八进制两端对齐
print(f'{789 :=#20o}')
#十进制两端对齐
print(f'{-23456 :=+020n}')
#二进制两端对齐
print(f'{2341 :=#20b}')
print("="*36)

"""
        案例十四 数字的千位分隔符
"""
print(f'{"数字的千位分隔符 " :^30s}' + "\n")
#逗号标志一般与d(十进制)或f(浮点数)一起使用,不能与n(常规数字)一起使用
#n标志表示的数字格式是以区域/语言的本地化设置相关,与逗号标志连用可能会冲突
num = 1335445.4329879
print(f'{int(num) :,d}')
print(f'{float(num) :,f}')
print(f'{float(num) :,.4f}')
print("="*36)

"""
        案例十五 "_"分隔符
"""
#对于十进制以三位为一组;对于二进制、八进制、十六进制一四位为一组
separator = "'_'分隔符"
print(f'{separator :^30s}' + "\n")
numberOne = 345241987
#十进制
print(f'{numberOne :#_d}')
#二进制
print(f'{numberOne :#_b}')
#八进制
print(f'{numberOne :#_o}')
#十六进制
print(f'{numberOne :#_x}')
print("="*36)
"""
        案例十六 自定义日期格式
"""
print(f'{"自定义日期格式" :^30s}' + "\n")
d = datetime.date(2021, 12, 2)
print(f'{d :%Y}-{d :%m}-{d :%d}')
print(f'{d :%Y}年{d :%m}月{d :%d}日')
t = datetime.time(14,18,50)
print(f'{t :%X}')
t = datetime.datetime.now()
print(f'{t :%c}')
print("="*36)

"""
        案例十七 使用format方法
"""
print(f'{"使用format方法" :^30s}.' + "\n")
print('{0:d} 的二进制为: {0:#b}.'.format(29))
print('文件{0}来源于用户{1}长度为{2}字节.'.format('2.jpg','Jim',31234))
print('这个程序是用{nameOne}编写的,当然也可用{nameTwo}来编写.'.format(nameOne = 'C++',nameTwo = 'Python'))
print("="*36)

"""
        案例十八 省略格式占位符的名称和序号

"""
print(f'{"省略格式占位符的名称和序号" :^30s}' + "\n")
a = 30
b = 34
c = a + b
print('{}+{}= {}'.format(a,b,c))
dc = 345
print('{:d}转换为八进制后:{:#o},{:d}转换为十六进制后:{:#x}'.format(dc,dc,dc,dc))
print("="*36)

"""
        案例十九 字符串模板

"""
print(f'{"字符串模板" :^30s}' + "\n")
tp = string.Template('天空飘着几朵$what')
s1 = tp.substitute(what = '白云')
print(f'模板一的处理结果:{s1}')
s2 = tp.substitute(what = '棉花糖')
print(f'模板二的处理结果:{s2}')
tp = string.Template('屏幕尺寸为${len}inch')
s3 = tp.substitute(len = '13.5')
print(f'模板三的处理结果为:{s3}')
print("="*36)

"""
        案例二十 字符串模板的安全替换模式

"""
print(f'{"字符串模板的安全替换模式" :^30s}' + "\n")
t = string.Template('$who likes $ footBall')
r = t.safe_substitute(who = 'Jack')
print(r)
print("="*36)

"""
        案例二十一 文本缩进

"""
print(f'{"文本缩进" :^30s}' + "\n")
sourceOne = "首行文本\n第二行文本\n第三行文本"
resultOne = textwrap.indent(text=sourceOne,prefix='￥$*')
print(resultOne + '\n')
sourceTwo = "这是文本\n\n\n\n\n这是另外一个文本"
print(sourceTwo)
def ignoreETLines(line):
        if line == '\n' or line == '\r':
                return False
        return True
resultTwo = textwrap.indent(text=sourceTwo,prefix='&&',predicate=ignoreETLines)
print(resultTwo)
print("="*36)

"""
        案例二十二 嵌套使用格式化语法

"""
print(f'{"嵌套使用格式化语法" :^30s}' + "\n")
num = input('请输入一个十进制整数:')
type = input('请输入要打印的格式:')
valtypes = ('b','x','o')
if not type in valtypes:
        print('您输入的格式类型无效.')
else:
        num = int(num)
        print(f'处理结果:{num:#{type}}')