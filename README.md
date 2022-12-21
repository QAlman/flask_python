# Repository for Bot
[Ветка - master](https://gitlab.wiam.ru/tests/tg-scoring-bot/tree/master) , 
[Ветка - dev](https://gitlab.wiam.ru/tests/tg-scoring-bot/tree/bot_dev)


# Краткое описание
app.py - Телеграмм бот написанный на python + flask 
После запуска приложения,  в телеграмм бот -- @tg_scoring_my_bot --

Можно отправлять сообщения с определенным ключем-паролем
и автоматически приходит ответ (с результатом запроса) для того пользователя, который отправил сообщение с ключем

scheduler_bot.py - Скрипт написанный на python  
После запуска телеграмм бот -- @tg_scheduler_my_bot --

Автоматически отправляет сообщение с данными в группу

## Структура:

*app.py - основной файл для запуска приложения

*MarksData_1.xlsx - файл для сохранения результатом запроса в формате xlsx (для возможной на будущее передачи данныхв виде файла на почту итд)

*MarksData_2.csv - файл для сохранения результатом запроса в формате csv (для возможной на будущее передачи данныхв виде файла на почту итд)

*requirements.txt - список используемых библиотек необходимых для запуска проекта

*script_prod.sql -  запрос к базе для прода

*sql_sample_1.sql - запрос к базе с настройками для тестовой базы

## Для запуска:

[Основная документация по запуску flask](https://flask-russian-docs.readthedocs.io/ru/latest/quickstart.html)

Запуск приложения возможен с несколькими параметрами - 
app.run(host='0.0.0.0')
app.run(host='151.11.11.1', port=1212)
app.run()

в среде bash - flask run 

*порт 5000 для Falsk- по умолчанию.

Для пересылки сообщений бота в наше приложение
необходимо выполнить POST запрос к - https://api.telegram.org/bot{токен-телеграм-бота}/setWebhook

формата -{"url": "https://{URL приложения}"}

Ответом должно быть  - {
    "ok": true,
    "result": true,
    "description": "Webhook was set"
}



