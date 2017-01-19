# coding:utf8
# 将整数除法按照小数出结果
from __future__ import division


def jia(x, y):
    return x + y


def jian(x, y):
    return x - y


def cheng(x, y):
    return x * y


def chu(x, y):
    return x / y


def operator(x, o, y):
    if o == "+":
        return jia(x, y)
    elif o == "-":
        return jian(x, y)
    elif o == "*":
        return cheng(x, y)
    elif o == "/":
        return chu(x, y)
    else:
        pass  # 代码桩


#print operator(2, '*', 5)

# 修改成switch形式
if __name__ =="__main__":
    num =  operator_switch = {"+": jia, "-": jian, "*": cheng, "/": chu}
    print "num:",num

def f(x,o,y):
    return operator_switch.get(o)(x,y)
if __name__ =="__main__":
    print f(3,"+",8)
