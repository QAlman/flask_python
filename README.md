# Repository for Bot
[Ветка - main](https://github.com/QAlman/flask_python/tree/main) , 
[Ветка - dev](https://github.com/QAlman/flask_python/tree/site_dev)


# Краткое описание
app.py - Сайт  написанный на python + flask 


## Структура:

*app.py - основной файл для запуска приложения

*MarksData_1.xlsx - файл для сохранения результатом запроса в формате xlsx (для возможной на будущее передачи данныхв виде файла на почту итд)

*MarksData_2.csv - файл для сохранения результатом запроса в формате csv (для возможной на будущее передачи данныхв виде файла на почту итд)

*requirements.txt - список используемых библиотек необходимых для запуска проекта


## Для запуска:

[Основная документация по запуску flask](https://flask-russian-docs.readthedocs.io/ru/latest/quickstart.html)

Запуск приложения возможен с несколькими параметрами - 
app.run(host='0.0.0.0')
app.run(host='151.11.11.1', port=1212)
app.run()

в среде bash - flask run 

*порт 5000 для Falsk- по умолчанию.




