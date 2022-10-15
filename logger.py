from datetime import datetime
import os


filename = "logdata.log"


def write(mess):
    now = datetime.now()
    with open(filename, "a", encoding='utf8') as log:
        data = f"{now.strftime('%d.%d.%y %H:%M:%S')}: {mess}\n"
        log.write(data)


def read_all():
    try:
        with open(filename, "r", encoding="utf-8") as log:
            return log.read()
    except:
        return "Записи отсутствуют!"


def clear():
    try:
        os.remove("logdata.log")
        return 1
    except:
        return 0