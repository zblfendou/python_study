# coding:utf8
# a test module
__author__ = 'jack zhang'
# 导入模块，方便使用模块中的方法
import sys


def test():
    args = sys.argv
    print 'args:', args
    if len(args) == 1:
        print 'hello, world!'
    elif len(args) == 2:
        print  'hello , %s !' % args[1]
    else:
        print 'Too many arguments!'


if __name__ == '__main__':
    test()

# 优先导入cStringIO ，如果不存在则导入StringIO
try:
    import cStringIO as StringIO
except ImportError:
    import StringIO

try:
    import json
except ImportError:
    import simplejson as json


def _private_1(name):
    return 'Hello, %s' % name


def _private_2(name):
    return 'Hi, %s' % name


def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)


if __name__ == '__main__':
    print greeting('jack zhang')
# 下载ez_setup.py安装包
# from urllib import urlopen
# data = urlopen('http://peak.telecommunity.com/dist/ez_setup.py')
# open('ez_setup.py','wb').write(data.read())
# exit

# 导入图片处理第三方模块
from PIL import Image as image

im = image.open("test.png")
print im.format, im.size, im.mode
# im.thumbnail((200,100))
# im.save('thumb.jpg','JPEG')
# im.rotate(45).show()

import glob, os

size = 128, 128
for infile in glob.glob("*.jpg"):
    file, ext = os.path.splitext(infile)
    im = image.open(infile)
    im.thumbnail(size, image.ANTIALIAS)
    im.save(file + '.jpg', 'JPEG')


# 定义Student类，练习默认函数、设置和获取属性名
class Student():
    def __init__(self):
        pass

    def _print_address(self):
        print "%s 的地址是：%s" % (self._name, self._address)

    def _print_age(self):
        print "%s 的年龄是: %s" % (self._name, self._age)

    def set_name(self, name):
        self._name = name

    def set_age(self, age):
        self._age = age

    def set_address(self, address):
        self._address = address

    def get_name(self):
        return self._name

    def get_address(self):
        return self._address

    def get_age(self):
        return self._age


if __name__ == "__main__":
    s = Student()
    s.set_name("jack zhang")
    s.set_age(28)
    s.set_address("地盛西路1号")
    s._print_address()
    s._print_age()


# 定义Animal和Dog ，练习继承和多态
class Animal:
    def run(self):
        print 'Animal is running...'


class Dog(Animal):
    # 练习多态
    def run(self):
        print 'dog is running...'

    def eat(self):
        print 'dog is eating...'

    # 判断变量类型
    def _isInstance(self, v):
        return isinstance(self, v)

    # 自定义len方法
    def __len__(self):
        return 100


class Cat(Animal):
    pass


# 定义MyObject类，练习getattr()、setattr()、hasattr()
class MyObject(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x ** 2


obj = MyObject()
hasattr(obj, 'x')  # 有属性'x'吗？
hasattr(obj, 'y')  # 有属性'y'吗？
setattr(obj, 'x', 25)  # 设置obj.x值
setattr(obj, 'y', 15)  # 添加属性y，并赋值
getattr(obj, 'y') == 15  # 判断y属性是否设置成功，并比较值是否是设置的
print getattr(obj, 'y')


def readData(fp):
    pass


def readImage(fp):
    if hasattr(fp, 'read'):
        return readData(fp)
    return None


# 动态绑定属性和方法
class Car(object):
    pass


c = Car()
c.name = '卡罗拉'  # 动态给实例绑定一个属性name
print c.name


# 给实例绑定一个方法
def set_name(self, name):
    self._name = name;


from types import MethodType

c.set_name = MethodType(set_name, c, Car)
c.set_name = 1234
print c.set_name


class TestCar():
    __slots__ = ("name", "price")
    pass


tc = TestCar()
tc.name = '雷凌'
tc.price = 1954666
tc.color = 'red'


# 将类中把方法设置成属性调用使用@property
# 避免属性直接暴露导致无法检查参数，随便改写数据
class Family(object):
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise ValueError("age must be an integer!")
        if value < 0 or value > 101:
            raise ValueError("age must be 0~100!")
        self._age = value
