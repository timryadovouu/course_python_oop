"""=======================РАБОТА-С-АТРИБУТАМИ-ОБЪЕКТОВ=======================SUMMARY========================================"""


def bar_0():
    class MyObject:
        pass

    obj = MyObject()

    obj.attr = 1  # установка атрибута
    obj.attr  # получение значения атрибута
    obj.attr = 2  # изменение значения атрибута
    del obj.attr  # удаление атрибута


# __getattribute__() — вызывается при обращении к любому атрибуту
# __getattr__() — вызывается при обращении к несуществующему атрибуту
# __setattr__() — вызывается при установке атрибута или изменении его значения
# __delattr__() — вызывается при удалении любого атрибута

def bar_1():
    """__getattribute__"""

    class Cat:
        def __init__(self, name):
            self.name = name  # имя кошки

        def __getattribute__(self, attr):
            print(f'Возвращаю значение атрибута {attr}')
            return object.__getattribute__(self, attr)  # получение значения атрибута attr объекта self

    cat = Cat('Кемаль')  # Возвращаю значение атрибута name
    print(cat.name)  # Кемаль


def bar_2():
    """__getattr__"""
    # если в теле метода __getattribute__() было возбуждено исключение AttributeError
    # если метод __getattr__() был явно вызван в теле метода __getattribute__()
    class Cat:
        def __init__(self, name):
            self.name = name

        def __getattr__(self, attr):
            print(f'Возвращаю значение по умолчанию')
            return None

    cat = Cat('Кемаль')

    print(cat.name)  # обращение к существующему атрибуту
    print(cat.age)  # обращение к несуществующему атрибуту
    print(cat.breed)  # обращение к несуществующему атрибуту

    # Кемаль
    # Возвращаю значение по умолчанию
    # None
    # Возвращаю значение по умолчанию
    # None

    class Cat:
        def __init__(self, name, breed):
            self.name = name
            self.breed = breed  # порода кошки

        def __getattr__(self, attr):
            if attr == 'info':
                return f'Имя: {self.name}\nПорода: {self.breed}'
            raise AttributeError

    cat = Cat('Кемаль', 'Британский')
    print(cat.info)
    # Имя: Кемаль
    # Порода: Британский


def bar_3():
    """__setattr__"""

    class Cat:
        def __init__(self, name, breed):
            self.name = name
            self.breed = breed

        def __setattr__(self, attr, value):
            attr = '_' + attr
            self.__dict__[attr] = value
            # object.__setattr__(self, attr, value)

    cat = Cat('Кемаль', 'Британский')
    print(cat.__dict__)  # {'_name': 'Кемаль', '_breed': 'Британский'}


def bar_4():
    """__delattr__"""

    class Cat:
        def __init__(self, name, breed):
            self.name = name
            self.breed = breed

        def __delattr__(self, attr):
            print(f'Удаляю атрибут {attr}')
            del self.__dict__[attr]
            # object.__delattr__(self, attr)

    cat = Cat('Кемаль', 'Британский')

    del cat.name
    print(cat.__dict__)
    # Удаляю атрибут name
    # {'breed': 'Британский'}
    del cat.breed
    print(cat.__dict__)
    # Удаляю атрибут breed
    # {}


def rec():
    """рекурсия"""

    class Cat:
        def __init__(self, name):
            self.name = name

        def __getattribute__(self, attr):
            print(f'Возвращаю значение атрибута {attr}')
            return self.__dict__[attr]

    cat = Cat('Кемаль')
    print(cat.name)

    # Возвращаю значение атрибута name
    # Возвращаю значение атрибута __dict__
    # Возвращаю значение атрибута __dict__
    # Возвращаю значение атрибута __dict__
    # Возвращаю значение атрибута __dict__
    # ...

    class Cat:
        def __init__(self, name, breed):
            self.name = name
            self.breed = breed

        def __setattr__(self, attr, value):
            print(f'Устанавливаю атрибуту {attr} значение {value}')
            attr = '_' + attr
            self.attr = value

    cat = Cat('Кемаль', 'Британский')
    print(cat.__dict__)
    # Устанавливаю атрибуту name значение Кемаль
    # Устанавливаю атрибуту attr значение Кемаль
    # Устанавливаю атрибуту attr значение Кемаль
    # Устанавливаю атрибуту attr значение Кемаль
    # ...


"""=======================РАБОТА-С-АТРИБУТАМИ-ОБЪЕКТОВ=======================TASKS==================================="""


def task_1():
    class Item:
        def __init__(self, name, price, quantity):
            self.name = name
            self.price = price
            self.quantity = quantity

        def __getattribute__(self, attr):
            if attr == 'total':
                return self.price * self.quantity
            elif attr == 'name':
                return object.__getattribute__(self, 'name').title()
            return object.__getattribute__(self, attr)

    fruit = Item('banana', 15, 5)
    print(fruit.price)
    print(fruit.name)
    print(fruit.quantity)
    print(fruit.total)


def task_2():
    class Logger:
        def __init__(self):
            pass

        def __setattr__(self, attr, value):
            print(f"Изменение значения атрибута {attr} на {value}")
            self.__dict__[attr] = value

        def __delattr__(self, attr):
            print(f"Удаление атрибута {attr}")
            del self.__dict__[attr]

    obj = Logger()
    obj.attr = 1
    del obj.attr


def task_3():
    class Ord:
        def __getattr__(self, attr):
            return ord(attr)

    obj = Ord()
    print(obj.a)
    print(obj.b)


def task_4():
    class DefaultObject:
        def __init__(self, default=None, **kwargs):
            self.default = default
            self.__dict__.update(kwargs)

        def __getattr__(self, item):
            return self.default

    # TEST_4:
    god = DefaultObject(default=0, name='Tyr', mythology='scandinavian')
    print(god.__dict__)
    print(god.name)
    print(god.mythology)
    print(god.age)


def task_5():
    class NonNegativeObject:
        def __init__(self, **kwargs):
            # self.__dict__.update({k: abs(v) if isinstance(v, (int, float)) else v for k, v in kwargs.items()})
            for k, v in kwargs.items():
                setattr(self, k, v)

        def __setattr__(self, attr, value):
            if isinstance(value, (int, float)):
                value = abs(value)
            object.__setattr__(self, attr, value)

    point = NonNegativeObject(x=1, y=-2, z=0, color='black')
    print(point.__dict__)
    print(point.x)
    print(point.y)
    print(point.z)
    print(point.color)


def task_6():
    class AttrsNumberObject:
        def __init__(self, **kwargs):
            self.__dict__.update(kwargs)
            self.attrs_num = len(self.__dict__)

        def __setattr__(self, key, value):
            object.__setattr__(self, key, value)
            self.__dict__["attrs_num"] += 1

        def __delattr__(self, item):
            object.__delattr__(self, item)
            self.__dict__["attrs_num"] -= 1

    music_group = AttrsNumberObject(name='Woodkid', genre='pop')
    print(music_group.__dict__)
    print(music_group.attrs_num)
    music_group.country = 'France'
    print(music_group.__dict__)
    print(music_group.attrs_num)


def task_7():
    class Const:
        def __init__(self, **kwargs):
            self.__dict__.update(kwargs)

        def __setattr__(self, key, value):
            if key in self.__dict__:
                raise AttributeError("Изменение значения атрибута невозможно")
            object.__setattr__(self, key, value)
            # if hasattr(self, key):
            #     raise AttributeError('Изменение значения атрибута невозможно')
            # object.__setattr__(self, key, value)

        def __delattr__(self, item):
            raise AttributeError("Удаление атрибута невозможно")

    videogame = Const(name='Cuphead')

    videogame.developer = 'Studio MDHR'
    print(videogame.name)
    print(videogame.developer)

def task_8():
    class ProtectedObject:
        def __init__(self, **kwargs):
            for k, v in kwargs.items():
                object.__setattr__(self, k, v)
                # super().__setattr__(key, value)

        def __getattribute__(self, attr):
            if attr.startswith("_"):
                raise AttributeError("Доступ к защищенному атрибуту невозможен")
            else:
                return object.__getattribute__(self, attr)

        def __setattr__(self, key, value):
            if key.startswith("_"):
                raise AttributeError("Доступ к защищенному атрибуту невозможен")
            object.__setattr__(self, key, value)

        def __delattr__(self, attr):
            if attr.startswith("_"):
                raise AttributeError("Доступ к защищенному атрибуту невозможен")
            return object.__delattr__(self, attr)

    user = ProtectedObject(login='PG_kamiya', _password='alreadybanned')

    try:
        user._password = 'qwerty12345'
    except AttributeError as e:
        print(e)