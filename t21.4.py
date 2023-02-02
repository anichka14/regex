import re
import datetime


""" T21.4 У текстовому файлі містяться дати у форматі dd.mm.yyyy або
підкреслення для запису дат вручну __.__.____ Знайти всі дати у тексті.
Замість підкреслень вставити поточну дату. Зберегти оновлений текст. """


DATE1 = r"\b\d{1,2}\.\d{1,2}\.\d{1,4}\b"
DATE2 = r"\b\_{2}\.\_{2}\.\_{4}\b"


def date_now(match: re.match):
    date_in_file = match.group()
    # print(date_in_file)
    if re.search(DATE2, date_in_file):
        day = datetime.date.today()
        date_in_file = day.strftime("%d.%m.%Y")

    return date_in_file


def change_dates(string):
    return re.sub(DATE2, date_now, string)


if __name__ == "__main__":
    with open("data_21.4.txt", "r+", encoding="utf-8") as f:
        text = f.read()
        f.seek(0)  # Переміщаємося на початкову (нульову) позицію файлу
        for dates in re.findall(DATE1, text):
            print(dates, end=";\n")
        text = change_dates(text)
        print(text, file=f)

