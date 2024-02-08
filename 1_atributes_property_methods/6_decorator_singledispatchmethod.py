from functools import singledispatchmethod
from datetime import date
from dateutil.relativedelta import relativedelta
import typing

"""==============DECORATOR-SINGLEDISPATCHMETHOD==================SUMMARY============================================"""


def bar_0():
    class Cat:
        def __init__(self, breed, name, birth_date):
            self.breed = breed
            self.name = name
            if isinstance(birth_date, date):
                self.birth_date = birth_date
            elif isinstance(birth_date, str):
                self.birth_date = date.fromisoformat(birth_date)
            else:
                raise ValueError(f'неверный формат даты: {birth_date}')

    cat = Cat('Британский', 'Кемаль', 1617173745)


def bar_1():
    class Cat:
        def __init__(self, breed, name):
            self.breed = breed
            self.name = name

        @classmethod
        def create_british_cat(cls, name):
            return cls('Британский', name)

        @classmethod
        def create_kemal_cat(cls, breed):
            return cls(breed, 'Кемаль')

    cat1 = Cat('Британский', 'Кемаль')
    cat2 = Cat.create_british_cat('Роджер')
    cat3 = Cat.create_kemal_cat('Шотландский')

    print(cat1.breed, cat1.name)
    print(cat2.breed, cat2.name)
    print(cat3.breed, cat3.name)


def bar_2():
    """singledispatchmethod"""

    class MyClass:
        @singledispatchmethod
        def base_implementation(self, arg):
            print('Базовая реализация')

        # @base_implementation.register
        # def int_implementation(self, arg: int):
        # нельзя объединить аннотации типов -- arg: int | float -- нельзя
        # Также мы не можем использовать абстрактные типы из модуля typing -- arg: typing.Iterable
        @base_implementation.register(int)
        def int_implementation(self, arg):
            print('Реализация для целочисленного аргумента')

        @base_implementation.register(str)
        def str_implementation(self, arg):
            print('Реализация для строкового аргумента')

    obj = MyClass()

    obj.base_implementation(1)
    obj.base_implementation('bee')
    obj.base_implementation([1, 2, 3])


def bar_3():
    """перегрузка метода __init__()"""

    class Cat:
        @singledispatchmethod
        def __init__(self, breed, name, age):
            self.breed = breed
            self.name = name
            self.age = age

        @__init__.register(list)
        def _from_list(self, data):  # НИЖНЕЕ ПОДЧЕРКИВАНИЕ -- ЗАЩИЩЕННЫЙ МЕТОД
            self.breed, self.name, self.age = data

    cat1 = Cat('Британский', 'Кемаль', 1)  # передаем все данные отдельно
    cat2 = Cat(['Манчкин', 'Роджер', 1])  # передаем список с данными

    print(cat1.breed, cat1.name, cat1.age)
    print(cat2.breed, cat2.name, cat2.age)


def bar_4():
    """сразу несколько"""

    class Cat:
        @singledispatchmethod
        def __init__(self, breed, name, age):
            self.breed = breed
            self.name = name
            self.age = age

        @__init__.register(list)
        @__init__.register(tuple)
        def _from_list_tuple(self, data):
            self.breed, self.name, self.age = data

    cat1 = Cat(('Британский', 'Кемаль', 1))
    cat2 = Cat(['Манчкин', 'Роджер', 1])

    print(cat1.breed, cat1.name, cat1.age)
    print(cat2.breed, cat2.name, cat2.age)


def bar_5():
    """Не только один тип на входе"""
    from multimethod import multimethod

    class MyClass:
        @multimethod
        def base_implementation(self, arg):
            print('Базовая реализация')

        @base_implementation.register
        def intfloat_implementation(self, arg: int | float):
            print('Реализация для целочисленного и вещественного аргументов')

    obj = MyClass()
    obj.base_implementation(1)
    obj.base_implementation(1.0)


def task_6():
    class MyClass:
        @singledispatchmethod
        def method(self, arg):
            print('Базовая реализация метода экземпляра')

        @method.register(int)  # перегружаем метод экземпляра
        def _method(self, arg):
            print('Реализация метода экземпляра для целочисленного аргумента')

        @singledispatchmethod
        @classmethod
        def class_method(cls, arg):
            print('Базовая реализация метода класса')

        @class_method.register(str)  # перегружаем метод класса
        @classmethod
        def _class_method(cls, arg):
            print('Реализация метода класса для строкового аргумента')

        @singledispatchmethod
        @staticmethod
        def static_method(arg):
            print('Базовая реализация статического метода')

        @static_method.register(list)  # перегружаем статический метод
        @staticmethod
        def _static_method(arg):
            print('Реализация статического метода для списочного аргумента')

    obj = MyClass()

    obj.method('bee')
    obj.method(1)
    print()

    obj.class_method(1)
    obj.class_method('bee')
    print()

    obj.static_method(1)
    obj.static_method(['b', 'e', 'e'])


"""==============DECORATOR-SINGLEDISPATCHMETHOD==================TASKS============================================"""


def task_1():
    class Processor:
        @singledispatchmethod
        @staticmethod
        def process(data):
            raise TypeError('Аргумент переданного типа не поддерживается')

        @process.register(int)
        @process.register(float)
        @staticmethod
        def _process_int(data):
            return data * 2

        @process.register(str)
        @staticmethod
        def _process_str(data):
            return data.upper()

        @process.register(list)
        @staticmethod
        def _process_list(data):
            return sorted(data)

        @process.register(tuple)
        @staticmethod
        def _process_list(data):
            return tuple(sorted(data))


def task_2():
    class Negator:
        @singledispatchmethod
        @staticmethod
        def neg(data):
            raise TypeError("Аргумент переданного типа не поддерживается")

        @neg.register(int)
        @neg.register(float)
        @staticmethod
        def _numbers(data):
            return -data

        @neg.register(bool)
        @staticmethod
        def _tf(data):
            return not data


def task_3():
    class Formatter:
        @singledispatchmethod
        @staticmethod
        def format(data):
            raise TypeError("Аргумент переданного типа не поддерживается")

        @format.register(int)
        @format.register(float)
        @staticmethod
        def _intfloat(data, prefix="Вещественное"):
            if isinstance(data, int):
                prefix = "Целое"
            print(f"{prefix} число: {data}")

        @format.register(list)
        @format.register(tuple)
        @staticmethod
        def _listtuple(data, postfix="списка"):
            if isinstance(data, tuple):
                postfix = "кортежа"
            print(f"Элементы {postfix}: {', '.join(map(str, data))}")

        @format.register(dict)
        @staticmethod
        def _dict(data):
            print(f"Пары словаря: {', '.join(map(str, data.items()))}")

    Formatter.format({'Cuphead': 1, 'Mugman': 3})
    Formatter.format({1: 'one', 2: 'two'})
    Formatter.format({1: True, 0: False})


def task_4():
    class BirthInfo:
        @singledispatchmethod
        def __init__(self, birth_date) -> typing.NoReturn:
            """iso format"""
            # self.birth_date = birth_date
            raise TypeError("Аргумент переданного типа не поддерживается")

        @__init__.register(date)
        def _dateformat(self, birth_date):
            self.birth_date = birth_date

        @__init__.register(str)
        def _dateformat(self, birth_date):
            try:
                self.birth_date = date.fromisoformat(birth_date)
            except:
                raise TypeError("Аргумент переданного типа не поддерживается")

        @__init__.register(tuple)
        @__init__.register(list)
        def _dateformat(self, birth_date):
            self.birth_date = date(year=birth_date[0], month=birth_date[1], day=birth_date[2])

        @property
        def age(self):
            return relativedelta(date.today(), self.birth_date).years
