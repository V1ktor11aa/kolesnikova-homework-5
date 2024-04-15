# Vika Kolesnikova
# Homework-5
# 01.04.2024
# Grodno-IT-Academy-Python 3.10


# Реализовать функцию get_ranges которая получает на вход непустой список неповторяющихся целых чисел,
# отсортированных по возрастанию, которая этот список “сворачивает”.
# get_ranges([0, 1, 2, 3, 4, 7, 8, 10])  #  "0-4, 7-8, 10"
# get_ranges([4,7,10])  # "4, 7, 10"
# get_ranges([2, 3, 8, 9])  # "2-3, 8-9"
def get_ranges(lst):
    ranges = []
    start = lst[0]
    end = lst[0]

    for i in range(1, len(lst)):
        if lst[i] == end + 1:
            end = lst[i]
        else:
            if start == end:
                ranges.append(str(start))
            else:
                ranges.append(f"{start}-{end}")
            start = end = lst[i]

    if start == end:
        ranges.append(str(start))
    else:
        ranges.append(f"{start}-{end}")

    return ', '.join(ranges)
    # Решение верно

# Напсать функцию standardise_phones которая принимает любое
# количество нестандартизированных телефонных номеров и возвращает
# список стандартизированных номеров в том порядке в котором они были
# введены. А если число не является номером - возвращает пустой список
# standardise_phones("298884455") # ["+375298884455"]
# standardise_phones("(29)888-44-55","8029 8885555","+375299998877","375299998867") # ["+375298884455","+375298885555","+375299998877","+375299998867"]
# standardise_phones("298884asd45") # []
import re

def standardise_phones(*args):
    def standardise(phone):
        if isinstance(phone, int):
            phone = str(phone)
        if not isinstance(phone, str):
            return None
        phone = re.sub(r'\D', '', phone)
        if len(phone) == 9:
            return "+375" + phone
        elif len(phone) == 11 and phone.startswith("80"):
            return "+375" + phone[2:]
        elif len(phone) == 12 and phone.startswith("375"):
            return "+375" + phone[3:]
        return None

    result = []
    for arg in args:
        standardized_phone = standardise(arg)
        if standardized_phone:
            result.append(standardized_phone)
    return result
    # Хорошее решение, есть более универсальное - см ответы
# Создайте декоратор handle_multiples который позволит функции rope_product
# вернуть лиш один ответ если задано одно число и много ответов списком если
# введённых значений будет несколько! И добавьте его к функции rope_product
# не меняя решения из предыдущего решения!
# rope_product(8) -> 18
# rope_product(7,11,23,45,32) -> [12, 54, 4374, 14348907, 118098]
# здесь можно пользоваться циклами
def handle_multiples(func):
    def wrapper(*args):
        if len(args) == 1:
            return func(*args)
        else:
            return [func(arg) for arg in args]
    return wrapper
    # Декоратор верный
# Создайте функцию rope_product, которая берёт позитивный цельный номер,
# который представляет собой длину верёвки. Длина этой
# верёвки может быть разделена на любое количество более
# малых цельных чисел. Верните максимальный продукт умножения
# малых цельных чисел. Решение не должно пользоваться циклами!

# rope_product(1) -> 1
# rope_product(4) -> 4
# rope_product(5) -> 6
# rope_product(6) -> 9
# rope_product(7) -> 12
# rope_product(11) -> 54
def handle_multiples(func):
    def wrapper(*args):
        if len(args) == 1:
            return func(*args)
        else:
            return [func(arg) for arg in args]
    return wrapper

@handle_multiples
def rope_product(n):
    if n <= 3:
        return n
    if n % 3 == 0:
        return 3**(n//3)
    if n % 3 == 1:
        return 4 * 3**((n-4)//3)
    return 2 * 3**((n-2)//3)
    # Вск верно
