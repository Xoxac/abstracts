# внутри нужно явно указать, что вернет функция, с помощью return
# return завершает функцию

def send_mail(from_name, age):
    text = f'Hi, my name is {from_name} and I am {age} years old'
    print(text)
send_mail('Xoxa', 39)



def get_sqrt(x):
    res = None if x < 0 else x ** 0.5    # return поддерживает тернарные операторы
    return (res, x)    # В return можно вписать кортеж (можно без скобок)
a, b = get_sqrt(49)    # кортеж можно распаковать множественным присваиванием
print(a, b)


# функция принимает себя как аргумент - сложная задача решается несколькими вызовами
def get_max2(a, b):
    return a if a > b else b
x, y, z = 5, 7, 9
print(get_max2(x, get_max2(y, z)))

def get_max3(a, b, c):
    return get_max2(a, get_max2(b, c))
print(get_max3(4, 5, 6))


# выбор функции
# если флаг True, вычисляем периметр, если False - площадь (0 - False, 1 - True в IT)
from random import randint
fl = randint(0, 1)
if fl:
    def get_rect(a, b):
        return 2*(a+b)
else:
    def get_rect(a, b):
        return a*b
print(get_rect(2, 4))


# если ввели RECT, юзаем площадь прямоугольника, иначе - квадрата
# tp = input('word: ').strip()
tp = 'asfg'
if tp == 'RECT':
    def get_sq(lenght, width):
        return lenght*width
else:
    def get_sq(x):
        return x**2


# функции отбора четных / нечетных чисел
def even(x):
    return x % 2 == 0    # вернет True или False
for i in range(1, 10):
    if even(i):
        print(i)


# lst_d = list(map(int, input('digs: ').split()))
lst_d = [2, 3, 4, 5, 6, 7]
def nev(x):
    return x % 2 != 0
lst = [x for x in lst_d if nev(x)]
print(*lst)









