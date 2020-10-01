# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(495, 420)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboSerial = QtWidgets.QComboBox(self.centralwidget)
        self.comboSerial.setGeometry(QtCore.QRect(0, 20, 231, 22))
        self.comboSerial.setObjectName("comboSerial")
        self.btnConnect = QtWidgets.QPushButton(self.centralwidget)
        self.btnConnect.setGeometry(QtCore.QRect(250, 20, 75, 23))
        self.btnConnect.setObjectName("btnConnect")
        self.listData = QtWidgets.QListWidget(self.centralwidget)
        self.listData.setGeometry(QtCore.QRect(20, 180, 256, 192))
        self.listData.setObjectName("listData")
        self.labelClock = QtWidgets.QLabel(self.centralwidget)
        self.labelClock.setGeometry(QtCore.QRect(20, 80, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.labelClock.setFont(font)
        self.labelClock.setObjectName("labelClock")
        self.btnStart = QtWidgets.QPushButton(self.centralwidget)
        self.btnStart.setGeometry(QtCore.QRect(20, 150, 75, 23))
        self.btnStart.setObjectName("btnStart")
        self.btnStop = QtWidgets.QPushButton(self.centralwidget)
        self.btnStop.setGeometry(QtCore.QRect(120, 150, 75, 23))
        self.btnStop.setObjectName("btnStop")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnConnect.setText(_translate("MainWindow", "Connect"))
        self.labelClock.setText(_translate("MainWindow", "00:00:02.323"))
        self.btnStart.setText(_translate("MainWindow", "Start"))
        self.btnStop.setText(_translate("MainWindow", "Stop"))
