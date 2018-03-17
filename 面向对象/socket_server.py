# -*- coding: utf-8 -*-
'''
import socket
server=socket.socket()
server.bind(('localhost',8888))  #绑定要监听端口
server.listen()  #监听

print(' 我要开始等电话了')
conn.addr = server.accept()  #等电话打进来
print(conn,addr) #conn就是客户端连过来而在服务器端为其生成的一个连接实例

print('电话来了')
data=conn.recv(1024)
print("recv:",data)
conn.send(data.upper())
server.close()
'''
#!/usr/bin/env python
# -*- coding:utf-8 -*-

import socket

ip_port = ('localhost',8888)

sk = socket.socket()
sk.bind(ip_port)
sk.listen(5)

while True:
    print('server waiting...')
    conn,addr = sk.accept()

    client_data = conn.recv(1024)
    print(client_data)
    conn.sendall('不要回答,不要回答,不要回答')


    conn.close()
