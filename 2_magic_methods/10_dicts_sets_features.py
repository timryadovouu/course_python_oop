def bar_0():
    class Key:
        def __init__(self, data):
            self.data = data

        def __repr__(self):
            return f'Key({repr(self.data)})'

        def __hash__(self):
            print('Вызов метода __hash__()', self.data)
            return hash(self.data)

        def __eq__(self, other):
            print('Вызов метода __eq__()')
            if isinstance(other, Key):
                return self.data == other.data
            return NotImplemented

    data = {}

    data[Key('one')] = 1
    data[Key('two')] = 2
    data[Key('three')] = 3

    print()
    print(data)

    # Вызов метода __hash__() one
    # Вызов метода __hash__() two
    # Вызов метода __hash__() three
    # {Key('one'): 1, Key('two'): 2, Key('three'): 3}


def bar_1():
    """добавление пары с уже имеющимся ключом"""

    class Key:
        def __init__(self, data):
            self.data = data

        def __repr__(self):
            return f'Key({repr(self.data)})'

        def __hash__(self):
            print('Вызов метода __hash__()', self.data)
            return 1

        def __eq__(self, other):
            print('Вызов метода __eq__()', self.data, other.data)
            if isinstance(other, Key):
                return self.data == other.data
            return NotImplemented

    data = {}

    data[Key('one')] = 1
    data[Key('two')] = 2

    print()
    data[Key('two')] = 'два'

    print()
    print(data)

    # Вызов метода __hash__() one
    # Вызов метода __hash__() two
    # Вызов метода __eq__() one two
    #
    # Вызов метода __hash__() two
    # Вызов метода __eq__() one two
    # Вызов метода __eq__() two two
    #
    # {Key('one'): 1, Key('two'): 'два'}


def bar_2():
    """поиск ключей"""

    class Key:
        def __init__(self, data):
            self.data = data

        def __repr__(self):
            return f'Key({repr(self.data)})'

        def __hash__(self):
            print('Вызов метода __hash__()', self.data)
            return 1

        def __eq__(self, other):
            print('Вызов метода __eq__()', self.data, other.data)
            if isinstance(other, Key):
                return self.data == other.data
            return NotImplemented

    data = {}

    data[Key('one')] = 1
    data[Key('two')] = 2

    print()
    data[Key('two')]
    # Вызов метода __hash__() one
    # Вызов метода __hash__() two
    # Вызов метода __eq__() one two
    #
    # Вызов метода __hash__() two
    # Вызов метода __eq__() one two
    # Вызов метода __eq__() two two


def bar_3():
    """Быстрое сравнение ключей"""

    def fast_match(key, target_key):  # key и target_key — сравниваемые ключи
        if key is target_key:
            return True  # ключи равны, если это один и тот же объект
        if hash(key) != hash(target_key):
            return False  # ключи не равны, если не равны их хеш-значения
        return key == target_key

    class Key:
        def __init__(self, data):
            self.data = data

        def __repr__(self):
            return f'Key({repr(self.data)})'

        def __hash__(self):
            print('Вызов метода __hash__()', self.data)
            return 1

        def __eq__(self, other):
            print('Вызов метода __eq__()', self.data, other.data)
            if isinstance(other, Key):
                return self.data == other.data
            return NotImplemented

    data = {}

    key = Key('one')

    data[key] = 1
    data[key] = 'один'

    print()
    print(data)

    # Вызов метода __hash__() one
    # Вызов метода __hash__() one
    #
    # {Key('one'): 'один'}


def bar_4():
    from time import perf_counter

    def search_time_test(collection, numbers):
        start = perf_counter()

        for num in numbers:
            num in collection

        end = perf_counter()
        return end - start

    numbers = range(1000)

    d = dict(zip(numbers, numbers))
    s = set(numbers)
    l = list(numbers)

    print(search_time_test(d, numbers))
    print(search_time_test(s, numbers))
    print(search_time_test(l, numbers))


def bar_5():
    """разница ~30 раз -- кортеж вин"""
    from pympler import asizeof

    tuples = [('Python', 1991) for _ in range(1000000)]
    dicts = [{'Python': 1991} for _ in range(1000000)]

    tuples_size = asizeof.asizeof(tuples)
    dicts_size = asizeof.asizeof(dicts)

    print('Размер списка с кортежами', tuples_size, 'байт')
    print('Размер списка с словарями', dicts_size, 'байт')


bar_5()
