colors = 'redgreenblue'
colors_split = colors.split('e') # список цветов по отдельности

colors_joined = ' and '.join(colors_split) # объединение строк
print(colors_joined) # r and dgr and  and nblu and

print(colors.isdigit()) # строка состоит из цифр?
# False
print(colors.isalpha()) # строка состоит из букв?
# False
print(colors.isalnum()) # строка состоит из цифр и букв?
# False

print(colors.upper()) # REDGREENBLUE

print(colors[-2:2:-1]) # [START:STOP:STEP]

print(len(colors))

print(colors.find('e')) # возвращает индекс

L = ['THIS', 'IS', 'LOWER', 'STRING']
print(list(map(str.lower, L)))

# 2.4.1

# Задана переменная numbers, которая ссылается на некоторую строку,
# состоящую из чисел и пробелов. Пример такой строки:
# numbers = '1 2 3 4 5 6 7'
#Напишите программу, которая каждое число из строки numbers, выводит построчно.

numbers = '1 2 3 4 5 6 7'
num_split = numbers.split()
print("\n".join(num_split))

# Форматирование строк

age = 25
my_age = "I'm %d years old" % (age) # в шаблоне присутствует специальный символ %d
print(my_age)
# Мы создали строковую переменную,
# в середину которой поместили число без необходимости разбивать строки на
# несколько и потом склеивать их. Чтобы это сделать, в шаблоне строки
# необходимо указывать место и тип объекта, который нужно поместить на это место,
# помещая специальный символ %d. Он указывает, что на этом месте
# должно стоять целое число (digit).
# %d, %i Целое число, %f Число с плавающей точкой

pi = 31.4159265
print("%.4e" % (pi))

l = [12,3,456,78]
n = str(l)
n = n.replace("]", '')
n = n.replace("[", '')
n = n.replace(",", '')
n = n.replace(" ", '')
n = int(n)
print(type(n))