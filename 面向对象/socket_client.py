# -*- coding: utf-8 -*-
'''
import socket

client=socket.socket()  #申明socket类型，同时声称socket对象
client.connect(('localhost',8888))

client.send(b"hello,world")
data=client.recv(1024)
print('recv:',data)

client.close()
'''
#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket
ip_port = ('localhost',8888)

sk = socket.socket()
sk.connect(ip_port)

sk.sendall('请求占领地球')

server_reply = sk.recv(1024)
print(server_reply)

sk.close()

