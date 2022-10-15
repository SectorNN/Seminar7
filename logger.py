from datetime import datetime
from locale import getpreferredencoding


filename = "logdata.log"


def write(mess):
    now = datetime.now()
    with open(filename, "a", encoding='utf8') as log:
        data = f"{now.strftime('%d.%d.%y %H:%M:%S')}: {mess}\n"
        print (data)
        log.write(data)


def read_all():
    with open(filename, "r", encoding="utf-8") as log:
        print(log.read())