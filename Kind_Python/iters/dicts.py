# ключом может быть любой неизменяемый тип данных
# значением - любой тип данных
# топ вариант
dic = {'house': 'дом',
       'tree': 'дерево',
       'road': 'дорога'}
print(dic['tree'])

# ключи - только строки без кавычек, символы разрешенные в переменных
dic2 = dict(one=1, two=2, tre=3)
print(dic2['two'])

# список в словарь
lst = ['+7', '+6', '+5', '+4']
ad = dict.fromkeys(lst, 'country code')
print(ad)

# генератор словаря с нуля, из кортежа, из другого словаря
squares = {x: x ** 2 for x in range(1, 11) if x % 2 == 0}

tuples_list = [('one', 1), ('two', 2), ('three', 3)]
dict_comprehension = {k: v for k, v in tuples_list}

original_dict = {'a': 1, 'b': 2, 'c': 3}
modified_dict = {k: v + 10 for k, v in original_dict.items()}

# список списков в словарь
lst = [[2, 'bad'], [3, 'mid'], [4, 'good']]
print(dict(lst))

oc = '1 говно неудовлетворительно удовлетворительно хорошо отлично'.split()
n = int(oc.pop(0))
print(n)
dd = {key+n: value for key, value in enumerate(oc)}
print(dd[4])

inm = 'И что сказать и что сказать и нечего и точка'.lower().split()
nm = {i: inm.count(i) for i in inm}
if 'и' in nm:
    print(nm['и'])
else:
    print('0')


# добавление, перезапись, удаление значения по ключу
dic['sun'] = 'солнце'
dic[False] = 'ложь'
dic['road'] = ['e95', 'm1']
del dic['tree']
print(dic)

# Проверить, есть ли ключ
print('sun' in dic)
print('road' not in dic)

# сложная строка в словарь
i = 'one=1 two=2 three=3'.split()  # => ['one=1', 'two=2', 'three=3']
k = [z.split('=') for z in i]  # => [['one', '1'], ['two', '2'], ['three', '3']]
for v in range(len(k)):
    k[v][1] = int(k[v][1])  # => [['one', 1], ['two', 2], ['three', 3]
d = dict(k)  # => {'one': 1, 'two': 2, 'three': 3}

ff = '1=one 2=two 3=three'.split()  # => ['one=1', 'two=2', 'three=3']
dd = [z.split('=') for z in ff]  # => [['one', '1'], ['two', '2'], ['three', '3']]
dig = {int(a): b for a, b in dd}  # => {1: 'one', 2: 'two', 3: 'three'}

nu = '+71234567890 +71234567854 +61234576890 +52134567890 +21235777890 +21234567110 +71232267890'.split()
dih = {}
sem, shes, pet, dva = [[] for i in range(4)]
for i in nu:
    if i[1] == '7':
        sem.append(i)
        dih['+7'] = sem
    elif i[1] == '6':
        shes.append(i)
        dih['+6'] = shes
    elif i[1] == '5':
        pet.append(i)
        dih['+5'] = pet
    elif i[1] == '2':
        dva.append(i)
        dih['+2'] = dva
print(*sorted(dih.items()), sep='\n')

names = '+71234567890 Сергей +71234567810 Сергей +51234567890 Михаил +72134567890 Николай'.split('+')
names.pop(0)
dfg = [i.split() for i in names]
for i in dfg:
    i[0] = f'+{i[0]}'
print(dfg)
dij = {a: b for a, b in dfg}
serg, mixa, nik = [[] for i in range(3)]
dico = {}
for i in dij:
    if dij[i] == 'Сергей':
        serg.append(i)
        dico['Сергей'] = serg
    elif dij[i] == 'Михаил':
        mixa.append(i)
        dico['Михаил'] = mixa
    elif dij[i] == 'Николай':
        nik.append(i)
        dico['Николай'] = nik
print(dico)

# кэширование данных
# при повторном вводе того же самого числа результат не вычислялся,
# а бралось ранее вычисленное значение из словаря
dii = {}
while True:
    i = int(input("dig, 0 = finish: "))
    if i == 0:
        print('program finished')
        break
    if i not in dii:
        print(round(i ** 0.5, 2))
        dii[i] = round(i ** 0.5, 2)
    else:
        print(f'значение из кеша: {dii[i]}')

# -- методы --
add = ad.copy()  # то же самое, что add = dict(ad)
ad.clear()
add.get('+7')  # По ключу +7 вернет country code. В отл от add['+7'] не вернет ошибку, если ключ не существует
add.setdefault('+7')  # если ключ существует, вернет как add.get()
add.setdefault('666')  # если не существует, запишет 666: None
add.setdefault('666', 'Satan')  # если не существует, запишет 666: 'Satan'
add.pop('+7')  # несуществующий - ошибка
add.pop('+7', False)  # несуществующий - вернет False
add.popitem()  # удаляет последнюю пару
add.keys()  # вернет список ключей
add.values()  # вернет список значений
add.items()  # вернет список кортежей ключ - значение
add.update(
    dico)  # обновит словарь add значениями словаря dico: добавит несуществующие пары, по существующим ключам заменит значения
d3 = {**add, **dic}  # объединение словарей, то же самое что add | dic
# add.fromkeys()    # формирует словарь с ключами, указанными в списке

# вывести ключи и значения
for key, value in add.items():
    print(key, value)


# морзянка
morze = {'а': '.-',
         'б': '-...',
         'в': '.--',
         'г': '--.',
         'д': '-..',
         'е': '.',
         'ё': '.',
         'ж': '...-',
         'з': '--..',
         'и': '..',
         'й': '.---',
         'к': '-.-',
         'л': '.-..',
         'м': '--',
         'н': '-.',
         'о': '---',
         'п': '.--.',
         'р': '.-.',
         'с': '...',
         'т': '-',
         'у': '..-',
         'ф': '..-.',
         'х': '....',
         'ц': '-.-.',
         'ч': '---.',
         'ш': '----',
         'щ': '--.-',
         'ъ': '--.--',
         'ы': '-.--',
         'ь': '-..-',
         'э': '..-..',
         'ю': '..--',
         'я': '.-.-',
         ' ': '-...-'}
inp = list(input('введите текст для перевода в морзянку: ').lower())
otv = []
for i in inp:
    otv.append(morze[i])
print(*otv)

inp = input('введите морзянку: ').split()
print(inp)
otv = []
for i in inp:
    for key, val in morze.items():
        if i == val:
            otv.append(key)
print(*otv)



# люто сложный генератор
def len_st(d):
    return d, len(d)
cities = input('cities: ').split()
d = {s: s_len for s, s_len in (len_st(s) for s in cities)}
print(d)


# транслитератор
t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}
def trans(st, sep='-'):
    words = st.lower().split()
    result = []
    for word in words:
        trans_word = ''.join(t.get(char, char) for char in word)
        result.append(trans_word)
    return sep.join(result)
inn = input()
print(trans(inn))
print(trans(inn, sep='+'))
# t.get(char, char) - Метод get у словаря имеет следующий синтаксис:
# key - ключ, значение которого нужно получить. default - значение, которое возвращается,
# если ключ не найден в словаре. Если default не указан, по умолчанию возвращается None.
# Если char присутствует в словаре t, метод возвращает значение, соответствующее этому ключу
# (например, для char = 'а' вернется 'a'). Если char отсутствует в словаре t, метод
# возвращает сам char (например, для символа 'f', который отсутствует в словаре t, вернется 'f').
