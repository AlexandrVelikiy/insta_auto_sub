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
        Form.resize(519, 510)
        Form.setMinimumSize(QtCore.QSize(519, 510))
        Form.setMaximumSize(QtCore.QSize(519, 510))
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 470, 501, 31))
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
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(10, 90, 501, 381))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.log = QtWidgets.QTextBrowser(self.verticalLayoutWidget_4)
        self.log.setObjectName("log")
        self.verticalLayout_4.addWidget(self.log)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(-10, 10, 497, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(10, 30, 118, 13))
        self.label_5.setObjectName("label_5")
        self.label_countAll = QtWidgets.QLabel(Form)
        self.label_countAll.setGeometry(QtCore.QRect(210, 30, 31, 16))
        self.label_countAll.setObjectName("label_countAll")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(10, 50, 118, 13))
        self.label_6.setObjectName("label_6")
        self.label_count24hour = QtWidgets.QLabel(Form)
        self.label_count24hour.setGeometry(QtCore.QRect(210, 50, 41, 16))
        self.label_count24hour.setObjectName("label_count24hour")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(10, 70, 179, 13))
        self.label_7.setObjectName("label_7")
        self.label_countLaststart = QtWidgets.QLabel(Form)
        self.label_countLaststart.setGeometry(QtCore.QRect(210, 70, 41, 16))
        self.label_countLaststart.setObjectName("label_countLaststart")
        self.label_timer_text = QtWidgets.QLabel(Form)
        self.label_timer_text.setGeometry(QtCore.QRect(270, 30, 117, 13))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_timer_text.setFont(font)
        self.label_timer_text.setObjectName("label_timer_text")
        self.label_timer_text_2 = QtWidgets.QLabel(Form)
        self.label_timer_text_2.setGeometry(QtCore.QRect(270, 50, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_timer_text_2.setFont(font)
        self.label_timer_text_2.setObjectName("label_timer_text_2")
        self.label_timer = QtWidgets.QLabel(Form)
        self.label_timer.setGeometry(QtCore.QRect(430, 30, 118, 13))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_timer.setFont(font)
        self.label_timer.setObjectName("label_timer")
        self.label_timer_2 = QtWidgets.QLabel(Form)
        self.label_timer_2.setEnabled(True)
        self.label_timer_2.setGeometry(QtCore.QRect(430, 50, 118, 13))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_timer_2.setFont(font)
        self.label_timer_2.setObjectName("label_timer_2")

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
        self.label_countAll.setText(_translate("Form", "0"))
        self.label_6.setText(_translate("Form", "Обработано за сутки:"))
        self.label_count24hour.setText(_translate("Form", "0"))
        self.label_7.setText(_translate("Form", "Обработано с последнего запуска:"))
        self.label_countLaststart.setText(_translate("Form", "0"))
        self.label_timer_text.setText(_translate("Form", "Время работы:"))
        self.label_timer_text_2.setText(_translate("Form", "Время работы:"))
        self.label_timer.setText(_translate("Form", "0:00:00"))
        self.label_timer_2.setText(_translate("Form", "0:00:00"))
