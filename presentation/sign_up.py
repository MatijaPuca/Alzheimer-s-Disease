# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui_files\sign_up.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(897, 477)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(60, 40, 351, 301))
        self.groupBox.setObjectName("groupBox")
        self.username = QtWidgets.QLineEdit(self.groupBox)
        self.username.setGeometry(QtCore.QRect(110, 40, 191, 21))
        self.username.setObjectName("username")
        self.usernameLabel = QtWidgets.QLabel(self.groupBox)
        self.usernameLabel.setGeometry(QtCore.QRect(10, 40, 91, 16))
        self.usernameLabel.setObjectName("usernameLabel")
        self.email = QtWidgets.QLineEdit(self.groupBox)
        self.email.setGeometry(QtCore.QRect(110, 190, 191, 21))
        self.email.setText("")
        self.email.setObjectName("email")
        self.emailLabel = QtWidgets.QLabel(self.groupBox)
        self.emailLabel.setGeometry(QtCore.QRect(10, 190, 91, 16))
        self.emailLabel.setObjectName("emailLabel")
        self.passwordLabel = QtWidgets.QLabel(self.groupBox)
        self.passwordLabel.setGeometry(QtCore.QRect(10, 230, 91, 16))
        self.passwordLabel.setObjectName("passwordLabel")
        self.password = QtWidgets.QLineEdit(self.groupBox)
        self.password.setGeometry(QtCore.QRect(110, 230, 191, 21))
        self.password.setObjectName("password")
        self.confirmPasswordLabel = QtWidgets.QLabel(self.groupBox)
        self.confirmPasswordLabel.setGeometry(QtCore.QRect(10, 270, 91, 16))
        self.confirmPasswordLabel.setObjectName("confirmPasswordLabel")
        self.confirmPassword = QtWidgets.QLineEdit(self.groupBox)
        self.confirmPassword.setGeometry(QtCore.QRect(110, 270, 191, 21))
        self.confirmPassword.setObjectName("confirmPassword")
        self.firstNameLabel = QtWidgets.QLabel(self.groupBox)
        self.firstNameLabel.setGeometry(QtCore.QRect(10, 90, 81, 16))
        self.firstNameLabel.setObjectName("firstNameLabel")
        self.firstName = QtWidgets.QLineEdit(self.groupBox)
        self.firstName.setGeometry(QtCore.QRect(110, 90, 191, 21))
        self.firstName.setObjectName("firstName")
        self.lastNameLabel = QtWidgets.QLabel(self.groupBox)
        self.lastNameLabel.setGeometry(QtCore.QRect(10, 140, 81, 16))
        self.lastNameLabel.setObjectName("lastNameLabel")
        self.lastName = QtWidgets.QLineEdit(self.groupBox)
        self.lastName.setGeometry(QtCore.QRect(110, 140, 191, 21))
        self.lastName.setObjectName("lastName")
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(480, 40, 341, 301))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(10, 40, 58, 16))
        self.label.setObjectName("label")
        self.age = QtWidgets.QLineEdit(self.groupBox_2)
        self.age.setGeometry(QtCore.QRect(130, 40, 111, 21))
        self.age.setObjectName("age")
        self.height = QtWidgets.QLineEdit(self.groupBox_2)
        self.height.setGeometry(QtCore.QRect(130, 80, 113, 21))
        self.height.setObjectName("height")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 71, 16))
        self.label_2.setObjectName("label_2")
        self.weight = QtWidgets.QLineEdit(self.groupBox_2)
        self.weight.setGeometry(QtCore.QRect(130, 120, 113, 21))
        self.weight.setObjectName("weight")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(10, 120, 71, 16))
        self.label_3.setObjectName("label_3")
        self.createAccountButton = QtWidgets.QPushButton(Dialog)
        self.createAccountButton.setGeometry(QtCore.QRect(440, 420, 121, 32))
        self.createAccountButton.setAutoDefault(False)
        self.createAccountButton.setObjectName("createAccountButton")
        self.cancelButton = QtWidgets.QPushButton(Dialog)
        self.cancelButton.setGeometry(QtCore.QRect(280, 420, 121, 32))
        self.cancelButton.setAutoDefault(False)
        self.cancelButton.setObjectName("cancelButton")
        self.client = QtWidgets.QRadioButton(Dialog)
        self.client.setGeometry(QtCore.QRect(370, 390, 99, 20))
        self.client.setObjectName("client")
        self.healthcare = QtWidgets.QRadioButton(Dialog)
        self.healthcare.setGeometry(QtCore.QRect(440, 390, 121, 20))
        self.healthcare.setObjectName("healthcare")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(400, 370, 71, 16))
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox.setTitle(_translate("Dialog", "Basic information"))
        self.usernameLabel.setText(_translate("Dialog", "Username"))
        self.emailLabel.setText(_translate("Dialog", "Email"))
        self.passwordLabel.setText(_translate("Dialog", "Password"))
        self.confirmPasswordLabel.setText(_translate("Dialog", "Confirm Pass"))
        self.firstNameLabel.setText(_translate("Dialog", "First Name"))
        self.lastNameLabel.setText(_translate("Dialog", "Last Name"))
        self.groupBox_2.setTitle(_translate("Dialog", "Personal Information"))
        self.label.setText(_translate("Dialog", "Age"))
        self.label_2.setText(_translate("Dialog", "Height (in.)"))
        self.label_3.setText(_translate("Dialog", "Weight (lb)"))
        self.createAccountButton.setText(_translate("Dialog", "Create account"))
        self.cancelButton.setText(_translate("Dialog", "Cancel"))
        self.client.setText(_translate("Dialog", "Patient"))
        self.healthcare.setText(_translate("Dialog", "Healthcare Provider"))
        self.label_4.setText(_translate("Dialog", "Sign up as:"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())