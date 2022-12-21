import array
import json
import time
import numpy as np
import pandas
from flask import Flask
from flask import request
import requests
from dotenv import load_dotenv
from os.path import join, dirname
import os.path
import pandas as pd
import os
import os.path
import sqlalchemy
import datetime
import openpyxl

# from prettytable import PrettyTable
# from prettytable import from_csv


app = Flask(__name__)

# код взят из присланного скрипта , данные пользователя можно менять произвольно
# login = os.environ.get("DB_USER", "crm_vayvnd")
# password = os.environ.get("DB_PASSWORD", "crm_vayvnd")
# host = os.environ.get("DB_HOST", "localhost:5445") # порт базы меняется
# db_name = os.environ.get("DB_NAME", "crm_vayvnd")
# engine = sqlalchemy.create_engine(f'postgresql://{login}:{password}@{host}/{db_name}')

# создается .env файл с переменными окуда беруться все данные пользователя, пути итд
# для безопастности лучше, но не критично в текущей реализации


def get_from_env(key):
    dotenv_path = join(dirname(__file__), ".env")
    load_dotenv(dotenv_path)
    return os.environ.get(key)


login = get_from_env("DB_USER")
password = get_from_env("DB_PASSWORD")
host = get_from_env("DB_HOST") # порт базы меняется
port = get_from_env("DB_PORT")
db_name = get_from_env("DB_NAME")
engine = sqlalchemy.create_engine(f'postgresql://{login}:{password}@{host}:{port}/{db_name}')
file_name_1 = 'MarksData_1.xlsx'
file_name_2 = 'MarksData_2.xlsx'
file_name_3 = 'MarksData_3.xlsx'
file_name_csv = 'MarksData_2.csv'


def sql_script_1():
    with open('script_prod.sql', 'r', encoding="utf8") as query:
        sql = query.read()
    df = pd.read_sql(sqlalchemy.text(sql), engine) # возвращает значение выборки скрипта в текстовом формате
    de = df.to_excel(file_name_1) # пишем в файл
    d_csv = df.to_csv(file_name_csv)  # пишем в файл
    query.close()

    return df


def sql_script_2():
    with open('script_prod.sql', 'r', encoding="utf8") as query:
        sql = query.read()
    df = pd.read_sql(sqlalchemy.text(sql), engine)
    de = df.to_csv(file_name_csv)
    query.close()

    return df


def get_datatime():
    x = datetime.datetime.now() # текущее время
    # y = x.strftime("%f") # разные варианты форматирования
    y = x.strftime("%d/%m/%Y %H:%M:%S") # разные варианты форматирования
    z = str(y)

    return z


def send_message(chat_id, text):
    method = "sendMessage"
    token = get_from_env("TELEGRAM_BOT_TOKEN") # обычно токен берется из файла .env
    url = f"https://api.telegram.org/bot{token}/{method}"
    data = {"chat_id": chat_id, "text": text}
    requests.post(url, data=data)


@app.route('/', methods=["POST"])
def start_bot():
    print(request.json)
    # switch = request.json["message"]["text"] # получаем текст отправленный в бот
    # Если текст соответсвует ключу то проиcходит отправка данных первого скрипта либо второго
    # для остальных отправляется ответ заглушка
    switch = request.json["message"]["text"]
    if switch == "initial":
        a = sql_script_1()
        d = a.to_dict()

        h = d['dt_1'][0]
        h2 = d['dt_5'][0]
        h3 = d['dt_10'][0]
        h4 = d['dt_last'][0]
        h5 = d['dt_now'][0]
        ar_last_day_ = d['ar_last_day'][0]
        ar_last_day = "{:.1%}".format(ar_last_day_)
        requests_last_day = d['requests_last_day'][0]
        ar_today_ = d['ar_today'][0]
        ar_today = "{:.1%}".format(ar_today_)
        requests_today = d['requests_today'][0]
        NPL_1_ = d['npl1_mean'][0]
        NPL_1 = "{:.1%}".format(NPL_1_)
        NPL_1S_ = d['npl1_$_mean'][0]
        NPL_1S = "{:.1%}".format(NPL_1S_)
        NPL_5_ = d['npl5_mean'][0]
        NPL_5 = "{:.1%}".format(NPL_5_)
        NPL_5S_ = d['npl5_$_mean'][0]
        NPL_5S = "{:.1%}".format(NPL_5S_)
        NPL_10_ = d['npl10_mean'][0]
        NPL_10 = "{:.1%}".format(NPL_10_)
        NPL_10S_ = d['npl10_$_mean'][0]
        NPL_10S = "{:.1%}".format(NPL_10S_)
        avg_check_last_day = d['avg_check_last_day'][0]
        agreements_last_day = d['agreements_last_day'][0]
        avg_check_today = d['avg_check_today'][0]
        agreements_today = d['agreements_today'][0]
        npl1_mean_last_month_ = d['npl1_mean_last_month'][0]
        npl1_mean_last_month = "{:.1%}".format(npl1_mean_last_month_)
        npl1_S_mean_last_month_ = d['npl1_$_mean_last_month'][0]
        npl1_S_mean_last_month = "{:.1%}".format(npl1_S_mean_last_month_)
        npl5_mean_last_month_ = d['npl5_mean_last_month'][0]
        npl5_mean_last_month = "{:.1%}".format(npl5_mean_last_month_)
        npl5_S_mean_last_month_ = d['npl5_$_mean_last_month'][0]
        npl5_S_mean_last_month = "{:.1%}".format(npl5_S_mean_last_month_)
        npl10_mean_last_month_ = d['npl10_mean_last_month'][0]
        npl10_mean_last_month = "{:.1%}".format(npl10_mean_last_month_)
        npl10_S_mean_last_month_ = d['npl10_$_mean_last_month'][0]
        npl10_S_mean_last_month = "{:.1%}".format(npl10_S_mean_last_month_)


        init = ('✔️' + 'Initilal clients spoiler' + '\n\n' + str(h) + '\b\b\b' + 'NPL_1*' + '\b\b\b\b' + str(NPL_1) + (' ( 1 m = ' + str(npl1_mean_last_month) + ')')
                             + '\n' + '\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b' + 'NPL_1$' + '\b\b\b\b' + str(NPL_1S) + (' ( 1 m = ' + str(npl1_S_mean_last_month) + ')')
                             + '\n' + str(h2) + '\b\b\b' + 'NPL_5*' + '\b\b\b\b' + str(NPL_5) + (' ( 1 m = ' + str(npl5_mean_last_month) + ')')
                             + '\n' + '\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b' + 'NPL_5$' + '\b\b\b\b' + str(NPL_5S) + (' ( 1 m = ' + str(npl5_S_mean_last_month) + ')')
                             + '\n' + str(h3) + '\b\b\b' + 'NPL_10*' + '\b\b' + str(NPL_10) + (' ( 1 m = ' + str(npl10_mean_last_month) + ')')
                             + '\n' + '\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b' + 'NPL_10$' + '\b\b' + str(NPL_10S) + (' ( 1 m = ' + str(npl10_S_mean_last_month) + ')')
                             + '\n\n' + '🔻' + 'Last day statistics:'
                             + '\n' + str(h4) + '\b\b\b' + ('AR = ' + str(ar_last_day)) + '\b\b' + ('Avg check = ' + str(avg_check_last_day) + '$')
                             + '\n' + '\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b' + ('Requests =  ' + str(requests_last_day))
                             + '\n' + '\b\b' + '\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b' + ('Agreements = ' + str(agreements_last_day))
                             + '\n\n' + '🔻' + 'Today statistics (on 2pm):'
                             + '\n' + str(h5) + '\b\b\b' + ('AR = ' + str(ar_today)) + '\b\b' + ('Avg check = ' + str(avg_check_today) + '$')
                             + '\n' + '\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b' + ('Requests =  ' + str(requests_today))
                             + '\n' + '\b\b' + '\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b' + ('Agreements = ' + str(agreements_today))
                             + '\n\n\n' + '.')


        #chat_id = request.json["message"]["chat"]["id"]
        chat_id = "-889304904"
        send_message(chat_id, init)


    elif switch == "223344":
        dr = sql_script_1()
        ds = dr.to_markdown()
        dj = dr.to_json()
        #dd = dr.to_dict()
        dd = "Hi"

        #chat_id = request.json["message"]["chat"]["id"]
        chat_id = "-889304904"
        send_message(chat_id, dd)


    else:
        chat_id = request.json["message"]["chat"]["id"]
        send_message(chat_id, f" Я тоже так могу -'{switch}' )) ")

    return {"ok": True}


if __name__ == '__main__':
    app.run()
