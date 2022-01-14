"""
        方法成员

"""

"""
        案例一百九十四 实例方法

"""
print(f'{"案例一百九十四 实例方法" :^30s}' + "\n")

class bytes_converter:
        def __init__(self,numbase = 16):
             if numbase not in (2,8,16):
                     raise Exception('numbase 参数的有效值为: 2、8、16')
             self._base = numbase
        def convert_to_str(self,bts):
                if type(bts) is not bytes:
                        raise TypeError('bts 参数应为 bytes 类型')
                r = []
                for b in bts:
                        if self._base == 2:
                                r.append(bin(b))
                        elif self._base == 8:
                                r.append(oct(b))
                        elif self._base == 16:
                                r.append(hex(16))
                        else:
                                r.append(str(b))
                return '_'.join(r)
orgb = b'k76h52e'
cb,co,cx = bytes_converter(2),bytes_converter(8),bytes_converter(16)
strb = cb.convert_to_str(orgb)
stro = co.convert_to_str(orgb)
strx = cx.convert_to_str(orgb)
print(f'原字节序列: {orgb}\n')
print(f' 二进制: {strb}\n 八进制: {stro}\n 十六进制: {strx}')

print("="*36)

"""
        案例一百九十五 类方法

"""
print(f'{"案例一百九十五 类方法" :^30s}' + "\n")

class demoClass:
        @classmethod
        def do_something(cls,a,b,c):
                print(f' 类方便被调用,参数:\n cls: {cls}\n a: {a}\n b: {b}\n c: {c}' )
demoClass.do_something(100,200,300)

print("="*36)

"""
        案例一百九十六 静态方法

"""
print(f'{"案例一百九十六 静态方法" :^30s}' + "\n")

class data_helper:
        @staticmethod
        def disconnect():
                print(f' 静态方法 {data_helper.disconnect.__name__} 被调用')
data_helper.disconnect()

print("="*36)