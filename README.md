# Знакомство с языком Python (семинары) #

## Урок 8. Python: от простого к практике ##

### Задание: Создать телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах##

**Программа должна:**

1. Показывать общий список телефонов в справочнике
2. Добавлять новую запись о телефоне
3. Редактировать существующую запись
4. Удалять запись.
5. Выводить помощь и информацию о программе
6. Иметь возможность экспортировать базу данных о телефонах в различные форматы
7. Иметь возможность импортировать базу данных.

**Модули программы:**

* _main_ - Главный модуль программы. Из него запускаем все остальные модули
* _model_ - Модуль, в котором описана модель данных - структура записи (поля)
* _io\_module_ - Модуль, в котором содердатся процедуры работы с файлом базы данных, а так же - процедуры импорта и экспорта
* _view\_module_ - Модуль, который умеет красиво отображать данные, и сожержит инструменты взаимодействия с пользователем
* _controller_ - Модуль, в котором находится основная логика приложения.
* _settings_ - Модуль, в котором содержатся различные настройки приложения.
* _log_ - Модуль журналирования действий

*Это доработка программы из домашнего задания к 7-му уроку. Добавил работу с SQLite. Благодаря модульности - потребовалось изменить только две процедуры:
* _io\_module.load\_db()_
* _io\_module.save\_db()_
