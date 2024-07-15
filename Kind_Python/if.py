# a, b, c, d = list(map(int, input().split()))
#
# biggest_otk = max(c, d)
# biggest_konv = max(a, b)
# smallest_otk = min(c, d)
# smallest_konv = min(a, b)
#
#
# if biggest_otk+2 <= biggest_konv and smallest_otk+2 <= smallest_konv:
#     print("ДА")
# else:
#     print("НЕТ")

# обычный if не возвращает значений, а выполняет блок кода по условию.
# тернарный if возвращает значение.
a, b = 4, 3
res = a*2 if a > b else b
print(res)
l = [1, 2, a if a > b else b, 3, 4]
print(max(l))
print('a - ' + ('chetnoe' if a%2==0 else 'nechetnoe') + ' chislo')

t = int(input())
print(t + 1 if t in range(59) else 0)




