# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt6 UI code generator 6.6.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(801, 799)
        MainWindow.setMinimumSize(QtCore.QSize(801, 799))
        MainWindow.setMaximumSize(QtCore.QSize(801, 799))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(parent=self.centralwidget)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 764, 759))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.d20_terrain = QtWidgets.QLineEdit(parent=self.scrollAreaWidgetContents)
        self.d20_terrain.setMaximumSize(QtCore.QSize(211, 20))
        self.d20_terrain.setObjectName("d20_terrain")
        self.gridLayout_2.addWidget(self.d20_terrain, 1, 3, 1, 1)
        self.clear = QtWidgets.QPushButton(parent=self.scrollAreaWidgetContents)
        self.clear.setMaximumSize(QtCore.QSize(131, 61))
        self.clear.setObjectName("clear")
        self.gridLayout_2.addWidget(self.clear, 0, 1, 2, 1)
        self.gen_creature = QtWidgets.QPushButton(parent=self.scrollAreaWidgetContents)
        self.gen_creature.setMaximumSize(QtCore.QSize(261, 23))
        self.gen_creature.setObjectName("gen_creature")
        self.gridLayout_2.addWidget(self.gen_creature, 2, 2, 1, 1)
        self.gen_all = QtWidgets.QPushButton(parent=self.scrollAreaWidgetContents)
        self.gen_all.setMaximumSize(QtCore.QSize(171, 61))
        self.gen_all.setObjectName("gen_all")
        self.gridLayout_2.addWidget(self.gen_all, 0, 0, 2, 1)
        self.gen_terrain = QtWidgets.QPushButton(parent=self.scrollAreaWidgetContents)
        self.gen_terrain.setMaximumSize(QtCore.QSize(261, 23))
        self.gen_terrain.setObjectName("gen_terrain")
        self.gridLayout_2.addWidget(self.gen_terrain, 1, 2, 1, 1)
        self.d20_creature = QtWidgets.QLineEdit(parent=self.scrollAreaWidgetContents)
        self.d20_creature.setMaximumSize(QtCore.QSize(211, 20))
        self.d20_creature.setObjectName("d20_creature")
        self.gridLayout_2.addWidget(self.d20_creature, 2, 3, 1, 1)
        self.description = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.description.setMaximumSize(QtCore.QSize(761, 111))
        self.description.setStyleSheet("background-color: rgb(129, 243, 255);")
        self.description.setText("")
        self.description.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.description.setWordWrap(True)
        self.description.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.LinksAccessibleByMouse|QtCore.Qt.TextInteractionFlag.TextSelectableByMouse)
        self.description.setObjectName("description")
        self.gridLayout_2.addWidget(self.description, 5, 0, 1, 4)
        self.explanation = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.explanation.setMaximumSize(QtCore.QSize(761, 16777215))
        self.explanation.setAutoFillBackground(False)
        self.explanation.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.explanation.setWordWrap(True)
        self.explanation.setIndent(-1)
        self.explanation.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.LinksAccessibleByMouse|QtCore.Qt.TextInteractionFlag.TextSelectableByMouse)
        self.explanation.setObjectName("explanation")
        self.gridLayout_2.addWidget(self.explanation, 6, 0, 1, 4)
        self.title = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.title.setMaximumSize(QtCore.QSize(761, 51))
        self.title.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.LinksAccessibleByMouse|QtCore.Qt.TextInteractionFlag.TextSelectableByMouse)
        self.title.setObjectName("title")
        self.gridLayout_2.addWidget(self.title, 4, 0, 1, 4)
        self.category = QtWidgets.QComboBox(parent=self.scrollAreaWidgetContents)
        self.category.setObjectName("category")
        self.category.addItem("")
        self.category.addItem("")
        self.gridLayout_2.addWidget(self.category, 0, 3, 1, 1)
        self.gen_other = QtWidgets.QPushButton(parent=self.scrollAreaWidgetContents)
        self.gen_other.setMaximumSize(QtCore.QSize(261, 23))
        self.gen_other.setObjectName("gen_other")
        self.gridLayout_2.addWidget(self.gen_other, 0, 2, 1, 1)
        self.d20_all = QtWidgets.QLineEdit(parent=self.scrollAreaWidgetContents)
        self.d20_all.setMaximumSize(QtCore.QSize(169, 20))
        self.d20_all.setObjectName("d20_all")
        self.gridLayout_2.addWidget(self.d20_all, 2, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Random Encounter Generator"))
        self.d20_terrain.setPlaceholderText(_translate("MainWindow", "If you manually rolled, place it here."))
        self.clear.setText(_translate("MainWindow", "Clear"))
        self.gen_creature.setText(_translate("MainWindow", "Generate Creature"))
        self.gen_all.setText(_translate("MainWindow", "Generate Encounter"))
        self.gen_terrain.setText(_translate("MainWindow", "Generate Terrain"))
        self.d20_creature.setPlaceholderText(_translate("MainWindow", "If you manually rolled, place it here."))
        self.explanation.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.title.setText(_translate("MainWindow", "<html><head/><body><p><br/></p><p><br/></p></body></html>"))
        self.category.setItemText(0, _translate("MainWindow", "Underdark"))
        self.category.setItemText(1, _translate("MainWindow", "The Silken Paths"))
        self.gen_other.setText(_translate("MainWindow", "Generate Illumination and Space"))
        self.d20_all.setPlaceholderText(_translate("MainWindow", "If you manually rolled, place it here."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
