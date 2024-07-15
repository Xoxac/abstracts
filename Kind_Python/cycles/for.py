from random import randint

# ПОМНИ цикл for...else, где else выполняется только если цикл не был прерван break.

# for удобен для перебора итерируемых объектов
lis = [i*2 for i in range(-10, -20, -2)]
p = 1
for i in lis:
    p *= i
print(p)    # произведение всех элементов списка


# найти сумму дробей от 1/2 до 1/n
summ = 0
n = 9
for i in range(2, n+1):
    summ += 1/n
print(summ)

# факториал
n = 10
fact = 1
for i in range(1, n+1):
    fact *= i
print(fact)
print()

# елочка
n = 14
pr = int(n/2 - 1)
stv = int(n/2 - 2)
for i in range(1, n+1, 2):
    print(' '*pr + '*'*i)
    pr -= 1
print(' '*stv + '|_|')


# enumerate при каждой итерации возвращает кортеж (индекс, элемент)
b = [randint(-10, 10) for i in range(1, 10)]
# for i, f in enumerate(b):
    # b[i] = f**2
# print(b)

h = [[1, 4, 6],
     [1, 5, 8],
     [4, 9, 0]]

for i, ij, ijl in h:
    print(i, ij, ijl)

# minimum
u = b[0]
for i in b:
    if i < u:
        u = i
print(b)
print(u)


# вложенные циклы
for i in range(1, 4):
    for j in range (1, 6):
        print(f'i = {i}, j = {j}', end=' ')
    print()


a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
b = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
c = []
for i, row in enumerate(a):
    r = []
    for j, x in enumerate(row):
        r.append(x + b[i][j])
    c.append(r)
print(c)


# заменить все пробелы на дефис
ll = ['sdfge     egr gerg', 'wfwef      wfwetw ee', 'qrq rwq  qwr   rwq']
for i in range(len(ll)):
    st = ll[i].split()
    k = '-'.join(st)
    print(k)


# проверить, не соседствует ли единица с другой единицей по горизонтали, вертикали или диагонали в матрице 5х5
lis = [[1, 0, 1, 0, 0], [0, 0, 1, 1, 1], [0, 0, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 0, 0]]
flag = 1
for i in lis:
    for j in i:
        print(j, end=' ')
    print()
for i in range(4):
    for j in range(4):
        my_sum = lis[i][j] + lis[i][j+1] + lis[i+1][j] + lis[i+1][j+1]
        if my_sum > 1:
            flag = 0
            break
        else:
            my_sum = 0
if flag == 1:
    print('YES')
else:
    print('NO')


# диагональная симметрия
li = [[2, 3, 4, 5, 6],
      [3, 2, 7, 8, 9],
      [4, 7, 2, 0, 4],
      [5, 8, 0, 2, 1],
      [6, 9, 4, 1, 2]]

for i in li:
    for j in i:
        print(j, end=' ')
    print()

# можно так
fl = 0
for i in range(len(li)):
    for j in range(len(li[i])):
        if li[i][j] == li[j][i]:
            fl += 1
print(fl != 0)

# или
lil = [li[1][0], li[2][0], li[2][1], li[3][0], li[3][1], li[3][2], li[4][0], li[4][1], li[4][2], li[4][3]]
lir = [li[0][1], li[0][2], li[1][2], li[0][3], li[1][3], li[2][3], li[0][4], li[1][4], li[2][4], li[3][4]]
print(lil)
print(lir)
print(lil == lir)


# сортировка выбором
lll = [9, 7, 6, 8]
for i in range(len(lll)):
    min_index = i
    for j in range(i + 1, len(lll)):
      if lll[j] < lll[min_index]:
        min_index = j
    lll[i], lll[min_index] = lll[min_index], lll[i]
print(lll)


# наименьшее количество купюр достоинством в 1, 2, 4, 8, 16, 32 и 64, которым можно выплатить сумму n
n = 3523542
s64 = 0
cup = [1, 2, 4, 8, 16, 32, 64]
rcup = list(reversed(cup))
lk = []
for i in rcup:
    if n%i == 0:
        lk.append(n // i)
        break
    else:
        lk.append(n // i)
        n = n%i
print(lk)

