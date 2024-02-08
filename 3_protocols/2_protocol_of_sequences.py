"""==================ПРОТОКОЛ-ПОСЛЕДОВАТЕЛЬНОСТЕЙ===================================SUMMARY=========================="""


def bar_0():
    """неизменяемая последовательность"""

    class Order:
        def __init__(self, cart, customer):
            self.cart = list(cart)  # список покупок
            self.customer = customer  # имя покупателя

        def __len__(self):
            return len(self.cart)

        def __getitem__(self, key):
            if not isinstance(key, int):
                raise TypeError('Индекс должен быть целым числом')
            if key < 0 or key >= len(self.cart):
                raise IndexError('Неверный индекс')
            return self.cart[key]

        def __contains__(self, item):
            """определяет поведение при проверке на принадлежность с помощью оператора in"""
            return item in self.cart

        def __iter__(self):
            """определяет поведение при передаче в функцию iter(), возвращает итератор для последовательности"""
            yield from self.cart

    order = Order(['банан', 'яблоко', 'лимон'], 'Кемаль')

    print(len(order))
    print(order[1])
    print('дыня' in order)
    print('лимон' in order)
    print(*order, sep=', ')


def bar_1():
    """изменяемая последовательность"""

    class Order:
        def __init__(self, cart, customer):
            self.cart = list(cart)
            self.customer = customer

        def check_key(self, key):  # отдельный метод для проверки индекса на корректность
            if not isinstance(key, int):
                raise TypeError('Индекс должен быть целым числом')
            if key < 0 or key >= len(self.cart):
                raise IndexError('Неверный индекс')
            return key

        def __len__(self):
            return len(self.cart)

        def __getitem__(self, key):
            key = self.check_key(key)
            return self.cart[key]

        def __contains__(self, item):
            return item in self.cart

        def __iter__(self):
            yield from self.cart

        def __setitem__(self, key, value):
            key = self.check_key(key)
            self.cart[key] = value

        def __delitem__(self, key):
            key = self.check_key(key)
            del self.cart[key]

    order = Order(['банан', 'яблоко', 'лимон'], 'Кемаль')
    print(*order, sep=', ')
    order[1] = 'ананас'
    del order[2]
    print(*order, sep=', ')


def bar_2():
    """function slice"""
    slice1 = slice(10)  # start=None, stop=10, step=None
    slice2 = slice(1, 10)  # start=1, stop=10, step=None
    slice3 = slice(1, 10, 2)  # start=1, stop=10, step=2

    print(slice1)  # slice(None, 10, None)
    print(slice2)  # slice(1, 10, None)
    print(slice3)  # slice(1, 10, 2)

    nums = [1, 2, 3, 4, 5]
    print(nums[slice(1, None, None)])  # равнозначно nums[1:]
    print(nums[slice(3)])  # равнозначно nums[:3]
    print(nums[slice(1, 3)])  # равнозначно nums[1:3]
    print(nums[slice(1, 4, 2)])  # равнозначно nums[1:4:2]

    slice1 = slice(10)  # start=None, stop=10, step=None
    slice2 = slice(1, 10)  # start=1, stop=10, step=None
    slice3 = slice(1, 10, 2)  # start=1, stop=10, step=2
    print(slice1.start, slice1.stop, slice1.step)  # None 10 None
    print(slice2.start, slice2.stop, slice2.step)  # 1 10 None
    print(slice3.start, slice3.stop, slice3.step)  # 1 10 2

    class Order:
        """Аналогичная реализация методов __setitem__() и __delitem__(), чтобы пользоваться срезами"""

        def __init__(self, cart, customer):
            self.cart = list(cart)
            self.customer = customer

        def __len__(self):
            return len(self.cart)

        def __getitem__(self, key):
            if isinstance(key, slice):
                return Order(self.cart[key], self.customer)
            if not isinstance(key, int):
                raise TypeError('Индекс должен быть целым числом')
            if key < 0 or key >= len(self.cart):
                raise IndexError('Неверный индекс')
            return self.cart[key]

        def __contains__(self, item):
            return item in self.cart

        def __iter__(self):
            yield from self.cart

    order1 = Order(['банан', 'яблоко', 'лимон', 'дыня', 'грейпфрут'], 'Кемаль')
    order2 = order1[1:]
    order3 = order1[2:4]
    order4 = order1[1:5:2]

    print(*order2, sep=', ')  # яблоко, лимон, дыня, грейпфрут
    print(*order3, sep=', ')  # лимон, дыня
    print(*order4, sep=', ')  # яблоко, дыня


def bar_3():
    """to reversed"""

    class Order:
        def __init__(self, cart, customer):
            self.cart = list(cart)
            self.customer = customer

        def __len__(self):
            return len(self.cart)

        def __getitem__(self, key):
            if not isinstance(key, int):
                raise TypeError('Индекс должен быть целым числом')
            if key < 0 or key >= len(self.cart):
                raise IndexError('Неверный индекс')
            return self.cart[key]

        def __contains__(self, item):
            return item in self.cart

        def __iter__(self):
            yield from self.cart

        def __reversed__(self):
            return reversed(self.cart)

    order = Order(['банан', 'яблоко', 'лимон'], 'Кемаль')

    print(*order, sep=', ')
    print(*reversed(order), sep=', ')


def bar_4():
    """метод __contains__() можно считать как частью протокола последовательности, так и нет
    может быть опущен, так как если у объекта есть длина и возможность обращаться к его
    элементам по индексам, то этого достаточно, чтобы проитерироваться по нему вручную.
    Метод __iter__() также может быть опущен, так как если у объекта есть длина и возможность обращаться к его
    элементам по индексам, то этого достаточно, чтобы проитерироваться по нему вручную.
    Таким образом, если в некотором классе определены методы __len__() и __getitem__(),
    то его экземпляры уже можно назвать последовательностью."""

    class Order:
        def __init__(self, cart, customer):
            self.cart = list(cart)
            self.customer = customer

        def __len__(self):
            return len(self.cart)

        def __getitem__(self, key):
            if not isinstance(key, int):
                raise TypeError('Индекс должен быть целым числом')
            if key < 0 or key >= len(self.cart):
                raise IndexError('Неверный индекс')
            return self.cart[key]

        def __iter__(self):
            print('Вызов метода __iter__()')
            yield from self.cart

    order = Order(['банан', 'яблоко', 'лимон'], 'Кемаль')

    print('арбуз' in order)
    print('лимон' in order)
    # Вызов метода __iter__()
    # False
    # Вызов метода __iter__()
    # True


def bar_5():
    slice1 = slice(10)  # start=None, stop=10, step=None
    slice2 = slice(1, 10)  # start=1, stop=10, step=None
    slice3 = slice(1, 10, 2)  # start=1, stop=10, step=2

    print(slice1.indices(5))  # (0, 5, 1)
    print(slice2.indices(50))  # (1, 10, 1)
    print(slice3.indices(8))  # (1, 8, 2)


def bar_6():
    """если в классе определен магический метод __len__(), но не определен магический метод __bool__(),
     то именно __len__() будет использоваться для всех логических приведений"""

    class MyClass:
        def __len__(self):
            return 0

    print(bool(MyClass()))  # False


# Реализовав в классе магические методы __getitem__() и __len__() мы можем передавать его экземпляры в функцию choice()

"""==================ПРОТОКОЛ-ПОСЛЕДОВАТЕЛЬНОСТЕЙ=====================================TASKS=========================="""


def task_1():
    class ReversedSequence:
        def __init__(self, sequence):
            self.sequence = sequence

        def __len__(self):
            return len(self.sequence)

        def __getitem__(self, item):
            return self.sequence[len(self.sequence) - 1 - item]

        def __iter__(self):
            yield from reversed(self.sequence)

    reversed_numbers = ReversedSequence((1, 2, 3, 4, 5))
    for num in reversed_numbers:
        print(num)


def task_2():
    class SparseArray:
        def __init__(self, default):
            self.default = default
            self.sequence = {}

        def __getitem__(self, key):
            return self.sequence.get(key, self.default)

        def __setitem__(self, key, value):
            self.sequence[key] = value

    array = SparseArray(None)

    array[0] = 'Timur'
    array[1] = 'Arthur'

    print(array[0])
    print(array[1])
    print(array[2])


def task_3():
    # from itertools import cycle
    class CyclicList:
        def __init__(self, iterable=()):
            self.iterable = list(iterable) or []

        def append(self, obj):
            self.iterable.append(obj)

        def pop(self, index=-1):
            return self.iterable.pop(index)

        def __len__(self):
            return len(self.iterable)

        # def __iter__(self):
        #     yield from cycle(self.iterable)

        def __getitem__(self, key):
            return self.iterable[key % len(self.iterable)]

    cyclic_list = CyclicList([1, 2, 3])

    print(cyclic_list[1])
    print(cyclic_list[2])
    print(cyclic_list[5])
    print(cyclic_list[12])


def task_4():
    from copy import deepcopy
    class SequenceZip:
        def __init__(self, *args):
            self.data = zip(*deepcopy(args))

        def __len__(self):
            x = 0
            for _ in deepcopy(self.data):
                x += 1
            return x

        def __getitem__(self, key):
            qwe = deepcopy(self.data)
            for _ in range(key):
                next(qwe)
            return next(qwe)

    # TEST_2:
    test = SequenceZip('ABC', ['bee', 'geek', 'python'], [1, 2, 3])

    print(len(test))
    print(test[1])
    print(test[2])

    # TEST_3:
    print(len(SequenceZip([1, 2, 3, 4])))
    print(len(SequenceZip(range(5), [1, 2, 3, 4])))
    print(len(SequenceZip(range(5), [1, 2, 4], 'data')))


def task_5():
    class OrderedSet:
        def __init__(self, iterable=()):
            self.iterable = []
            for item in iterable:
                if item not in self.iterable:
                    self.iterable.append(item)

        def add(self, item):
            if item not in self.iterable:
                self.iterable.append(item)

        def discard(self, item):
            if item in self.iterable:
                del self.iterable[self.iterable.index(item)]

        def __len__(self):
            return len(self.iterable)

        def __contains__(self, item):
            return item in self.iterable

        def __eq__(self, other):
            if isinstance(other, OrderedSet):
                return self.iterable == other.iterable
            elif isinstance(other, set):
                return set(self.iterable) == other
            return NotImplemented

        def __iter__(self):
            yield from self.iterable

    # TEST_4:
    print(OrderedSet(['green', 'red', 'blue']) == OrderedSet(['green', 'red', 'blue']))
    print(OrderedSet(['green', 'red', 'blue']) == OrderedSet(['red', 'blue', 'green']))
    print(OrderedSet(['green', 'red', 'blue']) == {'blue', 'red', 'green'})
    print(OrderedSet(['green', 'red', 'blue']) == ['green', 'red', 'blue'])
    print(OrderedSet(['green', 'red', 'blue']) == 100)


def task_6():
    from copy import deepcopy

    class AttrDict:
        def __init__(self, data={}):
            self.data = deepcopy(data)

        def __len__(self):
            return len(self.data)

        def __getitem__(self, key):
            return self.data[key]

        def __setitem__(self, key, value):
            self.data[key] = value

        def __getattr__(self, key):
            return self.data[key]

        def __iter__(self):
            yield from self.data

    attrdict = AttrDict()

    attrdict['school_name'] = 'BEEGEEK'
    print(attrdict['school_name'])
    print(attrdict.school_name)


def task_7():
    from copy import deepcopy
    class PermaDict:
        def __init__(self, data={}):
            self.data = deepcopy(data)

        def __len__(self):
            return len(self.data)

        def __iter__(self):
            yield from self.data.keys()

        def keys(self):
            yield from self.data.keys()

        def values(self):
            yield from self.data.values()

        def items(self):
            return ((k, v) for k, v in self.data.items())

        def __getitem__(self, key):
            return self.data[key]

        def __setitem__(self, key, value):
            if key in self.data:
                raise KeyError("Изменение значения по ключу невозможно")
            self.data[key] = value

        def __delitem__(self, key):
            del self.data[key]

    permadict = PermaDict({'name': 'Timur', 'city': 'Moscow'})

    try:
        permadict['name'] = 'Arthur'
    except KeyError as e:
        print(e)


def task_8():
    from copy import deepcopy

    class HistoryDict:
        def __init__(self, data={}):
            self.data = deepcopy(data)
            self.arr = {k: [v] for k, v in deepcopy(data).items()}

        def __len__(self):
            return len(self.data)

        def __iter__(self):
            yield from self.data.keys()

        def __getitem__(self, key):
            return self.data[key]

        def __setitem__(self, key, value):
            # if key in self.data:
            #     self.arr[key].append(value)
            # else:
            #     self.arr.setdefault(key, [value])
            self.arr.setdefault(key, []).append(value)
            self.data[key] = value

        def __delitem__(self, key):
            del self.data[key]
            del self.arr[key]

        def keys(self):
            yield from self.data.keys()

        def values(self):
            yield from self.data.values()

        def items(self):
            return ((k, v) for k, v in self.data.items())

        def history(self, key):
            return self.arr.get(key, [])

        def all_history(self):
            return self.arr

    # TEST_8:
    historydict = HistoryDict({'name': 'Irenica', 'country': 'Russia', 'level': 'junior', })

    print(historydict.all_history())

    historydict['country'] = 'Italy'
    historydict['level'] = 'middle'
    historydict['level'] = 'senior'

    print(historydict.all_history())

    del historydict['level']

    print(historydict.all_history())

    historydict['level'] = 'God'

    print(historydict.all_history())


def task_9():
    class MutableString:
        def __init__(self, string=""):
            self.string = string

        def lower(self):
            self.string = self.string.lower()

        def upper(self):
            self.string = self.string.upper()

        def __str__(self):
            return self.string

        def __repr__(self):
            return f"{self.__class__.__name__}({repr(self.string)})"

        def __len__(self):
            return sum(1 for _ in self.string)

        def __getitem__(self, index):
            if isinstance(index, slice):
                return MutableString(self.string[index])
            return self.string[index]

        def __setitem__(self, index, value):
            qwe = list(self.string)
            qwe[index] = value
            self.string = "".join(qwe)

        def __delitem__(self, index):
            if isinstance(index, int):
                self.string = self.string[0:index] + self.string[index + 1:]
            if isinstance(index, slice):
                qwe = list(self.string)
                del qwe[index]
                self.string = "".join(qwe)

        def __add__(self, other):
            if isinstance(other, MutableString):
                return self.string + other.string
            return NotImplemented

        def __iter__(self):
            yield from self.string

    mutablestring = MutableString('beegeek')

    del mutablestring[1:3]
    print(mutablestring)


def task_10():
    from copy import deepcopy

    class Grouper:
        def __init__(self, iterable, key):
            self.iterable = deepcopy(iterable)
            self.key = key
            self.data = {}
            for item in deepcopy(iterable):
                self.data.setdefault(key(item), []).append(item)

        def add(self, obj):
            result = self.key(obj)
            if result in self.data:
                self.data[result].append(obj)
            else:
                self.data.setdefault(result, [obj])

        def group_for(self, obj):
            return self.key(obj)

        def __len__(self):
            return sum(1 for _ in self.data.keys())

        def __iter__(self):
            return ((k, v) for k, v in self.data.items())

        def __contains__(self, key):
            return key in self.data.keys()

        def __getitem__(self, key):
            return self.data[key]

    grouper = Grouper(['hi'], key=lambda s: s[0])

    print(grouper.group_for('hello'))
    print(grouper.group_for('bee'))
    print(grouper['h'])
    print('b' in grouper)
