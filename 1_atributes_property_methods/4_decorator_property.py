import os

"""===================DECORATOR-PROPERTY==========================SUMMARY============================================"""


def bar_0():
    class Cat:
        def __init__(self, name):
            self._name = name  # имя кошки

        @property
        def name(self):  # геттер свойства name
            return self._name

        @name.setter
        def name(self, name):  # сеттер свойства name
            if isinstance(name, str) and name.isalpha():
                self._name = name
            else:
                raise ValueError('Некорректное имя')

        @name.deleter
        def name(self):  # делитер свойства name
            del self._name

    # or

    # class Cat:
    #     def __init__(self, name):
    #         self._name = name
    #
    #     def get_name(self):
    #         return self._name
    #     name = property(get_name)  # свойство, имеющее только геттер
    #
    #     def set_name(self, name):
    #         if isinstance(name, str) and name.isalpha():
    #             self._name = name
    #         else:
    #             raise ValueError('Некорректное имя')
    #     name = name.setter(set_name)  # свойство, имеющее геттер предыдущего свойства, а также сеттер
    #
    #     def del_name(self):
    #         del self._name
    #     name = name.deleter(del_name)  # свойство, имеющее геттер и сеттер предыдущего свойства, а также делитер

"""===================DECORATOR-PROPERTY==========================TASKS============================================"""

def task_1():
    class Person:
        def __init__(self, name, surname):
            self.name = name
            self.surname = surname

        @property
        def fullname(self):
            return f"{self.name} {self.surname}"

        @fullname.setter
        def fullname(self, info):
            self.name, self.surname = info.split()

def task_2():
    def hash_function(password):
        hash_value = 0
        for char, index in zip(password, range(len(password))):
            hash_value += ord(char) * index
        return hash_value % 10 ** 9

    class Account:
        def __init__(self, login, password):
            self._login = login
            self.password = password

        @property
        def login(self):
            return self._login

        @login.setter
        def login(self, value):
            raise AttributeError("Изменение логина невозможно")

        @property
        def password(self):
            return self._password

        @password.setter
        def password(self, data):
            self._password = hash_function(data)

def task_3():
    class QuadraticPolynomial:
        def __init__(self, a, b, c):
            self.a, self.b, self.c = a, b, c

        @property
        def x1(self):
            if self.b ** 2 - 4 * self.a * self.c > 0:
                return (-self.b - (self.b ** 2 - 4 * self.a * self.c) ** 0.5) / (2 * self.a)
            elif self.b ** 2 - 4 * self.a * self.c == 0:
                return (-self.b) / (2 * self.a)
            return None

        @property
        def x2(self):
            if self.b ** 2 - 4 * self.a * self.c > 0:
                return (-self.b + (self.b ** 2 - 4 * self.a * self.c) ** 0.5) / (2 * self.a)
            elif self.b ** 2 - 4 * self.a * self.c == 0:
                return (-self.b) / (2 * self.a)
            return None

        @property
        def view(self):
            sign_c = "+" if self.c >= 0 else "-"
            sign_b = '+' if self.b >= 0 else '-'
            return f"{self.a}x^2 {sign_b} {abs(self.b)}x {sign_c} {abs(self.c)}"

        @property
        def coefficients(self):
            return self.a, self.b, self.c

        @coefficients.setter
        def coefficients(self, info):
            self.a, self.b, self.c = info

def task_4():
    class Color:
        def __init__(self, hexcode):
            self.hexcode = hexcode

        @property
        def hexcode(self):
            return self._hexcode

        @hexcode.setter
        def hexcode(self, data):
            self._hexcode = data
            self.r = int(data[0:2], 16)
            self.g = int(data[2:4], 16)
            self.b = int(data[4:], 16)

    color = Color('0000FF')
    print(color.hexcode)
    print(color.r)
    print(color.g)
    print(color.b)
    color.hexcode = 'A782E3'
    print(color.hexcode)
    print(color.r)
    print(color.g)
    print(color.b)

