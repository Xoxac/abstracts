# IF
number=int(input("insert number: "))
if number%2==0:
    print("chetnoe.")
else:
    print("nechetnoe.")

res="this number is  "
txt=input("ins name of digit: ")
txt=txt.lower()
if txt=="one" or txt=="ein":
    res+="1"
elif txt=="two" or txt=="zwei":
    res+="2"
elif txt=="three" or txt=="drei":
    res+="3"
else:
    res+="not found"
print(res)

# ТЕРНАРНЫЙ ОПЕРАТОР
# ЗНАЧЕНИЕ if УСЛОВИЕ else ЗНАЧЕНИЕ
# по сравнению с условным оператором тернарный оператор возвращает результат.
# Другими словами, вся описанная выше конструкция имеет значение, и это значение,
# например, может быть присвоено переменной. Сначала проверяется УСЛОВИЕ,
# указанное после ключевого слова if. Если УСЛОВИЕ истинно, то резуль-
# татом всего выражения является ЗНАЧЕНИЕ, указанное перед ключевым
# словом if. Если УСЛОВИЕ окажется ложным, то результатом всего выра-
# жения будет ЗНАЧЕНИЕ, указанное после ключевого слова else.

num=int(input("ins number: "))
res="chet" if num%2==0 else "nechet"
print("this is ", res, " number")

# выводит первую и последнюю буквы, если введен текст, и сам объект и его тип если не текст
val=eval(input("введите выражение: "))
a, b=val[0], val[-1] if type(val)==str else (val, type(val))
print(a)
print(b)




# Напишите программу, в которой проверяется, делится ли введенное
# пользователем число на 3. Учесть, что если число делится на 3, то оста-
# ток от деления этого числа на 3 равен нулю.
p=int(input("ins: "))
if p%3==0:
    print("yes")
else:
    print("no")

# Напишите программу, в которой вычисляется факториал числа. Фак-
# ториалом n! числа n называется произведение всех чисел от единицы
# до этого числа: n! = 1 x 2 x 3 x … x n. Число, для которого вычисляется фак-
# ториал, вводится пользователем с клавиатуры. В программе должна вы-
# полняться проверка того, что пользователь ввел положительное число
# (используйте условный оператор).

yd = int(input("ins: "))
ft = 1
if yd>=0:
    ll = [i for i in range(1, yd+1)]
    for num in ll:
        ft *= num # то же, что ft = ft * num

print(ll)
print(ft)

# Напишите программу, в которой отображаются числа из последова-
# тельности Фибоначчи. Первые два числа в последовательности равны
# единице, а каждое следующее равно сумме двух предыдущих значений
# (то есть речь о числах 1, 1, 2, 3, 5, 8, 13, 21, 34, 55 и так далее). Количество
# чисел в последовательности вводится с клавиатуры.

ch = int(input("kol-vo chisel: "))
fib = [1, 1]
for i in range(ch):
    fib.append(fib[i]+fib[i+1])
print(fib)



# print(('t' in "python") or ('t' in "django"))
# # True
#
# # можно проверить, находится ли число 1 в промежутке (0,4)
# cond1 = 0 < 1
# cond2 = 1 < 4
# print(cond1 and cond2)
# # True
#
# # Сравнение строк
# # Цифра меньше буквы:
# # '2' < 'a'
# # True
# # 'b' < '0'
# # False
# # Из двух цифр меньше та, что обозначает меньшее число:
# # '1' < '2'
# # True
# # '5' < '2'
# # False
# # Латинские буквы меньше кириллицы:
# # 'f' < 'ф'
# # True
# # 'л' < 'l'
# # False
# # Заглавная буквы меньше строчной:
# # 'Q' < 'q'
# # True
# # 'r' < 'R'
# # False
# # Из двух букв одного регистра меньше та, что раньше по алфавиту:
# # 'a' < 'b'
# # True
# # 'Я' < 'Ч'
# # False
# # Если первые символы у обеих строк равны, сравнение происходит по второму символу и так далее.
#
# n = input("N   ")
# print(type(n))
# print("3" and "7" in n)
#
# # Эквивалентные объекты всегда равны, но равные объекты не всегда эквивалентны.
# a = [1, 2, 3]
# b = [1, 2, 3]
# print(a == b)  # True
# print(a is b)  # False

# Задание 3.2.2 Дано n-значное целое число N. Определите, начинается ли оно с чётной цифры.
# n = list(map(int, (input("N   "))))
# print(n[0] % 2 == 0)

# list_1 = [1, 2]
#
# list_2 = [1, 2, 3]
# val = list_2.pop()
#
# print(list_1 == list_2)

# is_rainy = True  # дождь будет
#
# if is_rainy:
#     print("Брать зонт")
# else:
#     print("Не брать зонт")

# name = input("Введите название на этикетке  ")
# if name == "Арорат":
#     print("fake!")
# else:
#     print("not fake")

# bud = 2500
# cost = int(input("price is  "))
# if cost <= bud:
#     print("OK")
# else:
#     print("NO")

# Если в условном операторе вы не используете логический оператор или оператор сравнения,
# то интерпретатор приведёт переменную к bool — то есть произведёт неявное приведение типов за вас — и проверит её значение.
# int	Любое целое число отличное от нуля
# Например: -5, 10	0
# float	Любое число с плавающей запятой, отличное от нуля
# Например: -0.6, 45.5	0.0
# str	Любая непустая строка
# Например: "String"	""
# list	Любой не пустой список
# Например: [1, 2, 3]	[]
# dict	Любой не пустой словарь
# Например: {"one": 1, "two": 2}	{}
# NoneType	—	None
# Если мы абсолютно точно знаем, что приходит на вход, то можно пользоваться знаниями выше.
# Если такой уверенности нет, лучше проводить преобразование явно.
# if pozitive_num:  # нет смысла проверять len(pozitive_num)
#    # если список не пустой печатаем его
#    print("Список положительных чисел равен: ", pozitive_num)
# else:
#    # печатаем, если список оказался пустым
#    print("Список положительных чисел пустой")
# # Хорошо
# if greeting:
#
# # Плохо
# if greeting == True:
#
# # Совсем неправильно
# if greeting is True:

# ТЕРНАРНЫЙ ОПЕРАТОР
# a, b = 1, 2
# min = a if a < b else b
# print(min) # 1

# Запишите условие проверки целого числа А: является ли оно кратным двум или трём?
# a = int(input("digit  "))
# if a % 2 == 0:
#     print("chetnoe")
# elif a % 3 == 0:
#     print("kratno 3")
# else:
#     print("ne kratno")

# one = 12
# two = 30
# result = one % 2 == 0 and two % 2 == 0 # OR print((one % 2 == 0) and (two % 2 == 0))
# print(result)

# Нам нужно написать программу, с помощью которой можно определить, является ли данное время суток утром,
# и вывести соответствующее сообщение. Утром считается временной промежуток с 6:00 (включительно) до 12:00 (не включительно).
# hour = int(input())
# if 6 <= hour < 12:
#     print("Утро!!!")

# Напишите программу, которая бы принимала на вход номер месяца, определяла сезон и выводила сообщение в зависимости от номера месяца:
# «Весна» для 3, 4, 5 месяцев;
# «Лето» для 6, 7, 8 месяцев;
# «Осень» для 9, 10, 11 месяцев;
# «Зима» для 12, 1, 2 месяцев.
# mes = int(input("mesec   "))
# if mes == 3 or 4 or 5:
#     print("spring")
# elif mes == 6 or 7 or 8:
#     print("summer")
# elif mes == 9 or 10 or 11:
#     print("summer")
# elif mes == 12 or 1 or 2:
#     print("winter")
# else:
#     print("choose 1...12")
# хорошо
# month in [3, 4, 5]
# плохо
# month == 3 or month == 4 or month == 5
# month = int(input())
#
# if month in [3, 4, 5]:
#     print("Весна")
# elif month in [6, 7, 8]:
#     print("Лето")
# elif month in [9, 10, 11]:
#     print("Осень")
# elif month in [12, 1, 2]:
#     print("Зима")


# Запишите условие, которое является истинным, когда только одно из чисел А, В и С меньше 45.
# (A < 45 and B >= 45 and C >= 45) or (A >= 45 and B < 45 and C >= 45) or (A >= 45 and B >= 45 and C < 45)

# Дано натуральное восьмизначное число. Выясните, является ли оно палиндромом (читается одинаково слева направо и справа налево).
# a = list(input("insert 8-digits number  "))
# if a[0] == a[7] and a[1] == a[6] and a[2] == a[5] and a[3] == a[4]: #OR if a == a[::-1]
#     print("palindrom")
# else:
#     print("not palindrom")

# # ИТОГОВОЕ ПРАКТИЧЕСКОЕ ЗАДАНИЕ
# import webbrowser
# # На основе предложенной схемы составьте код, который будет печатать, что необходимо надеть, в зависимости от погодных условий.
# url = "https://lms-cdn.skillfactory.ru/assets/courseware/v1/252e593ab0eaee18c0fdd71fa4a62333/asset-v1:SkillFactory+FPW-2.0+27AUG2020+type@asset+block/FPW-2.0_B3.5_1.jpeg"
# webbrowser.open(url)
# futshordozh = "https://lookastic.ru/%D0%BC%D1%83%D0%B6%D1%81%D0%BA%D0%B0%D1%8F-%D0%BC%D0%BE%D0%B4%D0%B0/%D0%BA%D0%B0%D0%BA-%D0%BD%D0%BE%D1%81%D0%B8%D1%82%D1%8C/%D0%B4%D0%BE%D0%B6%D0%B4%D0%B5%D0%B2%D0%B8%D0%BA-%D1%84%D1%83%D1%82%D0%B1%D0%BE%D0%BB%D0%BA%D0%B0-%D1%81-%D0%BA%D1%80%D1%83%D0%B3%D0%BB%D1%8B%D0%BC-%D0%B2%D1%8B%D1%80%D0%B5%D0%B7%D0%BE%D0%BC-%D1%88%D0%BE%D1%80%D1%82%D1%8B/48879"
# temperature = int(input("insert temperature:  "))
# isRain = input("rain if any: hard / light  ")
# if 20 <= temperature <= 30 and isRain:
#     print("futbolka, shorti i dozhdevik")
#     webbrowser.open(futshordozh)
# elif 20 <= temperature <= 30 and not isRain:
#     print("futbolka i shorti")
# else:
#     if 0 <= temperature:
#         if not isRain:
#             print("palto")
#         elif isRain == "hard":
#             print("palto, sapogi i zont")
#         else:
#             print("palto i dozhdevik")
#     else:
#         print ("puhovik")
