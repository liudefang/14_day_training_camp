# -*- encoding: utf-8 -*-
# @Time    : 18-6-27 下午4:42
# @Author  : mike.liu
# @File    : 12 元类.py

# 元类是类的类，是类的模板
# 元类是用来控制如何创建类的，正如类是创建对象的模板一样，而元类的主要目的是为了控制类的创建行为
# 元类的实例化的结果为我们用class定义的类，正如类的实例为对象(f1对象是Foo类的一个实例，
# Foo类是 type 类的一个实例)
# 步骤一：如果说People=type（类名，类的父类们，类的名称空间),那么我们定义元类如下，来控制类的创建
class Mymeta(type):     # 继承默认元类的一堆属性
    def __init__(self, class_name, class_bases, class_dic):
        if '__doc__' not in class_dic or not class_dic.get('__doc__').strip():
            raise TypeError('必须为类指定文档注释')

        if not class_name.istitle():
            raise TypeError('类名首字母必须大写')

        super(Mymeta, self).__init__(class_name, class_bases, class_dic)

class People(object, metaclass=Mymeta):
    country = 'China'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):
        print('%s is talking' % self.name)

# 步骤二：如果我们想控制类实例化的行为，那么需要先储备知识__call__方法的使用
class People(object, metaclass=type):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __call__(self, *args, **kwargs):
        print(self.args, kwargs)


# 调用类People，并不会触发__call__
obj = People('egon', 18)

# 调用对象obj(1,2,3,a=1,b=2,c=3),才会触发对象的绑定方法obj.__call__(1,2,3,a=1,b=2,c=3)

# 总结：如果说类People是元类type的实例，那么在元类type内肯定也有一个__call__，会调用People('egon','18')

# 步骤三：自定义元类，控制类的调用(即实例化)的过程
class Mymeta(type): # 继承默认元类的一堆属性
    def __init__(self, class_name, class_bases, class_dic):
        if not class_name.istitle():
            raise TypeError('类名首字母必须大写')

        super(Mymeta, self).__init__(class_name, class_bases, class_dic)

    def __call__(self, *args, **kwargs):
        print(self, args, kwargs)

        # 1.实例化People,产生空对象obj
        obj = object.__new__(self)

        # 2. 调用People下的函数__init__,初始化obj
        self.__init__(obj, *args, **kwargs)

        # 3. 返回初始化好了的obj
        return obj

obj = People('egon', 18)
print(obj.__dict__)


# 步骤四：
class Mymeta(type):  # 继承默认元类的一堆属性
    def __init__(self, class_name, class_bases, class_dic):
        if not class_name.istitle():
            raise TypeError('类名首字母必须大写')

        super(Mymeta, self).__init__(class_name, class_bases, class_dic)

    def __call__(self, *args, **kwargs):
        print(self, args, kwargs)

        # 1.调用self，即People下的函数__new__，在该函数内完成：1.产生空对象obj 2.初始化 3.返回obj
        obj = self.__new__(self, *args, **kwargs)

        # 2. 一定记得返回obj，因为实例化People(),取得就是__call__的返回值
        return  obj

class People(object, metaclass=Mymeta):
    country = 'China'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):
        print('%s is talking' % self.name)

    def __new__(cls, *args, **kwargs):
        obj = object.__new__(cls)
        cls.__init__(obj, *args, **kwargs)
        return obj

obj = People('egon', 18)
print(obj.__dict__)

# 步骤五：基于元类实现单例模式，比如数据库对象，实例化时参数都一样，就没有必要重复产生对象，浪费内存
class Mysql:
    __instance = None
    def __init__(self, host='127.0.0.1', port='3306'):
        self.host = host
        self.port = port

    @classmethod
    def singleton(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance=cls(*args, **kwargs)

        return cls.__instance

obj1=Mysql()
obj2=Mysql()
print(obj1 is obj2)

# 应用：定制元类实现单例模式
class Mymeta(type):
    def __init__(self, name, bases, dic):   # 定义类Mysql时就触发
        self.__instance=None
        super().__init__(name, bases, dic)

    def __call__(self, *args, **kwargs):    # mysql(...)时触发

        if not self.__instance:
            self.__instance=object.__new__(self)    # 产生对象
            self.__init__(self.__instance, *args, **kwargs)
            # 上述两步可以合成下面一步
            # self.__instance=super().__call__(*args, **kwargs)
        return self.__instance

class Mysql(metaclass=Mymeta):
    def __init__(self, host='127.0.0.1', port='3306'):
        self.host = host
        self.port = port
obj1 = Mysql()
obj2 = Mysql()




