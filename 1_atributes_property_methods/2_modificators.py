def getter():
    """Метод, который возвращает значение атрибута и при этом не изменяет его, называется геттером."""
    class Cat:
        def __init__(self, name):
            self._name = name  # имя кошки

        def get_name(self):  # геттер, используется для получения имени
            return self._name

    cat = Cat('Кемаль')
    print(cat.get_name())

def setter():
    """Метод, который сохраняет значение в атрибуте либо изменяет значение атрибута, называется сеттером."""

    class Cat:
        def __init__(self, name):
            self._name = name

        def get_name(self):
            return self._name

        def set_name(self, name):  # сеттер, используется для изменения имени
            if isinstance(name, str) and name.isalpha():  # проверка имени перед заменой
                self._name = name
            else:
                raise ValueError('Некорректное имя')

    cat = Cat('Кемаль')
    print(cat.get_name())

    cat.set_name('Роджер')
    print(cat.get_name())

def deleter():
    """Метод, который удаляет атрибут из объекта, называется делитером"""

    class Cat:
        def __init__(self, name):
            self._name = name

        def get_name(self):
            return self._name

        def set_name(self, name):
            if isinstance(name, str) and name.isalpha():
                self._name = name
            else:
                raise ValueError('Некорректное имя')

        def del_name(self):  # делитер, используется для удаления имени
            del self._name

    cat = Cat('Кемаль')
    cat.del_name()
    print(cat.get_name())  # AttributeError: 'Cat' object has no attribute '_name'

def task_1():
    from math import pi

    class Circle:
        def __init__(self, radius):
            self._radius = radius
            self._diameter = radius + radius
            self._area = self._radius ** 2 * pi
        def get_radius(self):
            return self._radius
        def get_diameter(self):
            return self._diameter
        def get_area(self):
            return self._area

    circle = Circle(5)
    print(circle.get_radius())
    print(circle.get_diameter())
    print(round(circle.get_area()))


def task_2():
    class BankAccount:
        def __init__(self, balance=0):
            self._balance = balance

        def get_balance(self):
            return self._balance

        def deposit(self, amount):
            self._balance += amount

        def withdraw(self, amount):
            if self._balance - amount < 0:
                raise ValueError("На счете недостаточно средств")
            else:
                self._balance -= amount

        def transfer(self, account, amount):
            self.withdraw(amount)
            account.deposit(amount)

def task_3():
    class User:
        def __init__(self, name, age):
            self.set_name(name)
            self.set_age(age)

        def get_name(self):
            return self._name

        def set_name(self, new_name):
            if isinstance(new_name, str) and new_name.isalpha():
                self._name = new_name
                # return self._name
            else:
                raise ValueError('Некорректное имя')

        def get_age(self):
            return self._age

        def set_age(self, new_age):
            if isinstance(new_age, int) and new_age in range(0, 111):
                self._age = new_age
                # return self._age
            else:
                raise ValueError('Некорректный возраст')
