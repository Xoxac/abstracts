# sep - разделитель, по умолчанию пробел
print(1, 2, 3, sep=" | ")

# end - конец строки, по умолчанию \n
print("Hello", end=" ")
print("World!")

# eval - вместо приведения к нужному типу
print(abs(eval(input('abs - ins one digit: '))))

# split() строки по пробелу
a, b = map(float, input("summa - ins two digits: ").split())
print(f'summa: {a+b}')

a = 7
b = -4
c = 3
print(a, b, c, sep="\n")



