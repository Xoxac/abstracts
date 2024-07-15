# кортежи неизменяемы, но изменяемые типы данных внутри кортежа можно менять

tu1 = 1, 2, 3
tu2 = (4, 5, 6)*2    # вернет не кортеж с кортежами, а кортеж с повторениями
print(tu1, tu2)

a, b = (1), (1,)
print(type(a), type(b))

a, b = (1, 2)
print(a, b)
a, b = 'ra'
print(a, b)

print(len(tu1))
print(tu1[0:2])

# кортеж можно использовать как ключ словаря
d = {}
d[tu1] = 'tuple'
print(d)

# занимают меньше памяти
l = [1, 2, 3]
print(l.__sizeof__(), tu1.__sizeof__())

# объединить кортежи
tu3 = tu1 + tu2
print(tu3)

# кортеж можно сделать из любого итерируемого объекта
a = tuple([6, 6, 6])
b = tuple('hello Python')

print(b.count('l'))
print(b.index('o'))    # index(что, от какого элемента, до какого)
print('P' in b)


# выкинуть элемент кортежа, не превращая его в список
# i = tuple(input().split())
hh = ('Воронеж', 'Самара', 'Тольятти', 'Ульяновск', 'Пермь')
if 'Ульяновск' in hh:
    n = hh.index('Ульяновск')
    f = hh[0:n] + hh[n+1:]
    print(*f)
else:
    print(*hh)


# отбрасываем столбцы и строки
t = ((1, 0, 0, 0, 0),
     (0, 1, 0, 0, 0),
     (0, 0, 1, 0, 0),
     (0, 0, 0, 1, 0),
     (0, 0, 0, 0, 1))
n = int(input('dig: '))
ll = [[i for i in j] for j in t]
ll = ll[:n]
for i in range(len(ll)):
    ll[i] = ll[i][:n]
for i in ll:
    print(*i)


