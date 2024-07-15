# ЗНАЧЕНИЕ if УСЛОВИЕ else ЗНАЧЕНИЕ for ПЕРЕМЕННАЯ in ДИАПАЗОН if УСЛОВИЕ

A=tuple(k for k in range(1,21) if k%3!=0)
print(A)

B=[2**(k//2) if k%2==0 else 3**(k//2) for k in range(15)]
print(B)

C=[0 if k==0 or k==1 else k**2 for k in range(13) if not k in [2,5,7]]
print(C)

Alpha=A[::-1] # кортеж в обратном порядке
print(Alpha)

Bravo=B[::2] # элементы через один с первого
print(Bravo)

Charlie=B[1::2] # элементы через один со второго
print(Charlie)

# ресурсосберегающий генератор через YIELD (поддерживает только ОДИН ОБХОД):
# обычный генератор:
a = [x**2 for x in range(10)]
print(type(a))
print(a)
# ресурсосберегающий генератор:
b = (x**2 for x in range(10))
print(b)
print(next(b))
print(next(b))
print(next(b))
# ресурсосберегающий генератор через YIELD:
def gen(nums):
    for i in nums:
        yield i**2
c = gen([1, 2, 3, 4, 5])
print(c)
print(next(c))
print(next(c))
print(next(c))

