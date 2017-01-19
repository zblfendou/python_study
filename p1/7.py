#coding:utf8
#定义全局变量
x='i am jack'
def test():
    #定义局部变量
    x='i am tom'
    print x
    global y
    y= 'abcd'


test()
print x
print y