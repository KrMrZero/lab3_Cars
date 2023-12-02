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

class Delete(QWidget):
    def __init__(self):
        super().__init__()

        # Обнуление всех пааметров в файлах
        for i in range(0, 8):
            with open(f'Parametrs/{i}.txt', 'w', encoding='utf-8') as file:
                file.readable()
            file.close()


        self.setWindowTitle("Удаление профиля")
        self.resize(330,100)

        self.DeleteWidgets()

        self.layout = QGridLayout()
        self.layout.addWidget(self.label,0,0)
        self.layout.addWidget(self.entry,0,1)
        self.layout.addWidget(self.buttonBack, 1, 0)
        self.layout.addWidget(self.buttonDelete, 1, 1)

        self.setLayout(self.layout)


        self.show()

    def DeleteWidgets(self):

        def clickBack():
            self.window = WindowMain.Main()
            self.window.show()

            self.close()

        def clickDelete():
            car = []
            with open(f'Parametrs/0.txt', 'r', encoding='utf-8') as file:
                str = file.read()
            file.close()

            # Проверка на "нулевой" параметр
            if str == '':
                message = QMessageBox()
                message.setWindowTitle('Ошибка')
                message.setIcon(QMessageBox.Critical)
                message.setText('Машины с таким номером нет в базе')
                message.exec_()
            else:
                table =  Name.allTable
                for j in range(len(table)):
                    car = fnmatch(table[j], f'{str}*')
                    if car is True:
                        break
                table.pop(j)
                # Очистка списка и запись
                with open('cars.txt', 'w+', encoding='utf-8') as file:
                    file.writelines(table)
                file.close()
                Name.allTable = table

                # Удаление пустой строки в конце
                with open('cars.txt', 'r+') as f:
                    lines = f.readlines()
                    lines[-1] = lines[-1].strip()
                    f.seek(0)
                    f.writelines(lines)
                    f.truncate()

                message = QMessageBox()
                message.setWindowTitle('Отчёт')
                message.setText('Автомобиль успешно удалён!')
                message.exec_()

                window = WindowMain.Main()
                window.updateTable()
                window.show()

                self.close()




        self.label = QLabel()
        self.label.setText('Выберете гос. номер авто')
        self.entry = QLineEdit(self,
                               placeholderText='Пример: A000AA000',
                               clearButtonEnabled=True)
        self.entry.textChanged[str].connect(self.DeleteCar)




        self.buttonBack = QPushButton()
        self.buttonBack.setText('Назад')
        self.buttonBack.clicked.connect(clickBack)

        self.buttonDelete = QPushButton()
        self.buttonDelete.setText('Удалить')
        self.buttonDelete.clicked.connect(clickDelete)

        # Проверка выделенной ячейки
        with open('Parametrs/nomer.txt', 'r', encoding='utf-8') as file:
            b = file.read()
        file.close()
        for i in Name.avtoNomers:
            if b == i:
                self.entry.setText(f'{i}')
                break

    def DeleteCar(self,text):
        a = text
        # Проверка на существовование номера
        for i in Name.avtoNomers:
            if a == i:
                self.entry.setStyleSheet("QLineEdit"
                                              "{"
                                              "background : lightgreen;"
                                              "}")
                main_3.Main().writing(text, 0)
                break
            else:
                self.entry.setStyleSheet("QLineEdit"
                                              "{"
                                              "background : pink;"
                                              "}")
                main_3.Main().writing('', 0)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Delete()
    sys.exit(app.exec())

