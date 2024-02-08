import datetime
from functools import singledispatchmethod

"""==============СТРОКОВОЕ=ПРЕДСТАВЛЕНИЕ=ОБЪЕКТОВ==================SUMMARY=========================================="""


def bar_0():
    dt = datetime.date(2022, 10, 23)

    dt_str = str(dt)
    dt_repr = repr(dt)

    print(dt_str, type(dt_str))
    print(dt_repr, type(dt_repr))
    # 2020-10-23 <class 'str'>
    # datetime.date(2022, 10, 23) <class 'str'>

    dt1 = datetime.date(2022, 10, 23)
    dt2 = eval(repr(dt1))
    print(dt2)
    print(type(dt2))
    # 2022-10-23
    # <class 'datetime.date'>


def bar_1():
    dt = datetime.date(2022, 10, 23)

    print(str(dt) == dt.__str__())  # True
    print(repr(dt) == dt.__repr__())  # True

    """примечание"""
    """если объект передается в функцию format() в качестве самостоятельного аргумента,
     то для его отображения автоматически вызывается функция str()."""
    """Во всех остальных случаях, то есть когда объект не передается в качестве самостоятельного аргумента, 
    а, например, является элементом коллекции, вызывается функция repr()."""
    dt = datetime.date(2022, 10, 23)
    print('Дата: {}'.format(dt))  # Дата: 2022-10-23
    print(f'Дата: {dt}')  # Дата: 2022-10-23
    print()
    dates = [datetime.date(2022, 10, 23)]
    print(dates)
    print('Даты: {}'.format(dates))
    print(f'Даты: {dates}')


def bar_2():
    """Если методы __str__() и __repr__() не определены в классе, то используются их базовые реализации и
    их базовые реализации возвращают одно и то же значение."""

    class Cat:
        def __init__(self, name):
            self.name = name  # имя кошки

        def __str__(self):
            return f'Кот по имени {self.name}'

        def __repr__(self):
            return f"Cat('{self.name}')"

    cat = Cat('Кемаль')

    print(str(cat))
    print(repr(cat))
    # Кот по имени Кемаль
    # Cat('Кемаль')


def bar_3():
    """ Если в классе реализован метод __repr__(), но не реализован метод __str__(),
    то при передаче экземпляра данного класса в функцию str() вызывается реализованный метод __repr__()."""

    class Cat:
        def __init__(self, name):
            self.name = name

        def __repr__(self):
            return f"Cat('{self.name}')"

    cat = Cat('Кемаль')
    print(str(cat))  # Cat('Кемаль')
    print(repr(cat))  # Cat('Кемаль')
    print()

    """Однако если в классе реализован __str__(), но не реализован метод __repr__(), 
       то при передаче экземпляра данного класса в функцию repr() вызывается базовая реализация метода __repr__()"""

    class Cat:
        def __init__(self, name):
            self.name = name

        def __str__(self):
            return f'Кот по имени {self.name}'

    cat = Cat('Кемаль')

    print(str(cat))  # Кот по имени Кемаль
    print(repr(cat))  # <__main__.Cat object at 0x0000023C38CB6C80>


"""==============СТРОКОВОЕ=ПРЕДСТАВЛЕНИЕ=ОБЪЕКТОВ====================TASKS=========================================="""


def task_1():
    class Book:
        def __init__(self, title, author, year):
            self.title = title
            self.author = author
            self.year = year

        def __str__(self):
            return f'{self.title} ({self.author}, {self.year})'

        def __repr__(self):
            return f"Book('{self.title}', '{self.author}', {self.year})"


def task_2():
    class Vector:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def __str__(self):
            return f"Вектор на плоскости с координатами ({self.x}, {self.y})"

        def __repr__(self):
            return f"Vector({self.x}, {self.y})"


def task_3():
    class IPAddress:
        @singledispatchmethod
        def __init__(self, ipaddress):
            """строка из четырех целых чисел, разделенных точками"""
            self.ip = ipaddress

        @__init__.register(list)
        @__init__.register(tuple)
        def _for_list_tuple(self, ipaddress):
            """список или кортеж из четырех целых чисел"""
            self.ip = ".".join(map(str, ipaddress))

        def __str__(self):
            return self.ip

        def __repr__(self):
            return f"{self.__class__.__name__}({repr(self.ip)})"

def task_4():
    class PhoneNumber:
        def __init__(self, phone_number):
            """ddd ddd dddd"""
            self.phone_number = phone_number.replace(' ', '')

        def __str__(self):
            return f"({self.phone_number[:3]}) {self.phone_number[3:6]}-{self.phone_number[6:]}"

        def __repr__(self):
            return f"{self.__class__.__name__}({repr(self.phone_number)})"

def task_5():
    class AnyClass:
        def __init__(self, **kwargs):
            self.__dict__.update(kwargs)
        def __str__(self):
            return f"{self.__class__.__name__}: {', '.join(f'{k}={repr(v)}' for k, v in self.__dict__.items())}"

        def __repr__(self):
            return f"{self.__class__.__name__}({', '.join(f'{k}={repr(v)}' for k, v in self.__dict__.items())})"
