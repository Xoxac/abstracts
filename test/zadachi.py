from defs import prin

prin("Задание B5.2.9")

# Напишите программу, которая на вход принимает текст и выводит
# количество уникальных символов.

tekst = "jhgjgjjj" # input("text:  ")
lis = []

print(len(tekst))

for i in tekst: # оказалось, можно так: mnog = list(set(text))
    lis.append(i)

mnog = set(lis)

print(len(mnog))


prin("Задание 5.3.11")
# Напишите программу, которая на вход принимает последовательность целых чисел,
# и возвращает True, если все числа ненулевые, и False, если хотя бы одно число равно 0.

# L = list(map(int, input().split()))
#
# print(all(L))

prin("Задание 6.3.17")
# Используя функцию zip() внутри генераторов списков, вычислите поэлементные произведения списков L и M.
#  функция zip(), которая позволяет объединить два списка в новый список кортежей,
#  каждый из которых будет содержать по одному элементу из каждого списка

L = [i for i in range(10)]
M = [i for i in range(10, 0, -1)]

liss = [a * b for a, b in zip(L, M)]
print(liss)

prin("Задание 6.3.18")
# Реализуйте программу, которая сжимает последовательность символов.
# На вход подается последовательность вида: aaabbccccdaa
# Необходимо вывести строку, где каждая последовательность из одинаковых символов, идущих подряд,
# заменяется на один символ, и длину этой последовательности (включая последовательности единичной длины).
# Вывод должен выглядеть так: a3b2c4d1a2

posl = input()
lis_posl = [i for i in posl]
count = 1
dic = []
for index, value in enumerate(lis_posl):
    try:
        if value == lis_posl[index+1]:
            count += 1
        else:
            dic.append(value)
            dic.append(count)
            count = 1
    except:
        dic.append(value)
        dic.append(count)
        count = 1

print(*dic, sep="")

