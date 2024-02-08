import math

"""=======================УНАРНЫЕ-ОПЕРАТОРЫ-И-ФУНКЦИИ=======================SUMMARY=========================================="""


def bar_0():
    class Angle:
        def __init__(self, value):
            self.value = value  # градусная мера угла

        def __repr__(self):
            return f'Angle({self.value})'

        def __pos__(self):
            return Angle(self.value)

        def __neg__(self):
            return Angle(-self.value)

        def __invert__(self):
            if 0 <= self.value <= 180:
                return Angle(180 - self.value)
            return Angle(180 + self.value)

        # ----------------------------------

        def __abs__(self):
            return Angle(abs(self.value))

        def __round__(self, n=None):
            if n is None:
                return Angle(round(self.value))
            return Angle(round(self.value, n))

        def __trunc__(self):
            return Angle(math.trunc(self.value))

        def __floor__(self):
            return Angle(math.floor(self.value))

        def __ceil__(self):
            return Angle(math.ceil(self.value))

    angle = Angle(100)
    print(+angle)  # 100
    print(-angle)  # -100
    print(~angle)  # ~100
    print()
    angle_1 = Angle(-101.54)
    print(abs(angle_1))
    print(round(angle_1))
    print(round(angle_1, 1))
    print(math.trunc(angle_1))
    print(math.floor(angle_1))
    print(math.ceil(angle_1))


def bar_1():
    """меняем знак и минус 1, наверноЕ"""
    print(~0)  # -1
    print(~1)  # -2
    print(~9)  # -10
    print(~-10)  # 9
    print(~20)  # -21
    print(~True)  # равнозначно ~1 ----- -2
    print(~False)  # равнозначно ~0 ----- -1


"""=======================УНАРНЫЕ-ОПЕРАТОРЫ-И-ФУНКЦИИ=======================TASKS=========================================="""


def task_1():
    class ReversibleString:
        def __init__(self, string):
            self.string = string

        def __str__(self):
            return self.string

        def __neg__(self):
            return ReversibleString(self.string[::-1])

    string = ReversibleString('beegeek')

    print(-string)
    print(type(-string))


def task_2():
    class Money:
        def __init__(self, amount):
            self.amount = amount

        def __str__(self):
            return f"{self.amount} руб."

        def __pos__(self):
            return Money(abs(self.amount))

        def __neg__(self):
            return Money(-abs(self.amount))


def task_3():
    class Vector:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def __repr__(self):
            return f"{self.__class__.__name__}({self.x}, {self.y})"

        def __str__(self):
            return f"({self.x}, {self.y})"

        def __pos__(self):
            return Vector(self.x, self.y)

        def __neg__(self):
            return Vector(-self.x, self.y)

        def __abs__(self):
            return (self.x ** 2 + self.y ** 2) ** 0.5


def task_4():
    class ColoredPoint:
        def __init__(self, x, y, color=(0, 0, 0)):
            self.x = x
            self.y = y
            self.color = color  # кортеж из 3 чисел rbb

        def __str__(self):
            return f"({self.x}, {self.y})"

        def __repr__(self):
            return f"{self.__class__.__name__}({self.x}, {self.y}, {self.color})"

        def __pos__(self):
            return self.__class__(self.x, self.y, self.color)

        def __neg__(self):
            return self.__class__(-self.x, -self.y, self.color)

        def __invert__(self):
            return self.__class__(self.y, self.x, tuple(255 - c for c in self.color))

    point1 = ColoredPoint(1, 2, (100, 150, 200))
    point2 = ~point1

    print(repr(point1))
    print(repr(point2))


def task_5():
    class Matrix:
        def __init__(self, rows, cols, value=0):
            self.rows = rows
            self.cols = cols
            self.value = value
            self.matrix = [[value] * cols for _ in range(rows)]

        def get_value(self, r, c):
            return self.matrix[r][c]

        def set_value(self, r, c, value):
            self.matrix[r][c] = value

        def __repr__(self):
            return f"{self.__class__.__name__}({self.rows}, {self.cols})"

        def __str__(self):
            return "\n".join([' '.join(map(str, line)) for line in self.matrix])

        def __pos__(self):
            return self.__class__(self.rows, self.cols, self.value)

        def __neg__(self):
            qwe = Matrix(self.rows, self.cols)
            qwe.matrix = [[-_ for _ in line] for line in self.matrix]
            return qwe

        def __invert__(self):
            """транспонированная"""
            qwe = Matrix(self.rows, self.cols)
            qwe.matrix = [list(line) for line in zip(*self.matrix)]
            qwe.cols, qwe.rows = qwe.rows, qwe.cols
            return qwe

        def __round__(self, n=None):
            qwe = Matrix(self.rows, self.cols)
            if n is None:
                qwe.matrix = [list(map(round, line)) for line in self.matrix]
                return qwe
            qwe.matrix = [[round(_, n) for _ in line] for line in self.matrix]
            return qwe

