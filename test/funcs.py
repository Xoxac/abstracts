from defs import prin

# Функция представляет собой именованный блок программного кода, ко-
# торый можно выполнить, вызвав функцию. При вызове функции могут
# передаваться параметры, которые называются аргументами функции.

def show(txt):
    symbs=sorted(list(txt))
    print(symbs)
show("Python")

def sqsum(n):
    nums=[k*k for k in range(1, n+1)]
    return sum(nums)
m=10
print("сумма квадратов чисел от 1 до", str(m)+":", sqsum(m))

# Напишите программу, в которой описана функция, возвращающая ре-
# зультатом второе по величине число в списке, переданном функции в ка-
# честве аргумента.
def max2(arg):
    lis = list(arg)
    lis.remove(max(lis))
    m2 = max(lis)
    return m2
ll = [2, 3, 4, 5, 7, 3]
print(max2(ll))

# Напишите программу, в которой описана функция, возвращающая
# результатом сумму нечетных чисел. Количество чисел передается аргу-
# ментом функции.
def nech(arg):
    l = [i%2!=0 for i in range(arg)]
    print(sum(l))
nech(25)


def positive(x):
    return x > 0  # функция возвращает только True или False
result = filter(positive, [-2, -1, 0, 1, -3, 2, -3])


# map + filter
some_list = [i - 10 for i in range(20)]
def pow2(x): return x**2
def positive(x): return x > 0

print(some_list)
print(list(map(pow2, filter(positive, some_list))))


# LAMBDA
# эти две функции выполняют одно и тоже складывают два числа
def my_function(x1, x2):  # Обычная функция
   return x2 + x1

lambda x1, x2: x2 + x1  # Анонимная функция


# функция как параметр функции:
def operation(x, y, func):
    return func(x, y)
def summ(x, y):
    return x + y
def mult(x, y):
    return x * y
print(operation(2, 3, summ))  # 5

# функция как результат функции:
def sum(a, b): return a + b
def diff(a, b): return a - b
def select_operation(choice):
    if choice == 1:
        return sum
    else:
        return diff
operation = select_operation(1)



# prin("Задатак 5")

# объявили функцию для подсчета количества символов в тексте
# def char_frequency(text):
#
#    text = text.lower()
#    text = text.replace(" ", "")
#    text = text.replace("\n", "")
#    count = {}  # для подсчета символов и их количества
#    for char in text:
#        if char in count:  # если символ уже встречался, то увеличиваем его количество на 1
#            count[char] += 1
#        else:
#            count[char] = 1
#
#    for char, cnt in count.items():
#        print(f"Символ {char} встречается {cnt} раз")
#
#
# вызвали функцию в любом месте программы

# def pow_func(base, n=2): # base - позиционный - обязательный, n - именованый - необязательный
#    print(base ** n)
#
# pow_func(3)  # 9
# pow_func(5, 3)  # 125

# Напишите функцию, которая проверяет является ли число n, делителем числа a. И выводит на экран соответствующее
# сообщение, является ли число делителем или нет.

# def de(a, n):
#     n, a = int(n), int(a)
#     print("ovo je dobro") if a % n == 0 else print("to nije dobro")
#
# de(input(), input())

# prin("Задание 4.2.4")
# Напишите функцию, которая печатает “обратную лесенку” следующего типа:
# n = 3
# ***
# **
# *
#
# n = 4
# ****
# ***
# **
# *

# n = int(input("n:  "))
# def a(n):
#     lad = list()
#     for i in range(n):
#         row = "*"*(i+1)
#         lad.append(row)
#     lad.reverse()
#     print(lad)
#     return lad
#     # for i in lad:
#     #     print(i)
#
# b = a(n)
# print(b)

# prin("Задание 4.2.5")
# Напишите функцию, которая будет возвращать количество делителей числа а.
# Пример ввода: 5
# Пример вывода программы: 2
# def cnt(arg):
#     a = int(arg)
#     count = 0
#     if a<0:
#         step = -1
#     else:
#         step = 1
#     for i in range(-a, a+step, step):
#         try:
#             if a%i==0:
#                 count += 1
#         except:
#             pass
#     return count
# print(cnt(input()))

# prin("Задание 4.2.6")

# Напишите функцию, которая проверяет, является ли данная строка палиндромом или нет,
# и возвращается результат проверки.
# Пример:
# check_palindrome("test")  # False
# check_palindrome("Кит на море не романтик")  # True
# def pal(text):
#     text = text.lower()
#     text.replace(" ", "")
#     rev = text[::-1]
#     return (rev == text)
#
# print(pal(input("text:  ")))

# prin("Запакованные переменные, или что такое *args и **kwargs")
# amass = [1, 2, 3]
# print(amass)
# print(*amass)  # = print(amass[0], amass[1], .., amass[-1])
# di = {1: "key"}
# print(di)
# print(*di)
#
# a = [1, 2, 3]
# b = [*a, 4, 5, 6]
# print(b)  # [1, 2, 3, 4, 5, 6]


# Чтобы функция могла принимать неограниченное количество позиционных аргументов,
# есть специальная конструкция *args, а для именованных аргументов **kwargs.
# Аrgs и kwargs не являются зарезервированными словами, это просто общее обозначение

# def a(*args, **kwargs):  # = def a(arg, arg, .. , arg):
#     print(args, "\n", kwargs)
#
#
# a(1, 1, 2, 3, 5, 6, 7, n=1, asd=2, qw=2)

# args — это кортеж, а kwargs  — это словарь

# prin("Задание 4.3.2")

# Написать функцию, которая будет перемножать любое количество переданных ей аргументов.

# def mn(*arg, znak="*"):
#     global re
#     lis1 = arg
#
#     zn = znak
#
#     if zn == "*":
#         re = 1
#         for i in lis1:
#             re = re * i
#     elif zn == "/":
#         re = 1
#         for i in lis1:
#             try:
#                 re = re / i
#             except:
#                 print("Бомжих, не дели на 0! Без 0 это так:  ")
#     return re
#
#
# a = input()
# lisa = list(map(int, a.split()))
#
# # print(mn(*lisa))
# prin("Рекурсивные функции")
#
# def fact(n):
#     if n == 1:
#         return 1
#     return n*fact(n-1)
#
# print(fact(int(input("digit:  "))))

# prin("Задание 4.3.3")
# С помощью рекурсивной функции найдите сумму чисел от 1 до n.
# def su(n):
#     if n == 0:
#         return 0
#     return n+su(n-1)
#
# print(su(int(input("dig:  "))))

# prin("Задание 4.3.4")
# С помощью рекурсивной функции развернуть строку в обратную сторону
# def reverse_str(string):
#    if len(string) == 0:
#        return ''
#    else:
#        return string[-1] + reverse_str(string[:-1])
#
# reverse_str('test')  # tset
# prin("Задание 4.3.5")
# Дано натуральное число N. Вычислите сумму его цифр.
# При решении этой задачи нельзя использовать строки, списки, массивы и циклы

# def ss(n):
#     m = n%10
#     h = n//10
#     if h == 0 and m == 0:
#         return 0
#     else:
#         return m+ss(h)
#
# print(ss(856))

# prin("Функции-генераторы")


# Их задача выполнять те действия, которые прописаны в теле функции-генератора,
# дальше уходить в «спячку» и ждать следующего вашего обращения
# return - вернуть и выйти из функции
# yield - вернуть (что то странное) и остановиться на месте в функции
# def fib(): # - НЕ функция, а генератор
#     a, b = 0, 1
#     yield a
#     yield b
#
#     while True:
#         a, b = b, a + b
#         yield b
#
# a = fib()
# print(type(a))
# prin("Задание 4.4.1")
# Создать функцию-генератор, возвращающую бесконечную последовательность натуральных чисел.
# По умолчанию, она начинается с единицы и шагом 1, но пользователь может указать
# любой шаг и любое число в качестве аргумента функции,
# с которого будет начинаться последовательность.

# def inf(dig, step):
#     while True:
#         dig += step
#         yield dig
# for i in inf(2, 3):
#     print(i)

# prin("Задание 4.4.2")
# Создайте генератор, который по переданному списку создаёт последовательность,
# в которой элементы этого списка бесконечно циклично повторяются.
# Например, для списка [1, 2, 3] генератор создаст бесконечную последовательность 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, ... .

# def iii(arg:list):
#     while True:
#         for i in arg:
#             yield i
# count = 0
# for i in iii([1, 2, 3]):
#     if count >= 10:
#         break
#     print(i)
#     count += 1

