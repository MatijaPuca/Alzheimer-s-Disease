# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui_files\first_screen.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(788, 455)
        self.titleLabel = QtWidgets.QLabel(Dialog)
        self.titleLabel.setGeometry(QtCore.QRect(-20, 20, 791, 101))
        font = QtGui.QFont()
        font.setPointSize(27)
        self.titleLabel.setFont(font)
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setObjectName("titleLabel")
        self.signupButton = QtWidgets.QPushButton(Dialog)
        self.signupButton.setGeometry(QtCore.QRect(230, 230, 100, 32))
        self.signupButton.setAutoDefault(False)
        self.signupButton.setDefault(False)
        self.signupButton.setFlat(False)
        self.signupButton.setObjectName("signupButton")
        self.loginButton = QtWidgets.QPushButton(Dialog)
        self.loginButton.setGeometry(QtCore.QRect(440, 230, 100, 32))
        self.loginButton.setAutoDefault(False)
        self.loginButton.setObjectName("loginButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.titleLabel.setText(_translate("Dialog", "Alzheimer Disease Risk Assessment Software"))
        self.signupButton.setText(_translate("Dialog", "Sign up"))
        self.loginButton.setText(_translate("Dialog", "Log in"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())