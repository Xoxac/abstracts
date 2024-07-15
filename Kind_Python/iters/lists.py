import sys

def print_list(l: list):
    for i in l:
        print(*i)


dig = [i for i in range(1, 11)]
dig[0] = 9

# строка в список посимвольно
print(list('python'))  # ['p', 'y', 't', 'h', 'o', 'n']

# основные функции: len, min, max, sum, sorted, sorted(list, reverse=True)
print('srednee arifm = ', sum(dig) / len(dig))
print(max(list('python')))  # y имеет наибольший код
print(sorted(list('python')))

# операторы: +, *, in, del
mix = dig + list('python')
print(mix * 2)
print(12 in dig)
del dig[2:5]
print(dig)

# lst = list(map(int, input('ins digs: ').split()))
lst = dig
print(lst)

lst[2:5] = [44, 5, 77]
print(lst[2:])  # от второго до конца
print(lst[:3])  # от начала до третьего
print(lst[2:-2])  # от второго до предпоследнего не включительно
print(lst[-2:2:-2])  # от предпоследнего до второго через один
lst1 = lst[:]  # копировать список

m = [2, 3, 5, 5, 2, 2, 3, 3, 4, 5, 4, 4]
print(m[7:2:-1])

print(m.append('asd'))
print(m.insert(3, 'asd'))
print(m.remove('asd'))
print(m.pop(0))
print(m.count('asd'))
print(m.reverse())
# print(m.sort())
# print(sorted(m))
if 'asd' in m: print(m.index('asd'))

# st = input()
# lst = list(st)
# lst = lst[1:]
# lst.insert(0, 8)
# for i in lst:
#     if i == '-':
#         lst.remove('-')
# print("".join(list(map(str, lst))))

# name, otc, fam = input('ins IOF: ').split()
# print(fam, ' ', name[0],'.', otc[0],'. ', sep='')

# -- вложенные списки --
t = [['I', 'love', 'Python'],
     ['And', 'I', 'hate', 'war']]
print(t[0][1])
t[1][3] = 'Assembler'
print(t)

# d = []
# s1, s2, s3 = (list(map(int, input('ins 4 digs: ').split())) for _ in range(3))
# for s in (s1, s2, s3):
#     d.append(s)
# print(d)
# print(d[0][-1], d[1][-1], d[2][-1])

t = [["Скажи-ка", "дядя", "ведь", "не", "даром"],
     ["Я", "Python", "выучил", "с", "каналом"],
     ["Балакирев", "что", "раздавал?"]]

# print(input('word: ') in (t[0] or t[1] or t[2]))

# матрица 3 х 4:
ll = [[1] * 3] * 4
print(ll)
for i in ll:
    for j in i:
        print(j, end=' ')
    print()

print()

p = []
j = []
for i in range(4):
    for jz in range(3):
        p.append(0)
    j.append(p)
    p = []

for i in j:
    for d in i:
        print(d, end=' ')
    print()

# перебор по индексам               # то же самое, что
for i in range(len(t)):  # for i in t:
    for j in range(len(t[i])):  #     for j in i:
        print(t[i][j])  #         print(j)

# Двумерный список размером nn x nn, состоящий из нулей, а по главной диагонали - единицы
nn = 4
hg = [[1 if i == j else 0 for i in range(nn)] for j in range(nn)]

# for i in hg:
#     for x, j in enumerate(i):    # вывод без пробела в конце строки
#         if x == len(i)-1:
#             print(j)
#         else:
#             print(j, end=' ')

for i in hg:  # тоже без пробела в конце
    print(*i)

# генератор матрицы, где первая строка нули, потом единицы...
n = 5
lg = [[j for i in range(n)] for j in range(n)]
print_list(lg)

# попарное соединение списков
fg = 'Москва 15000 Уфа 1200 Самара 1090 Казань 1300'.split()
fgr = [[fg[i], int(fg[i + 1])] for i in range(0, len(fg), 2)]
print(fg)
print(fgr)


# -- сложные генераторы --
# при i = 0 перебирает значения j, затем при i = 1 ...
ass = [(i, j)
       for i in range(9) if i % 3 == 0
       for j in range(4) if j % 2 == 0
       ]
print(ass)


# таблица умножения:
tu = [(i*j)
      for i in range(1, 6)
      for j in range(1, 6)
      ]



# разбить список на подсписки
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sublists = [lst[i:i+3] for i in range(0, len(lst), 3)]
print(sublists)
# вывод одномерного списка построчно (по 5)
# перебираем индексы с шагом 5 и выводим их
for i in range(0, len(tu), 5):
    print(*tu[i:i+5])


ttu = [[i*j for i in range(1, 6)] for j in range(1, 6)]
print_list(ttu)

# склеить матрицу в список
tyy = [x for row in ttu for x in row]
print(tyy)

print(tu == tyy, tu is tyy)
print()

# поменять строки и столбцы в матрице:
A = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 8, 7, 6]]
print_list(A)
print()
# Сначала i принимает значение [0].
# Во вложенном генераторе формируется строка из [0] элементов каждого списка.
A = [[row[i] for row in A] for i in range(len(A[0]))]
print_list(A)


# генератор списка как итерируемый объект
g = [u**2 for u in [x+1 for x in range(5)]]
print(g)


# разбить список на квадратную матрицу N x N
dd = list(map(int, input('digs: ').split()))
N = int(len(dd)**0.5)    # корень квадратный = возведение в степень 0.5
sgf = [dd[i:i+N] for i in range(0, len(dd), N)]
print_list(sgf)



t = ["– Скажи-ка, дядя, ведь не даром",
    "Я Python выучил с каналом",
    "Балакирев что раздавал?",
    "Ведь были ж заданья боевые,",
    "Да, говорят, еще какие!",
    "Недаром помнит вся Россия",
    "Как мы рубили их тогда!"
    ]
lst = [[j for j in i.split() if len(j) > 3] for i in t]
print_list(lst)