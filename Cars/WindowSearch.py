from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import *
from PyQt5.QtCore import *



from Names import Name
import WindowCreate
import WindowChange
import WindowDelete
import WindowMain

class myWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(myWindow, self).__init__(parent)

        self.show()
        self.setWindowTitle("Поиск")
        self.setFixedSize(1050,500)


        def WM():
            self.window = WindowMain.Main()
            self.window.show()

            self.close()

        def clickChange():
            self.window =  WindowChange.Change()
            self.window.show()
            self.close()

        self.centralwidget  = QtWidgets.QWidget(self)
        self.lineEdit       = QtWidgets.QLineEdit(self.centralwidget)
        self.view           = QtWidgets.QTableView(self.centralwidget)
        self.comboBox       = QtWidgets.QComboBox(self.centralwidget)
        self.label          = QtWidgets.QLabel(self.centralwidget)
        self.buttonBack     = QtWidgets.QPushButton(self)
        self.button2        = QtWidgets.QPushButton(self)

        self.view.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)


        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.view, 1, 0, 1, 3)
        self.gridLayout.addWidget(self.comboBox, 0, 2, 1, 1)
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.buttonBack,2,0,1,2)
        self.gridLayout.addWidget(self.button2,2,2,1,1)

        self.setCentralWidget(self.centralwidget)
        self.label.setText("Regex Filter")


        self.model = QtGui.QStandardItemModel(self)





        str = Name.allTable
        head = Name.headers
        for rowName in range(len(str)):
            a = str[rowName].split(' ')
            for j in range(8):
                a[j] = a[j].replace('\n', '').replace('_', ' ')
            self.model.invisibleRootItem().appendRow(
                [   QtGui.QStandardItem("{0}".format(a[column]))
                    for column in range(len(head))
                    ]
                )
        # self.model.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        # self.model.horizontalHeader().setStretchLastSection(True)
        # self.model.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.proxy = QtCore.QSortFilterProxyModel(self)
        self.proxy.setSourceModel(self.model)

        self.view.setModel(self.proxy)
        self.comboBox.addItems(["Столбец №{0}".format(x) for x in range(self.model.columnCount())])

        self.lineEdit.textChanged.connect(self.on_lineEdit_textChanged)
        self.comboBox.currentIndexChanged.connect(self.on_comboBox_currentIndexChanged)

        self.horizontalHeader = self.view.horizontalHeader()
        self.horizontalHeader.sectionClicked.connect(self.on_view_horizontalHeader_sectionClicked)


        self.buttonBack.setText('Вернуться к базе машин')
        self.buttonBack.clicked.connect(WM)

        self.button2.setText('Изменить')
        self.button2.clicked.connect(clickChange)

    @QtCore.pyqtSlot(int)
    def on_view_horizontalHeader_sectionClicked(self, logicalIndex):
        self.logicalIndex   = logicalIndex
        self.menuValues     = QtWidgets.QMenu(self)
        self.signalMapper   = QtCore.QSignalMapper(self)

        self.comboBox.blockSignals(True)
        self.comboBox.setCurrentIndex(self.logicalIndex)
        self.comboBox.blockSignals(True)

        valuesUnique = [    self.model.item(row, self.logicalIndex).text()
                            for row in range(self.model.rowCount())
                            ]

        actionAll = QtWidgets.QAction("All", self)
        actionAll.triggered.connect(self.on_actionAll_triggered)
        self.menuValues.addAction(actionAll)
        self.menuValues.addSeparator()

        for actionNumber, actionName in enumerate(sorted(list(set(valuesUnique)))):
            action = QtWidgets.QAction(actionName, self)
            self.signalMapper.setMapping(action, actionNumber)
            action.triggered.connect(self.signalMapper.map)
            self.menuValues.addAction(action)

        self.signalMapper.mapped.connect(self.on_signalMapper_mapped)

        headerPos = self.view.mapToGlobal(self.horizontalHeader.pos())

        posY = headerPos.y() + self.horizontalHeader.height()
        posX = headerPos.x() + self.horizontalHeader.sectionPosition(self.logicalIndex)

        self.menuValues.exec_(QtCore.QPoint(posX, posY))

    @QtCore.pyqtSlot()
    def on_actionAll_triggered(self):
        filterColumn = self.logicalIndex
        filterString = QtCore.QRegExp(  "",
                                        QtCore.Qt.CaseInsensitive,
                                        QtCore.QRegExp.RegExp
                                        )

        self.proxy.setFilterRegExp(filterString)
        self.proxy.setFilterKeyColumn(filterColumn)

    @QtCore.pyqtSlot(int)
    def on_signalMapper_mapped(self, i):
        stringAction = self.signalMapper.mapping(i).text()
        filterColumn = self.logicalIndex
        filterString = QtCore.QRegExp(  stringAction,
                                        QtCore.Qt.CaseSensitive,
                                        QtCore.QRegExp.FixedString
                                        )

        self.proxy.setFilterRegExp(filterString)
        self.proxy.setFilterKeyColumn(filterColumn)

    @QtCore.pyqtSlot(str)
    def on_lineEdit_textChanged(self, text):
        search = QtCore.QRegExp(    text,
                                    QtCore.Qt.CaseInsensitive,
                                    QtCore.QRegExp.RegExp
                                    )

        self.proxy.setFilterRegExp(search)

    @QtCore.pyqtSlot(int)
    def on_comboBox_currentIndexChanged(self, index):
        self.proxy.setFilterKeyColumn(index)




if __name__ == "__main__":
    import sys

    app  = QtWidgets.QApplication(sys.argv)
    main = myWindow()
    sys.exit(app.exec_())



# def random_word():
#     letters = "abcdedfg"
#     word = "".join([choice(letters) for _ in range(randint(4, 7))])
#     return word
#
#
# class Widget(QWidget):
#     def __init__(self, *args, **kwargs):
#         QWidget.__init__(self, *args, **kwargs)
#         self.setLayout(QVBoxLayout())
#
#         tv1 = QTableView(self)
#         tv2 = QTableView(self)
#         model = QStandardItemModel(8, 4, self)
#         proxy = SortFilterProxyModel(self)
#         proxy.setSourceModel(model)
#         tv1.setModel(model)
#         tv2.setModel(proxy)
#         self.layout().addWidget(tv1)
#         self.layout().addWidget(tv2)
#
#         for i in range(model.rowCount()):
#             for j in range(model.columnCount()):
#                 item = QStandardItem()
#                 item.setData(random_word(), Qt.DisplayRole)
#                 model.setItem(i, j, item)
#
#         flayout = QFormLayout()
#         self.layout().addLayout(flayout)
#         for i in range(model.columnCount()):
#             le = QLineEdit(self)
#             flayout.addRow("column: {}".format(i), le)
#             le.textChanged.connect(lambda text, col=i:
#                                    proxy.setFilterByColumn(QRegExp(text, Qt.CaseSensitive, QRegExp.FixedString),
#                                                            col))


