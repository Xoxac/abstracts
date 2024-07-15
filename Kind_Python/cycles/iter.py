from random import randint


lis = [randint(-10, 10) for i in range(10)]
print(lis)

print('-'*30)

it = iter(lis)    # it стал итератором для перебора итерируемого объекта
print(next(it))
print(next(it))

print('-'*30)

r = range(5)
it = iter(r)
print(next(it))
print(next(it))

# оператор for неявно вызывает итератор и завершает работу, получая ошибку StopIteration



