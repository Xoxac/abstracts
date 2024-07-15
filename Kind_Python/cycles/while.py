# -- WHILE --
# строгие операторы < > = работают быстрее, чем <= >=

s = 0
i = 1
n = 1000
while i <= n and i <= 50:
    s += i
    i += 1
print(s)

# -- проверка пароля
# pass_true = 'password'
# ps = ''
# while ps != pass_true:
#     print('access denied')
#     ps = input('ins yor pass: ')
# print('access allowed')

# -- квадраты чисел от n до m
# n, m = list(map(int, (input().split())))
# d = 0
# sq = []
# while n <= m:
#     d = n**2
#     sq.append(d)
#     n += 1
# print(*sq)


# -- заменить много тире подряд на одно
# st = input('str: ')
# while st.count('--') != 0:
#     st = st.replace('--', '-')
# print(st)


# -- перемножить цифры строки
# d = list(map(int, list(input())))
# cou = 1
# pr = 1
# while cou <= len(d):
#     pr = pr*d[cou-1]
#     cou += 1
# print(pr)


# -- fibonacci
# n = int(input('dig: '))
# fib = [1, 1]
# c = 1
# while len(fib) < n:
#     fib.append(fib[c-1]+fib[c])
#     c += 1
# print(fib)


# while в while+break = if
# n, m = list(map(int, input().split()))
# cou = n
# lis = []
# while n < m:
#     while n%2 != 0:
#         lis.append(n)
#         break
#     n += 1
# print(*lis)


# -- break заканчивает цикл, continue пропускает одну итерацию
# например, программа суммирует нечетные значения, пока пользователь не введет 0.
# continue пропускает то, что в теле цикла стоит ниже continue и возвращается на начало цикла.
# s = 0
# d = 1
# while d != 0:
#     d = int(input('dig: '))
#     if d % 2 == 0:
#         continue
#     s += d
#     print('s = ' + str(s))


# -- блок в else после тела цикла выполняется после штатного завершения цикла while
s = 0
i = -10
while i < 100:
    if i == 0:
        break    # По break - нештатное прерывание
    s += 1/i
    i += 1
else:
    print('summa calculated correctly')
print(s)



