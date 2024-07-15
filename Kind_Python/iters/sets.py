# множества - изменяемые неупорядоченные коллекции уникальных элементов
# элементы - только неизменяемые типы и не другие множества
# обратиться к элементу по индексу невозможно
# множества равны, если имеют одинаковое количество одинаковых элементов, неважно, в каком порядке
# сравнение равенств < и > возможно, если все элементы одного присутствуют в другом


a = {1, 2, 3, 'hello', 2, 3}
print(a, type(a))

a = set([1, 2, 3, 4, 3, 2])
print(a)
a = set('abracadabra')
print(a)
a = set(range(7))
print(a)

a.add(8)
print(a)
a.update(['df', 'dfa'])  # можно добавить любой итерируемый объект
print(a)

a.discard('df')  # a.remove() вернет ошибку, если элемента нет, а a.discard не вернет
print(a)

print(a.pop())  # вернет случайный элемент и удалит его из множества
a.clear()

# выбрать все уникальные цифры из введенной строки
# ss = set(input())
ss = 'Python 3.9.11 - best language!'
ld = set(map(str, [i for i in range(10)]))
ns = []
for i in ss:
    if i in ld:
        ns.append(i)
ans = set(ns)
print(*ans)

# пересечение множеств вернет множество совпадающих элементов
# с перезаписыванием первого множества: seta &= setb
seta = {1, 2, 3, 4}
setb = {3, 4, 5, 6, 7}

setc = seta & setb
print(setc)
# или
print(seta.intersection(setb))

# объединение множеств
# с перезаписыванием первого множества: seta |= setb
setc = seta | setb
print(setc)
# или
print(seta.union(setb))

# вычитание - из первого множества удаляются элементы, встречающиеся во втором. Второе никуда не идет
print(seta - setb, setb - seta)

# симметричная разность - возвращает несовпадающие элементы
print(seta ^ setb)

# список в множество путем генератора
d = [1, 2, '1', '2', -4, 3, 4]
ax = {int(x) for x in d if int(x) > 0}
print(ax)

inm = input('ins strs: ').lower().split()
nm = {i for i in inm if len(i) >= 3}
print(len(nm))


# список книг каждого автора
lst_in = ['Пушкин: Сказка о рыбаке и рыбке',
          'Есенин: Письмо к женщине',
          'Тургенев: Муму',
          'Пушкин: Евгений Онегин',
          'Есенин: Русь']
tmp = [i.split(':') for i in lst_in]
d = {}
# Переменная j на каждой итерации будет списком, содержащим два элемента: имя автора и название произведения
for j in tmp:
    # Если автор (первый элемент списка j) еще не существует в словаре d, создается новая запись, где ключом будет имя автора, а значением — множество с одним элементом (название произведения)
    if j[0] not in d:
        d[j[0]] = {j[1]}
    d[j[0]].add(j[1])
print(d)
