# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(519, 184)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(170, 150, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.lineEdit_chromepath = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_chromepath.setEnabled(True)
        self.lineEdit_chromepath.setGeometry(QtCore.QRect(10, 120, 421, 20))
        self.lineEdit_chromepath.setObjectName("lineEdit_chromepath")
        self.pushButton_path = QtWidgets.QPushButton(Dialog)
        self.pushButton_path.setGeometry(QtCore.QRect(437, 120, 75, 23))
        self.pushButton_path.setObjectName("pushButton_path")
        self.spinBox_timeout = QtWidgets.QSpinBox(Dialog)
        self.spinBox_timeout.setGeometry(QtCore.QRect(10, 70, 42, 22))
        self.spinBox_timeout.setObjectName("spinBox_timeout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(60, 70, 141, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 100, 401, 16))
        self.label_2.setObjectName("label_2")
        self.dateTime_stop = QtWidgets.QDateTimeEdit(Dialog)
        self.dateTime_stop.setGeometry(QtCore.QRect(90, 40, 108, 20))
        self.dateTime_stop.setObjectName("dateTime_stop")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 40, 65, 13))
        self.label_3.setObjectName("label_3")
        self.label_chromepath = QtWidgets.QLabel(Dialog)
        self.label_chromepath.setGeometry(QtCore.QRect(10, 150, 261, 16))
        self.label_chromepath.setObjectName("label_chromepath")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 57, 13))
        self.label_4.setObjectName("label_4")
        self.dateTime_start = QtWidgets.QDateTimeEdit(Dialog)
        self.dateTime_start.setGeometry(QtCore.QRect(90, 10, 108, 20))
        self.dateTime_start.setObjectName("dateTime_start")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(230, 40, 171, 16))
        self.label_5.setObjectName("label_5")
        self.checkBox_sheduled = QtWidgets.QCheckBox(Dialog)
        self.checkBox_sheduled.setGeometry(QtCore.QRect(230, 10, 191, 17))
        self.checkBox_sheduled.setObjectName("checkBox_sheduled")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setGeometry(QtCore.QRect(420, 40, 71, 20))
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Настройки"))
        self.pushButton_path.setText(_translate("Dialog", "Изменить"))
        self.label.setText(_translate("Dialog", "Пауза между проверками"))
        self.label_2.setText(_translate("Dialog", "Каталог с GoogleChromePortable:"))
        self.label_3.setText(_translate("Dialog", "Остановить:"))
        self.label_chromepath.setText(_translate("Dialog", "C:\\Usersalex\\Downloads\\GoogleChromePortable"))
        self.label_4.setText(_translate("Dialog", "Запустить:"))
        self.label_5.setText(_translate("Dialog", "Запланированное время работы"))
        self.checkBox_sheduled.setText(_translate("Dialog", "Включить запуск по расписанию"))
