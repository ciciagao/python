# -*- coding: utf-8 -*-
#方法一:普通方法
'''

class Foo(object):
    def __init__(self,name):
        self.name = name
f = Foo('alex')
'''
#方法二：装逼方法
def __init__(self,name,age):
    self.name=name
    self.age=age
def func(self):
    print('hello %s'%self.name)
Foo = type('Foo', (object,), {'talk': func,'__init__':__init__})
print(type(Foo))
f = Foo('gqq',18)
f.talk()
print(type(Foo))
#这说明type是类的类，装逼技能

