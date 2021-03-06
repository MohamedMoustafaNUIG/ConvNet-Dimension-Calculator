from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(698, 335)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 190, 421, 21))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(420, 0, 20, 301))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(30, 60, 111, 31))
        self.comboBox.setMaximumSize(QtCore.QSize(111, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 10, 91, 30))
        self.label.setObjectName("label")
        
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 120, 111, 21))
        self.label_2.setObjectName("label_2")
        
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(30, 150, 104, 31))
        self.textEdit.setObjectName("textEdit")
        
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(150, 150, 104, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(170, 120, 71, 21))
        self.label_3.setObjectName("label_3")
        
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(250, 50, 51, 21))
        self.label_4.setObjectName("label_4")
        
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(300, 120, 41, 21))
        self.label_5.setObjectName("label_5")
        
        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(220, 80, 104, 31))
        self.textEdit_3.setObjectName("textEdit_3")
        
        self.textEdit_4 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_4.setGeometry(QtCore.QRect(270, 150, 104, 31))
        self.textEdit_4.setObjectName("textEdit_4")
        
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(160, 210, 91, 30))
        self.label_6.setObjectName("label_6")
        
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(60, 245, 41, 21))
        self.label_7.setObjectName("label_7")
        
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(180, 245, 41, 21))
        self.label_8.setObjectName("label_8")
        
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(315, 245, 41, 21))
        self.label_9.setObjectName("label_9")
        
        self.textEdit_5 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_5.setGeometry(QtCore.QRect(23, 270, 101, 31))
        self.textEdit_5.setObjectName("textEdit_5")
        
        self.textEdit_6 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_6.setGeometry(QtCore.QRect(150, 270, 101, 31))
        self.textEdit_6.setObjectName("textEdit_6")
        
        self.textEdit_7 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_7.setGeometry(QtCore.QRect(280, 270, 101, 31))
        self.textEdit_7.setObjectName("textEdit_7")
        
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(460, 260, 93, 28))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(580, 260, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(510, 10, 101, 30))
        self.label_10.setObjectName("label_10")
        
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(510, 70, 51, 21))
        self.label_11.setObjectName("label_11")
        
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(510, 110, 51, 21))
        self.label_12.setObjectName("label_12")
        
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(510, 150, 51, 21))
        self.label_13.setObjectName("label_13")
        
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(600, 150, 51, 21))
        self.label_14.setObjectName("label_14")
        
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(600, 110, 51, 21))
        self.label_15.setObjectName("label_15")
        
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(600, 70, 51, 21))
        self.label_16.setObjectName("label_16")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        
        self.comboBox.setItemText(0, _translate("MainWindow", "Convolutional"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Pooling"))
        
        self.label.setText(_translate("MainWindow", "LAYER DETAILS"))
        self.label_2.setText(_translate("MainWindow", "Number of Kernels"))
        self.label_3.setText(_translate("MainWindow", "Kernel Size"))
        self.label_4.setText(_translate("MainWindow", "Padding"))
        self.label_5.setText(_translate("MainWindow", "Stride"))
        self.label_6.setText(_translate("MainWindow", "INPUT DETAILS"))
        self.label_7.setText(_translate("MainWindow", "Width"))
        self.label_8.setText(_translate("MainWindow", "Height"))
        self.label_9.setText(_translate("MainWindow", "Depth"))
        
        self.pushButton.setText(_translate("MainWindow", "Calculate"))
        self.pushButton_2.setText(_translate("MainWindow", "Clear"))

        self.label_10.setText(_translate("MainWindow", "OUTPUT DETAILS"))
        self.label_11.setText(_translate("MainWindow", "Width"))
        self.label_12.setText(_translate("MainWindow", "Height"))
        self.label_13.setText(_translate("MainWindow", "Depth"))
        self.label_14.setText(_translate("MainWindow", "N/A"))
        self.label_15.setText(_translate("MainWindow", "N/A"))
        self.label_16.setText(_translate("MainWindow", "N/A"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
