"""==============DECORATOR-SINGLEDISPATCHMETHOD==================SUMMARY============================================"""


def bar_0():
    """В примере выше метод __new__() создает экземпляр класса MyClass,
     присваивает его переменной instance и возвращает данный экземпляр."""

    class MyClass:
        def __new__(cls, *args, **kwargs):
            print(args, kwargs)
            instance = object.__new__(cls)
            # instance = super().__new__(cls)  # можно и так определить
            return instance

    obj = MyClass(1, 2, c=3, d=4)

    # print(obj)
    # print(type(obj))


def bar_1():
    class Cat:
        def __new__(cls, *args, **kwargs):
            print('1. Создание экземпляра класса Cat')
            instance = object.__new__(cls)
            return instance

        def __init__(self, name):
            print('2. Инициализация созданного экземпляра класса Cat')
            self.name = name

    # cat = Cat('Кемаль')
    #  or
    cat = Cat.__new__(Cat)
    Cat.__init__(cat, 'Кемаль')

    print(type(cat))
    print(cat.name)


def bar_2():
    """Создание синглтонов, то есть объектов существующих в единственном экземпляре. """

    class Singleton:
        _instance = None

        def __new__(cls, *args, **kwargs):
            if cls._instance is None:  # при первом вызове создаем объект
                cls._instance = object.__new__(cls)
            return cls._instance

    first = Singleton()
    second = Singleton()

    print(first)
    print(second)
    print(first is second)
    # < __main__.bar_2. < locals >.Singleton object at 0x0000024A98E1EF50 >
    # < __main__.bar_2. < locals >.Singleton object at 0x0000024A98E1EF50 >
    # True

# Для определения финализатора используется магический метод __del__().
# Финализатор – это специальный метод, который используется для выполнения действий по очистке перед уничтожением объекта.
def bar_3():
    """финализатор"""

    class MyClass:
        def __del__(self):
            print('Bye')

    obj = MyClass()
    del obj
    # выведет Bye
    # del не уничтожает объект, а удаляет связь между именем и объектом.
    # -----------
    # выводит если количество ссылок на объект памяти равен 0, поэтому:
    # obj1 = MyClass()
    # obj2 = obj1
    # del obj1
    # ничего не выведет

def bar_4():
    """локальные переменные функции существуют только при ее вызове"""
    class MyClass:
        def __del__(self):
            print('Bye')

    def func():
        print('Hi')
        obj = MyClass()

    func()
    # Hi
    # Bye



"""==============DECORATOR-SINGLEDISPATCHMETHOD==================TASKS============================================"""


def task_1():
    """Реализуйте класс Config, который соответствует шаблону синглтон и описывает конфигурационный объект
    с фиксированными параметрами. При создании экземпляра класс не должен принимать никаких аргументов."""

    class Config:
        _instance = None

        def __new__(cls, *args, **kwargs):
            if cls._instance is None:
                cls._instance = object.__new__(cls)
                cls._instance.program_name = 'GenerationPy'
                cls._instance.environment = 'release'
                cls._instance.loglevel = 'verbose'
                cls._instance.version = '1.0.0'
            return cls._instance

    config = Config()

    print(config.program_name)
    print(config.environment)
    print(config.loglevel)
    print(config.version)
