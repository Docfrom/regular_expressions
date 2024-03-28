import csv
import re

phone_pattern = r'(\+7|8)*[\s\(]*(\d{3})[\)\s-]*(\d{3})[-]*(\d{2})[-]*(\d{2})[\s\(]*(доб\.)*[\s]*(\d+)*[\)]*'
phone_con = r'+7(\2)-\3-\4-\5\6\7'

with open("phonebook_raw.csv", encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)

def create_list():
    new_list = []
    for i in contacts_list:
        new_name = ' '.join(i[:3]).split(' ')
        res = [new_name[0], new_name[1], new_name[2], i[3], i[4], re.sub(phone_pattern, phone_con, i[5]), i[6]]
        new_list.append(res)
    return sorted_list(new_list)

def sorted_list(new_list):
    sort_list = []
    for i in range(len(new_list)):
        for j in range(len(new_list)):
            if new_list[i][0] == new_list[j][0]:
                new_list[i] = [x or y for x, y in zip(new_list[i], new_list[j])]
        if new_list[i] not in sort_list:
            sort_list.append(new_list[i])
    return sort_list


with open("phonebook.csv", "w", encoding="utf-8") as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(create_list())