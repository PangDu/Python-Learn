from http.server import CGIHTTPRequestHandler,HTTPServer
CGIHTTPRequestHandler.cgi_directories.append('/cgis')
sv_addr = 'localhost',6668
with HTTPServer(sv_addr,CGIHTTPRequestHandler) as server:
    print(' HTTP服务器已启动')
    print(' 现在可以访问CGI脚本')
    server.serve_forever()

#http://localhost:6668/work/download/GitHub/Python/Python-Learn/11_socket/cgis/hello.py