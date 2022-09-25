"""
        ------ 字符串表达式 ------

"""

"""
    案例一 单行文本

"""
textOne = '这是一行用单引号包裹的文本'
print(textOne)
textTwo = "这是一行用双引号包裹的文本"
print(textTwo)
print('\n')

"""
    案例二 处理字符串中出现的引号

"""
print("My name is \"Tom\" ")
print('My name is \'Tom\'')
print('a touch "screen" interface')
print("not to 'talk'")
print('\n')

"""
    案例三 多行文本

"""
mtext = """
--------------------------------------------
函数名称: get_string_operation
开发者: zhao yun
发布日期: 2021 - 12 - 01
版本: 1.0
-------------------------------------------
函数功能: 字符串处理
调用方法:
    string = get_string_operation()
该函数需要传入需要处理的字符串
"""
print(mtext)

class Test:
    """
    1、这是一个测试类
    2、不包含方法
    """
pass
print(f'{Test.__name__}类的帮助文档：\n{Test.__doc__}')