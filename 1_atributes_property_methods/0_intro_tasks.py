import functools
import sys


def task_1(n, count=1):
    """дартс"""
    matrix = [[1]*n for _ in range(n)]
    while count < n - count:
        for i in range(count, n - count):
            for j in range(count, n - count):
                matrix[i][j] += 1
        count += 1
    [print(*now) for now in matrix]

def task_2(string):
    """скобочная последовательность"""
    import re
    if not string:
        return True
    else:
        if re.findall(r"\(\)", string):
            return task_2(re.sub(r"\(\)",r"",  string))
        else:
            return False
    # def is_correct_bracket_sequence(sequence):
    #     count = 0
    #     for char in sequence:
    #         count = count + 1 if char == '(' else count - 1
    #         if count < 0:
    #             return False
    #     return count == 0

def inversions(sequence):
    """количество пар инверсий i < j ai > aj"""
    import itertools
    combinations_list = [pair for pair in itertools.combinations(sequence, r=2) if sequence[sequence.index(pair[0])] > sequence[sequence.index(pair[1])]]
    print([pair for pair in itertools.combinations(sequence, r=2)])
    return len(combinations_list)

def task_4():
    """покемоны"""
    import sys, collections
    c_dict = collections.Counter(map(str.rstrip, sys.stdin))
    print(sum(c_dict.values()) - len(c_dict))


def jsonify(func):
    """декоратор json"""
    import functools, json
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return json.dumps(func(*args, **kwargs))
    return wrapper

def task_6():
    """определить нормальные координаты"""
    import sys, re
    data = map(str.rstrip, sys.stdin)
    print(*[(-90 <= eval(f"{pair}")[0] <= 90) and (-180 <= eval(f"{pair}")[1] <= 180) for pair in data], sep="\n")


def quantify(iterable, predicate):
    if not predicate: predicate = bool
    return sum(map(predicate, iterable))

def pycon(year, month):
    """Найти четвертый четверг месяца"""
    import datetime, calendar
    answer = []
    for ind_day in range(calendar.monthrange(year, month)[1]):
        if calendar.day_name[calendar.weekday(year=year, month=month, day=ind_day + 1)] == "Thursday":
            answer.append(datetime.date(year, month=month, day=ind_day + 1))
    isk_d = calendar.monthcalendar(year, month)[(3, 4)[not calendar.monthcalendar(year, month)[0][3]]][3]
    print(f"{isk_d}.{month:02}.{year}")
    return datetime.datetime.strftime(answer[3], "%d.%m.%Y")
    # print(pycon(2012, 3))

def is_integer(string):
    """является целым?"""
    import re
    if re.fullmatch(r"-?\d+", string):
        return True
    return False


def is_decimal(string):
    """целое или вещественное"""
    import re
    if re.fullmatch(r"-?\d*?\.?\d+?|-?\d+\.", string):
        return True
    return False

def is_fraction(string):
    """является ли дробью"""
    import re
    # print(re.findall(r"-?\d+/[1-9]\d*", string))
    if re.fullmatch(r"-?\d+/0*[1-9]+[0-9]*", string):
        return True
    return False

def intersperse(iterable, delimiter):
    """должна возвращать генератор, разделенный delimiter"""

    # if not iterable:
    #     return
    # it = iter(iterable)
    # yield next(it)
    # for el in it:
    #     yield delimiter
    #     yield el
    # return ( if q != 0 else w for q,w in enumerate(iterable))
    for ind, w in enumerate(iterable):
        if ind:
            yield delimiter
        yield w

    # data = intersperse(['John Warner Backus', 5, 'Niklaus Emil Wirth', True, 'Lawrence Gordon Tesler', None, {1, 2, 3}, {'hello': 'world'}], '—')
    # print(list(data))
    # print(*intersperse([1, 2, 3], 0))

def annual_return(start, percent, years):
    """простые проценты"""
    return (start * (1 + percent/100)**i for i in range(1, years+1))

def pluck(data, path, default=None):
    """Функция должна возвращать значение по ключу path из словаря data"""
    if "." not in path:
        return data.get(path, default)
    else:
        dot_ind = path.index(".")
        return pluck(data[path[:dot_ind]], path[dot_ind+1:], default)


def recviz(func):
    """Показывает вызовы функций и их значений """
    import functools
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.num += 1
        # print(type(args), args)
        # print(f"Глубина: {wrapper.num} -- Функция: {func.__name__}({args[0]})")
        Args = ', '.join(map(repr, args)) if len(args) != 1 else repr(args[0])
        KWArgs = ", " + ', '.join(f'{k}={repr(v)}' for k, v in kwargs.items()) if kwargs else ""
        print("\t"*wrapper.num + f"-> {func.__name__}({Args}{KWArgs})")
        value = func(*args, **kwargs)
        wrapper.num -= 1
        print("\t"*(wrapper.num+1) + f"<- {repr(value)}")
        return value
    wrapper.num = -1
    return wrapper

# @recviz
# def add(a, b, c, d):
#     return a + b + c + d
# add(1, 2, c=2, d=5)
print()

# @recviz
# def add(a, b, c, d, e):
#     return (a + b + c) * (d + e)
# add('a', b='b', c='c', d=3, e=True)
print()

# @recviz
# def fib(n):
#     if n <= 2:
#         return 1
#     else:
#         return fib(n - 1) + fib(n - 2)
# fib(4)


