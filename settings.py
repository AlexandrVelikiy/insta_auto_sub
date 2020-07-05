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
        Dialog.resize(519, 180)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(160, 130, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.checkBox_autostart = QtWidgets.QCheckBox(Dialog)
        self.checkBox_autostart.setGeometry(QtCore.QRect(10, 10, 161, 17))
        self.checkBox_autostart.setObjectName("checkBox_autostart")
        self.lineEdit_chromepath = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_chromepath.setGeometry(QtCore.QRect(10, 90, 411, 20))
        self.lineEdit_chromepath.setObjectName("lineEdit_chromepath")
        self.pushButton_path = QtWidgets.QPushButton(Dialog)
        self.pushButton_path.setGeometry(QtCore.QRect(430, 89, 75, 23))
        self.pushButton_path.setObjectName("pushButton_path")
        self.spinBox = QtWidgets.QSpinBox(Dialog)
        self.spinBox.setGeometry(QtCore.QRect(10, 36, 42, 22))
        self.spinBox.setObjectName("spinBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(60, 40, 141, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 401, 16))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Настройки"))
        self.checkBox_autostart.setText(_translate("Dialog", "Запускать автоматически"))
        self.pushButton_path.setText(_translate("Dialog", "Изменить"))
        self.label.setText(_translate("Dialog", "Пауза между проверками"))
        self.label_2.setText(_translate("Dialog", "Каталог с GoogleChromePortable"))
