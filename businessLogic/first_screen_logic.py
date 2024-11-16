from PyQt5 import QtCore, QtGui, QtWidgets
import presentation.first_screen as first_screen
from businessLogic import login_logic, navigation, sign_up_logic

class FirstScreen(QtWidgets.QDialog, first_screen.Ui_Dialog):
    def __init__(self, parent=None):
        super(FirstScreen, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Sign up / Login")
        # close the window
        self.signupButton.clicked.connect(self.clickSignUp)
        self.loginButton.clicked.connect(self.clickLogin)


    def clickSignUp(self):
        navigation.close()
        navigation.set(sign_up_logic.SignUp())
        navigation.show()

    def clickLogin(self):
        navigation.close()
        navigation.set(login_logic.Login())
        navigation.show()