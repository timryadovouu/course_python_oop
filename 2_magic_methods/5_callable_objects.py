import random
from datetime import date

"""=======================ВЫЗЫВАЕМЫЕ-ОБЪЕКТЫ=======================SUMMARY======================================"""


def bar_0():
    class Cat:
        def __init__(self, name):
            self.name = name  # имя кошки

        def __call__(self):
            print('Меня зовут', self.name)

    cat = Cat('Кемаль')
    cat()  # равнозначно cat.__call__()

    # Меня зовут Кемаль

    class Cat:
        def __init__(self, name):
            self.name = name

        def __call__(self, speech):
            print('Меня зовут', self.name, 'и я делаю', speech)

    cat = Cat('Кемаль')
    cat('Мяу')  # равнозначно cat.__call__('Мяу') ---- Меня зовут Кемаль и я делаю Мяу
    cat('Мяяяяяy')  # равнозначно cat.__call__('Мяяяяяy') ---- Меня зовут Кемаль и я делаю Мяяяяяy


def bar_1():
    """__call__() может быть хорошей альтернативой замыканиям"""

    def line_generator(k, b):
        def func(x):
            return k * x + b

        return func

    line_func1 = line_generator(2, 5)  # получаем функцию y = 2*x + 5
    line_func2 = line_generator(-6, 9)  # получаем функцию y = -6*x + 9

    print(line_func1(10))  # выводим значение 2*10 + 5 = 25
    print(line_func2(4))  # выводим значение -6*4 + 9 = -15

    # -----------------------------------------------------------------------
    class LineGenerator:
        def __init__(self, k, b):
            self.k = k
            self.b = b

        def __call__(self, x):
            return self.k * x + self.b

    line_func1 = LineGenerator(2, 5)  # получаем функцию y = 2*x + 5
    line_func2 = LineGenerator(-6, 9)  # получаем функцию y = -6*x + 9

    print(line_func1(10))  # выводим значение 2*10 + 5 = 25
    print(line_func2(4))  # выводим значение -6*4 + 9 = -15


def bar_2():
    """Метод __call__() позволяет реализовывать декораторы на основе классов"""

    def uppercase_decorator(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs).upper()

        return wrapper

    @uppercase_decorator
    def greet(name):
        return f'Привет, {name}'

    print(greet('Кемаль'))  # ПРИВЕТ, КЕМАЛЬ

    # ------------------------------------------------
    class UppercaseDecorator:
        def __init__(self, func):
            self.func = func

        def __call__(self, *args, **kwargs):
            return self.func(*args, **kwargs).upper()

    @UppercaseDecorator
    def greet(name):
        return f'Привет, {name}'

    print(greet('Кемаль'))  # ПРИВЕТ, КЕМАЛЬ


def bar_3():
    """Магический метод __call__() может быть полезен в классах, чьи экземпляры часто изменяют своё состояние"""

    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def __call__(self, x, y):
            self.x, self.y = x, y

    point = Point(1, 2)
    print(point.x, point.y)  # 1 2

    point(3, 4)
    print(point.x, point.y)  # 3 4


def bar_4():
    print(hasattr(int, '__call__'))  # True
    print(hasattr(len, '__call__'))  # True
    print(hasattr(1, '__call__'))  # False
    # ---------------------------------------
    print(callable(int))  # True
    print(callable(len))  # True
    print(callable(1))  # False


"""=======================ВЫЗЫВАЕМЫЕ-ОБЪЕКТЫ==========================TASKS=========================================="""


def task_1():
    class Calculator:
        def __init__(self):
            pass

        def __call__(self, a, b, operation):
            if operation == '/' and b == 0:
                raise ValueError('Деление на ноль невозможно')
            return eval(f'{a}{operation}{b}')

    # TEST_4:
    calculator = Calculator()

    print(calculator(10, 0, '+'))
    print(calculator(10, 0, '-'))
    print(calculator(10, 0, '*'))


def task_2():
    class RaiseTo:
        def __init__(self, degree):
            self.degree = degree

        def __call__(self, x):
            return x ** self.degree

    raise_to_two = RaiseTo(2)

    print(raise_to_two(2))
    print(raise_to_two(3))
    print(raise_to_two(4))


def task_3():
    class Dice:
        def __init__(self, sides):
            self.sides = sides

        def __call__(self):
            return random.randint(1, self.sides)

    kingdice = Dice(6)

    print(kingdice() in [1, 2, 3, 4, 5, 6])
    print(kingdice() in [1, 2, 3, 4, 5, 6])
    print(kingdice() in [7, 8, 9, 10])


def task_4():
    class QuadraticPolynomial:
        def __init__(self, a, b, c):
            self.a = a
            self.b = b
            self.c = c

        def __call__(self, x):
            return self.a * x ** 2 + self.b * x + self.c

    func = QuadraticPolynomial(1, 2, 1)

    print(func(1))
    print(func(2))


def task_5():
    class Strip:
        def __init__(self, chars):
            self.chars = chars

        def __call__(self, string):
            return string.strip(self.chars)

    strip = Strip('.,+-')

    print(strip('     --++beegeek++--'))
    print(strip('-bee...geek-'))
    print(strip('-+,.b-e-e-g-e-e-k-+,.'))


def task_6():
    class Filter:
        def __init__(self, predicate):
            self.predicate = predicate
            if predicate is None:
                self.predicate = bool

        def __call__(self, iterable):
            return list(filter(self.predicate, iterable))

    non_empty = Filter(None)

    sequence = ([], False, 1, (), 'Linus Torvalds', {5, 6, 7}, True, {}, set(), '')
    print(non_empty(sequence))


def task_7():
    class DateFormatter:
        __codes_dict = {"ru": "%d.%m.%Y",
                        "us": "%m-%d-%Y",
                        "ca": "%Y-%m-%d",
                        "br": "%d/%m/%Y",
                        "fr": "%d.%m.%Y",
                        "pt": "%d-%m-%Y"}

        def __init__(self, county_code):
            self.country_code = county_code

        def __call__(self, d):
            """d — дата (тип date)"""
            return d.strftime(self.__codes_dict[self.country_code])

    ru_format = DateFormatter('ru')

    print(ru_format(date(2022, 11, 7)))


def task_8():
    class CountCalls:
        def __init__(self, func):
            self.func = func
            self.calls = 0

        def __call__(self, *args, **kwargs):
            self.calls += 1
            return self.func(*args, **kwargs)

    @CountCalls
    def add(a, b):
        return a + b

    print(add(1, 2))
    print(add(2, 3))
    print(add.calls)


def task_9():
    class CachedFunction:
        def __init__(self, func):
            self.func = func
            self.cache = {}

        def __call__(self, *args):
            result = self.cache.get(args) or self.func(*args)
            self.cache.setdefault(args, result)
            return result
            # if not self.cache.get(args):
            #     self.cache[args] = self.func(*args)
            # return self.cache[args]

    @CachedFunction
    def slow_fibonacci(n):
        if n == 1:
            return 0
        elif n in (2, 3):
            return 1
        return slow_fibonacci(n - 1) + slow_fibonacci(n - 2)

    slow_fibonacci(5)
    for args, value in sorted(slow_fibonacci.cache.items()):
        print(args, value)


def task_10():
    class SortKey:
        def __init__(self, *args):
            self.args = args

        def __call__(self, obj):
            print(obj)
            print(self.args)
            print(tuple(obj.__dict__[i] for i in self.args))
            # print([getattr(obj, attribute) for attribute in self.args])
            return tuple(obj.__dict__[i] for i in self.args)

    class User:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def __repr__(self):
            return f'User({self.name}, {self.age})'

    users = [User('Gvido', 67), User('Timur', 30), User('Arthur', 20)]

    print(sorted(users, key=SortKey('age')))  # сортировка на основе атрибута age
    print(sorted(users, key=SortKey('name', 'age')))  # сортировка на основе атрибута name, а затем age

