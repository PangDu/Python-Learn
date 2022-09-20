"""
        ------ 字符串编码 ------

"""
"""
        案例三十六 编码与解码

"""
print(f'{"编码与解码" :^30s}' + "\n")
str = "测试字符串!"
#默认是UTF-8编码
strByte = str.encode()
print(f'原字符串为:{str}\n编码后: {strByte}')
print(f'解码后字符串为:{strByte.decode()}')
str = "qwecte^&&E"
strByte = str.encode(encoding='ASCII')
print(f'原字符串:{str}\n编码后:{strByte}')
print(f'解码后:{strByte.decode()}')
print("="*36)

"""
        案例三十七 ord与chr函数

"""
print(f'{"ord与chr函数" :^30s}' + "\n")
str = "一二三四五六七八九十"
#输出每个字符的Unicode编码
for c in str:
    print(f'{c} -> {ord(c)}')
codes = (20987,39123,20912,30417,29678,21569)
for n in codes:
    print(f'{n} -> {chr(n)}')
print("="*36)
