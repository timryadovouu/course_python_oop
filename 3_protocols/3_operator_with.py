"""==================ОПЕРАТОР-WITH==================================================SUMMARY=========================="""

def bar_0():
    """example"""
    file = open('output.txt', mode='w', encoding='utf-8')
    try:
        file.write('Python generation!')
    except Exception as error:
        print(f'При записи в файл возникла ошибка: {error}')
    finally:
        file.close()

def bar_1():
    """равносильный переход"""
    # --------------------------------------
    # file = open('output.txt', mode='w', encoding='utf-8')
    # try:
    #     file.write('Python generation!')
    # finally:
    #     file.close()
    # --------------------------------------
    with open('output.txt', mode='w', encoding='utf-8') as file:
        file.write('Python generation!')

def bar_2():
    """examples"""
    file = open('output.txt', mode='w', encoding='utf-8')
    with file:
        file.write('Python generation!')
    # --------------------------------------------------
    with open('file.txt', encoding='utf-8') as file, open('output.txt', mode='w', encoding='utf-8') as output:
        for index, line in enumerate(file, 1):
            output.write(f'{index}. {line}')
    # or -- or -- or
    with open('file.txt', encoding='utf-8') as file:
        with open('output.txt', mode='w', encoding='utf-8') as output:
            for index, line in enumerate(file, 1):
                output.write(f'{index}. {line}')
    # --------------------------------------------------
    file = open('output.txt', mode='w', encoding='utf-8')
    with file:
        print(file.closed)  # False
    print(file.closed)  # True
    # --------------------------------------------------
    with open('output.txt', mode='w', encoding='utf-8') as file:
        print(file.readable(), file.writable())  # False True
    with open('output.txt', mode='r', encoding='utf-8') as file:
        print(file.readable(), file.writable())  # True False
    # --------------------------------------------------
    # связка для проверки существования файла
    try:
        with open('file.txt', encoding='utf-8') as file:
            print(file.read())
    except Exception as error:
        print(f'Произошла ошибка {error}')
    # --------------------------------------------------==
    with open('file.txt', encoding='utf-8') as file, open('output.txt', mode='w', encoding='utf-8') as output:
        for index, line in enumerate(file, 1):
            output.write(f'{index}. {line}')
    # ---
    with (
        open('file.txt', encoding='utf-8') as file,
        open('output.txt', mode='w', encoding='utf-8') as output
    ):
        for index, line in enumerate(file, 1):
            output.write(f'{index}. {line}')

"""==================ОПЕРАТОР-WITH==================================================TASKS=========================="""

def task_1():
    def print_file_content(filename):
        try:
            with open(filename, "r", encoding="utf-8") as file:
                print(file.read())
        except FileNotFoundError:
            print("Файл не найден")

    with open('Precepts_of_Zote.txt', 'w', encoding='utf-8') as file:
        file.write('Сражения и путешествия берут своё')
    print_file_content('Precepts_of_Zote.txt')

def task_2():
    def non_closed_files(files):
        return [file for file in files if not file.closed]

def task_3():
    def log_for(logfile, date_str):
        with (
            open(logfile, mode="r", encoding="utf-8") as in_file,
            open(f"log_for_{date_str}.txt", mode="w", encoding="utf-8") as output_file
        ):
            for line in in_file.readlines():
                if line.startswith(date_str):
                    output_file.write(line[line.find(" ") + 1:])

    with open('log.txt', 'w', encoding='utf-8') as file:
        print('2022-01-01 INFO: User logged in', file=file)
        print('2022-01-01 ERROR: Invalid input data', file=file)
        print('2022-01-02 INFO: User logged out', file=file)
        print('2022-01-03 INFO: User registered', file=file)

    log_for('log.txt', '2022-01-01')

    with open('log_for_2022-01-01.txt', encoding='utf-8') as file:
        print(file.read())
