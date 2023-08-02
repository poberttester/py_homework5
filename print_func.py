from functions import abs_path_separator, dict_gen,fibonachi_gen
from input_data import some_path, name_list, salary_list, extra_list, fibonachi_input


def print_abs_path_separator():
    """Функция выводит в консоль ответ по заданию 1"""

    print(abs_path_separator(some_path))


def print_dict_gen():
    """Функция выводит в консоль ответ по заданию 2"""

    print(dict_gen(name_list, salary_list, extra_list))


def print_fibonachi_gen():
    """Функция выводит в консоль ответ по заданию 3"""

    print(fibonachi_gen(fibonachi_input))