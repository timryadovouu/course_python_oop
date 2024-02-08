"""==============DECORATOR-CLASSMETHOD-STATICMETHOD==============SUMMARY============================================"""

# МЕТОДЫ ЭКЗЕМПЛЯРА --- имеют обязательный параметр self --- МЕТОДЫ ЭКЗЕМПЛЯРА
# Методы класса и статические методы можно вызывать не только через класс, но и через экземпляр класса.
def bar_0():
    class Cat:
        def __init__(self, name, age):
            self.name = name  # имя кошки
            self.age = age  # возраст кошки
            self.favorite_things = []  # список любимых вещей кошки

        def about(self):
            return f'Имя: {self.name}, возраст: {self.age}'  # обращаемся к атрибутам объекта

        def loves(self, thing):
            self.favorite_things.append(thing)  # изменяем значение атрибута объекта

    cat = Cat('Кемаль', 1)

    cat.loves('Тимур')  # вызов метода через экземпляр
    Cat.loves(cat, 'Дом')  # вызов метода через класс

    print(Cat.about(cat))  # вызов метода через класс
    print(cat.favorite_things)

# МЕТОДЫ КЛАССА --- имеют обязательный параметр cls --- МЕТОДЫ КЛАССА
# Методы класса и статические методы можно вызывать не только через класс, но и через экземпляр класса.
def bar_1():
    # example
    # class MyClass:
    #     @classmethod
    #     def my_classmethod(cls):
    #         print('Это метод класса')
    #         print(cls)
    #
    # MyClass.my_classmethod()  # out:: Это метод класса <\n> <class '__main__.bar_1.<locals>.MyClass'>
    class Cat:
        def __init__(self, breed, name):
            self.breed = breed
            self.name = name

        @classmethod
        def british(cls, name):
            return cls('Британский', name)  # равнозначно Cat('Британский', name)

    cat = Cat.british('Кемаль')
    print(cat.breed, cat.name)

# СТАТИЧЕСКИЕ МЕТОДЫ --- СТАТИЧЕСКИЕ МЕТОДЫ --- СТАТИЧЕСКИЕ МЕТОДЫ --- СТАТИЧЕСКИЕ МЕТОДЫ
# Не имеют обязательного параметра self или cls
# Поэтому статические методы не могут изменять ни состояние объекта, ни состояние класса
# Статические методы можно считать обычными функциями, которые помещены в класс для удобства
# Методы класса и статические методы можно вызывать не только через класс, но и через экземпляр класса.

def bar_2():
    #example
    # class MyClass:
    #     @staticmethod
    #     def my_staticmethod():
    #         print('Это статический метод')
    #
    # MyClass.my_staticmethod()  # Это статический метод

    class Cat:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def get_age(self, in_human_years=False):
            if in_human_years:
                return Cat.age_in_human_years(self.age)  # переводим кошачьи года в человеческие
            return self.age

        @staticmethod
        def age_in_human_years(age):
            return (age + (age < 5) - (age > 8)) * 7  # переводим кошачьи года в человеческие

    cat = Cat('Кемаль', 2)

    print(cat.get_age())  # возраст в кошачьих годах --- 2
    print(cat.get_age(True))  # возраст в человеческих годах --- 21

def bar_3():
    """ Помимо того, что методы экземпляра могут изменять состояние объекта, они так же могут получать доступ к
     самому классу через атрибут __class__ экземпляра класса. Это означает, что методы экземпляра также могут
     изменять состояние класса."""
    class MyClass:
        def method(self):
            print('Это метод экземпляра')
            print(self)
            print(self.__class__)

    obj = MyClass()
    obj.method()

"""==============DECORATOR-CLASSMETHOD-STATICMETHOD==============TASKS============================================"""

def task_1():
    class Circle:
        def __init__(self, radius):
            self.radius = radius

        @classmethod
        def from_diameter(cls, d):
            return cls(d / 2)

def task_2():
    class Rectangle:
        def __init__(self, length, width):
            self.length = length
            self.width = width

        @classmethod
        def square(cls, side):
            return cls(side, side)

    rectangle = Rectangle(4, 5)
    print(rectangle.length)
    print(rectangle.width)

    rectangle = Rectangle.square(5)
    print(rectangle.length)
    print(rectangle.width)

def task_3():
    class QuadraticPolynomial:
        def __init__(self, a, b, c):
            self.a = a
            self.b = b
            self.c = c

        @classmethod
        def from_iterable(cls, iterable):
            return cls(*iterable)

        @classmethod
        def from_str(cls, string):
            return cls(*map(float, string.split()))

def task_4():
    class Pet:
        pets = []

        def __init__(self, name):
            self.name = name
            Pet.pets.append(self)
            # self.__class__.pets.append(self)

        @classmethod
        def first_pet(cls):
            return cls.pets[0] if cls.pets else None

        @classmethod
        def last_pet(cls):
            return cls.pets[-1] if cls.pets else None

        @classmethod
        def num_of_pets(cls):
            return len(cls.pets)
def task_5():
    import re
    class CaseHelper:
        @staticmethod
        def is_snake(line):
            if re.fullmatch(r"([a-z]+_)\1*[a-z]+|[a-z]+", line):
                return True
            return False

        @staticmethod
        def is_upper_camel(line):
            if re.fullmatch(r"^([A-Z][a-z]+)([A-Z][a-z]+)*\2*", line):
                return True
            return False

        @staticmethod
        def to_snake(line):
            """принимает в качестве аргумента строку в стиле Upper Camel Case, записывает ее в стиле Snake Case"""
            if re.fullmatch(r"[A-Z][a-z]+", line):
                return line.lower()
            else:
                qwe = line[0] + re.sub(r"([A-Z])", r"_\1", line[1:])
                return qwe.lower()

        @staticmethod
        def to_upper_camel(line):
            """принимает в качестве аргумента строку в стиле Snake Case, записывает ее в стиле Upper Camel Case"""
            if re.fullmatch(r"[a-z]+", line):
                return line.capitalize()
            else:
                return "".join(map(lambda item: item.capitalize(), re.split(r"_", line)))