"""=======================ПРЕОБРАЗОВАНИЕ-ТИПОВ=======================SUMMARY========================================"""


def bar_0():
    """Если в классе отсутствуют __bool__() и __len__(), то все экземпляры этого класса считаются истинными"""

    class Angle:
        def __init__(self, value):
            self.value = value  # градусная мера угла

    print(bool(Angle(-110)))  # True
    print(bool(Angle(0)))  # True
    print(bool(Angle(0.0)))  # True
    print(bool(Angle(120.1)))  # True

    class Angle:
        def __init__(self, value):
            self.value = value

        def __bool__(self):
            # return bool(self.value)
            return self.value != 0

    print(bool(Angle(-110)))  # True
    print(bool(Angle(0)))  # False
    print(bool(Angle(0.0)))  # False
    print(bool(Angle(120.1)))  # True

    # Помимо __bool__(), за приведение объекта к логическому типу и его поведение при передаче в функцию bool()
    # может отвечать __len__()

    class Angle:
        def __init__(self, value):
            self.value = value

        def __len__(self):
            print('Вызов метода __len__()')
            return self.value != 0

    print(bool(Angle(-110)))  # True
    print(bool(Angle(0)))  # False
    print(bool(Angle(120.1)))  # True


def bar_1():
    """__int__(), __float__() и __complex__()"""

    class Angle:
        def __init__(self, value):
            self.value = value

        def __int__(self):
            return int(self.value)

        def __complex__(self):
            return complex(self.value)

        def __float__(self):
            return float(self.value)

    angle1 = Angle(100)
    angle2 = Angle(100.1)

    print(int(angle1))
    print(int(angle2))
    print(complex(angle1))
    print(complex(angle2))
    print(float(angle1))
    print(float(angle2))


def bar_2():
    class Angle:
        def __init__(self, value):
            self.value = value

        def __index__(self):
            print('Вызов метода __index__()')
            return self.value

    angle = Angle(100)

    print(int(angle))
    print(float(angle))
    print(bin(angle))
    print(oct(angle))
    print(hex(angle))
    # Вызов метода __index__()
    # 100
    # Вызов метода __index__()
    # 100.0
    # Вызов метода __index__()
    # 0b1100100
    # Вызов метода __index__()
    # 0o144
    # Вызов метода __index__()
    # 0x64

"""=======================ПРЕОБРАЗОВАНИЕ-ТИПОВ===========================TASKS======================================"""


def task_1():
    class Vector:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def __str__(self):
            return f"({self.x}, {self.y})"

        def __bool__(self):
            return self.x != 0 or self.y != 0

        def __int__(self):
            return int((self.x ** 2 + self.y ** 2) ** 0.5)

        def __float__(self):
            return float((self.x ** 2 + self.y ** 2) ** 0.5)

        def __complex__(self):
            return complex(self.x, self.y)

    vector = Vector(3, 4)

    print(vector)
    print(int(vector))
    print(float(vector))
    print(complex(vector))


def task_2():
    class Temperature:
        """температура в градусах по шкале Цельсия"""

        def __init__(self, temperature):
            self.temperature = temperature

        def __str__(self):
            return f"{round(self.temperature, 2)}°C"
            # return f'{self.temperature.__round__(2)}°C'

        def to_fahrenheit(self):
            return 32 + 9 * self.temperature / 5

        @classmethod
        def from_fahrenheit(cls, tf):
            return cls(5 * (tf - 32) / 9)

        def __bool__(self):
            return self.temperature > 0

        def __int__(self):
            return int(self.temperature)

        def __float__(self):
            return float(self.temperature)

    t = Temperature.from_fahrenheit(41)

    print(t)
    print(int(t))
    print(float(t))
    print(t.to_fahrenheit())


def task_3():
    from functools import total_ordering

    @total_ordering
    class RomanNumeral:
        _new_dict = {"M": 1000, "CM": 900, "D": 500, "CD": 400, "C": 100, "XC": 90, "L": 50, "XL": 40, "X": 10, "IX": 9,
                     "V": 5, "IV": 4, "I": 1}

        def __init__(self, num):
            self.number = num
            self.int_number = 0

        def __str__(self):
            return self.number

        def __int__(self):
            qwe = self.number
            for k, v in self._new_dict.items():
                while qwe.startswith(k):
                    self.int_number += v
                    qwe = qwe[len(k):]
            return self.int_number

        def to_roman(self, num):
            roman = ""
            # while num > 0:
            for k, v in self._new_dict.items():
                while num >= v:
                    roman += k
                    num -= v
            # self.number = roman
            return roman

        def __add__(self, other):
            if isinstance(other, RomanNumeral):
                result = self.__int__() + other.__int__()
                return RomanNumeral(self.to_roman(result))
            return NotImplemented

        def __sub__(self, other):
            if isinstance(other, RomanNumeral):
                result = self.__int__() - other.__int__()
                return RomanNumeral(self.to_roman(result))
            return NotImplemented

        def __eq__(self, other):
            if isinstance(other, RomanNumeral):
                return self.number == other.number
            return NotImplemented

        def __lt__(self, other):
            if isinstance(other, RomanNumeral):
                return self.__int__() < other.__int__()
            return NotImplemented

    # TEST_7:
    romans1 = ['I', 'X', 'L', 'IV', 'IX', 'XLV', 'CXXIV', 'MCMXCIV']
    romans2 = ['I', 'V', 'L', 'VI', 'XI', 'XXV', 'CDXLVIII', 'MCMXCI']

    for x, y in zip(romans1, romans2):
        number = RomanNumeral(x) + RomanNumeral(y)
        print(number, int(number))
    print()
    # TEST_8:
    romans1 = ['III', 'X', 'L', 'C', 'M', 'XXV', 'XC', 'MMMCMXXXV']
    romans2 = ['II', 'V', 'X', 'L', 'D', 'IV', 'VIII', 'MCMXCIV']

    for x, y in zip(romans1, romans2):
        number = RomanNumeral(x) - RomanNumeral(y)
        print(number, int(number))

