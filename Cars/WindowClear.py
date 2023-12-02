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

class Clear(QWidget):
    def __init__(self):
        super().__init__()

        # Обнуление всех пааметров в файлах
        for i in range(0, 8):
            with open(f'Parametrs/{i}.txt', 'w', encoding='utf-8') as file:
                file.readable()
            file.close()


        self.setWindowTitle("Очистка базы")
        self.resize(330,100)

        self.ClearWidgets()

        self.layout = QGridLayout()
        self.layout.addWidget(self.label,0,0)
        self.layout.addWidget(self.entry,0,1)
        self.layout.addWidget(self.buttonBack, 1, 0)
        self.layout.addWidget(self.buttonDelete, 1, 1)

        self.setLayout(self.layout)


        self.show()

    def ClearWidgets(self):

        def clickBack():
            self.window = WindowMain.Main()
            self.window.show()

            self.close()

        def clickClear():

            if self.flag:
                msgBox = QMessageBox()
                msgBox.setText("Вы уверены?")
                msgBox.setWindowTitle("Очистить")
                msgBox.setIcon(QMessageBox.Question)
                buttonCancelar = msgBox.addButton("Отменить", QMessageBox.YesRole)
                buttonAceptar = msgBox.addButton("Да", QMessageBox.RejectRole)
                msgBox.setDefaultButton(buttonAceptar)
                msgBox.exec_()

                if msgBox.clickedButton() == buttonAceptar:
                    with open('cars.txt','w') as file:
                        file.readable()
                    file.close
                    msgBox.close()

                    self.window = WindowMain.Main()
                    self.window.updateTable()
                    self.window.show()
                    self.close()

                elif msgBox.clickedButton() == buttonCancelar:
                    msgBox.close()
            else:
                message = QMessageBox()
                message.setWindowTitle('Ошибка')
                message.setIcon(QMessageBox.Critical)
                message.setText('Неверный пароль')
                message.exec_()


        self.label = QLabel()
        self.label.setText('Введите пароль')
        self.entry = QLineEdit()
        self.entry.setEchoMode(QtWidgets.QLineEdit.Password)
        self.entry.textChanged[str].connect(self.ClearData)
        self.entry.setText('password')
        self.entry.setAlignment(Qt.AlignCenter)


        self.buttonBack = QPushButton()
        self.buttonBack.setText('Назад')
        self.buttonBack.clicked.connect(clickBack)

        self.buttonDelete = QPushButton()
        self.buttonDelete.setText('Очистить')
        self.buttonDelete.clicked.connect(clickClear)


    def ClearData(self,text):
        a = text
        if a == 'adminBetter':
            self.flag = True
        if a is None or a !='adminBetter':
            self.flag = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Clear()
    sys.exit(app.exec())

