from functools import total_ordering

"""=======================СРАВНЕНИЕ-ОБЪЕКТОВ=======================SUMMARY=========================================="""


def bar_0():
    class Point:
        """если в классе не определено, как будет происходить сравнение с помощью оператора ==,
         оно будет равносильно сравнению с помощью is"""

        def __init__(self, x, y):
            self.x = x
            self.y = y

    p1 = Point(1, 2)
    p2 = Point(1, 2)

    print(p1 is p2)  # False
    print(p1 == p2)  # False
    print(p1 == p1)  # True
    print(p2 == p2)  # True


def bar_1():
    """Python автоматически реализует метод __ne__(), если метод __eq__() уже реализован
     При реализованном методе __ne__() метод __eq__() автоматически не реализуется."""

    class Point:
        """p1 == p2 равносильно вызову p1.__eq__(p2)"""

        def __init__(self, x, y):
            self.x = x
            self.y = y

        def __eq__(self, other):
            """for == """
            if isinstance(other, Point):
                return self.x == other.x and self.y == other.y
            return False

        def __ne__(self, other):
            """for != """
            if isinstance(other, Point):
                return self.x != other.x or self.y != other.y
            return True

    p1 = Point(1, 2)
    p2 = Point(1, 2)
    p3 = Point(3, 4)

    print(p1 == p2)  # True
    print(p1 == p3)  # False
    print(p2 == p3)  # False
    # --------------------------
    print(p1 == (1, 2))  # False
    # --------------------------
    print(p1 != p2)  # False
    print(p1 != p3)  # True
    print(p2 != p3)  # True


def bar_2():
    """константу NotImplemented рекомендуется возвращать в методе __eq__(),
    если сравнение для объектов каких-либо типов не определено."""

    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y

    p1 = Point(1, 2)
    p2 = Point(1, 2)

    print(p1.__eq__(p2))  # NotImplemented

    # рекомендованная реализация
    class NewPoint:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def __eq__(self, other):
            if isinstance(other, Point):
                return self.x == other.x and self.y == other.y
            return NotImplemented

    p1 = NewPoint(1, 2)
    p2 = NewPoint(1, 2)

    print(p1 == p2)  # True
    print(p1 == None)  # False
    print(p1 == (1, 2))  # False


def bar_3():
    """
    __lt__() отвечает за сравнение на меньше -- выражение fruit1 < fruit2 равносильно вызову fruit1.__lt__(fruit2)
    __gt__() отвечает за сравнение на больше -- выражение fruit1 > fruit2 равносильно вызову fruit1.__gt__(fruit2)
    Если в классе реализовано сравнение на больше (меньше), то сравнение на меньше (больше) для объектов этого класса
    можно считать реализованным автоматически.
    Аналогично себя ведут и нестрогие сравнения на больше/меньше.
    """

    class Fruit:
        def __init__(self, name, mass):
            self.name = name  # название фрукта
            self.mass = mass  # масса фрукта в граммах

        def __eq__(self, other):
            if isinstance(other, Fruit):
                return self.mass == other.mass  # два фрукта равны, если равны их массы
            return NotImplemented

        def __lt__(self, other):
            if isinstance(other, Fruit):
                return self.mass < other.mass
            return NotImplemented

        def __gt__(self, other):
            if isinstance(other, Fruit):
                return self.mass > other.mass
            return NotImplemented

    fruit1 = Fruit('банан', 150)
    fruit2 = Fruit('яблоко', 180)

    print(fruit1 < fruit2)  # True
    print(fruit1 > fruit2)  # False
    print(fruit2 < fruit1)  # False
    print(fruit2 > fruit1)  # True


def bar_4():
    """
    __le__() отвечает за сравнение на меньше или = -- выражение fruit1 <= fruit2 равносильно вызову fruit1.__le__(fruit2)
    __ge__() отвечает за сравнение на больше или =-- выражение fruit1 >= fruit2 равносильно вызову fruit1.__ge__(fruit2)
    """

    class Fruit:
        def __init__(self, name, mass):
            self.name = name
            self.mass = mass

        def __eq__(self, other):
            if isinstance(other, Fruit):
                return self.mass == other.mass
            return NotImplemented

        def __le__(self, other):
            if isinstance(other, Fruit):
                return self.mass <= other.mass
            return NotImplemented

        def __ge__(self, other):
            if isinstance(other, Fruit):
                return self.mass >= other.mass
            return NotImplemented

    fruit1 = Fruit('банан', 150)
    fruit2 = Fruit('яблоко', 180)
    fruit3 = Fruit('груша', 150)

    print(fruit1 <= fruit2)  # True
    print(fruit1 >= fruit2)  # False
    print(fruit1 <= fruit3)  # True
    print(fruit1 >= fruit3)  # True


def bar_5():
    """@total_ordering позволяет определить в классе лишь метод __eq__() и
    один из методов __lt__(), __le__(), __gt__() или __ge__().
    Все недостающие методы декоратор определит и реализует самостоятельно."""

    @total_ordering
    class Fruit:
        def __init__(self, name, mass):
            self.name = name
            self.mass = mass

        def __eq__(self, other):
            if isinstance(other, Fruit):
                return self.mass == other.mass
            return NotImplemented

        def __lt__(self, other):
            if isinstance(other, Fruit):
                return self.mass < other.mass
            return NotImplemented


def bar_6():
    """sorted -- min -- max"""

    @total_ordering
    class Fruit:
        def __init__(self, name, mass):
            self.name = name
            self.mass = mass

        def __repr__(self):
            return f'Fruit({repr(self.name)}, {self.mass})'

        def __eq__(self, other):
            if isinstance(other, Fruit):
                return self.mass == other.mass
            return NotImplemented

        def __lt__(self, other):
            if isinstance(other, Fruit):
                return self.mass < other.mass
            return NotImplemented

    fruits = [Fruit('яблоко', 180), Fruit('груша', 160), Fruit('авокадо', 170), Fruit('банан', 150)]

    print(sorted(fruits))  # [Fruit('банан', 150), Fruit('груша', 160), Fruit('авокадо', 170), Fruit('яблоко', 180)]
    print(min(fruits))  # Fruit('банан', 150)
    print(max(fruits))  # Fruit('яблоко', 180)


"""=======================СРАВНЕНИЕ-ОБЪЕКТОВ==========================TASKS=========================================="""


def task_1():
    class Vector:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def __repr__(self):
            return f"{self.__class__.__name__}({self.x}, {self.y})"

        def __eq__(self, other):
            if isinstance(other, Vector):
                return self.x == other.x and self.y == other.y
            elif isinstance(other, tuple):
                return (other[0], other[1]) == (self.x, self.y) and len(other) == 2
            return NotImplemented

    a = Vector(1, 2)
    pair1 = (1, 2)
    pair2 = (3, 4)
    pair3 = (5, 6, 7)
    pair4 = (1, 2, 3, 4)
    pair5 = (1, 4, 3, 2)

    print(a == pair1)
    print(a == pair2)
    print(a == pair3)
    print(a == pair4)
    print(a == pair5)


def task_2():
    @total_ordering
    class Word:
        def __init__(self, word):
            self.word = word

        def __repr__(self):
            return f"{self.__class__.__name__}({repr(self.word)})"

        def __str__(self):
            return self.word.capitalize()

        def __eq__(self, other):
            if isinstance(other, Word):
                return len(self.word) == len(other.word)
            return NotImplemented

        def __le__(self, other):
            if isinstance(other, Word):
                return len(self.word) <= len(other.word)
            return NotImplemented

def task_3():
    @total_ordering
    class Month:
        def __init__(self, year, month):
            self.year = year
            self.month = month

        def __str__(self):
            return f"{self.year}-{self.month}"

        def __repr__(self):
            return f"{self.__class__.__name__}({self.year}, {self.month})"

        def __eq__(self, other):
            if isinstance(other, self.__class__):
                return self.month == other.month and self.year == self.year
            elif isinstance(other, tuple):
                return self.month == other[1] and self.year == other[0] and len(other) == 2
            return NotImplemented

        def __lt__(self, other):
            if isinstance(other, self.__class__):
                return (self.year, self.month) < (other.year, other.month)
            elif isinstance(other, tuple):
                return len(other) == 2 and (self.year, self.month) < other
            return NotImplemented


def task_4():
    @total_ordering
    class Version:
        def __init__(self, version):
            """2.8.1, if 2 -> 2.0.0, if 2.1 -> 2.1.0"""
            self.version = ".".join(version.split(".") + ["0"] * (2 - version.count(".")))
            self.compare = tuple(list(map(int, self.version.split("."))))

        def __str__(self):
            return self.version

        def __repr__(self):
            return f"{self.__class__.__name__}({repr(self.version)})"

        def __eq__(self, other):
            if isinstance(other, self.__class__):
                return self.version == other.version
            return NotImplemented

        def __lt__(self, other):
            if isinstance(other, self.__class__):
                return self.compare < other.compare
            return NotImplemented