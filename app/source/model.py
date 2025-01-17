# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'model.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(380, 505)
        Dialog.setStyleSheet("background: #303133;")
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(False)
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(-2, 0, 391, 511))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.tabWidget.setFont(font)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet("background: #303133;\n"
" color:white")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setIconSize(QtCore.QSize(38, 39))
        self.tabWidget.setElideMode(QtCore.Qt.ElideLeft)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabBarAutoHide(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.line_2 = QtWidgets.QFrame(self.tab)
        self.line_2.setGeometry(QtCore.QRect(0, 379, 389, 3))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.pushButton_cancel = QtWidgets.QPushButton(self.tab)
        self.pushButton_cancel.setGeometry(QtCore.QRect(260, 430, 100, 31))
        self.pushButton_cancel.setStyleSheet(":active{\n"
"font-size: 13px;\n"
"border: 2px solid gold;\n"
"background: #262729;\n"
"color: orange;\n"
"border-radius: 3px;\n"
"}\n"
":hover {\n"
"color:rgb(255, 0, 127);\n"
"border: 2px solid rgb(185, 0, 92)\n"
"}\n"
":focus {\n"
"color:rgb(31, 213, 183);\n"
"border:2ps solid rgb(31, 213, 183);\n"
"}")
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.field_9 = QtWidgets.QPushButton(self.tab)
        self.field_9.setGeometry(QtCore.QRect(260, 260, 100, 100))
        self.field_9.setStyleSheet(":enabled{\n"
"\n"
"font-size: 40px; \n"
"text-align:center;\n"
"font: 26pt \"Verdana\";\n"
"font-weight:100 !important;\n"
"background:#222222;\n"
"color: #b1361e !important;\n"
"border: 1px solid black;\n"
"border-radius: 3px;\n"
"\n"
"}\n"
"\n"
":hover {\n"
"border: 1px solid #866cc7;\n"
"}\n"
"")
        self.field_9.setText("")
        self.field_9.setCheckable(True)
        self.field_9.setObjectName("field_9")
        self.field_2 = QtWidgets.QPushButton(self.tab)
        self.field_2.setGeometry(QtCore.QRect(140, 20, 100, 100))
        self.field_2.setStyleSheet(":enabled{\n"
"font-size: 40px; \n"
"text-align:center;\n"
"font: 26pt \"Verdana\";\n"
"font-weight:100 !important;\n"
"background:#222222;\n"
"color: #b1361e !important;\n"
"border: 1px solid black;\n"
"border-radius: 3px;\n"
"\n"
"}\n"
"\n"
":hover {\n"
"border: 1px solid #866cc7;\n"
"}\n"
"")
        self.field_2.setText("")
        self.field_2.setCheckable(True)
        self.field_2.setObjectName("field_2")
        self.field_7 = QtWidgets.QPushButton(self.tab)
        self.field_7.setGeometry(QtCore.QRect(20, 260, 100, 100))
        self.field_7.setStyleSheet(":enabled{\n"
"font-size: 40px; \n"
"text-align:center;\n"
"font: 26pt \"Verdana\";\n"
"font-weight:100 !important;\n"
"background:#222222;\n"
"color: #b1361e !important;\n"
"border: 1px solid black;\n"
"border-radius: 3px;\n"
"\n"
"}\n"
"\n"
":hover {\n"
"border: 1px solid #866cc7;\n"
"}\n"
"")
        self.field_7.setText("")
        self.field_7.setCheckable(True)
        self.field_7.setObjectName("field_7")
        self.field_3 = QtWidgets.QPushButton(self.tab)
        self.field_3.setGeometry(QtCore.QRect(260, 20, 100, 100))
        self.field_3.setStyleSheet(":enabled{\n"
"font-size: 40px; \n"
"text-align:center;\n"
"font: 26pt \"Verdana\";\n"
"font-weight:100 !important;\n"
"background:#222222;\n"
"color: #b1361e !important;\n"
"border: 1px solid black;\n"
"border-radius: 3px;\n"
"\n"
"}\n"
"\n"
":hover {\n"
"border: 1px solid #866cc7;\n"
"}\n"
"")
        self.field_3.setText("")
        self.field_3.setCheckable(True)
        self.field_3.setObjectName("field_3")
        self.field_8 = QtWidgets.QPushButton(self.tab)
        self.field_8.setGeometry(QtCore.QRect(140, 260, 100, 100))
        self.field_8.setStyleSheet(":enabled{\n"
"font-size: 40px; \n"
"text-align:center;\n"
"font: 26pt \"Verdana\";\n"
"font-weight:100 !important;\n"
"background:#222222;\n"
"color: #b1361e !important;\n"
"border: 1px solid black;\n"
"border-radius: 3px;\n"
"\n"
"}\n"
"\n"
":hover {\n"
"border: 1px solid #866cc7;\n"
"}\n"
"")
        self.field_8.setText("")
        self.field_8.setCheckable(True)
        self.field_8.setObjectName("field_8")
        self.label_winner = QtWidgets.QLabel(self.tab)
        self.label_winner.setGeometry(QtCore.QRect(30, 390, 211, 21))
        font = QtGui.QFont()
        font.setFamily("Meiryo")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.label_winner.setFont(font)
        self.label_winner.setStyleSheet("color: rgb(160, 229, 0)")
        self.label_winner.setText("")
        self.label_winner.setObjectName("label_winner")
        self.field_5 = QtWidgets.QPushButton(self.tab)
        self.field_5.setGeometry(QtCore.QRect(140, 140, 100, 100))
        self.field_5.setStyleSheet(":enabled{\n"
"font-size: 40px; \n"
"text-align:center;\n"
"font: 26pt \"Verdana\";\n"
"font-weight:100 !important;\n"
"background:#222222;\n"
"color: #b1361e !important;\n"
"border: 1px solid black;\n"
"border-radius: 3px;\n"
"\n"
"}\n"
"\n"
":hover {\n"
"border: 1px solid #866cc7;\n"
"}\n"
"")
        self.field_5.setText("")
        self.field_5.setCheckable(True)
        self.field_5.setObjectName("field_5")
        self.pushButton_restart = QtWidgets.QPushButton(self.tab)
        self.pushButton_restart.setGeometry(QtCore.QRect(20, 430, 221, 31))
        self.pushButton_restart.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.pushButton_restart.setStyleSheet(":active{\n"
"font-size: 13px;\n"
"border: 2px solid gold;\n"
"background: #262729;\n"
"color: orange;\n"
"border-radius: 3px;\n"
"}\n"
":hover {\n"
"color:rgb(255, 0, 127);\n"
"border: 2px solid rgb(185, 0, 92)\n"
"}")
        self.pushButton_restart.setObjectName("pushButton_restart")
        self.field_4 = QtWidgets.QPushButton(self.tab)
        self.field_4.setGeometry(QtCore.QRect(20, 140, 100, 100))
        self.field_4.setStyleSheet(":enabled{\n"
"font-size: 40px; \n"
"text-align:center;\n"
"font: 26pt \"Verdana\";\n"
"font-weight:100 !important;\n"
"background:#222222;\n"
"color: #b1361e !important;\n"
"border: 1px solid black;\n"
"border-radius: 3px;\n"
"\n"
"}\n"
"\n"
":hover {\n"
"border: 1px solid #866cc7;\n"
"}\n"
"")
        self.field_4.setText("")
        self.field_4.setCheckable(True)
        self.field_4.setObjectName("field_4")
        self.field_6 = QtWidgets.QPushButton(self.tab)
        self.field_6.setGeometry(QtCore.QRect(260, 140, 100, 100))
        self.field_6.setStyleSheet(":enabled{\n"
"font-size: 40px; \n"
"text-align:center;\n"
"font: 26pt \"Verdana\";\n"
"font-weight:100 !important;\n"
"background:#222222;\n"
"color: #b1361e !important;\n"
"border: 1px solid black;\n"
"border-radius: 3px;\n"
"\n"
"}\n"
"\n"
":hover {\n"
"border: 1px solid #866cc7;\n"
"}\n"
"")
        self.field_6.setText("")
        self.field_6.setCheckable(True)
        self.field_6.setObjectName("field_6")
        self.field_1 = QtWidgets.QPushButton(self.tab)
        self.field_1.setEnabled(True)
        self.field_1.setGeometry(QtCore.QRect(20, 20, 100, 100))
        self.field_1.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(26)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(12)
        self.field_1.setFont(font)
        self.field_1.setStyleSheet(":enabled{\n"
"font-size: 40px; \n"
"text-align:center;\n"
"font: 26pt \"Verdana\";\n"
"font-weight:100 !important;\n"
"background:#222222;\n"
"color: #b1361e !important;\n"
"border: 1px solid black;\n"
"border-radius: 3px;\n"
"\n"
"}\n"
"\n"
":hover {\n"
"border: 1px solid #866cc7;\n"
"}\n"
"")
        self.field_1.setText("")
        self.field_1.setCheckable(True)
        self.field_1.setChecked(False)
        self.field_1.setAutoRepeat(False)
        self.field_1.setAutoExclusive(False)
        self.field_1.setAutoDefault(True)
        self.field_1.setDefault(False)
        self.field_1.setFlat(False)
        self.field_1.setObjectName("field_1")
        self.line_3 = QtWidgets.QFrame(self.tab)
        self.line_3.setGeometry(QtCore.QRect(-3, 419, 389, 3))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(220, 210, 151, 251))
        font = QtGui.QFont()
        font.setPointSize(5)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:silver")
        self.label_2.setObjectName("label_2")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.tab_2)
        self.commandLinkButton.setEnabled(True)
        self.commandLinkButton.setGeometry(QtCore.QRect(19, 40, 31, 41))
        self.commandLinkButton.setAutoFillBackground(False)
        self.commandLinkButton.setAutoDefault(False)
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.label = QtWidgets.QLabel(self.tab_2)
        self.label.setGeometry(QtCore.QRect(51, 54, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Miriam")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("color:silver")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit.setGeometry(QtCore.QRect(113, 46, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("border: 0px; color: orange")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(113, 107, 241, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("border: 0px; color: orange")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(10, 30, 81, 61))
        self.label_4.setStyleSheet("background: rgba()")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setGeometry(QtCore.QRect(53, 110, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Miriam")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color:silver")
        self.label_5.setObjectName("label_5")
        self.commandLinkButton_2 = QtWidgets.QCommandLinkButton(self.tab_2)
        self.commandLinkButton_2.setEnabled(True)
        self.commandLinkButton_2.setGeometry(QtCore.QRect(20, 95, 31, 41))
        self.commandLinkButton_2.setAutoFillBackground(False)
        self.commandLinkButton_2.setAutoDefault(False)
        self.commandLinkButton_2.setObjectName("commandLinkButton_2")
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(10, 90, 81, 71))
        self.label_3.setStyleSheet("background: rgba()")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Крестики нолики"))
        self.pushButton_cancel.setText(_translate("Dialog", "Выход"))
        self.pushButton_restart.setText(_translate("Dialog", "Начать заново"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "► Игра  "))
        self.label_2.setText(_translate("Dialog", "░░█▀░░░░░░░░░░░▀▀███████░░░░\n"
"░░█▌░░░░░░░░░░░░░░░▀██████░░░\n"
"░█▌░░░░░░░░░░░░░░░░███████▌░░\n"
"░█░░░░░░░░░░░░░░░░░████████░░\n"
"▐▌░░░░░░░░░░░░░░░░░▀██████▌░░\n"
"░▌▄███▌░░░░▀████▄░░░░▀████▌░░\n"
"▐▀▀▄█▄░▌░░░▄██▄▄▄▀░░░░████▄▄░\n"
"▐░▀░░═▐░░░░░░══░░▀░░░░▐▀░▄▀▌▌\n"
"▐░░░░░▌░░░░░░░░░░░░░░░▀░▀░░▌▌\n"
"▐░░░▄▀░░░▀░▌░░░░░░░░░░░░▌█░▌▌\n"
"░▌░░▀▀▄▄▀▀▄▌▌░░░░░░░░░░▐░▀▐▐░\n"
"░▌░░▌░▄▄▄▄░░░▌░░░░░░░░▐░░▀▐░░\n"
"░█░▐▄██████▄░▐░░░░░░░░█▀▄▄▀░░\n"
"░▐░▌▌░░░░░░▀▀▄▐░░░░░░█▌░░░░░░\n"
"░░█░░▄▀▀▀▀▄░▄═╝▄░░░▄▀░▌░░░░░░\n"
"░░░▌▐░░░░░░▌░▀▀░░▄▀░░▐░░░░░░░\n"
"░░░▀▄░░░░░░░░░▄▀▀░░░░█░░░░░░░\n"
"░░░▄█▄▄▄▄▄▄▄▀▀░░░░░░░▌▌░░░░░░\n"
"░░▄▀▌▀▌░░░░░░░░░░░░░▄▀▀▄░░░░░\n"
"▄▀░░▌░▀▄░░░░░░░░░░▄▀░░▌░▀▄░░░\n"
"░░░░▌█▄▄▀▄░░░░░░▄▀░░░░▌░░░▌▄▄\n"
"░░░▄▐██████▄▄░▄▀░░▄▄▄▄▌░░░░▄░\n"
"░░▄▌████████▄▄▄███████▌░░░░░▄\n"
"░▄▀░██████████████████▌▀▄░░░░\n"
"▀░░░█████▀▀░░░▀███████░░░▀▄░░\n"
"░░░░▐█▀░░░▐░░░░░▀████▌░░░░▀▄░\n"
"░░░░░░▌░░░▐░░░░▐░░▀▀█░░░░░░░▀\n"
"░░░░░░▐░░░░▌░░░▐░░░░░▌░░░░░░░\n"
"░╔╗║░╔═╗░═╦═░░░░░╔╗░░╔═╗░╦═╗░\n"
"░║║║░║░║░░║░░░░░░╠╩╗░╠═╣░║░║░\n"
"░║╚╝░╚═╝░░║░░░░░░╚═╝░║░║░╩═╝░\n"
""))
        self.commandLinkButton.setText(_translate("Dialog", "CommandLinkButton"))
        self.label.setText(_translate("Dialog", "GitHub - "))
        self.lineEdit.setText(_translate("Dialog", "https://github.com/Developer-Python"))
        self.lineEdit_2.setText(_translate("Dialog", "https://vk.com/fullstack02"))
        self.label_5.setText(_translate("Dialog", "VK      - "))
        self.commandLinkButton_2.setText(_translate("Dialog", "CommandLinkButton"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", " Автор™ "))
