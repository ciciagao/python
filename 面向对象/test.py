# -*- coding: utf-8 -*-
import os
import time

#数据文件的路径
b=os.path.dirname(__file__)
print(b)
a=os.path.abspath(os.path.dirname(__file__))
time.sleep(2)
print(a)
print(a.split('\\'))
# BASE_DIR = '\\'.join(os.path.abspath(os.path.dirname(__file__)).split('\\')[:-1])
# #data_path = os.path.join(BASE_DIR,'data')
# time.sleep(2)
# print(BASE_DIR)

ss=[1,2,3]
print(ss[:-1])