from defs import prin

matrix = [
    [1, 2],
    [3, 4],
    [5, 6]
]

for row in matrix:
   for element in row:
       print(element, end = " ")
   print()

print(matrix[1][1])

for i in range(len(matrix)):
   for j in range(len(matrix[i])):
       print(matrix[i][j], end = " ")
   print()

print()
print()

print("TASK")
# Дана двумерная матрица 3x3 (двумерный массив).
# Необходимо определить максимум и минимум каждой строки, а также их индексы.

matrix = [
   [9, 2, 1],
   [2, 5, 3],
   [4, 8, 5]
]

for rows in matrix:
    ma = max(rows)
    mi = min(rows)
    print("max: ", rows.index(ma), "min: ", rows.index(mi))

prin("ЗАДАНИЕ 3.8.1")

# Напишите цикл, который ищет наибольший элемент в матрице

matrix = [[1, 2, 3],
          [7, -1, 2],
          [4, 8, 7],
          [123, 2, -1]]
lis = list()

for i in matrix:
    lis += i
print(max(lis))

prin("Задание 3.8.2")

# Напишите код, который определяет, является ли матрица квадратной
# (то есть количество строк равно количеству столбцов).
# В конце программа должна выводить на экран значение True или False
# в зависимости от заданной матрицы

rows = len(matrix[0])
elems = len(matrix)
print ("True") if rows == elems else print("False")

