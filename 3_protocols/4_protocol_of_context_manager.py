"""==================ПРОТОКОЛ-КОНТЕКСТНЫХ-МЕНЕДЖЕРОВ===============PART1==============SUMMARY=========================="""


def bar_0():
    class CustomContextManager:
        def __enter__(self):
            print('Вход в контекстный менеджер...')
            return 'Python generation!'

        def __exit__(self, exc_type, exc_value, traceback):
            print('Выход из контекстного менеджера...')
            print(exc_type, exc_value, traceback, sep='\n')

    with CustomContextManager() as manager:
        print(manager)

    # Вход в контекстный менеджер...
    # Python generation!
    # Выход из контекстного менеджера...
    # None
    # None
    # None

    with CustomContextManager() as manager:
        print(manager)
        print(manager[100])


def bar_1():
    """Обработка исключений внутри блока with"""

    class CustomContextManager:
        def __enter__(self):
            print('Вход в контекстный менеджер...')
            return 'Python generation!'

        def __exit__(self, exc_type, exc_value, traceback):
            print('Выход из контекстного менеджера...')
            if isinstance(exc_value, IndexError):
                print(f'Тип возникшего исключения: {exc_type}')
                print(f'Текст исключения: {exc_value}')
                return True  # подавляем возбужденное исключение IndexError
            return False  # все остальные типы исключений не подавляются

    with CustomContextManager() as manager:
        print(manager)
        print(manager[100])  # обращаемся по несуществующему индексу


# Примеры использования встроенных контекстных менеджеров
def bar_2():
    with open('output.txt', mode='w', encoding='utf-8') as file:
        print('__enter__' in dir(file))  # наличие метода __enter__()
        print('__exit__' in dir(file))  # наличие метода __exit__()
        file.write('Python generation!')
    # True
    # True


def bar_3():
    from decimal import Decimal, localcontext

    num1 = Decimal('1')
    num2 = Decimal('9')

    print(num1 / num2)  # по умолчанию 28 знаков после запятой

    with localcontext() as ctx:
        ctx.prec = 5  # устанавливаем 5 знаков после запятой
        print(num1 / num2)

    with localcontext() as ctx:
        ctx.prec = 10  # устанавливаем 10 знаков после запятой
        print(num1 / num2)


def bar_4():
    import os
    with os.scandir('.') as entries:
        for entry in entries:
            print(entry.name, '--->', entry.stat().st_size, 'bytes')


def bar_5():
    from tempfile import TemporaryFile
    with TemporaryFile(mode='r+') as file:
        file.write('Python generation!')
        file.seek(0)
        content = file.read()
        print(content)


def bar_6():
    """обеспечивает примитивную блокировку для предотвращения одновременного изменения общего ресурса
     несколькими потоками в многопоточном приложении.
     Создает защищенную область (критическая секция), которая предотвращает одновременный доступ из разных
    потоков к общим ресурсам."""

    from threading import Lock
    with Lock() as lock:
        pass
    # защищенная область
    # смело выполняем любые действия, не думая о гонке потоков


def bar_7():
    class CustomContextManager:
        def __init__(self, value):
            self.value = value

        def __enter__(self):
            print('Вход в контекстный менеджер...')
            return self

        def __exit__(self, exc_type, exc_value, traceback):
            print('Выход из контекстного менеджера...')

        def __repr__(self):
            return f'CustomContextManager(value={repr(self.value)})'

    with CustomContextManager('pygen') as manager:
        print(manager)
        print(manager.value)

    # Вход в контекстный менеджер...
    # CustomContextManager(value='pygen')
    # pygen
    # Выход из контекстного менеджера...


def bar_8():
    class CustomContextManager:
        def __init__(self, value):
            self.value = value

        def __enter__(self):
            print('Вход в контекстный менеджер...')
            self.name = 'Кемаль'
            self.breed = 'Британский'
            return self

        def __exit__(self, exc_type, exc_value, traceback):
            print('Выход из контекстного менеджера...')

    with CustomContextManager('pygen') as manager:
        print(manager.value)
        print(manager.name)
        print(manager.breed)

    # Вход в контекстный менеджер...
    # pygen
    # Кемаль
    # Британский
    # Выход из контекстного менеджера...


"""==================ПРОТОКОЛ-КОНТЕКСТНЫХ-МЕНЕДЖЕРОВ===============PART1==============TASKS=========================="""


def is_context_manager(obj):
    return hasattr(obj, "__enter__") and hasattr(obj, "__exit__")


"""==================ПРОТОКОЛ-КОНТЕКСТНЫХ-МЕНЕДЖЕРОВ===============PART2==============SUMMARY========================"""


# Несколько примеров реализации контекстных менеджеров
def foo_0():
    class Trace:
        def __enter__(self):
            print('Начало выполнения блока with')

        def __exit__(self, exc_type, exc_value, traceback):
            if exc_value:
                print(f'Во время выполнения блока with было возбуждено исключение {exc_value}')
            print('Конец выполнения блока with')
            return True  # обрабатываем все типы исключений

    with Trace():
        print('Python generation!')

    # Начало выполнения блока with
    # Python generation!
    # Конец выполнения блока with

    with Trace():
        print('Python generation!')
        print(1 / 0)

    # Начало выполнения блока with
    # Python generation!
    # Во время выполнения блока with было возбуждено исключение division by zero
    # Конец выполнения блока with


def foo_1():
    class WritableTextFile:
        def __init__(self, path):
            self.path = path

        def __enter__(self):
            self.file = open(self.path, mode='w', encoding='utf-8')
            return self.file

        def __exit__(self, exc_type, exc_value, traceback):
            if self.file:
                self.file.close()

    with WritableTextFile('output.txt') as file:
        file.write('Python generation!')


def foo_2():
    import sys
    class RedirectedStdout:
        def __init__(self, new_output):
            self.new_output = new_output

        def __enter__(self):
            self.standard_output = sys.stdout
            sys.stdout = self.new_output

        def __exit__(self, exc_type, exc_value, traceback):
            sys.stdout = self.standard_output

    with open('output.txt', mode='w', encoding='utf-8') as file:
        with RedirectedStdout(file):
            print('Python generation!')
        print('Возврат к стандартному потоку вывода')


def foo_3():
    from time import perf_counter, sleep

    class Timer:
        def __enter__(self):
            self.start = perf_counter()
            return self

        def __exit__(self, exc_type, exc_value, traceback):
            self.elapsed = perf_counter() - self.start

    with Timer() as timer:
        sleep(0.7)
        sleep(1.5)
    print('Затраченное время:', timer.elapsed)


def foo_4():
    """foo_3"""
    from time import perf_counter, sleep

    class Timer:
        def __enter__(self):
            self.start = perf_counter()
            self.end = 0.0
            return lambda: self.end - self.start

        def __exit__(self, exc_type, exc_value, traceback):
            self.end = perf_counter()

    with Timer() as timer:
        sleep(0.7)
        sleep(1.5)
    print('Затраченное время:', timer())


"""==================ПРОТОКОЛ-КОНТЕКСТНЫХ-МЕНЕДЖЕРОВ===============PART2==============TASKS=========================="""


def task_1():
    class SuppressAll:
        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc_val, exc_tb):
            return True

    print('start')
    with SuppressAll():
        print('Python generation!')
        raise ValueError
    print('end')


def task_2():
    class Greeter:
        def __init__(self, name):
            self.name = name

        def __enter__(self):
            print(f"Приветствую, {self.name}!")
            return self

        def __exit__(self, exc_type, exc_val, exc_tb):
            print(f"До встречи, {self.name}!")

    with Greeter('Кейв'):
        print('...')


def task_3():
    class Closer:
        def __init__(self, obj):
            self.obj = obj

        def __enter__(self):
            return self.obj

        def __exit__(self, exc_type, exc_val, exc_tb):
            try:
                self.obj.close()
            except AttributeError:
                print("Незакрываемый объект")
                return True
            # if hasattr(self.obj, 'close'):
            #     self.obj.close()
            # else:
            #     print('Незакрываемый объект')

    with Closer(5) as i:
        i += 1
    print(i)


def task_4():
    class ReadableTextFile:
    def __init__(self, filename):
        self.filename = open(filename, mode="r", encoding="utf-8", newline='\r\n')

    def __enter__(self):
        return self.filename

    def __exit__(self, exc_type, exc_val, exc_tb):
        return True

    with open('glados_quotes.txt', 'w', encoding='utf-8') as file:
        print('Только посмотрите!', file=file)
        print('Как величаво она парит в воздухе', file=file)
        print('Как орел', file=file)
        print('На воздушном шаре', file=file)

    with ReadableTextFile('glados_quotes.txt') as file:
        print(file)
        for line in file:
            print(line)

    with open('poem.txt', 'w', encoding='utf-8') as file:
        print('Я кашлянул в звенящей тишине,', file=file)
        print('И от шального эха стало жутко…', file=file)
        print('Расскажет ли утятам обо мне', file=file)
        print('под утро мной испуганная утка?', file=file)

    with ReadableTextFile('poem.txt') as file:
        for line in file:
            print(line)


def task_5():
    class Reloopable:
    def __init__(self, file):
       self.file = file

    def __enter__(self):
        return self.file.readlines()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
    

    with open('file.txt', 'w') as file:
        file.write('Evil is evil\n')
        file.write('Lesser, greater, middling\n')
        file.write('Makes no difference\n')
        
    with Reloopable(open('file.txt')) as reloopable:
        for line in reloopable:
            print(line.strip())
        for line in reloopable:
            print(line.strip())


def task_6():
    pass


def task_7():
    pass


def task_8():
    pass


def task_9():
    pass
