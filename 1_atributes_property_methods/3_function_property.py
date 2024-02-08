def task_0():
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

        name = property(get_name, set_name)

    print(Cat.name.fget)                                   # обращаемся к геттеру свойства
    print(Cat.name.fset)                                   # обращаемся к сеттеру свойства
    print(Cat.name.fdel)                                   # обращаемся к делитеру свойства


def task_01():
    """Обратите внимание, что в инициализаторе мы не создаем атрибут name, мы обращаемся к уже имеющемуся свойству
    name и изменяем его значение, что приводит к вызову сеттера, внутри которого происходит создание атрибута _name с
    соответствующим значением."""
    class Cat:
        def __init__(self, name):
            self.name = name

        def get_name(self):
            return self._name

        def set_name(self, name):
            if isinstance(name, str) and name.isalpha():
                self._name = name
            else:
                raise ValueError('Некорректное имя')

        name = property(get_name, set_name)

    cat = Cat(-1)
    print(cat.name)

def task_02():
    class Cat:
        def __init__(self, name):
            self._name = name

        def get_name(self):
            return self._name

        def del_name(self):
            del self._name

        name = property(get_name, fdel=del_name, doc='Имя кошки. Доступно только для чтения.')

    cat = Cat('Кемаль')
    del cat.name  # равнозначно cat.del_name()
    print(cat.name)  # AttributeError: 'Cat' object has no attribute '_name'
    print(Cat.name.__doc__)

def task_1():
    class Rectangle:
        def __init__(self, length, width):
            self.length = length
            self.width = width

        def get_perimeter(self):
            return 2 * (self.width + self.length)

        def get_area(self):
            return self.width * self.length

        perimeter = property(get_perimeter)
        area = property(get_area)

    rectangle = Rectangle(4, 5)

    rectangle.length = 2
    rectangle.width = 3
    print(rectangle.length)
    print(rectangle.width)
    print(rectangle.perimeter)
    print(rectangle.area)

def task_2():
    class HourClock:
        def __init__(self, hours):
            self.hours = hours

        def get_hour(self):
            return self._hours

        def set_hour(self, hour):
            if isinstance(hour, int) and hour in range(1, 13):
                self._hours = hour
            else:
                raise ValueError("Некорректное время")

        hours = property(get_hour, set_hour)

def task_3():
    class Person:
        def __init__(self, name, surname):
            self.name = name
            self.surname = surname

        def get_fullname(self):
            return f"{self.name} {self.surname}"

        def set_fullname(self, info):
            self.name, self.surname = info.split()

        fullname = property(get_fullname, set_fullname)

    person = Person('Джон', 'Маккарти')

    person.fullname = 'Алан Тьюринг'
    print(person.name)
    print(person.surname)
