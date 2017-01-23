# coding:utf8
# 动物
class Animal(object):
    pass


# 哺乳和鸟
class Mammal(Animal):
    pass


class Bird(Animal):
    pass


# 各种动物
class Dog(Mammal):
    pass


class Bat(Mammal):
    pass


class Parrot(Bird):
    pass


class Ostrich(Bird):
    pass


# 奔跑和飞行
class Runnable(object):
    def run(self):
        print 'Running...'


class Flyable(object):
    def fly(self):
        print 'flying...'


# 多继承、多继承、多继承
# Mixin的目的就是给一个类增加多个功能，这样，在设计类的时候，我们优先考虑通过多重继承来组合多个Mixin的功能，而不是设计多层次的复杂的继承关系
# class Dog(Mammal, Runnable):
#     pass
#
#
# class Bat(Mammal, Flyable):
#     pass



# 定制类
class Student(object):
    def __init__(self, name):
        self.name = name

    # __str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的。
    def __str__(self):
        return 'Student object (name:%s)' % self.name

    __repr__ = __str__


class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1  # 初始化两个计数器a,b

    # 必须实现一个__iter__()方法，该方法返回一个迭代对象，然后，Python的for循环就会不断调用该迭代对象的next()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环
    def __iter__(self):
        return self  # 实例本身就是迭代对象，故返回自己

    def next(self):
        self.a, self.b = self.b, self.a + self.b  # 计算下一个值
        if self.a > 100000:  # 退出循环条件
            raise StopIteration();
        return self.a  # 返回下一个值
