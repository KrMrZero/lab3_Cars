from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

from Names import Name
import WindowCreate
import WindowChange
import WindowDelete
import WindowSearch
import WindowClear
import Test



class Main(QWidget):
    def __init__(self):
        super().__init__()

        # Обнуление выделенной ячейки
        with open(f'Parametrs/nomer.txt', 'w', encoding='utf-8') as file:
            file.readable()
        file.close()

        # Обнуление всех пааметров в файлах
        for i in range(0, 8):
            with open(f'Parametrs/{i}.txt', 'w', encoding='utf-8') as file:
                file.readable()
            file.close()

        Test.UnitTest().TestDoors()


        self.setWindowTitle("Авто-база")
        self.resize(1500,500)

        self.CreateTable()

        self.layout = QGridLayout()
        self.layout.addWidget(self.table,0,0,1,5)
        self.layout.addWidget(self.button, 1, 0)
        self.layout.addWidget(self.button2, 1, 1)
        self.layout.addWidget(self.button3, 1, 2)
        self.layout.addWidget(self.button4, 1, 3)
        self.layout.addWidget(self.button5, 1, 4)
        self.setLayout(self.layout)

        # Получение значений из выделенной области
        self.setup_connection()

        self.show()

    def CreateTable(self):

        def clickCreate():
            self.window = WindowCreate.Create()
            self.window.show()
            self.close()

        def clickChange():
            self.window =  WindowChange.Change()
            self.window.show()
            self.close()

        def clickDelete():
            self.window = WindowDelete.Delete()
            self.window.show()
            self.close()

        def clickSearch():
            self.window = WindowSearch.myWindow()
            self.window.show()
            self.close()

        def clickClear():
            self.window = WindowClear.Clear()
            self.window.show()
            self.close()

        str = Name.allTable
        # Количество строк и колонок
        self.table = QTableWidget(len(str),len(Name.headers))
        self.table.clear()
        # Имя колонок
        self.table.setHorizontalHeaderLabels(Name.headers)
        # Запрет редактирования таблицы
        self.table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        # Заполнение таблицы
        if len(str) != 0:
            for i in range(len(str)):
                a= str[i].split(' ')
                for j in range(len(a)):
                    # self.table.setColumnWidth(j, 100)
                    a[j]= a[j].replace('\n','').replace('_',' ')
                    self.table.setItem(i, j, QTableWidgetItem(f'{a[j]}'))


        # Авторасстягивание таюлицы по ширине
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.button = QPushButton()
        self.button.setText('Создать')
        self.button.clicked.connect(clickCreate)

        self.button2 = QPushButton()
        self.button2.setText('Изменить')
        self.button2.clicked.connect(clickChange)

        self.button3 = QPushButton()
        self.button3.setText('Удалить')
        self.button3.clicked.connect(clickDelete)


        self.button4 = QPushButton()
        self.button4.setText('Поиск')
        self.button4.clicked.connect(clickSearch)


        self.button5 = QPushButton()
        self.button5.setText('Очистить базу')
        self.button5.clicked.connect(clickClear)


    # Оновление таблицы
    def updateTable(self):
        with open('cars.txt', 'r', encoding='utf-8') as file:
            allTable = file.readlines()
        file.close()
        new_str = allTable

        if len(Name.allTable) < len(new_str):
            # Дополнение таблицы
            # Добавление пустой строки
            for i in range(len(new_str)-len(Name.allTable)):
                self.rowPosition = self.table.rowCount()
                self.table.insertRow(self.rowPosition)

            for j in range(len(new_str)-len(Name.allTable)):
                a = new_str[len(Name.allTable)+j].split(' ')
                for i in range(len(a)):
                    self.table.setItem(len(Name.allTable)+j,i,QTableWidgetItem(f'{a[i]}'))
            Name.allTable = new_str

            avtoNomers = []
            for i in range(len(new_str)):
                with open('cars.txt', 'r', encoding='utf-8') as file:
                    str = file.readlines()
                file.close()
                a = str[i].split(' ')
                avtoNomers.append(a[0])
            Name.avtoNomers = avtoNomers

        elif len(new_str)==0:
            self.table.clear()

        elif len(Name.allTable) > len(new_str):
            self.table.clear()
            for j in range(len(new_str)):
                a = new_str[i].split(' ')
                for i in range(len(a)):
                    self.table.setItem(j,i,QTableWidgetItem(f'{a[i]}'))
            Name.allTable = new_str


        else:
            # Обновление таблицы
            self.table.clear()
            for i in range(len(new_str)):
                a = new_str[i].split(' ')
                for j in range(len(a)):
                    self.table.setItem(i, j, QTableWidgetItem(f'{a[j]}'))


    # Получение значений из выделенной области
    # -----------
    def setup_connection(self):
        # connected function to item selection changed trigger of my_table
        self.table.itemSelectionChanged.connect(self.action_report_in_view)

    def action_report_in_view(self, *arg):
        values = []
        for selected_item in self.table.selectedItems():
            # create [item from col 0, item from col 1]
            values.insert(selected_item.column(), selected_item.text())
        self.add_to_log(values)

    def add_to_log(self, value):
        with open('Parametrs/nomer.txt', 'w', encoding='utf-8') as file:
            try:
                # self.reportView.appendPlainText(str(value))
                file.write(value[0])
            except(IndexError):
                file.readable()
    # ------------------


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Main()
    sys.exit(app.exec())