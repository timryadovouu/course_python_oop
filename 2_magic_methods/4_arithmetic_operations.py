import math

"""=======================АРИФМЕТИЧЕСКИЕ-ОПЕРАЦИИ=======================SUMMARY======================================"""


# __add__() — определяет поведение для сложения (оператор +)
# __sub__() — определяет поведение для вычитания (оператор -)
# __mul__() — определяет поведение для умножения (оператор *)
# __truediv__() — определяет поведение для обычного деления (оператор /)
# __floordiv__() — определяет поведение для целочисленного деления (оператор //)
# __mod__() — определяет поведение для деления по модулю (оператор %)

def bar_0():
    class PiggyBank:
        def __init__(self, coins):
            self.coins = coins  # количество монет в копилке

        def __repr__(self):
            return f'PiggyBank({self.coins})'

        def __add__(self, other):
            if isinstance(other, int):
                return PiggyBank(self.coins + other)
            elif isinstance(other, PiggyBank):
                return PiggyBank(self.coins + other.coins)
            return NotImplemented

    bank1 = PiggyBank(10)
    bank2 = bank1 + 5
    bank3 = bank1 + bank2

    print(bank1)  # PiggyBank(10)
    print(bank2)  # PiggyBank(15)
    print(bank3)  # PiggyBank(25)


def bar_1():
    class PiggyBank:
        def __init__(self, coins):
            self.coins = coins

        def __repr__(self):
            return f'PiggyBank({self.coins})'

        def __add__(self, other):
            return PiggyBank(self.coins + other)

    bank = PiggyBank(10)

    print(bank + 5)  # PiggyBank(15)
    # для типа int не реализовано сложение с типом PiggyBank
    # print(5 + bank)  # TypeError: unsupported operand type(s) for +: 'int' and 'PiggyBank'


# Для реализации арифметических операций, не учитывающих порядок операндов:
# __radd__() — определяет поведение для сложения (оператор +)
# __rsub__() — определяет поведение для вычитания (оператор -)
# __rmul__() — определяет поведение для умножения (оператор *)
# __rtruediv__() — определяет поведение для обычного деления (оператор /)
# __rfloordiv__() — определяет поведение для целочисленного деления (оператор //)
# __rmod__() — определяет поведение для деления по модулю (оператор %)

def bar_2():
    class PiggyBank:
        def __init__(self, coins):
            self.coins = coins

        def __repr__(self):
            return f'PiggyBank({self.coins})'

        def __add__(self, other):
            return PiggyBank(self.coins + other)

        def __radd__(self, other):
            print('Вызов метода __radd__()')
            return self.__add__(other)

    bank = PiggyBank(10)

    print(5 + bank)
    # Вызов метода __radd__()
    # PiggyBank(15)
    num = 3
    print(num.__add__(bank))  # NotImplemented


# __lshift__() — определяет поведение для двоичного сдвига влево (оператор <<)
# __rshift__() — определяет поведение для двоичного сдвига вправо (оператор >>)
# __and__() — определяет поведение для двоичного И (оператор &)
# __or__() — определяет поведение для двоичного ИЛИ (оператор |)
# __xor__() — определяет поведение для двоичного XOR, (оператор ^)
# также имеют отраженные версии (с префиксом r)

"""=======================АРИФМЕТИЧЕСКИЕ-ОПЕРАЦИИ=======================TASKS========================================"""


def task_1():
    class FoodInfo:
        def __init__(self, proteins, fats, carbohydrates):
            self.proteins = proteins
            self.fats = fats
            self.carbohydrates = carbohydrates

        def _as_tuple(self):
            return self.proteins, self.fats, self.carbohydrates

        def __repr__(self):
            return f"{self.__class__.__name__}({self.proteins}, {self.fats}, {self.carbohydrates})"

        def __add__(self, other):
            if isinstance(other, self.__class__):
                return self.__class__(*(s + v for s, v in zip(self._as_tuple(), other._as_tuple())))
            return NotImplemented

        def __mul__(self, other):
            if isinstance(other, (int, float)):
                return self.__class__(other * self.proteins, self.fats * other, self.carbohydrates * other)
            return NotImplemented

        def __truediv__(self, other):
            if isinstance(other, (int, float)):
                return self.__class__(self.proteins / other, self.fats / other, self.carbohydrates / other)
            return NotImplemented

        def __floordiv__(self, other):
            if isinstance(other, (int, float)):
                return self.__class__(self.proteins // other, self.fats // other, self.carbohydrates // other)
            return NotImplemented

    food1 = FoodInfo(10, 20, 30)
    food2 = FoodInfo(10, 20, 30)

    not_supported = [food2, [], {}, set(), '', frozenset(), ()]

    for item in not_supported:
        print(food1.__add__(item))
        print(food1.__floordiv__(item))
        print(food1.__mul__(item))
        print(food1.__truediv__(item))


def task_2():
    class Vector:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def __repr__(self):
            return f"{self.__class__.__name__}({self.x}, {self.y})"

        def _as_tuple(self):
            return self.x, self.y

        def __add__(self, other):
            if isinstance(other, self.__class__):
                return self.__class__(*(i + j for i, j in zip(self._as_tuple(), other._as_tuple())))
            return NotImplemented

        def __sub__(self, other):
            if isinstance(other, self.__class__):
                return self.__class__(*(i - j for i, j in zip(self._as_tuple(), other._as_tuple())))
            return NotImplemented

        def __mul__(self, other):
            if isinstance(other, (int, float)):
                return self.__class__(*(i * other for i in self._as_tuple()))
            return NotImplemented

        def __rmul__(self, other):
            return self.__mul__(other)

        def __truediv__(self, other):
            if isinstance(other, (int, float)):
                return self.__class__(*(i / other for i in self._as_tuple()))
            return NotImplemented

        def __rtruediv__(self, other):
            return self.__truediv__(other)

    a = Vector(3, 4)

    print(a * 2)
    print(2 * a)
    print(a / 2)


def task_3():
    class SuperString:
        def __init__(self, string):
            self.string = string

        def __str__(self):
            return self.string

        def __add__(self, other):
            if isinstance(other, str):
                return SuperString(self.string + other)
            elif isinstance(other, SuperString):
                return SuperString(self.string + other.string)
            return NotImplemented

        def __mul__(self, other):
            if isinstance(other, int):
                return SuperString(self.string * other)
            return NotImplemented

        def __rmul__(self, other):
            return self.__mul__(other)

        def __truediv__(self, other):
            if isinstance(other, int):
                return SuperString(self.string[0:len(self.string) // other])
            return NotImplemented

        def __lshift__(self, other):
            """<<"""
            if isinstance(other, int):
                if other >= len(self.string):
                    return ""
                else:
                    return SuperString(self.string[0:len(self.string) - other])
            return NotImplemented

        def __rshift__(self, other):
            """>>"""
            if isinstance(other, int):
                if other >= len(self.string):
                    return ""
                else:
                    return SuperString(self.string[other:])
            return NotImplemented

    s1 = SuperString('bee')
    s2 = SuperString('geek')

    new_s1 = s1 << 1
    new_s2 = s2 >> 1
    new_s3 = s1 + s2
    new_s4 = s1 * 2
    new_s5 = s2 / 2

    print(new_s1, type(new_s1))
    print(new_s2, type(new_s2))
    print(new_s3, type(new_s3))
    print(new_s4, type(new_s4))
    print(new_s5, type(new_s5))


"""==============ОПЕРАТОРЫ-СОСТАВНОГО-ПРИСВАИВАНИЯ=========================SUMMARY==================================="""


def bar_3():
    nums = [1, 2, 3]
    print(id(nums), nums)  # <ID_1111111111111> [1, 2, 3]
    nums = nums + [4, 5, 6]
    print(id(nums), nums)  # <ID_22222222222> [1, 2, 3, 4, 5, 6]
    # --------------------------------------------------
    nums = [1, 2, 3]
    print(id(nums), nums)  # <ID_111111111111> [1, 2, 3]
    nums += [4, 5, 6]
    print(id(nums), nums)  # <ID_111111111111> [1, 2, 3, 4, 5, 6]

# __iadd__() — определяет поведение для сложения (оператор +=)
# __isub__() — определяет поведение для вычитания (оператор -=)
# __imul__() — определяет поведение для умножения (оператор *=)
# __itruediv__() — определяет поведение для обычного деления (оператор /=)
# __ifloordiv__() — определяет поведение для целочисленного деления (оператор //=)
# __imod__() — определяет поведение для деления по модулю (оператор %=)
# Префикс i в названиях методов составного присваивания является сокращением слова inplace (на месте).

def bar_4():
    class PiggyBank:
        def __init__(self, coins):
            self.coins = coins  # количество монет в копилке

        def __repr__(self):
            return f'PiggyBank({self.coins})'

        def __add__(self, other):
            return PiggyBank(self.coins + other)  # создаем и возвращаем новый объект

        def __iadd__(self, other):
            self.coins += other
            return self  # возвращаем измененный объект

    bank = PiggyBank(10)
    bank += 10
    bank += 5
    print(bank)  # PiggyBak(25)

#  Если в классе не определены магические методы с префиксом i, но определены их основные версии (без префикса i),
#  то операторами составного присваивания пользоваться можно. Однако результатами таких арифметических операций
#  всегда будут новые объекты


"""==============ОПЕРАТОРЫ-СОСТАВНОГО-ПРИСВАИВАНИЯ=========================TASKS====================================="""


def task_4():
    class Time:
        def __init__(self, hours, minutes):
            self.hours = hours % 24 + minutes // 60
            self.minutes = minutes % 60

        def __str__(self):
            return f"{self.hours:02}:{self.minutes:02}"

        def __add__(self, other):
            if isinstance(other, Time):
                return Time((self.hours + other.hours + (self.minutes + other.minutes) // 60) % 24,
                            (self.minutes + other.minutes) % 60)
            return NotImplemented

        def __iadd__(self, other):
            if isinstance(other, Time):
                self.hours += (other.hours + (self.minutes + other.minutes) // 60)
                self.hours %= 24
                self.minutes += other.minutes % 60
                self.minutes %= 60
                return self
            return NotImplemented

    t = Time(22, 0)
    t += Time(3, 0)
    print(t)

    # TEST_9:
    t1 = Time(15, 50)
    t2 = Time(2, 20)
    print(t1 + t2)

    t1 += Time(2, 20)
    print(t1)


def task_5():
    class Queue:
        """Очередь — абстрактный тип..."""

        def __init__(self, *args):
            self.a = list(map(str, args))
            self.new_queue = {pair[0]: pair[1] for pair in enumerate(list(args))}

        def __str__(self):
            # print(self.a)
            # print(self.new_queue)
            return " -> ".join(self.a)

        def add(self, *args):
            self.a += list(map(str, args))
            # self.a.extend(list(map(str, args)))
            self.new_queue |= {pair[0]: pair[1] for pair in enumerate(list(args), start=len(self.a) - 1)}
            return self

        def pop(self):
            if self.a and self.new_queue:
                element = self.a.pop(0)
                self.new_queue |= {pair[0]: pair[1] for pair in enumerate(self.a)}
                return element
            return None
            # return self.a.pop(0) if self.a else None

        def __add__(self, other):
            if isinstance(other, Queue):
                return Queue(*(self.a + other.a))
            return NotImplemented

        def __iadd__(self, other):
            if isinstance(other, Queue):
                self.a += other.a
                self.new_queue |= {pair[0]: pair[1] for pair in enumerate(list(other.a), start=len(self.a) - 1)}
                return self
            return NotImplemented

        def __rshift__(self, n):
            """>>"""
            if isinstance(n, int):
                if n >= len(self.a):
                    return ""
                else:
                    return Queue(*self.a[n:])
            return NotImplemented

        def __eq__(self, other):
            if isinstance(other, Queue):
                # print(self.a, self.new_queue, other.a, other.new_queue)
                return other.new_queue == self.new_queue
            return NotImplemented

        # def __ne__(self, other):
        #     if isinstance(other, Queue):
        #         return other.new_queue != self.new_queue
        #     return NotImplemented

    # TEST_10:
    queue = Queue(1, 2, 3)
    print(queue.__add__([]))
    print(queue.__iadd__('bee'))
    print(queue.__rshift__('geek'))
