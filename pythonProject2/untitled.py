# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(382, 229)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalSlider = QtWidgets.QSlider(self.groupBox)
        self.horizontalSlider.setMaximum(100)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.gridLayout.addWidget(self.horizontalSlider, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(self.groupBox)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setTextVisible(True)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 2, 1, 1, 1)
        self.horizontalScrollBar = QtWidgets.QScrollBar(self.groupBox)
        self.horizontalScrollBar.setMaximum(100)
        self.horizontalScrollBar.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar.setObjectName("horizontalScrollBar")
        self.gridLayout.addWidget(self.horizontalScrollBar, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.checkBox_txtVis = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_txtVis.setAcceptDrops(False)
        self.checkBox_txtVis.setChecked(True)
        self.checkBox_txtVis.setObjectName("checkBox_txtVis")
        self.gridLayout_2.addWidget(self.checkBox_txtVis, 0, 0, 1, 1)
        self.checkBox_invert = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_invert.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkBox_invert.setObjectName("checkBox_invert")
        self.gridLayout_2.addWidget(self.checkBox_invert, 0, 1, 1, 1)
        self.radioBtn_percnet = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioBtn_percnet.setChecked(True)
        self.radioBtn_percnet.setObjectName("radioBtn_percnet")
        self.gridLayout_2.addWidget(self.radioBtn_percnet, 1, 0, 1, 1)
        self.radioBtn_value = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioBtn_value.setObjectName("radioBtn_value")
        self.gridLayout_2.addWidget(self.radioBtn_value, 1, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.horizontalSlider, self.checkBox_txtVis)
        Form.setTabOrder(self.checkBox_txtVis, self.checkBox_invert)
        Form.setTabOrder(self.checkBox_invert, self.radioBtn_percnet)
        Form.setTabOrder(self.radioBtn_percnet, self.radioBtn_value)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_3.setText(_translate("Form", "ProgressBar"))
        self.label.setText(_translate("Form", "Slider"))
        self.label_2.setText(_translate("Form", "ScrollBar"))
        self.groupBox_2.setTitle(_translate("Form", "ProgressBar Setting"))
        self.checkBox_txtVis.setText(_translate("Form", "textVisible"))
        self.checkBox_invert.setText(_translate("Form", "InvertedAppearance"))
        self.radioBtn_percnet.setText(_translate("Form", "ShowFormat-Percent"))
        self.radioBtn_value.setText(_translate("Form", "ShowFormat-Value"))