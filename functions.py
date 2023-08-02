import re


def abs_path_separator(abs_path: str):
    """Функция принимает на вход строку - абсолютный путь до файла и
     возвращает кортеж из трёх элементов: путь, имя файла, расширение файла."""

    *path, name, extension = re.split('[/ .]', abs_path)
    tuple_result = (path, name, extension)
    return tuple(tuple_result)


def dict_gen(name: list, rate: list, premium_procents: list):
    """Генератор словаря принимает на вход три списка одинаковой длины.
       Возвращает словарь с именем в качестве ключа и суммой премии в качестве значения.
       Сумма рассчитывается как ставка умноженная на процент премии"""

    premium = [float(i.replace('%', '')) for i in premium_procents]
    premium_amount = [premium[index] * rate[index] for index in range(len(premium))]

    return {name[i]: premium_amount[i] for i in range(len(premium_amount))}


def fibonachi_gen(n: int):
    """"Генератор чисел Фибоначи до заданного числа"""

    fibonacci_numbers = [0, 1]
    if n == 0:
        fibonacci_numbers = [0]
        return fibonacci_numbers

    i = 1
    while i < n:
        fibonacci_numbers.append(fibonacci_numbers[i - 1] + fibonacci_numbers[i])
        i += 1

    return fibonacci_numbers

