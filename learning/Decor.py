def log_decorator(func):
    def wrap(*args, **kwargs):
        print(f"before function")
        func(*args, **kwargs)

    return wrap


@log_decorator
def hello(string="None"):
    print(string)


hello("Hallo")

# p1 = "        Bang!   "
# p2 = "       Bang!   "
#
#
# def who_first(person1, person2):
#     p1 = person1.find("Bang!")
#     p2 = person2.find("Bang!")
#     if (p1 < p2):
#         print(f"the first person was faster ")
#     elif (p1 > p2):
#         print(f"the second person was faster")
#     else:
#         print("tie")


# who_first(p1, p2)
# multiplier = lambda x, y: x * y
# print(multiplier(2, 3))  # анонимная функция
#
# ages = [18, 16, 21, 12, 33]
#
# print(list(filter(lambda age: age >= 18, ages)))  # lamda выражение

# -------------------------------------------------
# def is_adult(age):
#     return age >= 18
#
#
# ages = [18, 16, 21, 12, 33]
#
# print(list(filter(is_adult, ages)))

# def square(number):
#     return number * number
#
#
# numbers = [1, 2, 3, 4, 5]  # list []
#
# for x in map(square, numbers):  # передаем функцию без скобок как аргумент
#     print(x)
#
# print(list(map(square, numbers)))  # сразу сформировать в лист
# ----------------------------
# def square(*args):
#     return [x * x for x in args]  # лист компрехеншен
#
#
# res = square(1, 2, 3, 4, 5, 6)
# print(res)
# ------------------------------------------------------------
# def string_strip(strip_chars=" "): # вложенные функции
#     def do_strip(string): № без этого стринг работать не будет
#         return string.strip(strip_chars)
#
#     return do_strip
#
#
# str1 = string_strip("!")
# print(str1("! some "))
