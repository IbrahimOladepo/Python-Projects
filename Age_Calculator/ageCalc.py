# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ageCalcUi.ui'
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


    def showMonths(self):
        monthsList = [
            "JANUARY", "FEBRUARY", "MARCH", "APRIL", "MAY", "JUNE", "JULY",
            "AUGUST", "SEPTEMBER", "OCTOBER", "NOVEMBER", "DECEMBER"
        ]

        self.monthComboBox.clear()
        for i in monthsList:
            self.monthComboBox.addItem(i)

    def showDays(self):
        months = {
            "JANUARY": 31, "FEBRUARY": 29, "MARCH": 31, "APRIL": 30, "MAY": 31,
            "JUNE": 30, "JULY": 31, "AUGUST": 31, "SEPTEMBER": 30, "OCTOBER": 31,
            "NOVEMBER": 30, "DECEMBER": 31
        }

        month = self.monthComboBox.currentText()

        for i in months:
            if (i == month):
                days = months[i]

        self.dayComboBox.clear()
        for i in range(1, days + 1):
            self.dayComboBox.addItem(str(i))

    def calculate(self):
        name = self.nameLineEdit.text()
        year = self.yearComboBox.currentText()
        month = self.monthComboBox.currentText()
        day = self.dayComboBox.currentText()

        if (len(name) == 0 or len(year) == 0 or len(month) == 0 or len(day) == 0):
            self.displayLabel.setText(" CHOOSE CORRECT VALUES MEN!!! ")
        else:
            self.dt = agefcn(name, int(year), month, int(day))
            text = " YOU ARE " + str(self.dt[0][1]) + " YEARS AND " + str(self.dt[0][2]) + " DAYS OLD. "
            self.displayLabel.setText(text)

    def saveToDb(self):
        try:
            con = sqlite3.connect('agedata.sqlite')
            cur = con.cursor()

            name = self.nameLineEdit.text()
            year = self.yearComboBox.currentText()
            month = self.monthComboBox.currentText()
            day = self.dayComboBox.currentText()

            data = agefcn(name, int(year), month, int(day))
            addagetodb(data)
            self.displayLabel.setText(" SAVED TO DATABASE.")

            con.commit()
            cur.close()
            con.close()
        except IOError as Err:
            print("Error somewhere: " + str(Err))

    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(481, 381)
        font = QtGui.QFont()
        font.setPointSize(16)
        Dialog.setFont(font)
        Dialog.setAutoFillBackground(False)
        Dialog.setStyleSheet(_fromUtf8("background-color: rgb(0, 103, 179);"))
        Dialog.setModal(False)
        self.yearLabel = QtGui.QLabel(Dialog)
        self.yearLabel.setGeometry(QtCore.QRect(20, 110, 51, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.yearLabel.setFont(font)
        self.yearLabel.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.yearLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.yearLabel.setObjectName(_fromUtf8("yearLabel"))
        self.monthLabel = QtGui.QLabel(Dialog)
        self.monthLabel.setGeometry(QtCore.QRect(170, 110, 71, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.monthLabel.setFont(font)
        self.monthLabel.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.monthLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.monthLabel.setObjectName(_fromUtf8("monthLabel"))
        self.dayLabel = QtGui.QLabel(Dialog)
        self.dayLabel.setGeometry(QtCore.QRect(380, 110, 51, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.dayLabel.setFont(font)
        self.dayLabel.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
""))
        self.dayLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.dayLabel.setObjectName(_fromUtf8("dayLabel"))
        self.nameLabel = QtGui.QLabel(Dialog)
        self.nameLabel.setGeometry(QtCore.QRect(20, 10, 71, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.nameLabel.setFont(font)
        self.nameLabel.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255)"))
        self.nameLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.nameLabel.setObjectName(_fromUtf8("nameLabel"))
        self.nameFrame = QtGui.QFrame(Dialog)
        self.nameFrame.setGeometry(QtCore.QRect(20, 50, 445, 45))
        self.nameFrame.setStyleSheet(_fromUtf8("background-color: rgb(95, 157, 202);"))
        self.nameFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.nameFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.nameFrame.setObjectName(_fromUtf8("nameFrame"))
        self.nameLineEdit = QtGui.QLineEdit(self.nameFrame)
        self.nameLineEdit.setGeometry(QtCore.QRect(2, 2, 441, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.nameLineEdit.setFont(font)
        self.nameLineEdit.setAutoFillBackground(False)
        self.nameLineEdit.setStyleSheet(_fromUtf8("background-color: rgb(0, 62, 107);\n"
"color: rgb(255, 255, 255);"))
        self.nameLineEdit.setFrame(False)
        self.nameLineEdit.setObjectName(_fromUtf8("nameLineEdit"))

        self.yearFrame = QtGui.QFrame(Dialog)
        self.yearFrame.setGeometry(QtCore.QRect(20, 148, 85, 45))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.yearFrame.setFont(font)
        self.yearFrame.setStyleSheet(_fromUtf8("background-color: rgb(95, 157, 202);"))
        self.yearFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.yearFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.yearFrame.setObjectName(_fromUtf8("yearFrame"))
        self.yearComboBox = QtGui.QComboBox(self.yearFrame)
        self.yearComboBox.setGeometry(QtCore.QRect(2, 2, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.yearComboBox.setFont(font)
        self.yearComboBox.setStyleSheet(_fromUtf8("background-color: rgb(0, 62, 107);\n"
"color: rgb(255, 255, 255);"))
        self.yearComboBox.setFrame(False)
        self.yearComboBox.setObjectName(_fromUtf8("yearComboBox"))

        for i in range(2016, 1919, -1):
            self.yearComboBox.addItem(str(i))

        ##########     ComboBox Event    #########
        self.yearComboBox.activated.connect(self.showMonths)
        ##########################################

        self.dayFrame = QtGui.QFrame(Dialog)
        self.dayFrame.setGeometry(QtCore.QRect(378, 148, 85, 45))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.dayFrame.setFont(font)
        self.dayFrame.setStyleSheet(_fromUtf8("background-color: rgb(95, 157, 202);"))
        self.dayFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.dayFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.dayFrame.setObjectName(_fromUtf8("dayFrame"))
        self.dayComboBox = QtGui.QComboBox(self.dayFrame)
        self.dayComboBox.setGeometry(QtCore.QRect(2, 2, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.dayComboBox.setFont(font)
        self.dayComboBox.setStyleSheet(_fromUtf8("background-color: rgb(0, 62, 107);\n"
"color: rgb(255, 255, 255);"))
        self.dayComboBox.setFrame(False)
        self.dayComboBox.setObjectName(_fromUtf8("dayComboBox"))

        self.monthFrame = QtGui.QFrame(Dialog)
        self.monthFrame.setGeometry(QtCore.QRect(168, 148, 145, 45))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.monthFrame.setFont(font)
        self.monthFrame.setStyleSheet(_fromUtf8("background-color: rgb(95, 157, 202);"))
        self.monthFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.monthFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.monthFrame.setObjectName(_fromUtf8("monthFrame"))
        self.monthComboBox = QtGui.QComboBox(self.monthFrame)
        self.monthComboBox.setGeometry(QtCore.QRect(2, 2, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.monthComboBox.setFont(font)
        self.monthComboBox.setStyleSheet(_fromUtf8("background-color: rgb(0, 62, 107);\n"
"color: rgb(255, 255, 255);"))
        # self.monthComboBox.setCurrentText(_fromUtf8(""))
        self.monthComboBox.setFrame(False)
        self.monthComboBox.setObjectName(_fromUtf8("monthComboBox"))

        ##########     ComboBox Event     ########
        self.monthComboBox.activated.connect(self.showDays)
        ##########################################

        self.calculateFrame = QtGui.QFrame(Dialog)
        self.calculateFrame.setGeometry(QtCore.QRect(18, 228, 105, 45))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.calculateFrame.setFont(font)
        self.calculateFrame.setStyleSheet(_fromUtf8("background-color: rgb(0, 62, 107);"))
        self.calculateFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.calculateFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.calculateFrame.setObjectName(_fromUtf8("calculateFrame"))
        self.calculateButton = QtGui.QPushButton(self.calculateFrame)
        self.calculateButton.setGeometry(QtCore.QRect(2, 2, 101, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.calculateButton.setFont(font)
        self.calculateButton.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.calculateButton.setAutoDefault(False)
        self.calculateButton.setDefault(False)
        self.calculateButton.setFlat(True)
        self.calculateButton.setObjectName(_fromUtf8("calculateButton"))

        ##########     Button Event     ##########
        self.calculateButton.clicked.connect(self.calculate)
        ##########################################

        self.displayFrame = QtGui.QFrame(Dialog)
        self.displayFrame.setGeometry(QtCore.QRect(18, 288, 445, 45))
        self.displayFrame.setStyleSheet(_fromUtf8("background-color: rgb(95, 157, 202);"))
        self.displayFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.displayFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.displayFrame.setObjectName(_fromUtf8("displayFrame"))
        self.displayLabel = QtGui.QLabel(self.displayFrame)
        self.displayLabel.setGeometry(QtCore.QRect(2, 2, 441, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.displayLabel.setFont(font)
        self.displayLabel.setStyleSheet(_fromUtf8("background-color: rgb(0, 62, 107);\n"
"color: rgb(255, 255, 255);"))
        self.displayLabel.setText(_fromUtf8(""))
        self.displayLabel.setObjectName(_fromUtf8("displayLabel"))

        self.saveFrame = QtGui.QFrame(Dialog)
        self.saveFrame.setGeometry(QtCore.QRect(170, 228, 75, 45))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.saveFrame.setFont(font)
        self.saveFrame.setStyleSheet(_fromUtf8("background-color: rgb(0, 62, 107);"))
        self.saveFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.saveFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.saveFrame.setObjectName(_fromUtf8("saveFrame"))
        self.saveButton = QtGui.QPushButton(self.saveFrame)
        self.saveButton.setGeometry(QtCore.QRect(2, 2, 71, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.saveButton.setFont(font)
        self.saveButton.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255)"))
        self.saveButton.setAutoDefault(False)
        self.saveButton.setDefault(False)
        self.saveButton.setFlat(True)
        self.saveButton.setObjectName(_fromUtf8("saveButton"))

        ##########     Button Event     ##########
        self.saveButton.clicked.connect(self.saveToDb)
        ##########################################

        self.copyrightLabel = QtGui.QLabel(Dialog)
        self.copyrightLabel.setGeometry(QtCore.QRect(140, 340, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.copyrightLabel.setFont(font)
        self.copyrightLabel.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255)"))
        self.copyrightLabel.setObjectName(_fromUtf8("copyrightLabel"))
        self.saveFrame.raise_()
        self.displayFrame.raise_()
        self.calculateFrame.raise_()
        self.monthFrame.raise_()
        self.dayFrame.raise_()
        self.yearFrame.raise_()
        self.nameFrame.raise_()
        self.yearLabel.raise_()
        self.monthLabel.raise_()
        self.dayLabel.raise_()
        self.nameLabel.raise_()
        self.copyrightLabel.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "AGE CALCULATOR", None))
        self.yearLabel.setText(_translate("Dialog", "Year", None))
        self.monthLabel.setText(_translate("Dialog", "Month", None))
        self.dayLabel.setText(_translate("Dialog", "Day", None))
        self.nameLabel.setText(_translate("Dialog", "Name:", None))
        self.nameLineEdit.setPlaceholderText(_translate("Dialog", "Enter your name", None))
        self.calculateButton.setText(_translate("Dialog", "Calculate", None))
        self.saveButton.setText(_translate("Dialog", "Save", None))
        self.copyrightLabel.setText(_translate("Dialog", "© Oladepo Ibrahim", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

