# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainform.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(519, 426)
        Form.setMaximumSize(QtCore.QSize(519, 16777215))
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 390, 501, 31))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_start = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_start.setObjectName("pushButton_start")
        self.horizontalLayout_2.addWidget(self.pushButton_start)
        self.pushButton_pause = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_pause.setObjectName("pushButton_pause")
        self.horizontalLayout_2.addWidget(self.pushButton_pause)
        self.pushButton_stop = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_stop.setObjectName("pushButton_stop")
        self.horizontalLayout_2.addWidget(self.pushButton_stop)
        self.pushButton_config = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_config.setObjectName("pushButton_config")
        self.horizontalLayout_2.addWidget(self.pushButton_config)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(10, 10, 501, 381))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_7.addWidget(self.label_4)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_5.addWidget(self.label_5)
        self.horizontalLayout_5.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_countAll = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_countAll.setObjectName("label_countAll")
        self.verticalLayout_6.addWidget(self.label_countAll)
        self.horizontalLayout_5.addLayout(self.verticalLayout_6)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_7.addWidget(self.label_6)
        self.horizontalLayout_6.addLayout(self.verticalLayout_7)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_count24hour = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_count24hour.setObjectName("label_count24hour")
        self.verticalLayout_8.addWidget(self.label_count24hour)
        self.horizontalLayout_6.addLayout(self.verticalLayout_8)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_9.addWidget(self.label_7)
        self.horizontalLayout_8.addLayout(self.verticalLayout_9)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_countLaststart = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_countLaststart.setObjectName("label_countLaststart")
        self.verticalLayout_10.addWidget(self.label_countLaststart)
        self.horizontalLayout_8.addLayout(self.verticalLayout_10)
        self.verticalLayout_4.addLayout(self.horizontalLayout_8)
        self.log = QtWidgets.QTextBrowser(self.verticalLayoutWidget_4)
        self.log.setObjectName("log")
        self.verticalLayout_4.addWidget(self.log)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_start.setText(_translate("Form", "Старт"))
        self.pushButton_pause.setText(_translate("Form", "Пауза"))
        self.pushButton_stop.setText(_translate("Form", "Стоп"))
        self.pushButton_config.setText(_translate("Form", "Настройки"))
        self.label_4.setText(_translate("Form", "Статистика"))
        self.label_5.setText(_translate("Form", "Обработано всего:"))
        self.label_countAll.setText(_translate("Form", "label_countAll"))
        self.label_6.setText(_translate("Form", "Обработано за сутки:"))
        self.label_count24hour.setText(_translate("Form", "label_count24hour"))
        self.label_7.setText(_translate("Form", "Обработано с последнего запуска:"))
        self.label_countLaststart.setText(_translate("Form", "label_countLaststart"))
