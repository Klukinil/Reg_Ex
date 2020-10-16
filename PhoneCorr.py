import re
import csv
from pprint import pprint

#Открываем файл
def file_opener(file):
    with open(file, encoding='utf-8') as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
        return contacts_list

#Приводим ФИО в порядок
def file_correcter():
    contacts_list_corr = [contacts_list[0]]
    for contact_info in contacts_list[1:]:
        splitted = contact_info[0].split()
        if len(splitted) == 2:
            contact_info[1] = splitted[1]
            contact_info[0] = splitted[0]
        if len(splitted) == 3:
            contact_info[1] = splitted[1]
            contact_info[2] = splitted[2]
            contact_info[0] = splitted[0]
        if len(splitted) == 1:
            pass
        splitted_1 = contact_info[1].split()
        if len(splitted_1) == 2:
            contact_info[2] = splitted_1[1]
            contact_info[1] = splitted_1[0]
        contacts_list_corr.append(contact_info)

    # Приводим телефоны в порядок
    for contact in contacts_list_corr[1:]:
        pattern = re.compile(r'(\+7|8)\s*\(?(\d{3})\)?\s*-?(\d{3})\-?(\d{2})\-?(\d{2})(\s*\(?(доб.)\s*(\d{4})\)?)*')
        contact[5] = pattern.sub(r'+7(\2)\3-\4-\5 \7\8', contact[5])

    #Соединяем дубликаты
    for person in range(1,len(contacts_list_corr)):
        for person_1 in range(person+1, len(contacts_list_corr)):
            if contacts_list_corr[person][0] == contacts_list_corr[person_1][0] and contacts_list_corr[person][1] == \
                   contacts_list[person_1][1]:
                print(f'Внимание! Найдены дубли:{contacts_list_corr[person]} и {contacts_list_corr[person_1]}')
                for element in range(len(contacts_list_corr[person])):
                    if len(contacts_list_corr[person][element]) <= len(contacts_list_corr[person_1][element]):
                        contacts_list_corr[person][element] = contacts_list_corr[person][element]
                        contacts_list_corr[person_1][element] = ''
                        contacts_list_corr[person_1][0] = ''
                        contacts_list_corr[person_1][1] = ''

    #Убираем пустые строки
    i=0
    for contact in contacts_list_corr:
        if contact[0] == '':
            del contacts_list_corr[i]
        else:
            pass
        i +=1

    print(contacts_list_corr)
    return contacts_list_corr


#Записываем в файл
def file_creator(list_corr):
    with open("phonebook_corr.csv", "w", encoding='utf-8') as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(list_corr)
        print("Файл создан")


contacts_list = file_opener('phonebook_raw.csv')
contacts_corrected = file_correcter()
file_creator(contacts_corrected)


