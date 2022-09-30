# Процедуры работы с базой данных и внешними файлами

import settings
import json
import os

def load_db(): # читаем из файла json в список словарей
    if os.path.isfile(settings.db_file):
        with open(settings.db_file, 'r', encoding='UTF-8') as f:
            ret = json.load(f)
            return ret
    else: return []

def save_db(local_list): # пишем в файл json список словарей
    if len(local_list) > 0:
        with open(settings.db_file, 'w', encoding='UTF-8') as f:
            json.dump(local_list, f)
    return

def export_csv(phone_book: list): # экспорт csv
    rec_file = "phones.csv"
    with open(rec_file, mode='w', encoding="utf-8") as w:
        w.write('Title;Phone;DateTime;Note\n')
        for rec in phone_book:
            w.write(f'{rec["Title"]};{rec["Phone"]};{rec["Note"]};{rec["Datetime"]}\n')
    print(f'Данные экспортированы в файл {rec_file}')

def export_txt(phone_book: list): # экспорт txt
    rec_file = "phones.txt"
    with open(rec_file, mode='w', encoding="utf-8") as w:
        for rec in phone_book:
            w.write(f'{rec["Title"]}\t{rec["Phone"]}\t{rec["Note"]}\t{rec["Datetime"]}\n')
    print(f'Данные экспортированы в файл {rec_file}')

def export_json(phone_book: list): # экспорт json
    rec_file = "phones.json"
    with open(rec_file, mode='w', encoding="utf-8") as w:
        w.write(json.dumps(phone_book, indent=4))
    print(f'Данные экспортированы в файл {rec_file}')

def import_json(save_list): # импорт из json
    imp_file = input('Введите имя json - фала, или оставьте пустым - для отмены: ')
    if len(imp_file)>0:
        if os.path.isfile(imp_file):
            with open(imp_file, 'r', encoding='UTF-8') as f:
                ret = json.load(f)
                return ret
        else: return []
    else: return save_list # если отказались от импорта
