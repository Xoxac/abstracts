person = {} # с помощью фигурных скобок можно создать словарь

# словарь заполняется по принципу - ключ:объект (через двоеточие)
person = {'name' : 'Ivan Petrov', 'age' : 26}

# в него можно также добавлять новые объекты по ключу
person['age'] = 25    # person['age'] - значение по ключу age
person['email'] = 'ivan_petrov@example.com'
person['phone'] = '8(800)555-35-35'

print(person)
print(person['name'])
print(person.keys())
print(person.values())
print("||".join(person.keys()))

# Из словаря аналогично спискам можно удалить объект по его ключу.
# Словарь является упорядоченным.
# В функцию pop() всегда нужно передавать ключ удаляемого объекта:
person.pop('phone')
print(person)

# Задание 2.5.11

# Напишите программу, которая получает на вход название книги - title,
# фамилию автора - author и год выпуска - year.

# Полученные данные должны быть преобразованы в словарь book с ключами:
# title, author, year. Причем year нужно преобразовать в тип int.

book = {}
book["title"] = input(" insert title  ")
book["author"] = input(" insert author  ")
book["year"] = int(input(" insert issue year  "))
print(book)
print(book["year"])

# OR
# title = input(" insert title  ")
# author = input(" insert author  ")
# year = int(input(" insert issue year  "))
# book = {"title": title, "author": author, "year": int(year)}


abit1 = {"ФИО" : 'Фадеев О.Е.', "Количество баллов" : 283, "Заявление" : True}
abit2 = {"ФИО" : 'Дружинин И.Я.', "Количество баллов" : 278, "Заявление" : False}
abit3 = {"ФИО" : 'Афанасьев Д.Н.', "Количество баллов" : 276, "Заявление" : True}

abits = [abit1, abit2, abit3]

print(abits)

abit4 = {"ФИО" : 'Любимчиков А.Я.', "Количество баллов" : 269, "Заявление" : True}

abits.append(abit4)

print(abits)