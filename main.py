# -*- coding: windows-1251 -*-
import csv
import re

phone_number_pattern = re.compile(r"^(\+7|8)\D*(\d{3})\D*(\d{3})\D*(\d{2})\D*(\d{2})\D*(\d{4})?.*")
def format_phone(phone):
    numbers = phone_number_pattern.match(phone)
    if numbers.groups()[5]:
        phone = phone_number_pattern.sub(r"+7(\2)\3-\4-\5 доб.\6", phone)
    else:
        phone = phone_number_pattern.sub(r"+7(\2)\3-\4-\5", phone)

    return phone

with open("phonebook_raw.csv", "r", encoding="utf8") as f:
    raws_list = list(csv.reader(f, delimiter=","))

raws_info = {}
for raw in raws_list[1:]:
    lastname, firstname, surname, organization, position, phone, email = raw[:7]
    name = re.findall(r"([(А-Я][а-я]+)", lastname+firstname+surname)

    if len(name) < 2: continue

    raws_info.setdefault(name[0]+name[1], {})
    raw_info = raws_info.get(name[0]+name[1])
    print(name[0]+name[1])
    print(raw_info)

    raw_info["lastname"] = name[0]
    raw_info["firstname"] = name[1]

    # print(raw_info)
    if len(name) > 2 and not raw_info.get("surname"):
        raw_info["surname"] = name[2]

    if organization and not raw_info.get("organization"):
        raw_info["organization"] = organization

    if position and not raw_info.get("position"):
        raw_info["position"] = position

    if phone and not raw_info.get("phone"):
        raw_info["phone"] = format_phone(phone)

    if email and not raw_info.get("email"):
        raw_info["email"] = email

raws_list = [raws_list[0]]
for raw in raws_info.values():
    raws_list.append([
        raw.get("lastname"),
        raw.get("firstname"),
        raw.get("surname"),
        raw.get("organization"),
        raw.get("position"),
        raw.get("phone"),
        raw.get("email"),
    ])

with open("phonebook.csv", "w", encoding="utf8") as f:
    csv.writer(f, delimiter=',').writerows(raws_list)
