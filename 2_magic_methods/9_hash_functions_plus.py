# Поскольку у равных объектов должны быть равны и хеш-значения, то магический метод __hash__()
# по умолчанию использует идентификатор объекта. А именно, базовая реализация метода __hash__() возвращает
# значение id(obj) // 16.
"""===============================ХЭШ-ФУНКЦИИ=========================SUMMARY========================================"""


# Если неизменяемый пользовательский класс переопределяет метод __eq__(),
# то переопределение метода __hash__() остается на выбор.

def bar_0():
    class Point:
        def __init__(self, x, y):
            self._x = x
            self._y = y

    p1 = Point(1, 2)
    p2 = Point(1, 2)

    print(hash(p1), id(p1) // 16)  # x x
    print(hash(p2), id(p2) // 16)  # y y


def bar_1():
    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def __eq__(self, other):
            if isinstance(other, Point):
                return self.x == other.x and self.y == other.y
            return NotImplemented

    p = Point(1, 2)

    print(Point.__hash__)  # None
    print(hash(p))  # TypeError: unhashable type: 'Point'


"""===============================ХЭШ-ФУНКЦИИ===========================TASKS========================================"""


def task_1():
    class ColoredPoint:
        def __init__(self, x, y, color):
            self._x = x
            self._y = y
            self._color = color

        @property
        def color(self):
            return self._color

        @property
        def x(self):
            return self._x

        @property
        def y(self):
            return self._y

        def __repr__(self):
            return f"{self.__class__.__name__}({self._x}, {self._y}, {repr(self._color)})"

        def __eq__(self, other):
            if isinstance(other, ColoredPoint):
                return self._x == other._x and self._y == other._y and self._color == other._color
            return NotImplemented

        def __hash__(self):
            return hash((self._x, self._y, self._color))

    point = ColoredPoint(1, 2, 'white')

    try:
        point.color = 'black'
    except AttributeError as e:
        print('Error')


def task_2():
    class Row:
        def __init__(self, **kwargs):
            for k, v in kwargs.items():
                object.__setattr__(self, k, v)

        def __setattr__(self, key, value):
            if key in self.__dict__.keys():
                raise AttributeError("Изменение нового атрибута невозможна")
            raise AttributeError("Установка нового атрибута невозможна")

        def __delattr__(self, item):
            raise AttributeError("Удаление атрибута невозможно")

        def __repr__(self):
            return f"{self.__class__.__name__}({', '.join([f'{k}={repr(v)}' for k, v in self.__dict__.items()])})"

        def __eq__(self, other):
            if isinstance(other, self.__class__):
                return self.__dict__ == other.__dict__ and tuple(self.__dict__.keys()) == tuple(other.__dict__.keys())
            return NotImplemented

        def __hash__(self):
            return hash(tuple(self.__dict__.keys()))

    # TEST_4:
    row = Row(a=1, b=2, c=3)

    try:
        row.a = 10
    except AttributeError as e:
        print(e)
