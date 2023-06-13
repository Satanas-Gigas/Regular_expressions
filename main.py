# -*- coding: windows-1251 -*-
import csv
import re


with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
    contacts_list[4].pop(-1)

pattern = r"^(\w+[А-Яа-я])\W(\w+)\W(\w+)?\,+"
substitution = r"\1,\2,\3,"
for el in contacts_list[1:]:
    text = ','.join(el[0:3])
    text = re.sub(pattern, substitution, text).split(',')
    el[0], el[1], el[2] = text[0], text[1], text[2]

pattern = r"(\+7|8)\s?\W?(\d{3})\W?\s?(\d{3})\W?(\d{2})\W?(\d{2})(\ )?\(?(\ ?доб.)? ?(\d{4})?\)?"
substitution = r"+7(\2)\3-\4-\5\6\7\8"
for element in contacts_list[1:]:
    element[5] = re.sub(pattern, substitution, element[5])

for person in contacts_list[1:]:
    for row in contacts_list[contacts_list.index(person) + 1:]:
        if person[0] == row[0] and person[1] == row[1]:
            for i, atribute in enumerate(person):
                if not atribute:
                    person[i] = row[i]
            row[0] = 'del'
contacts_list = [row for row in contacts_list if row[0] != 'del']

with open("phonebook.csv", "w", encoding='utf-8', newline='') as f:
    data_writer = csv.writer(f, delimiter=',')
    data_writer.writerows(contacts_list)