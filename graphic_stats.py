import pandas as pd  
import numpy as np   
import matplotlib.pyplot as plt 


class GraphicStatistics:
    def __init__(self, argum):
        self.defen = pd.read_csv(argum)  # читаем csv

    def histogram(self):
        defen = (self.defen.groupby("STATE", as_index=False) 
              [["FEDERAL_REVENUE", "STATE_REVENUE", "LOCAL_REVENUE"]]
              .mean().sample(8, random_state=1))  # берём 8 штатов (ибо если больше то буде каша)

        shtaty = defen["STATE"].reset_index(drop=True)  # норм индексы
        znacheniya = defen[["FEDERAL_REVENUE", "STATE_REVENUE", "LOCAL_REVENUE"]]  
        procenty = znacheniya.div(znacheniya.sum(axis=1), axis=0) * 100  # проценты от общего

        x = np.arange(len(shtaty))  
        fig, ax = plt.subplots(figsize=(18, 10))  # создаём график

        cveta = ["royalblue", "seagreen", "darkorange"]  # цвета слоёв
        podpisy = ["Федеральный бюджет", "Бюджет штата", "Местный бюджет"]  # подписи

        nizhniy_sloy = np.zeros(len(shtaty))  
        for i, col in enumerate(procenty.columns):
            ax.bar(x, procenty[col], bottom=nizhniy_sloy, color=cveta[i], label=podpisy[i])  # слой
            ax.bar_label(ax.containers[i], fmt="%.0f%%", label_type="center", color="white")  # проценты
            nizhniy_sloy += procenty[col]  

        table = plt.table(
            cellText=np.round(znacheniya.values, 1),  # округлённые значения
            rowLabels=shtaty,  # названия штатов
            colLabels=["Федеральный", "Штат", "Местный"],  # колонки
            cellLoc="center",
            loc="bottom",
            bbox=[0, -0.45, 1, 0.35]  # позиция таблицы
        )
        table.set_fontsize(10)  # размер шрифта

        ax.set_xticks(x)
        ax.set_xticklabels(shtaty, fontsize=12)  # подписи штатов
        ax.set_ylim(0, 100)  # проценты
        ax.set_ylabel("%", fontsize=14)
        ax.set_title("Средние бюджеты школ по штатам (в %)", fontsize=18)

        ax.legend(loc="upper right", bbox_to_anchor=(1, 1), frameon=False, fontsize=12)  # легенда в углу
        plt.subplots_adjust(bottom=0.35)  # место под таблицу
        plt.show()  # вывод графика