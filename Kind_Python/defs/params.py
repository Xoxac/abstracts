# *args вернет кортеж из значений args
# **kwargs вернет словарь, заменив = на :
# перед *args можно указать фактические параметры, перед *kwargs именованные

def get_v(a, b, c, d=True):   # d - формальный параметр, можно не указывать при вызове
    if d:                     # a b c - фактические параметры, указывать обязательно
        print(f'a = {a}, b = {b}, c = {c}')
    return a * b * c

def os_path(*args, sep='\\'):   # любое число фактических и именованных аргументов, можно ноль
    return sep.join(args)       # вернет кортеж из значений аргументов

print(os_path('I learn ', ' Kind_Python', sep='/'))

def fun(*args, **kwargs):
    print(kwargs)               # вернет словарь из аргументы: значения аргументов
    return kwargs['sep'].join(args) # даст ошибку, если при вызове не указать sep

print(fun('I learn ', ' Kind_Python', sep='/', trim=True))


def get_biggest_city(*args):
    return max(args, key=len)
print(get_biggest_city('Питер', 'Москва', 'Самара', 'Воронеж'))



def get_data_fig(*args, **kwargs):
    return (sum(args),) + tuple(kwargs.values())   # вывести в один кортеж, а не кортеж с кортежами
print(get_data_fig(2, 3, 4, 5, tp=False, color=3))


from random import randint
tab = [[randint(0, 1) for i in range(5)] for j in range (5)]
for i in tab:
    for j in i:
        print(j, end=' ')
    print()

def is_isolate(mat):
    for i in mat:
        for j in i:
            return j + 

