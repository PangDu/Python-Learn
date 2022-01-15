from http.server import HTTPServer,CGIHTTPRequestHandler
sv_addr = 'localhost',9999
with HTTPServer(sv_addr,CGIHTTPRequestHandler) as server:
    print(' 服务器已启动,请在浏览器中的地址栏输入')
server.serve_forever()
#http://localhost:6666/cgi-bin/hello.py