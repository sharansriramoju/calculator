# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculator2.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.p1 = QtWidgets.QPushButton(self.centralwidget)
        self.p1.setGeometry(QtCore.QRect(90, 80, 51, 41))
        self.p1.setObjectName("p1")
        self.p2 = QtWidgets.QPushButton(self.centralwidget)
        self.p2.setGeometry(QtCore.QRect(150, 80, 51, 41))
        self.p2.setObjectName("p2")
        self.p7 = QtWidgets.QPushButton(self.centralwidget)
        self.p7.setGeometry(QtCore.QRect(90, 180, 51, 41))
        self.p7.setObjectName("p7")
        self.p0 = QtWidgets.QPushButton(self.centralwidget)
        self.p0.setGeometry(QtCore.QRect(150, 230, 51, 41))
        self.p0.setObjectName("p0")
        self.p9 = QtWidgets.QPushButton(self.centralwidget)
        self.p9.setGeometry(QtCore.QRect(210, 180, 51, 41))
        self.p9.setObjectName("p9")
        self.p8 = QtWidgets.QPushButton(self.centralwidget)
        self.p8.setGeometry(QtCore.QRect(150, 180, 51, 41))
        self.p8.setObjectName("p8")
        self.p6 = QtWidgets.QPushButton(self.centralwidget)
        self.p6.setGeometry(QtCore.QRect(210, 130, 51, 41))
        self.p6.setObjectName("p6")
        self.p5 = QtWidgets.QPushButton(self.centralwidget)
        self.p5.setGeometry(QtCore.QRect(150, 130, 51, 41))
        self.p5.setObjectName("p5")
        self.p4 = QtWidgets.QPushButton(self.centralwidget)
        self.p4.setGeometry(QtCore.QRect(90, 130, 51, 41))
        self.p4.setObjectName("p4")
        self.p3 = QtWidgets.QPushButton(self.centralwidget)
        self.p3.setGeometry(QtCore.QRect(210, 80, 51, 41))
        self.p3.setObjectName("p3")
        self.pp = QtWidgets.QPushButton(self.centralwidget)
        self.pp.setGeometry(QtCore.QRect(90, 230, 51, 41))
        self.pp.setObjectName("pp")
        self.p_prod = QtWidgets.QPushButton(self.centralwidget)
        self.p_prod.setGeometry(QtCore.QRect(330, 80, 51, 41))
        self.p_prod.setObjectName("p_prod")
        self.calculation = QtWidgets.QLineEdit(self.centralwidget)
        self.calculation.setGeometry(QtCore.QRect(100, 330, 171, 41))
        self.calculation.setObjectName("calculation")
        self.p_sub = QtWidgets.QPushButton(self.centralwidget)
        self.p_sub.setGeometry(QtCore.QRect(330, 180, 51, 41))
        self.p_sub.setObjectName("p_sub")
        self.result = QtWidgets.QLineEdit(self.centralwidget)
        self.result.setGeometry(QtCore.QRect(520, 140, 171, 41))
        self.result.setObjectName("result")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(520, 100, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.p_add = QtWidgets.QPushButton(self.centralwidget)
        self.p_add.setGeometry(QtCore.QRect(330, 130, 51, 41))
        self.p_add.setObjectName("p_add")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.p1.setText(_translate("MainWindow", "1"))
        self.p2.setText(_translate("MainWindow", "2"))
        self.p7.setText(_translate("MainWindow", "7"))
        self.p0.setText(_translate("MainWindow", "0"))
        self.p9.setText(_translate("MainWindow", "9"))
        self.p8.setText(_translate("MainWindow", "8"))
        self.p6.setText(_translate("MainWindow", "6"))
        self.p5.setText(_translate("MainWindow", "5"))
        self.p4.setText(_translate("MainWindow", "4"))
        self.p3.setText(_translate("MainWindow", "3"))
        self.pp.setText(_translate("MainWindow", "."))
        self.p_prod.setText(_translate("MainWindow", "*"))
        self.p_sub.setText(_translate("MainWindow", "-"))
        self.label.setText(_translate("MainWindow", "result"))
        self.p_add.setText(_translate("MainWindow", "+"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
