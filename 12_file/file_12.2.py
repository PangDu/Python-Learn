"""
        文件与I/O操作

"""

"""
        案例二百八十 读写文本文件

"""
import io
print(f'{"案例二百八十 读写文本文件" :^30s}' + "\n")
file_name = 'lines.txt'
with open(file_name,mode='wt',encoding='UTF-8') as file:
    file.write(' 第一行文本\n')
    file.write(' 第二行文本\n')
with open(file_name,mode='rt',encoding='utf-8') as file:
    content = file.read()
    print(f' content:\n{content}')
print("="*36)
"""
        案例二百八十一 读写二进制文件

"""
print(f'{"案例二百八十一 读写二进制文件" :^30s}' + "\n")
def generat_bytes():
    from random import randint
    i = 0
    bytearr = bytearray()
    while i < 20:
        n = randint(0,255)
        bytearr.append(n)
        i += 1
    return bytearr
file_name = 'my_data'
# 写入文件
with open(file_name,mode='wb') as f:
    bts = generat_bytes()
    f.write(bts)
    print(f' 二进制数据已写入{file_name}文件\n')
# 读取文件
with open(file_name,mode='rb') as f:
    bts = f.read()
    print(f' {file_name}文件内容:{bts}')
print("="*36)
"""
        案例二百八十二 内存流

"""
print(f'{"案例二百八十二 内存流" :^30s}' + "\n")
# StringIO(): 读写文本数据
# BytesIO(): 读写二进制数据
strio = io.StringIO()
strio.write(' 文本一\n')
strio.write(' 文本二\n')
print(f' 文本内存流的内容:\n{strio.getvalue()}')
binio = io.BytesIO()
bs =bytearray()
bs.extend([1,2,3,4,5])
binio.write(bs)
print(f' 二进制内存流的内容:\n{binio.getvalue()}')
print("="*36)