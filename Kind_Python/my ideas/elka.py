# елочка
from random import randint, shuffle
from colorama import Fore, Style
import os
from time import sleep

'''елка с лампочками, меняющимися каждую 0.3 секунды.
запускать В ТЕРМИНАЛЕ чтобы было красиво'''


def elka(n):
    global stv
    row = []
    pr = int(n / 2 - 1)
    stv = int(n / 2 - 2)
    for i in range(1, n + 1, 2):
        row.append(' ' * pr + '*' * i)
        pr -= 1
    return row


def ukr(elka):
    colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.BLUE]
    shuffle(colors)
    for i in range(len(elka)):
        lisi = list(elka[i])
        for j in range(len(elka[i])):
            if elka[i][j] == '*':
                if randint(1, 7) == 1:
                    rand = randint(0, len(colors) - 1)
                    lisi[j] = colors[rand] + '*' + Style.RESET_ALL
                    elka[i] = ''.join(lisi)
    return elka


while True:
    print(*ukr(elka(30)), (' ' * stv + '|_|'), sep='\n')
    sleep(0.3)
    os.system('cls')
