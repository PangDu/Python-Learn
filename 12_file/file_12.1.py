"""
        目录操作

"""

"""
        案例二百七十八 创建于删除目录

"""
print(f'{"案例二百七十八 创建于删除目录" :^30s}' + "\n")
# mkdir(): 创建目录,一般采用相对路径
# rmdir(): 删除制定目录,一般为相对路径
import os
dirs = 'folder1','folder2','folder3'
for d in dirs:
    try:
        os.mkdir(d)
        print(f' 已创建{d}目录')
    except FileExistsError:
        print(f' {d}目录已存在')

for d in dirs:
        try:
                os.rmdir(d)
                print(f' 删除{d}目录')
        except:
                pass
print("="*36)
"""
        案例二百七十九 创建与删除嵌套目录

"""
print(f'{"案例二百七十九 创建与删除嵌套目录" :^30s}' + "\n")
dirs = [
        '/src/lang/zh-chs',
        '/src/lang/zh-cht',
        '/src/logos/96dpi',
        '/src/icons/app/view'
]
for d in dirs:
        try:
                os.makedirs(d,exist_ok=True)
                print(f' 目录{d}已创建')
        except Exception:
                pass
for d in dirs:
        try:
                os.removedirs(d)
        except Exception:
                pass
print("="*36)