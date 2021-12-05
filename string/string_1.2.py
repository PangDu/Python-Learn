# - * - coding: UTF-8 - * -
"""
        ------ 代码注释与帮助文档 ------

"""

"""
    案例四 在代码中写注释

"""
#定义变量
varOne = 1000

#定义函数
def funtionOne():
    pass

#定义类
class Demo:                                 #声明新类
    def __init__(self) -> None:             #构造函数
        self.age = 18                       #属性 age
        self.name = "jack"                  #属性 name
        self.address = "北京"                #属性 address


"""
    案例五 为代码对象撰写帮助文档

"""
class cvt_bytes:
    "在字符串与字节序列之间转换"
    @staticmethod
    def tobytes(somestring):
        """
        将字符串对象转换为字节序列，参数somestring
        为字符串对象
        """
        return str(somestring).encode('UTF-8')
    
    @staticmethod
    def tostring(someBytes):
        """
        从字节序列还原字符串,参数someBytes为字节序列
        """
        bs = bytes(someBytes)
        return bs.decode('UTF-8')

print(help(cvt_bytes))