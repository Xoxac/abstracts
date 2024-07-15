s1 = ' I love '
s2 = 'Python'
s3 = 'Abracadabra'

print((s1 + ' ' + s2) * 3)
print(len(s1))
print('a' in s1)
print(s1 != 'I love')
print('cat' > 'cax') # False так как t < x (идет раньше по таблице кодировки)
print(ord('s'), ord('S')) # коды - номера символов в таблице
print("Сергей\nБалакирев")
print(s1[2], s1[1:3], s2[1:5:2], s2[::-1], s2[:4])
print('panda'[2:4])
print(s1 + s2[2::])

# a, b = input().split() # даст 2 строки, а = input().split() даст список с двумя строками!

print(s1.upper())
print(s3.count('ra', 2, 10)) # аргументами можно указать индексы, с какого по какой искать
print(s3.find('br', 2, 10)) # вернет индекс символа. .rfind - поиск справа налево
print(s3.index('br')) # то же самое, но вернет ошибку если не найдет
print(s3.replace('ra', 'f'))
print(s3.isalpha(), s1.isalpha(), s2.isdigit())
print(s2.rjust(10, '0')) # добавляет символы-заполнители до нужной длинны
print(s1.split()) # вернет список строк
print(" | ".join(['1', '2', '3'])) # соединит строки списка в строку
print(s1.strip()) # удалит все пробелы и переносы строк справа и слева (rstrip справа, lstrip слева)

# -- спецсимволы --
# знак \ это маркер начала спецсимвола (\n, \\, \", \t...) если комбинация существует
print("\tI love\n\tPythonn\b")

# экранировать спецсимвол можно, поставив еще один \
# экранировать все спецсимволы можно поставив r перед строкой
print("\\tI love\\n\\tPythonn\\b")
print(r"\tI love\n\tPythonn\b")


# -- форматирование --
print(f'Stroka "{s1.strip()}" with "{s3}"')
print('Stroka "{str1}" with "{str2}"'.format(str1=s1.strip(), str2=s3))

a = map(str, sorted(map(int, input('insert digs: ').split())))
b = " ".join(a)
print(f'{b}')


# -- ввод через sys --
import sys
print("Enter some lines of text (press Ctrl+D to end input): ")
lines = sys.stdin.readlines()
print("You entered: ")
for line in lines:
    print(line.strip())

