# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1083, 912)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.result_1 = QtWidgets.QLabel(self.centralwidget)
        self.result_1.setEnabled(False)
        self.result_1.setGeometry(QtCore.QRect(40, 120, 300, 300))
        self.result_1.setText("")
        self.result_1.setObjectName("result_1")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(530, 50, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.keyword = QtWidgets.QLineEdit(self.centralwidget)
        self.keyword.setGeometry(QtCore.QRect(410, 10, 113, 22))
        self.keyword.setObjectName("keyword")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 10, 251, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(170, 40, 231, 31))
        self.label_2.setObjectName("label_2")
        self.picsNum = QtWidgets.QLineEdit(self.centralwidget)
        self.picsNum.setGeometry(QtCore.QRect(410, 50, 113, 22))
        self.picsNum.setObjectName("picsNum")
        self.result_2 = QtWidgets.QLabel(self.centralwidget)
        self.result_2.setGeometry(QtCore.QRect(380, 120, 300, 300))
        self.result_2.setText("")
        self.result_2.setObjectName("result_2")
        self.result_3 = QtWidgets.QLabel(self.centralwidget)
        self.result_3.setGeometry(QtCore.QRect(720, 120, 300, 300))
        self.result_3.setText("")
        self.result_3.setObjectName("result_3")
        self.result_4 = QtWidgets.QLabel(self.centralwidget)
        self.result_4.setEnabled(False)
        self.result_4.setGeometry(QtCore.QRect(40, 440, 300, 300))
        self.result_4.setText("")
        self.result_4.setObjectName("result_4")
        self.result_5 = QtWidgets.QLabel(self.centralwidget)
        self.result_5.setEnabled(False)
        self.result_5.setGeometry(QtCore.QRect(380, 440, 300, 300))
        self.result_5.setText("")
        self.result_5.setObjectName("result_5")
        self.result_6 = QtWidgets.QLabel(self.centralwidget)
        self.result_6.setEnabled(False)
        self.result_6.setGeometry(QtCore.QRect(720, 440, 300, 300))
        self.result_6.setText("")
        self.result_6.setObjectName("result_6")
        self.nextButton = QtWidgets.QPushButton(self.centralwidget)
        self.nextButton.setEnabled(False)
        self.nextButton.setGeometry(QtCore.QRect(680, 50, 93, 28))
        self.nextButton.setObjectName("nextButton")
        self.lastButton = QtWidgets.QPushButton(self.centralwidget)
        self.lastButton.setEnabled(False)
        self.lastButton.setGeometry(QtCore.QRect(780, 50, 93, 28))
        self.lastButton.setCheckable(False)
        self.lastButton.setObjectName("lastButton")
        self.page = QtWidgets.QLabel(self.centralwidget)
        self.page.setGeometry(QtCore.QRect(890, 50, 181, 20))
        self.page.setText("")
        self.page.setObjectName("page")
        self.downloadMsg = QtWidgets.QLabel(self.centralwidget)
        self.downloadMsg.setGeometry(QtCore.QRect(280, 80, 221, 20))
        self.downloadMsg.setText("")
        self.downloadMsg.setObjectName("downloadMsg")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1083, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "pttBeauty_imgurDowlnloader"))
        self.pushButton.setText(_translate("MainWindow", "下載"))
        self.label.setText(_translate("MainWindow", "請輸入想在ptt表特版查詢的關鍵字:"))
        self.label_2.setText(_translate("MainWindow", "請輸入下載的張數:"))
        self.nextButton.setText(_translate("MainWindow", "下一頁"))
        self.lastButton.setText(_translate("MainWindow", "上一頁"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
