"""
        HTTP与CGI编程

"""

"""
        案例二百七十四 使用HTTP协议下载文件

"""
print(f'{"案例二百七十四 使用HTTP协议下载文件" :^30s}' + "\n")
from email import charset
from fileinput import filename
import http.client as httpc
file_name = 'test.jpg'
conn = httpc.HTTPConnection('p7.itc.cn')
conn.request('GET','/images01/20211225/f0c36f493de146e7bd4ebb08a3071573.jpeg')
resp = conn.getresponse()
with open(file_name,mode='wb')as f:
    data = bytearray(4096)
    while resp.readinto(data) > 0:
        f.write(data)
resp.close()
print("="*36)
"""
        案例二百七十五 简单的HTTP服务器

"""
print(f'{"案例二百七十五 简单的HTTP服务器" :^30s}' + "\n")
# 处理HTTP请求,可供调用的方法:
# send_response(): 发送服务器相关的响应头
# send_header(): 发送响应的HTTP头
# end_header: 在所有HTTP头发送完后,需调用此方法。会在响应消息中插入一个空白行,空白行后便是HTTP正文部分
# wfile: 要写入响应消息的正文,需使用wfile属性
from http.server import BaseHTTPRequestHandler, HTTPServer
class MyRequesthandler(BaseHTTPRequestHandler):
    def do_GET(self):
        body = """
        <html>
            <body>
            <h3>欢迎</h3>
            <div>来到我的小站</div>
            </body>
        </html>
        """
        # 发送响应头
        self.send_response(200,'ok')
        self.send_header('copyright','XZX')
        # 内容类型以及字符编码
        self.send_header('Content-Type','text/html;charset=UTF-8')
        self.end_headers()
        # 发送响应正文
        self.wfile.write(body.encode())
sv_addr = 'localhost',8060
with HTTPServer(sv_addr,MyRequesthandler) as sv:
    print(' 服务已初始化完成')
    print(' 请在浏览器地址栏中输入:http://localhost进行测试')
    sv.serve_forever()
print("="*36)
"""
        案例二百七十六 编写CGI脚本

"""
print(f'{"案例二百七十六 编写CGI脚本" :^30s}' + "\n")
print("="*36)
"""
        案例二百七十七 设置CGI脚本的查找目录

"""
print(f'{"案例二百七十七 设置CGI脚本的查找目录" :^30s}' + "\n")

print("="*36)