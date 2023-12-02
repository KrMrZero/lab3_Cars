from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import re
from fnmatch import *

from Names import Name
import WindowMain
import main_3
import Test


class Change(QWidget):
    def __init__(self):
        super().__init__()

        # Обнуление всех пааметров в файлах
        for i in range(0, 8):
            with open(f'Parametrs/{i}.txt', 'w', encoding='utf-8') as file:
                file.readable()
            file.close()

        self.setWindowTitle("Изменение автомобиля")
        self.resize(450,700)

        self.ChangeWidgets()

        self.layout = QVBoxLayout()

        self.layout.addLayout(self.Nomer)
        self.layout.addLayout(self.Color)
        self.layout.addLayout(self.Marks)
        self.layout.addLayout(self.Models)
        self.layout.addLayout(self.Year)
        self.layout.addLayout(self.Force)
        self.layout.addLayout(self.Light)
        self.layout.addLayout(self.Door)
        self.layout.addWidget(self.buttonCreate)
        self.layout.addWidget(self.buttonBack)


        self.setLayout(self.layout)

        self.show()

    def ChangeWidgets(self):

        def WM():
            self.window = WindowMain.Main()
            self.window.show()

            self.close()

        def ChangeTable():
            car=[]
            for i in range(0, 8):
                with open(f'Parametrs/{i}.txt', 'r', encoding='utf-8') as file:
                    str = file.read()
                file.close()

                # Проверка на "нулевой" параметр
                if str =='' and i==0:
                    message = QMessageBox()
                    message.setWindowTitle('Ошибка')
                    message.setIcon(QMessageBox.Critical)
                    message.setText('Машины с таким номером нет в базе')
                    message.exec_()
                    break
                elif str =='' and i ==5:
                    message = QMessageBox()
                    message.setWindowTitle('Ошибка')
                    message.setIcon(QMessageBox.Critical)
                    message.setText('Неправильный символ в строке "Мощность двигателя(л.с.)"')
                    message.exec_()
                    break
                elif str =='':
                    message = QMessageBox()
                    message.setWindowTitle('Ошибка')
                    message.setIcon(QMessageBox.Critical)
                    message.setText('Не все поля заполнены')
                    message.exec_()
                    break
                else:
                    car.append(str)
            if str !='':
                main_3.Main().ChangeCar(car)
                if Test.IntegrationTest().TestChange(car):
                    message = QMessageBox()
                    message.setWindowTitle('Отчёт')
                    message.setText('Информация об автомобиле успешно изменена!')
                    message.exec_()
                    # self.buttonCreate.clicked.disconnect()



        # Выбор номера авто
        self.entryNomer = QLineEdit(self,
                               placeholderText='Пример: A000AA000',
                               clearButtonEnabled=True)
        self.entryNomer.textChanged[str].connect(self.ChCar)
        self.labelNomer = QLabel()
        self.labelNomer.setText('Выберете гос. номер авто')

        self.Nomer = QHBoxLayout()
        self.Nomer.addWidget(self.labelNomer)
        self.Nomer.addWidget(self.entryNomer)

        # Цвет
        self.comboColor = QComboBox()
        self.comboColor.addItem('')
        self.comboColor.textActivated[str].connect(self.fColor)
        self.Color = self.BoxLayout(self.comboColor,1)


        # Марка
        self.comboMarks = QComboBox()
        self.comboMarks.addItem('')
        self.comboMarks.textActivated[str].connect(self.fMarks)
        self.Marks = self.BoxLayout(self.comboMarks,2)


        # Модель
        self.comboModels = QComboBox()
        self.comboModels.addItem('')
        self.comboModels.textActivated[str].connect(self.fModels)
        self.Models = self.BoxLayout(self.comboModels,3)


        # Год выпуска
        self.comboYear = QComboBox()
        self.comboYear.addItem('')
        self.comboYear.textActivated[str].connect(self.fYear)
        self.Year = self.BoxLayout(self.comboYear,4)


        # Мощность двигателя
        self.entryForce = QLineEdit()
        self.entryForce.textChanged[str].connect(self.AvtoForce)
        self.Force = self.BoxLayout(self.entryForce,5)


        # Фары
        self.comboLight = QComboBox()
        self.comboLight.addItem('')
        self.comboLight.textActivated[str].connect(self.fLight)
        self.Light = self.BoxLayout(self.comboLight,6)


        # Двери
        self.comboDoor = QComboBox()
        self.comboDoor.addItem('')
        self.comboDoor.textActivated[str].connect(self.fDoors)
        self.Door = self.BoxLayout(self.comboDoor,7)



        # Возвращение на главную
        self.buttonBack = QPushButton()
        self.buttonBack.setText('Вернуться к базе машин')
        self.buttonBack.clicked.connect(WM)

        # Создание профиля
        self.buttonCreate = QPushButton()
        self.buttonCreate.setText('Изменить автомобиль')
        self.buttonCreate.clicked.connect(ChangeTable)


        # Проверка выделенной ячейки
        with open('Parametrs/nomer.txt', 'r', encoding='utf-8') as file:
            b = file.read()
        file.close()
        for i in Name.avtoNomers:
            if b ==i:
                self.entryNomer.setText(f'{b}')
                break



    def ChCar(self, text):
        a = text
        for i in Name.avtoNomers:
            if a == i:

                # Поиск строки с профилем  по гос. номеру
                for j in range(len(Name.allTable)):
                    car = fnmatch(Name.allTable[j],f'{a}*')
                    if car is True:
                        avtoCar = Name.allTable[j].split(' ')
                        break

                main_3.Main().writing(text, 0)

                self.entryNomer.setStyleSheet("QLineEdit"
                                         "{"
                                         "background : lightgreen;"
                                         "}")
                # Цвет
                self.comboColor.clear()
                self.comboColor.addItem(avtoCar[1])
                self.fColor(avtoCar[1])
                self.comboColor.addItems(Name.color)
                # Марка
                self.comboMarks.clear()
                self.comboMarks.addItem(avtoCar[2])
                self.fMarks(avtoCar[2])
                self.comboMarks.currentTextChanged.connect(self.MarksModels)
                self.comboMarks.addItems(Name.marks)
                # Модель
                self.comboModels.clear()
                self.fModels(avtoCar[3])
                self.MarksModels(avtoCar[2])

                # Год выпуска
                self.comboYear.clear()
                self.comboYear.addItem(avtoCar[4])
                self.fYear(avtoCar[4])
                self.comboYear.addItems([str(i) for i in range(2023, 1900, -1)])
                # Мощность двигателя
                self.entryForce.setText(f'{avtoCar[5]}')
                main_3.Main().writing(avtoCar[5],5)
                # Фары
                self.comboLight.clear()
                self.comboLight.addItem(avtoCar[6])
                self.fLight(avtoCar[6])
                self.comboLight.addItems(Name.status1)
                # Двери
                self.comboDoor.clear()
                self.comboDoor.addItem(avtoCar[7])
                self.fDoors(avtoCar[7])
                self.comboDoor.addItems(Name.status2)
                break
            else:
                self.entryNomer.setStyleSheet("QLineEdit"
                                         "{"
                                         "background : pink;"
                                         "}")
                main_3.Main().writing('',0)

    def BoxLayout(self,widget,k):
        label = QLabel()
        label.setText(f'{Name.headers[k]}')
        self.Box = QHBoxLayout()
        self.Box.addWidget(label)
        self.Box.addWidget(widget)
        return self.Box

    def AvtoForce(self, text):
        if text is False:
            print(False)
        else:
            for i in text:
                if i == ' ':
                    self.entryForce.setStyleSheet("QLineEdit"
                                                  "{"
                                                  "background : pink;"
                                                  "}")
                    main_3.Main().writing('', 5)
            try:
                a = int(text)
                if a>5 and a<3000:
                    self.entryForce.setStyleSheet("QLineEdit"
                                             "{"
                                             "background : lightgreen;"
                                             "}")
                    main_3.Main().writing(text,5)
                else:
                    self.entryForce.setStyleSheet("QLineEdit"
                                             "{"
                                             "background : pink;"
                                             "}")
                    main_3.Main().writing('', 5)
            except(ValueError):
                self.entryForce.setStyleSheet("QLineEdit"
                                         "{"
                                         "background : pink;"
                                         "}")
                main_3.Main().writing('', 5)

    def MarksModels(self,text):
        marks = {}
        for i in range(len(Name.marks)):
            marks[Name.marks[i]] = i
        with open(f'data/allCars/{marks[str(text)]}.txt', 'r', encoding='utf-8') as file:
            models = file.readlines()[1:]
        with open('Parametrs/3.txt','r',encoding='utf-8') as file:
            m=file.read()

        self.comboModels.clear()
        for i in range(len(models)):
            models[i] = models[i].replace(' ', '_')
            models[i] = models[i].replace('\n', '')
            # print(models[i])
            if models[i]==m:
                self.comboModels.addItem(m)

        self.comboModels.addItems(models)





    def fColor(self, text):
        main_3.Main().writing(text, 1)
    def fMarks(self, text):
        main_3.Main().writing(text, 2)
    def fModels(self, text):
        main_3.Main().writing(text, 3)
    def fYear(self, text):
        main_3.Main().writing(text, 4)
    def fLight(self, text):
        main_3.Main().writing(text, 6)
    def fDoors(self, text):
        main_3.Main().writing(text, 7)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Change()
    sys.exit(app.exec())