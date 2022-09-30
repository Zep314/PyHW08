# Процедуры работы с базой данных и внешними файлами
import settings
import json
import os
import sqlite3

def load_db(): # читаем из SQL базы в список словарей
    ret = []
    try:
        sqlite_connection = sqlite3.connect(settings.db_file)
        cursor = sqlite_connection.cursor()
        sqlite_select_query = "SELECT title,phone,datetime,note FROM phones;"
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        for record in records:
            ret.append({'Title':record[0],
                        'Phone':record[1],
                        'Datetime':record[2],
                        'Note':record[3]})
        cursor.close()
    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)
        exit()
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
    return ret

def save_db(local_list): # пишем в SQL таблицу список словарей
    try:
        sqlite_connection = sqlite3.connect(settings.db_file)
        cursor = sqlite_connection.cursor()
        sqlite_delete_query = "DELETE FROM phones;" # сначала очистим всю таблицу
        cursor.execute(sqlite_delete_query)
        sqlite_connection.commit()
        for x in local_list: # а тут - запишем все данные
            sqlite_insert_query = f'INSERT INTO phones (title,phone,datetime,note) '\
                                  f'values(\'{x["Title"]}\',\'{x["Phone"]}\',\'{x["Datetime"]}\',\'{x["Note"]}\');'
            cursor.execute(sqlite_insert_query)
        sqlite_connection.commit()
        cursor.close()
    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)
        exit()
    finally:
        if (sqlite_connection):
            sqlite_connection.close()

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
