import os
import rational

import logger


def clear(): return os.system('cls')


def GetInt(msg):
    try:
        return int(input(msg))
    except:
        return GetInt(msg)


def item_sel(items):
    clear()
    input = ""
    for i in range(len(items)):
        print(f"{i}: {items[i]}")
    print()
    while input not in range(len(items)) and input != -1:
        input = GetInt("Выбирите необходимую операцию: ")
    return input

items = ["Ввести выражение для вычисления", "Посмотреть логи", "Выйти"]

selection = item_sel(items)

clear()

match selection:
    case 0:
        expr = input ("Введите выражение: ")
        res = rational.parse_all(expr)
        logger.write(f"Результат вычисления: {expr} = {res}")
    case 1:
        logger.read_all()