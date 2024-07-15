def get_v(a, b, c, d=True):   # d - формальный параметр, можно не указывать при вызове
    if d:                     # a b c - фактические параметры, указывать обязательно
        print(f'a = {a}, b = {b}, c = {c}')
    return a * b * c

# get_v(1, 2, 3)  # позиционные аргументы
# get_v(b=1, c=2, a=3, d=False)    # именованные аргументы
# get_v(1, c=2, b=3)  # позиционные и именованные аргументы (позиционные всегда сначала)


# формальные параметры: при сравнении строк не учитывается регистр и отбрасываются пробелы
def srav_str(s1, s2, reg=False, trim=True):
    if reg:
        s1 = s1.lower()
        s2 = s2.lower()
    if trim:
        s1 = s1.strip()
        s2 = s2.strip()
    return s1 == s2

print(srav_str('python ', ' Python'))
print(srav_str('python ', ' Python', reg=True))
print(srav_str('python ', ' Python', trim=False))



def check_password(passw, chars="$%!?@#"):
    return bool(set(passw) & set(chars)) and len(passw) >= 8


# расстановка тегов
def tegs (st, tag='h1', up=True):
    if up:
        tag = tag.upper()
    else:
        tag = tag.lower()
    return f'<{tag}>{st}</{tag}>'
imm = input()
print(tegs(imm, 'div'))
print(tegs(imm, "div", False))