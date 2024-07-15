# имя функции (print) - лишь ссылка на объект-функцию, () скобки - оператор ее вызова.
# имя - ссылка на объект-функцию, можно создать еще ссылку на тот же объект (f = print)
# DRY - don't repeat yourself - одинаковые блоки заменяются функцией
# параметр - определение внутри функции в скобках
# аргумент - передаваемое значение при вызове функции
# внутри нужно явно указать, что вернет функция, с помощью return

# f = print
# print = 'it was function print'
# f(print)

def send_mail(from_name, age):
    text = f'Hi, my name is {from_name} and I am {age} years old'
    print(text)
send_mail('Xoxa', 39)


# проверка корректности емейла
# цикл for...else, где else выполняется только если цикл не был прерван break
def dfj(mail):
    symb = '@._qwertyuiopasdfghjklzxcvbnm1234567890'
    if '@' in mail and '.' in mail:
        for i in mail:
            if i not in symb:
                print('НЕТ')
                break
        else:
            print('ДА')
    else:
        print('НЕТ')
dfj(input().lower())