# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'agecolor.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from agefcn import agefcn
from addagetodb import addagetodb
import sqlite3

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):

    def showDays(self):
        months = {
            "JANUARY": 31, "FEBRUARY": 29, "MARCH": 31, "APRIL": 30, "MAY": 31,
            "JUNE": 30, "JULY": 31, "AUGUST": 31, "SEPTEMBER": 30, "OCTOBER": 31,
            "NOVEMBER": 30, "DECEMBER": 31
        }

        month = self.month_comboBox.currentText()

        for i in months:
            if (i == month):
                days = months[i]

        self.day_comboBox.clear()
        for i in range(1, days + 1):
            self.day_comboBox.addItem(str(i))

    def showMonths(self):
        monthsList = [
            "JANUARY", "FEBRUARY", "MARCH", "APRIL", "MAY", "JUNE", "JULY",
            "AUGUST", "SEPTEMBER", "OCTOBER", "NOVEMBER", "DECEMBER"
        ]

        self.month_comboBox.clear()
        for i in monthsList:
            self.month_comboBox.addItem(i)

    def calculate(self):
        name = self.lineEdit.text()
        year = self.year_comboBox.currentText()
        month = self.month_comboBox.currentText()
        day = self.day_comboBox.currentText()

        if (len(name) == 0 or len(year) == 0 or len(month) == 0 or len(day) == 0):
            self.calculate_label.setText(" CHOOSE CORRECT VALUES MEN!!! ")
        else:
            self.dt = agefcn(name, int(year), month, int(day))
            text = " YOU ARE " + str(self.dt[0][1]) + " YEARS AND " + str(self.dt[0][2]) + " DAYS OLD. "
            self.calculate_label.setText(text)

    def saveToDb(self):
        try:
            con = sqlite3.connect('agedata.sqlite')
            cur = con.cursor()

            name = self.lineEdit.text()
            year = self.year_comboBox.currentText()
            month = self.month_comboBox.currentText()
            day = self.day_comboBox.currentText()

            data = agefcn(name, int(year), month, int(day))
            addagetodb(data)

            con.commit()
            cur.close()
            con.close()
        except IOError as Err:
            print("Error somewhere: " + str(Err))

    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(569, 301)
        Dialog.setAutoFillBackground(False)
        Dialog.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 0);"))
        Dialog.setModal(False)

        self.year_comboBox = QtGui.QComboBox(Dialog)
        self.year_comboBox.setGeometry(QtCore.QRect(20, 120, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.year_comboBox.setFont(font)
        self.year_comboBox.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.year_comboBox.setObjectName(_fromUtf8("year_comboBox"))

        for i in range(2016, 1919, -1):
            self.year_comboBox.addItem(str(i))

        ##########     ComboBox Event    #########
        self.year_comboBox.activated.connect(self.showMonths)
        ##########################################

        self.year_label = QtGui.QLabel(Dialog)
        self.year_label.setGeometry(QtCore.QRect(20, 80, 111, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Big John"))
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.year_label.setFont(font)
        self.year_label.setStyleSheet(_fromUtf8("color: rgb(0, 0, 127);"))
        self.year_label.setAlignment(QtCore.Qt.AlignCenter)
        self.year_label.setObjectName(_fromUtf8("year_label"))

        self.day_comboBox = QtGui.QComboBox(Dialog)
        self.day_comboBox.setGeometry(QtCore.QRect(430, 120, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.day_comboBox.setFont(font)
        self.day_comboBox.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.day_comboBox.setObjectName(_fromUtf8("day_comboBox"))

        self.month_comboBox = QtGui.QComboBox(Dialog)
        self.month_comboBox.setGeometry(QtCore.QRect(220, 120, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.month_comboBox.setFont(font)
        self.month_comboBox.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.month_comboBox.setObjectName(_fromUtf8("month_comboBox"))

        ##########     ComboBox Event     ########
        self.month_comboBox.activated.connect(self.showDays)
        ##########################################

        self.calculate_Button = QtGui.QPushButton(Dialog)
        self.calculate_Button.setGeometry(QtCore.QRect(20, 180, 111, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Big John"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.calculate_Button.setFont(font)
        self.calculate_Button.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 127);\n"
"color:rgb(255, 255, 0);"))
        self.calculate_Button.setObjectName(_fromUtf8("calculate_Button"))

        ##########     Button Event     ##########
        self.calculate_Button.clicked.connect(self.calculate)
        ##########################################

        self.calculate_label = QtGui.QLabel(Dialog)
        self.calculate_label.setGeometry(QtCore.QRect(150, 182, 391, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.calculate_label.setFont(font)
        self.calculate_label.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.calculate_label.setText(_fromUtf8(""))
        self.calculate_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.calculate_label.setObjectName(_fromUtf8("calculate_label"))

        self.savetodb_Button = QtGui.QPushButton(Dialog)
        self.savetodb_Button.setGeometry(QtCore.QRect(190, 240, 171, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Big John"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.savetodb_Button.setFont(font)
        self.savetodb_Button.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 127);\n"
"color:rgb(255, 255, 0);"))
        self.savetodb_Button.setDefault(False)
        self.savetodb_Button.setFlat(False)
        self.savetodb_Button.setObjectName(_fromUtf8("savetodb_Button"))

        ##########     Button Event     ##########
        self.savetodb_Button.clicked.connect(self.saveToDb)
        ##########################################

        self.month_label = QtGui.QLabel(Dialog)
        self.month_label.setGeometry(QtCore.QRect(220, 80, 111, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Big John"))
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.month_label.setFont(font)
        self.month_label.setStyleSheet(_fromUtf8("color: rgb(0, 0, 127);"))
        self.month_label.setAlignment(QtCore.Qt.AlignCenter)
        self.month_label.setObjectName(_fromUtf8("month_label"))

        self.day_label = QtGui.QLabel(Dialog)
        self.day_label.setGeometry(QtCore.QRect(430, 80, 111, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Big John"))
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.day_label.setFont(font)
        self.day_label.setStyleSheet(_fromUtf8("color: rgb(0, 0, 127);\n"
""))
        self.day_label.setAlignment(QtCore.Qt.AlignCenter)
        self.day_label.setObjectName(_fromUtf8("day_label"))

        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(150, 30, 391, 31))
        self.lineEdit.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))

        self.entername_label = QtGui.QLabel(Dialog)
        self.entername_label.setGeometry(QtCore.QRect(20, 30, 111, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Big John"))
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.entername_label.setFont(font)
        self.entername_label.setStyleSheet(_fromUtf8("color: rgb(0, 0, 127);"))
        self.entername_label.setAlignment(QtCore.Qt.AlignCenter)
        self.entername_label.setObjectName(_fromUtf8("year_label_2"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "AGE CALCULATOR", None))
        self.year_label.setText(_translate("Dialog", "SELECT YEAR", None))
        self.calculate_Button.setText(_translate("Dialog", "CALCULATE", None))
        self.savetodb_Button.setText(_translate("Dialog", "SAVE TO DATABASE", None))
        self.month_label.setText(_translate("Dialog", "SELECT MONTH", None))
        self.day_label.setText(_translate("Dialog", "SELECT DAY", None))
        self.entername_label.setText(_translate("Dialog", "ENTER NAME:", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
