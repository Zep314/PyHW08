# Основная логика программы

from log import add2log
import view_module
import io_module

def init(): # Приветствие, и загрузка данных
    print('Телефонный справочник')
    print('/help - вывод помощи')
    return io_module.load_db()

def _help():
    print('Обрабатываются следующие команды:')
    print('\t /help - вывод помощи')
    print('\t /info - вывод информации о программе')
    print('\t /exit или /quit - выход из программы')
    print('\t /list - вывод списка телефонов')
    print('\t /add  - добавить новый телефон')
    print('\t /edit - редактировать телефон')
    print('\t /del  - удалить телефон')
    print('\t /save - принудительно сохранить базу в файл')
    print('\t /exportcsv  - экспорт базы в csv формате')
    print('\t /exporttxt  - экспорт базы в txt формате')
    print('\t /exportjson  - экспорт базы в json формате')
    print('\t /importjson  - импорт базы из формата json')

def _info():
    print('Программа - телефонный справочник.')
    print('Выполнена в качестве командного домашнего задания')

def _save(phones): # Сохраняем в файл всю базу
    io_module.save_db(phones)

def _list(phones): # Выводим на экран всю базу
    view_module.show_records(phones)

def _del(): # Возвращаем номер записи к удалению
    return view_module.del_records()

def _get_edit_idx(): # Возвращаем номер записи к редактированию
    return view_module.get_edit_records()


def _exportcsv(phone_list): # Делаем экпорт в csv
    io_module.export_csv(phone_list)

def _exporttxt(phone_list): # Делаем экпорт в txt
    io_module.export_txt(phone_list)

def _exportjson(phone_list): # Делаем экпорт в json
    io_module.export_json(phone_list)

def _importjson(phone_list): # Импорт из json файла
    return io_module.import_json(phone_list)

def controller(): # Главный цикл

    phone_list = init() # Считываем всю базу из файла

    while True:
        inp = input('>>> ')
        add2log(inp,'>') # Записываем в журнал все, что вводят
        match inp.lower(): # парсим то, что пользователь навводил
            case '/help': _help()
            case '/info': _info()
            case '/exit': break
            case '/quit': break
            case '/list': _list(phone_list)
            case '/add' : phone_list.append(view_module.add())
            case '/edit':
                edit_idx = _get_edit_idx()
                if edit_idx > -1:
                    save = phone_list[edit_idx]
                    del phone_list[edit_idx]
                    phone_list.append(view_module.edit_record(save))

            case '/del' :
                del_idx = _del()
                if del_idx > -1: del phone_list[del_idx]
            case '/save':
                _save(phone_list)
                print('Данные записаны на диск')
            case '/exportcsv':
                _exportcsv(phone_list)
            case '/exporttxt':
                _exporttxt(phone_list)
            case '/exportjson':
                _exportjson(phone_list)
            case '/importjson':
                phone_list = _importjson(phone_list)
            case _ :
                print('Неверная команда. Для помощи наберите /help')
    _save(phone_list)
    print('Выход из программы.')
