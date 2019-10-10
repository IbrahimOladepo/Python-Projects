# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'age.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

        for i in range(1, days + 1):
            self.day_comboBox.addItem(str(i))

    def showMonths(self):
        monthsList = [
            "JANUARY", "FEBRUARY", "MARCH", "APRIL", "MAY", "JUNE", "JULY",
            "AUGUST", "SEPTEMBER", "OCTOBER", "NOVEMBER", "DECEMBER"
        ]

        for i in monthsList:
            self.month_comboBox.addItem(i)

    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(569, 112)

        self.year_comboBox = QtGui.QComboBox(Dialog)
        self.year_comboBox.setGeometry(QtCore.QRect(20, 60, 111, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.year_comboBox.setFont(font)
        self.year_comboBox.setObjectName(_fromUtf8("year_comboBox"))

        for i in range(2016, 1919, -1):
            self.year_comboBox.addItem(str(i))

        ##########     Button Event     ##########
        self.year_comboBox.activated.connect(self.showMonths)
        ##########################################

        self.year_label = QtGui.QLabel(Dialog)
        self.year_label.setGeometry(QtCore.QRect(20, 33, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.year_label.setFont(font)
        self.year_label.setAlignment(QtCore.Qt.AlignCenter)
        self.year_label.setObjectName(_fromUtf8("year_label"))

        self.day_label = QtGui.QLabel(Dialog)
        self.day_label.setGeometry(QtCore.QRect(430, 33, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.day_label.setFont(font)
        self.day_label.setAlignment(QtCore.Qt.AlignCenter)
        self.day_label.setObjectName(_fromUtf8("day_label"))

        self.day_comboBox = QtGui.QComboBox(Dialog)
        self.day_comboBox.setGeometry(QtCore.QRect(430, 60, 111, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.day_comboBox.setFont(font)
        self.day_comboBox.setObjectName(_fromUtf8("day_comboBox"))

        self.month_label = QtGui.QLabel(Dialog)
        self.month_label.setGeometry(QtCore.QRect(220, 33, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.month_label.setFont(font)
        self.month_label.setAlignment(QtCore.Qt.AlignCenter)
        self.month_label.setObjectName(_fromUtf8("month_label"))

        self.month_comboBox = QtGui.QComboBox(Dialog)
        self.month_comboBox.setGeometry(QtCore.QRect(220, 60, 111, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.month_comboBox.setFont(font)
        self.month_comboBox.setObjectName(_fromUtf8("month_comboBox"))

        ##########     Button Event     ##########
        self.month_comboBox.activated.connect(self.showDays)
        ##########################################

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "AGE CALCULATOR", None))
        self.year_label.setText(_translate("Dialog", "SELECT YEAR", None))
        self.day_label.setText(_translate("Dialog", "SELECT DAY", None))
        self.month_label.setText(_translate("Dialog", "SELECT MONTH", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

