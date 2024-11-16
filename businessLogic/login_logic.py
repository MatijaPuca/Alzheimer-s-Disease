from PyQt5 import QtCore, QtGui, QtWidgets
import presentation.login as login
from data import user as usr
from businessLogic import first_screen_logic, navigation, patient_logic, healthcare_logic

class Login(QtWidgets.QDialog, login.Ui_Dialog):
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Login")
        # close the window
        self.cancelButton.clicked.connect(self.cancel)
        self.loginButton.clicked.connect(self.completeLogin)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
    
    def cancel(self):
        sign_up_view = first_screen_logic.FirstScreen() # main screen
        self.setView(sign_up_view)

    def completeLogin(self):
        username = self.username.text()
        password = self.password.text()

        fields = [username, password]
        database = usr.User()
        user=database.authenticate(fields)
        database.close()

        if user != None:
            if user[6] == 0:
                patient_view = patient_logic.Patient(user= user) # main screen
                self.setView(patient_view)
            else:
                healthcare_view = healthcare_logic.Healthcare(healthcare = user) # main screen
                self.setView(healthcare_view)
        else:
            text = "Failure"
            info = "Unable to log in. Please check your credentials."
            icon = QtWidgets.QMessageBox.Critical
            msg = QtWidgets.QMessageBox()
            msg.setIcon(icon)
            msg.setText(text)
            msg.setInformativeText(info)
            msg.setWindowTitle(text)
            msg.exec_()


    def setView(self, view):
        navigation.close()
        navigation.set(view)
        navigation.show()