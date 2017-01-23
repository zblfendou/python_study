# coding:utf8
# a test module
__author__ = 'jack zhang'
import sys

print 'a', __name__


def test():
    args = sys.argv
    if len(args) == 1:
        print 'hello, world!'
    elif len(args) == 2:
        print  'hello , %s !' % args[1]
    else:
        print 'Too many arguments!'


if __name__ == '__main__':
    test()
