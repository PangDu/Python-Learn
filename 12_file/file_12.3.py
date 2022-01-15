"""
        数据文件

"""

"""
        案例二百八十三 读写CSV文件

"""
import csv
print(f'{"案例二百八十三 读写CSV文件" :^30s}' + "\n")
# 写入记录
with open('a.csv',mode='w',newline='') as f:
    wt = csv.writer(f)
    wt.writerow(['abc','def','ghi'])
    wt.writerow(['opq','rst','uvw'])
    wt.writerow([99,888,666666])
# 读取记录
with open('a.csv',mode='r',newline='') as f:
    rd = csv.reader(f)
    for row in rd:
        print(f' row: {row}')
print("="*36)
"""
        案例二百八十四 读写JSON文件

"""
import json
print(f'{"案例二百八十四 读写JSON文件" :^30s}' + "\n")
json_file = 'a.json'
obj = {
    'product_id' : 'C-00021',
    'product_name': 'NLVX',
    'product_sn' : 'D15CKF8PID2'
}
with open(json_file,mode='w') as fs:
        json.dump(obj,fs)
obj = {}
with open(json_file,mode='r') as fs:
    obj = json.load(fs)
    print(f' {json_file}中读出的内容:\n{obj}]')
print("="*36)
"""
        案例二百八十五 生成zip文件

"""
import zipfile
print(f'{"案例二百八十五 生成zip文件" :^30s}' + "\n")
file_name = 'abc.zip'
# 创建zip并添加文件
with zipfile.ZipFile(file_name,mode='w') as zp:
    # 将两字节序列对象添加到zip文档中
    zp.writestr('1.bin',b'\x2a\x37\x3c\x2f\x33')
    zp.writestr('2.bin',b'\x62\xb3\x19\x8d\x72')
    # 添加字符串对象
    zp.writestr('3.txt','测试数据')
# 解压缩
with zipfile.ZipFile(file_name,mode='r') as zp:
    zp.extractall()
    zp.printdir()
print("="*36)