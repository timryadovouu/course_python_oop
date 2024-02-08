from collections import defaultdict
from string import printable

"""===============================ХЭШ-ФУНКЦИИ=========================SUMMARY========================================"""


def bar_0():
    """нормальное распределение"""
    hashes = defaultdict(int)
    for char in printable:
        hashes[hash(char) % 20] += 1

    for hash_value, hash_count in sorted(hashes.items()):
        print(hash_value, '■' * hash_count)


"""===============================ХЭШ-ФУНКЦИИ===========================TASKS========================================"""

def task_1():
    def hash_function(obj):
        qwe = str(obj)
        temp1 = 0
        while qwe:
            if len(qwe) == 1:
                temp1 += ord(qwe[0])
            else:
                temp1 += ord(qwe[0]) * ord(qwe[-1])
            qwe = qwe[1:-1]
        temp2 = sum([(i + 1) * (-1) ** i * ord(str(obj)[i]) for i in range(len(str(obj)))])
        return (temp1 * temp2) % 123456791

    hash_function("qwer")
    hash_function("1234567")
    hash_function("python")


def task_2():
    pass