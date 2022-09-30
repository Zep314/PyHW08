# Отображение данных. Взаимодействие с человеком

import time
from log import add2log

def add(): # Добавление данных
    print('Добавление записи')
    title  = input('Введтие заголовок телефона: ')
    status = input('Телефон: ')
    note   = input('Описание: ')
    datetime= time.strftime("%Y.%m.%d %H:%M:%S",time.gmtime(time.time()))
    print('Данные добавлены')
    add2log('Добавление данных:','<')
    add2log(f'Title = {title}; Phone = {status} Note = {note};','<')
    return {
            'Title' : title,
            'Phone' : status,
            'Note' : note,
            'Datetime' : datetime
           } 

def show_records(local_list): # Отображение всей базы на экране красиво
    print(f'{"-"*1}Номер{"-"*1}+{"-"*25}Заголовок{"-"*25}+{"-"*4}Телефон{"-"*5}+{"-"*7}Время{"-"*7}')
    for i in range(len(local_list)):
        print(f'{i:7}|{local_list[i]["Title"]:59}|{local_list[i]["Phone"]:15}|{local_list[i]["Datetime"]:11}')
    print(f'{"-"*7}+{"-"*59}+{"-"*16}+{"-"*19}')
    add2log(f'Выведено {len(local_list)} строк базы данных','<')

def del_records(): # Возвратим индекс элемента списка для удаления
    print('Введите номер записи, которую хотите удалить, или -1 - чтобы отказаться')
    ret = int(input('Номер записи: '))
    add2log(str(ret),'<')
    return ret

def get_edit_records(): # Возвращаем индекс элемента списка для редактирования
    print('Введите номер записи, которую хотите редактировать, или -1 - чтобы отказаться')
    ret = int(input('Номер записи: '))
    add2log(str(ret),'<')
    return ret

def edit_record(local_list): # Интерфейс редактирования записи
    print(f'Заголовок телефона: {local_list["Title"]}')
    print(f'Телефон: {local_list["Phone"]}')
    print(f'Описание: {local_list["Note"]}')
    print('Введите новое значение, или оставьте поле пустым (Нажмите Enter)')
    title = ''
    phone = ''
    note = ''
    inp  = input('Введите заголовок: ')
    if len(inp) > 0: title = inp
    else: title = local_list["Title"]

    inp = input('Телефон: ')
    if len(inp) > 0: phone = inp
    else: phone = local_list["Phone"]

    inp = input('Описание: ')
    if len(inp) > 0: note = inp
    else: note = local_list["Note"]

    datetime = time.strftime("%Y.%m.%d %H:%M:%S",time.gmtime(time.time()))
    add2log(f'Редактирование записи {local_list["Title"]} => {title}; {local_list["Phone"]} => {phone} ;{local_list["Note"]} => {note}','<')
    return {
            'Title' : title,
            'Phone' : phone,
            'Note' : note,
            'Datetime' : datetime
           }
