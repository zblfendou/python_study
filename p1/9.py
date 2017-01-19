#coding:utf8
#from __future__ import division
import string
def a(x):
    if x<0:
        return -x
    return x
print abs(-12)
l = range(1,11)
print max(l)
print min(l)
print len(l)
s = 'hello'
print len(s)
print divmod(5,2)
print pow(2,3,4)
print round(10)
def f():
    pass
print callable(f)
print isinstance(l,list)
print cmp("def","def")
str = "abacdefg"
print str.capitalize()
print str.replace('a','hello',len(str))
ip = "192.168.1.3"
print ip.split('.',3)
print string.replace(str,'a','hello')
print l
t = [1,2,3,4,5,6,7,8,97]
def f(x):
    if x>=5:
        return True
print filter(f,t)

print filter(lambda x:x%2!=0,t)
