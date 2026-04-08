import os
import pandas as pd
from datetime import datetime

def log(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)  # выполняем исходную функцию

        file_path = "logs.csv"  # путь к файлу логов
        now = datetime.now()  # текущее время

        new_row = pd.DataFrame([{
            "id": pd.read_csv(file_path).shape[0] if os.path.exists(file_path) else 0,  # авто‑id
            "pc_username": os.getlogin(),  # имя пользователя ПК
            "function_name": func.__name__,  # имя вызываемой функции
            "Date in date.month.year": now.strftime("%d-%m-%Y"),  # дата
            "Time": now.strftime("%H:%M:%S")  # время
            }])

        new_row.to_csv(
            file_path,
            mode='a',
            header=not os.path.exists(file_path),  # заголовок только при первом создании файла
            index=False
        )

        print(f" Данные успешно записаны в {file_path}")  # уведомление
        return result  # возвращаем результат исходной функции

    return wrapper
