from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("ConvNet Calculator")
        MainWindow.resize(698, 335)
        MainWindow.setWindowIcon(QtGui.QIcon('Assets/NN_Icon.png'))

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.text_boxes = []

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
        self.comboBox.currentIndexChanged.connect(self.on_layer_changed, self.comboBox.currentIndex())

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 10, 91, 30))
        self.label.setObjectName("label")
        
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 120, 111, 21))
        self.label_2.setObjectName("label_2")
        
        self.kernel_num_txt = QtWidgets.QTextEdit(self.centralwidget)
        self.kernel_num_txt.setGeometry(QtCore.QRect(30, 150, 104, 31))
        self.kernel_num_txt.setObjectName("kernel_num_txt")
        self.text_boxes.append(self.kernel_num_txt)

        self.kernel_size_txt = QtWidgets.QTextEdit(self.centralwidget)
        self.kernel_size_txt.setGeometry(QtCore.QRect(150, 150, 104, 31))
        self.kernel_size_txt.setObjectName("kernel_size_txt")
        self.text_boxes.append(self.kernel_size_txt)

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(170, 120, 71, 21))
        self.label_3.setObjectName("label_3")
        
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(250, 50, 51, 21))
        self.label_4.setObjectName("label_4")
        
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(300, 120, 41, 21))
        self.label_5.setObjectName("label_5")
        
        self.padding_txt = QtWidgets.QTextEdit(self.centralwidget)
        self.padding_txt.setGeometry(QtCore.QRect(220, 80, 104, 31))
        self.padding_txt.setObjectName("padding_txt")
        self.text_boxes.append(self.padding_txt)

        self.stride_txt = QtWidgets.QTextEdit(self.centralwidget)
        self.stride_txt.setGeometry(QtCore.QRect(270, 150, 104, 31))
        self.stride_txt.setObjectName("stride_txt")
        self.text_boxes.append(self.stride_txt)

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
        
        self.inp_width_txt = QtWidgets.QTextEdit(self.centralwidget)
        self.inp_width_txt.setGeometry(QtCore.QRect(23, 270, 101, 31))
        self.inp_width_txt.setObjectName("inp_width_txt")
        self.text_boxes.append(self.inp_width_txt)

        self.inp_height_txt = QtWidgets.QTextEdit(self.centralwidget)
        self.inp_height_txt.setGeometry(QtCore.QRect(150, 270, 101, 31))
        self.inp_height_txt.setObjectName("inp_height_txt")
        self.text_boxes.append(self.inp_height_txt)

        self.inp_depth_txt = QtWidgets.QTextEdit(self.centralwidget)
        self.inp_depth_txt.setGeometry(QtCore.QRect(280, 270, 101, 31))
        self.inp_depth_txt.setObjectName("inp_depth_txt")
        self.text_boxes.append(self.inp_depth_txt)

        self.calculateButton = QtWidgets.QPushButton(self.centralwidget)
        self.calculateButton.setGeometry(QtCore.QRect(460, 260, 93, 28))
        self.calculateButton.setObjectName("calculateButton")
        self.calculateButton.clicked.connect(self.calculate)

        self.clearButton = QtWidgets.QPushButton(self.centralwidget)
        self.clearButton.setGeometry(QtCore.QRect(580, 260, 93, 28))
        self.clearButton.setObjectName("clearButton")
        self.clearButton.clicked.connect(self.clear)

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
        
        self.out_width_label = QtWidgets.QLabel(self.centralwidget)
        self.out_width_label.setGeometry(QtCore.QRect(600, 70, 55, 21))
        self.out_width_label.setObjectName("out_width_label")
        
        self.out_height_label = QtWidgets.QLabel(self.centralwidget)
        self.out_height_label.setGeometry(QtCore.QRect(600, 110, 55, 21))
        self.out_height_label.setObjectName("out_height_label")
        
        self.out_depth_label = QtWidgets.QLabel(self.centralwidget)
        self.out_depth_label.setGeometry(QtCore.QRect(600, 150, 55, 21))
        self.out_depth_label.setObjectName("out_depth_label")
        
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
        
        self.calculateButton.setText(_translate("MainWindow", "Calculate"))
        self.clearButton.setText(_translate("MainWindow", "Clear"))

        self.label_10.setText(_translate("MainWindow", "OUTPUT DETAILS"))
        self.label_11.setText(_translate("MainWindow", "Width"))
        self.label_12.setText(_translate("MainWindow", "Height"))
        self.label_13.setText(_translate("MainWindow", "Depth"))
        self.out_width_label.setText(_translate("MainWindow", ""))
        self.out_height_label.setText(_translate("MainWindow", ""))
        self.out_depth_label.setText(_translate("MainWindow", ""))
    
    def calculate(self):
        _translate = QtCore.QCoreApplication.translate

        self.out_width_label.setText(_translate("MainWindow", self.inp_width_txt.toPlainText()))
        self.out_height_label.setText(_translate("MainWindow", self.inp_height_txt.toPlainText()))
        self.out_depth_label.setText(_translate("MainWindow", self.inp_depth_txt.toPlainText()))
        self.update()
    
    def clear(self):
        _translate = QtCore.QCoreApplication.translate

        self.out_width_label.setText(_translate("MainWindow", ""))
        self.out_height_label.setText(_translate("MainWindow", ""))
        self.out_depth_label.setText(_translate("MainWindow", ""))

        for i in range(len(self.text_boxes)):
            self.text_boxes[i].setPlainText(_translate("MainWindow", ""))

        self.update()
        
    def update(self):
        self.out_width_label.adjustSize()
        self.out_height_label.adjustSize()
        self.out_depth_label.adjustSize()

    def on_layer_changed(self, value):
        if value == 0:
            self.padding_txt.setDisabled(False)
        else:
            self.padding_txt.setDisabled(True)

    def conv_layer(self, in_h, in_w, in_d, kernels, kernel_size, padding, stride):
        new_h = int((in_h-kernel_size+(2*padding))/stride)+1
        new_w = int((in_w-kernel_size+(2*padding))/stride)+1
        new_d = kernels
        return new_h, new_w, new_d

    def pooling_layer(self, in_h, in_w, in_d, window_size, stride):
        new_h = int((in_h-window_size)/stride)+1
        new_w = int((in_w-window_size)/stride)+1
        new_d = in_d
        return new_h, new_w, new_d

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())