"""
        上下文管理

"""

"""
        案例二百二十三 with语句

"""
print(f'{"案例二百二十三 with语句" :^30s}' + "\n")

with open('lines.txt',mode='wt',encoding='UTF-8') as file:
    file.write(' 今天是星期二\n')
    file.write(' 明天星期三\n')
print(f' 文件{"已" if file.close else "未"}关闭')

print("="*36)

"""
        案例二百二十四 自定义的类型支持上下文管理

"""
print(f'{"案例二百二十三 with语句" :^30s}' + "\n")

print("="*36)