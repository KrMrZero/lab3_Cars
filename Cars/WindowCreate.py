from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

from Names import Name
import WindowMain
import main_3
import Test



class Create(QWidget):
    def __init__(self):
        super().__init__()

        # Обнуление всех пааметров в файлах
        for i in range(0, 8):
            with open(f'Parametrs/{i}.txt', 'w', encoding='utf-8') as file:
                file.readable()
            file.close()

        self.setWindowTitle("Создание автомобиля")
        self.resize(450,700)

        self.CreateWidgets()

        self.layout = QVBoxLayout()

        self.layout.addLayout(self.frame)
        self.layout.addLayout(self.Color)
        self.layout.addLayout(self.Marks)
        self.layout.addLayout(self.Models)
        self.layout.addLayout(self.Year)
        self.layout.addLayout(self.Force)
        self.layout.addLayout(self.Light)
        self.layout.addLayout(self.Door)
        self.layout.addWidget(self.buttonCreate)
        self.layout.addWidget(self.buttonBack)


        # self.layout.addStretch()
        self.setLayout(self.layout)

        self.show()

    def CreateWidgets(self):

        def WM():
            self.window = WindowMain.Main()
            self.window.show()

            self.close()

        def readCheck():
            car=[]
            for i in range(0, 8):
                with open(f'Parametrs/{i}.txt', 'r', encoding='utf-8') as file:
                    str = file.read()
                file.close()

                # Проверка на "нулевой" параметр
                if str =='':
                    message = QMessageBox()
                    message.setWindowTitle('Ошибка сохранения')
                    message.setIcon(QMessageBox.Critical)
                    message.setText('Не все поля заполнены или заполнены неверно!')
                    message.exec_()
                    break
                else:
                    car.append(str)
            if str !='':
                main_3.Main().WritingCar(car)
                if Test.IntegrationTest().TestCreate(Name.allTable):
                    message = QMessageBox()
                    message.setWindowTitle('Отчёт')
                    message.setText('Автомобиль создан!')
                    message.exec_()
                    self.window = WindowMain.Main()
                    self.window.updateTable()
                    self.window.show()

                    self.close()
                    # self.buttonCreate.clicked.disconnect()


        # Гос номер
        self.entry = QLineEdit(self,
            placeholderText='Пример: A000AA000',
            clearButtonEnabled=True)
        self.entry.textChanged[str].connect(self.AvtoNomer)
        # Добавление в сетку
        self.frame = self.BoxLayout(self.entry,0)


        # Цвет
        self.comboColor = QComboBox()
        self.comboColor.addItem('')
        self.comboColor.addItems(Name.color)
        self.comboColor.textActivated[str].connect(self.fColor)

        self.Color = self.BoxLayout(self.comboColor,1)


        # Марка
        self.comboMarks = QComboBox(self)
        self.comboMarks.addItem('')
        self.comboMarks.addItems(Name.marks)
        self.comboMarks.currentTextChanged.connect(self.MarksModels)
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
        self.comboYear.addItems([str(i) for i in range(2023,1900,-1)])
        self.comboYear.textActivated[str].connect(self.fYear)

        self.Year = self.BoxLayout(self.comboYear,4)


        # Мощность двигателя
        self.entryForce = QLineEdit()
        self.entryForce.textChanged[str].connect(self.AvtoForce)

        self.Force = self.BoxLayout(self.entryForce,5)


        # Фары
        self.comboLight = QComboBox()
        self.comboLight.addItem('')
        self.comboLight.addItems(Name.status1)
        self.comboLight.textActivated[str].connect(self.fLight)

        self.Light = self.BoxLayout(self.comboLight,6)


        # Двери
        self.comboDoor = QComboBox()
        self.comboDoor.addItem('')
        self.comboDoor.addItems(Name.status2)
        self.comboDoor.textActivated[str].connect(self.fDoors)

        self.Door = self.BoxLayout(self.comboDoor,7)

        # self.AllPaametr = [self.entry,self.comboColor,self.comboMarks,
        #               self.comboModels,self.comboModels,
        #               self.entryForce,self.comboLight,self.comboDoor]
        #
        # for i in range(len(Name.headers)):
        #     self.AllPaametr[i] = self.BoxLayout(self.AllPaametr[i],i)

        # Возвращение на главную
        self.buttonBack = QPushButton()
        self.buttonBack.setText('Вернуться к базе машин')
        self.buttonBack.clicked.connect(WM)

        # Создание профиля
        self.buttonCreate = QPushButton()
        self.buttonCreate.setText('Соранить автомобиль')
        self.buttonCreate.clicked.connect(readCheck)
        # self.buttonCreate.update_table_signal.connect()





    def BoxLayout(self,widget,k):
        label = QLabel()
        label.setText(f'{Name.headers[k]}')
        self.Box = QHBoxLayout()
        self.Box.addWidget(label)
        self.Box.addWidget(widget)
        return self.Box

    def AvtoNomer(self, text):
        nomer_simv = Name.nomer_simv
        nums = Name.nomer_nums
        a = text
        if len(a) == 9:
            k = 0
            for n in nomer_simv:
                if n == a[0]:
                    k += 1
                if n == a[4]:
                    k += 1
                if n == a[5]:
                    k += 1
            for n in nums:
                if n == a[1]:
                    k += 1
                if n == a[2]:
                    k += 1
                if n == a[3]:
                    k += 1
                if n == a[6]:
                    k += 1
                if n == a[7]:
                    k += 1
                if n == a[8]:
                    k += 1

            if k == 9:
                for i in Name.avtoNomers:
                    if a == i:
                        self.entry.setStyleSheet("QLineEdit"
                                                 "{"
                                                 "background : pink;"
                                                 "}")
                        main_3.Main().writing("", 0)
                        message = QMessageBox()
                        message.setWindowTitle('Ошибка сохранения')
                        message.setIcon(QMessageBox.Critical)
                        message.setText('Номер уже существует!')
                        message.exec_()
                        break
                    else:
                        self.entry.setStyleSheet("QLineEdit"
                                "{"
                                "background : lightgreen;"
                                "}")
                        main_3.Main().writing(text, 0)
            else:
                self.entry.setStyleSheet("QLineEdit"
                                         "{"
                                         "background : pink;"
                                         "}")
                main_3.Main().writing("", 0)
        elif len(a)>=1:
            self.entry.setStyleSheet("QLineEdit"
                                         "{"
                                         "background : pink;"
                                         "}")
            main_3.Main().writing("", 0)

    def AvtoForce(self, text):
        if text is False:
            False
        else:
            for i in text:
                if i == ' ':
                    self.entryForce.setStyleSheet("QLineEdit"
                                                  "{"
                                                  "background : pink;"
                                                  "}")
                    main_3.Main().writing("",5)
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
                    main_3.Main().writing("",5)
            except(ValueError):
                self.entryForce.setStyleSheet("QLineEdit"
                                         "{"
                                         "background : pink;"
                                         "}")
                main_3.Main().writing("", 5)

    def MarksModels(self,text):
        marks = {}
        for i in range(len(Name.marks)):
            marks[Name.marks[i]] = i
        with open(f'data/allCars/{marks[str(text)]}.txt', 'r', encoding='utf-8') as file:
            models = file.readlines()[1:]

        for i in range(len(models)):
            models[i]=models[i].replace(' ','_')
            models[i] = models[i].replace('\n', '')

        self.comboModels.clear()
        self.comboModels.addItems(models)
        self.fModels(models[0])




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




class ChooseParams():
   def paramList(self):
      allMarks = Name.marks
      return allMarks


class ChooseUnitOfMeasurement():
    def unitOfMeasurement(self, parameter):
        marks = {}
        for i in range(len(Name.marks)):
            marks[Name.marks[i]]=i

        with open(f'data/allCars/{marks[str(parameter)]}', 'r' ,encoding='utf-8') as file:
            models = file.readlines()[1:]
        return models



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Create()
    sys.exit(app.exec())