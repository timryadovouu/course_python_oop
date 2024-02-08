import sys

"""===================================================SUMMARY======================================================="""


def foo_1():
    """
    getattr возвращает значение атрибута name объекта obj. Если объект obj не имеет атрибута name,
    возвращается значение по умолчанию default. Если значение по умолчанию не указано,
    возбуждается исключение AttributeError
    Функция getattr() принимает три аргумента:
    obj — объект
    name — имя атрибута
    default — значение по умолчанию
    """

    class Cat:
        night_vision = True
        paws_count = 4

    cat = Cat()
    cat.name = 'Кемаль'
    print(getattr(cat, 'name'))  # Кемаль
    print(getattr(cat, 'age', None))  # None
    print(getattr(cat, "night_vision"))  # True


def foo_2():
    """
    Функция setattr устанавливает объекту obj атрибут name со значением value. Если объект obj уже имеет атрибут name,
    его значение перезаписывается.
    Функция setattr() принимает три аргумента:
    obj — объект
    name — имя атрибута
    value — значение атрибута
    """

    class Cat:
        pass

    cat = Cat()
    cat.name = 'Кемаль'
    setattr(cat, 'age', 1)
    setattr(cat, 'name', 'Роджер')
    print(cat.age)  # 1
    print(cat.name)  # Роджер


def foo_3():
    """
    Функция delattr удаляет атрибут name у объекта obj. Если объект не имеет атрибута name, возбуждается исключение AttributeError.
    Функция delattr() принимает два аргумента:
    obj — объект
    name — имя атрибута
    """

    class Cat:
        pass

    cat = Cat()
    cat.name = 'Кемаль'
    cat.age = 1
    print(cat.__dict__)  # {'name': 'Кемаль', 'age': 1}
    delattr(cat, 'name')
    delattr(cat, 'age')
    print(cat.__dict__)  # {}


def foo_4():
    """
    Функция hasattr возвращает True, если объект obj имеет атрибут name, или False в противном случае.
    Функция hasattr() принимает два аргумента:
    obj — объект
    name — имя атрибута
    """

    class Cat:
        night_vision = True
        paws_count = 4

    cat = Cat()
    cat.name = 'Кемаль'
    print(hasattr(cat, 'name'))
    print(hasattr(cat, 'age'))
    print(hasattr(cat, 'night_vision'))


def foo_5():
    """Метод __init__() инициализирует атрибуты объекта"""

    class Cat:
        def __init__(self, breed, name):
            self.breed = breed  # порода кошки
            self.name = name  # имя кошки
            self.night_vision = True  # способность видеть в темноте -- фиксированное значение

    cat1 = Cat('Британский', 'Кемаль')
    cat2 = Cat('Манчкин', 'Роджер')
    print(cat1.breed, cat1.name)
    print(cat2.breed, cat2.name)


# nums = [1, 2, 3]
# text = 'beegeek'
# nums.append(4)
# text = text.lower()
# эквивалентно
# nums = [1, 2, 3]
# text = 'beegeek'
# list.append(nums, 4)
# text = str.lower(text)

"""===================================================TASKS========================================================="""


def task_0():
    """класс копилка"""

    class PiggyBank:
        def __init__(self, balance=0, volume=400):
            self.balance = balance
            self.volume = volume

        def add_coins(self, coins):
            if self.balance + coins > self.volume:
                raise ValueError('Копилка слишком мала!')
                # print("Копилка переполнена!")
            else:
                self.balance += coins

        def remove_coins(self, coins):
            if self.balance - coins < 0:
                raise ValueError('Берешь больше, чем есть!')
                # print("Берешь больше, чем есть!")
            else:
                self.balance -= coins

    piggybank = PiggyBank(volume=10)
    print(piggybank.balance)
    piggybank.add_coins(11)
    # piggybank.add_coins(2)
    # print(piggybank.balance)
    # piggybank.remove_coins(3)


def task_4():
    from math import pi
    class Circle:
        def __init__(self, radius):
            self.radius = radius
            self.diameter = self.radius * 2
            self.area = pi * self.radius ** 2

    circle = Circle(5)
    print(circle.radius)
    print(circle.diameter)
    print(circle.area)


def task_5():
    class Bee:
        def __init__(self, x=0, y=0):
            self.x = x
            self.y = y

        def move_up(self, n):
            self.y += n

        def move_down(self, n):
            self.y -= n

        def move_right(self, n):
            self.x += n

        def move_left(self, n):
            self.x -= n

    bee = Bee()
    bee.move_right(2)
    bee.move_right(2)
    bee.move_up(3)
    bee.move_left(1)
    bee.move_down(1)
    print(bee.x, bee.y)


def task_6():
    class Gun:
        def __init__(self):
            self.counter = -1

        def shoot(self):
            self.counter += 1
            if not self.counter % 2:
                print("pif")
            else:
                print("paf")

    gun = Gun()
    gun.shoot()
    gun.shoot()
    gun.shoot()
    gun.shoot()


def task_7():
    class Gun:
        def __init__(self):
            self.counter = 0

        def shoot(self):
            if not self.counter % 2:
                print("pif")
            else:
                print("paf")
            self.counter += 1

        def shots_count(self):
            return self.counter

        def shots_reset(self):
            self.counter = 0

    gun = Gun()
    print(gun.shots_count())
    gun.shoot()
    print(gun.shots_count())
    gun.shoot()
    print(gun.shots_count())


def task_8():
    class Scales:
        def __init__(self):
            self.right_mass = 0
            self.left_mass = 0

        def add_right(self, a_mass):
            self.right_mass += a_mass

        def add_left(self, a_mass):
            self.left_mass += a_mass

        def get_result(self):
            if self.right_mass == self.left_mass:
                return "Весы в равновесии"
            if self.right_mass > self.left_mass:
                return "Правая чаша тяжелее"
            return "Левая чаша тяжелее"

    scales = Scales()
    scales.add_right(2)
    scales.add_left(1)
    print(scales.get_result())


def task_9():
    class Vector:
        def __init__(self, x=0, y=0):
            self.x = x
            self.y = y

        def abs(self):
            return (self.x ** 2 + self.y ** 2) ** 0.5

    vector = Vector(3, 4)
    print(vector.x, vector.y)
    print(vector.abs())


def task_10():
    class Numbers:
        def __init__(self):
            self.num_list = []

        def add_number(self, num):
            self.num_list.append(num)

        def get_even(self):
            return list(filter(lambda x: x % 2 == 0, self.num_list))
        def get_odd(self):
            return list(filter(lambda x: x % 2 == 1, self.num_list))

    numbers = Numbers()
    numbers.add_number(3)
    numbers.add_number(2)
    numbers.add_number(1)
    numbers.add_number(4)
    print(numbers.get_even())
    print(numbers.get_odd())

def task_11():
    class TextHandler:
        def __init__(self):
            self.my_list = []
            self.min_len = self.max_len = 0
        def add_words(self, data):
            self.my_list.extend(data.split())
            self.min_len = min(map(len, self.my_list))
            self.max_len = max(map(len, self.my_list))

        def get_shortest_words(self):
            return [i for i in self.my_list if len(i) == self.min_len]
        def get_longest_words(self):
            return [i for i in self.my_list if len(i) == self.max_len]

    texthandler = TextHandler()
    print(texthandler.get_shortest_words())
    print(texthandler.get_longest_words())

    texthandler = TextHandler()
    texthandler.add_words('The world will hold my trial for your sins')
    texthandler.add_words('Never meant to see the sky, never meant to live')
    print(texthandler.get_shortest_words())
    print(texthandler.get_longest_words())

def task_12():
    class Todo:
        def __init__(self):
            self.things = []
            self.min_pr = self.max_pr = None
        def add(self, task, pr):
            self.things.append((task, pr))
            self.min_pr = min(self.min_pr or pr, pr)
            self.max_pr = max(self.max_pr or pr, pr)

        def get_by_priority(self, n):
            return [pair[0] for pair in self.things if pair[1] == n]

        def get_low_priority(self):
            return [pair[0] for pair in self.things if pair[1] == self.min_pr]
        def get_high_priority(self):
            return [pair[0] for pair in self.things if pair[1] == self.max_pr]

    todo = Todo()

    todo.add('Ответить на вопросы', 5)
    todo.add('Сделать картинки', 1)
    todo.add('Доделать задачи', 4)
    todo.add('Дописать конспект', 5)

    print(todo.get_low_priority())
    print(todo.get_high_priority())
    print(todo.get_by_priority(3))

def task_13():
    class Postman:
        def __init__(self):
            self.delivery_data = []
            self.houses, self.flats = [], []
        def add_delivery(self, *args):
            self.delivery_data.append((args[0], args[1], args[2]))
        def get_houses_for_street(self, street):
            for pair in self.delivery_data:
                if pair[0] == street and pair[1] not in self.houses:
                    self.houses.append(pair[1])
            return self.houses
        def get_flats_for_house(self, street, house):
            for pair in self.delivery_data:
                if pair[0] == street and pair[1] == house and pair[2] not in self.flats:
                    self.flats.append(pair[2])
            return self.flats
    postman = Postman()

    postman.add_delivery('Советская', 151, 74)
    postman.add_delivery('Советская', 151, 75)
    postman.add_delivery('Советская', 90, 2)
    postman.add_delivery('Советская', 151, 74)

    print(postman.get_houses_for_street('Советская'))
    print(postman.get_flats_for_house('Советская', 151))

def task_14():
    class Wordplay:
        def __init__(self, words=[]):
            self.words = words.copy()  # список

        def add_word(self, word):
            if word not in self.words:
                self.words.append(word)
        def words_with_length(self, n):
            return [item for item in self.words if len(item) == n]
        def only(self, *args):
            # print(set(args), set(self.words[0]))
            return [item for item in self.words if set(item).issubset(set(args))]
        def avoid(self, *args):
            return [item for item in self.words if not set(item).intersection(set(args))]

    words = ['Лейбниц', 'Бэббидж', 'Нейман', 'Джобс', 'да_Винчи', 'Касперский']
    wordplay = Wordplay(words)
    words.extend(['Гуев', 'Харисов', 'Светкин'])
    print(words)
    print(wordplay.words)

def task_15():
    import numpy as np
    class Knight:
        def __init__(self, horizontal, vertical, color):
            self.new_dict = {chr(ord("a") + i): i for i in range(8)}
            self.horizontal = horizontal  # a-h
            self.horizontal_num = self.new_dict[self.horizontal]  # 0-7
            self.vertical = vertical  # 1-8
            self.color = color  # b or w

        def get_char(self):
            return "N"

        def can_move(self, x, y):
            return abs(self.new_dict[x] - self.horizontal_num) * abs(y - self.vertical) == 2

        def move_to(self, x, y):
            if self.can_move(x, y):
                self.horizontal, self.vertical = x, y
                self.horizontal_num = self.new_dict[self.horizontal]

        def draw_board(self):
            board = [["."] * 8 for _ in range(8)].copy()
            for i in range(8):
                for j in range(8):
                    if j == self.horizontal_num and i == self.vertical - 1:
                        board[7 - i][j] = "N"
                    elif abs(j - self.horizontal_num) * abs(i - self.vertical + 1) == 2:
                        board[7 - i][j] = "*"
            print(*["".join(line) for line in board], sep="\n")

    knight = Knight('g', 7, 'black')
    knight.draw_board()

    # TEST_7:
    knight = Knight('d', 8, 'white')
    knight.draw_board()

    # TEST_8:
    knight = Knight('h', 1, 'black')
    knight.draw_board()