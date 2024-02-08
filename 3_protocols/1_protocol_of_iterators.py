"""==================ПРОТОКОЛ-ИТЕРИРУЕМЫХ-ОБЪЕКТОВ-И-ИТЕРАТОРОВ=====================SUMMARY=========================="""


def bar_0():
    words = ['hello', 'beegeek', 'python']
    iterator = iter(words)  # равнозначно words.__iter__()

    print(type(words))  # <class 'list'>
    print(type(iterator))  # <class 'list_iterator'>
    print(next(iterator))  # равнозначно iterator.__next__()

    # любой объект, не вызывающий исключение TypeError при передаче в функцию iter(), — итерируемый объект
    # любой объект, не вызывающий исключение TypeError при передаче в функцию next(), — итератор
    # любой объект, возвращающий сам себя при передаче в функцию iter(), — итератор


# Примеры создания итераторов
def bar_1():
    """бесконечный итератор"""
    # -1 это стоп значение
    zero_iterator = iter(int, -1)

    for i in range(5):
        print(next(zero_iterator))
    print(type(zero_iterator))  # <class 'callable_iterator'>


def bar_2():
    """счетчик"""

    class Counter:
        def __init__(self, low, high):
            self.low = low
            self.high = high

        def __iter__(self):
            return self

        def __next__(self):
            if self.low > self.high:
                raise StopIteration
            self.low += 1
            return self.low - 1

    counter1 = Counter(3, 10)  # создаем итератор Counter, передавая значения low=3, high=10
    for i in counter1:  # неявно вызываем функцию next()
        print(i)

    counter2 = Counter(100, 103)  # создаем итератор Counter, передавая значения low=100, high=103
    print(next(counter2))  # явно вызываем функцию next()
    print(next(counter2))  # явно вызываем функцию next()


def bar_3():
    """бесконечный итератор четных чисел"""

    class EvenNumbers:
        def __init__(self, begin):
            self.begin = begin + begin % 2

        def __iter__(self):
            return self

        def __next__(self):
            value = self.begin
            self.begin += 2
            return value  # self.begin - 2

    evens1 = EvenNumbers(10)  # все четные числа от 10 до бесконечности
    for index, num in enumerate(evens1):
        if index > 5:
            break
        print(num)

    evens2 = EvenNumbers(101)  # все четные числа от 102 до бесконечности
    print(next(evens2))
    print(next(evens2))
    print(next(evens2))
    print(next(evens2))


def bar_4():
    class Factorials:
        def __init__(self):
            self.value = 1
            self.index = 1

        def __iter__(self):
            return self

        def __next__(self):
            self.value *= self.index
            self.index += 1
            return self.value

    infinite_factorials = Factorials()

    for index, num in enumerate(infinite_factorials, 1):
        if index <= 10:
            print(f'Факториал числа {index} равен {num}')
        else:
            break


# Примеры создания итерируемых объектов

def bar_5():
    class Order:
        def __init__(self, cart, customer):
            self.cart = list(cart)  # список покупок
            self.customer = customer  # имя покупателя

        def __iter__(self):
            yield from self.cart  # или с помощью выражения return (elem for elem in self.cart)


"""==================ПРОТОКОЛ-ИТЕРИРУЕМЫХ-ОБЪЕКТОВ-И-ИТЕРАТОРОВ=======================TASKS=========================="""


def task_1():
    class Point:
        def __init__(self, x, y, z):
            self.x = x
            self.y = y
            self.z = z

        def __repr__(self):
            return f"Point({self.x}, {self.y}, {self.z})"

        def __iter__(self):
            yield from (self.x, self.y, self.z)

    points = [Point(4, 7, 0), Point(1, 5, 10), Point(12, 23, 44)]
    print(points)


def task_2():
    class DevelopmentTeam:
        def __init__(self):
            self._l = []

        def add_junior(self, *args):
            self._l.extend([(elem, "junior") for elem in args])

        def add_senior(self, *args):
            self._l.extend([(elem, "senior") for elem in args])

        def __iter__(self):
            yield from sorted(self._l, key=lambda pair: pair[1])

    beegeek = DevelopmentTeam()
    beegeek.add_junior('Timur')
    beegeek.add_junior('Arthur', 'Valery')
    beegeek.add_senior('Gvido')
    print(beegeek._l)
    print(*beegeek, sep='\n')


def task_3():
    class AttrsIterator:
        def __init__(self, obj):
            self._obj = list(obj.__dict__.items())
            self.index = -1

        def __iter__(self):
            return self

        def __next__(self):
            # attrs = [(key, self.obj.__dict__[key]) for key in self.obj.__dict__]
            self.index += 1
            if self.index >= len(self._obj):
                raise StopIteration
            return self._obj[self.index]

    class User:
        def __init__(self, name, surname, age):
            self.name = name
            self.surname = surname
            self.age = age

    user = User('Debbie', 'Harry', 77)
    attrsiterator = AttrsIterator(user)
    print(*attrsiterator)


def task_4():
    class SkipIterator:
        def __init__(self, iterable, n):
            self.iterable = iter(iterable)
            self.n = n
            self.f = False

        def __iter__(self):
            return self

        def __next__(self):
            try:
                if not self.f:
                    self.f = True
                    return next(self.iterable)

                for _ in range(self.n):
                    next(self.iterable)
                return next(self.iterable)
            except:
                raise StopIteration

    skipiterator = SkipIterator(iter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 5)
    print(*skipiterator)


def task_5():
    # import itertools
    class RandomLooper:
        def __init__(self, *args):
            # self.iterables = itertools.chain(*args)
            self.iterables = iter([el for obj in args for el in obj])

        def __iter__(self):
            return self

        def __next__(self):
            return next(self.iterables)

    colors = ['red', 'blue', 'green', 'purple']
    shapes = ['square', 'circle', 'triangle', 'octagon']
    randomlooper = RandomLooper(colors, shapes)
    print(list(randomlooper))


def task_6():
    class Peekable:
        def __init__(self, iterable):
            self.iterable = iter(iterable)
            self.qwe = list(iterable)
            self.counter = 0
            self._current = ""

        def __iter__(self):
            return self

        def __next__(self):
            if self.counter == 1:
                self.counter = 0
                return self._current
            self._current = next(self.iterable)
            return self._current

        def peek(self, default="None"):
            if self.counter == 0:
                if default == "None":
                    self._current = next(self.iterable)
                    self.counter += 1

                else:
                    self._current = next(self.iterable, default)
                    if self._current != default:
                        self.counter += 1
            return self._current

    iterator = Peekable('Python')

    print(next(iterator))
    print(iterator.peek())
    print(iterator.peek())
    print(next(iterator))
    print(iterator.peek())
    print(iterator.peek())

def task_7():
    class LoopTracker:
        def __init__(self, iterable):
            self.iterable = iter(iterable)
            self.help = len(list(iterable))
            self.count = 0
            self.empty_count = 0
            self.flag_first = False
            self._current = ""
            self._first = ""

        def __iter__(self):
            return self

        def __next__(self):
            try:
                if self.count == 0 and self.flag_first:
                    self.count += 1
                    return self._first
                self._current = next(self.iterable)
                if not self.flag_first:
                    self.flag_first = True
                    self._first = self._current
                self.count += 1
                return self._current
            except StopIteration:
                self.empty_count += 1
                raise

        @property
        def accesses(self):
            return self.count

        @property
        def empty_accesses(self):
            return self.empty_count

        @property
        def first(self):
            if not self.flag_first:
                try:
                    self._first = next(self.iterable)
                    self.flag_first = True
                except StopIteration:
                    raise AttributeError("Исходный итерируемый объект пуст")
            return self._first

        @property
        def last(self):
            if self._current:
                return self._current
            raise AttributeError("Последнего элемента нет")

        def is_empty(self):
            return self.count >= self.help

    loop_tracker = LoopTracker([1, 2, 3])

    print(next(loop_tracker))
    print(list(loop_tracker))

