# Функция уникальна тем, что возвращает в качестве результата значение выражения,
# переданного ей в виде текстовой строки. Другими # словами, если имеется некоторая текстовая строка,
# в которую «спрятана» команда, имеющая смысл в языке Python, то, передав эту текстовую
# строку функции eval(), мы получим в результате значение выражения, «спрятанного» в строке.

txt = "(2+3)/0.25-4*2.1"
print(txt, "=", eval(txt))
res = input("insert digits and * ** / + - : ")
print("your answer: ", eval(res))

# можно присвоить значения переменным прямо из строки:
a, b=eval(input("введите через запятую два числа: "))
print(type(a))
print(a, b)