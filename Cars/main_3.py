from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import Qt
from PyQt5.Qt import *
import sys
from fnmatch import *


import WindowCreate
from Names import Name

class Main():

    def writing(self,text,k):
        with open(f'Parametrs/{k}.txt','w',encoding='utf-8') as file:
            file.write(text)
        file.close()

    def WritingCar(self,car):
        s = self.AntiSplit(car)
        with open('cars.txt', 'a', encoding='utf-8') as file:
            file.write('\n' + s)
        file.close()

    def ChangeCar(self,car):
        table = Name.allTable
        text = self.AntiSplit(car)
        a = car[0]

        # Очистка списка
        with open('cars.txt', 'w', encoding='utf-8') as file:
            file.readable()
        file.close()

        # Поиск машины по номеру и перезапись базы
        for j in range(len(table)):
            cars = fnmatch(table[j], f'{a}*')
            if cars:
                table[j] = str(text)
        for i in table:
            with open('cars.txt', 'a', encoding='utf-8') as file:
                file.write(i)



    def AntiSplit(self,car):
        s = ''
        for i in range(len(car)):
            for j in car[i]:
                s += j
            if i != len(car) - 1:
                s += ' '
        return s