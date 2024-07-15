from defs import prin

# *lis буквально 1, 3, 5, 7
# def f(*args):
#     for i in args:
#         print(i)
#
# f(*lis)

def ret(arg: int):
    st = str(arg)
    lis = [a for a in st]
    return lis[::-1]

print(ret(245))


def w():
    a = 0
    while True:
        a+=1
        yield a

for i in w():
    print(i)
    