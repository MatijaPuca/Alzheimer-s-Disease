from PyQt5 import QtCore, QtGui, QtWidgets
import presentation.sign_up as sign_up
from businessLogic import first_screen_logic, navigation, login_logic
from data import user
from data import patient
from data import healthcare




class SignUp(QtWidgets.QDialog, sign_up.Ui_Dialog):
    def __init__(self, parent=None):
        super(SignUp, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Sign Up")
        # close the window
        self.populateHealthcareProviders()
        self.cancelButton.clicked.connect(self.cancel)
        self.createAccountButton.clicked.connect(self.completeSignUp)

        self.group = QtWidgets.QButtonGroup()
        self.group.setExclusive(False)  # Radio buttons are not exclusive
        self.group.buttonClicked.connect(self.check_buttons)
        self.group.addButton(self.healthcare)
        self.group.addButton(self.client)
        
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmPassword.setEchoMode(QtWidgets.QLineEdit.Password)


    def check_buttons(self, radioButton):
        # Uncheck every other button in this group
        for button in self.group.buttons():
            if button is not radioButton:
                button.setChecked(False)
        if self.client.isChecked():
            self.groupBox_2.setEnabled(True)
        else:
            self.groupBox_2.setEnabled(False)

    def populateHealthcareProviders(self): 
        self.healthcareDropdown.clear()
        database = patient.Patient()
        healthcares = database.getAllHealthcareProviders()
        for healthcare in healthcares:
            self.healthcareDropdown.addItem(healthcare[0])

    def cancel(self):
        sign_up_view = first_screen_logic.FirstScreen() # main screen
        self.setView(sign_up_view)

    def completeSignUp(self):
        username = self.username.text()
        email = self.email.text()
        fname = self.firstName.text()
        lname = self.lastName.text()
        passw = self.password.text()
        age = self.age.text()
        weight = self.weight.text()
        height = self.height.text()       
        isHealthcare =  self.healthcare.isChecked() # bool for healthcare.
        user_fields = [email, username, passw, fname, lname, isHealthcare]

        if isHealthcare == 0:
        # username, email, first_name, last_name, passw, age, weight, desired_weight, height
            database = user.User()
            print(user_fields)
            result1 = database.add(user_fields)
            database.close()
            database = patient.Patient()
            healthcare_id = database.getId(self.healthcareDropdown.currentText())
            database.close()
            database = patient.Patient()
            client_fields = [age, weight, height, database.getId(username)[0], healthcare_id[0] ]
            database.close()
            database = patient.Patient()
            result2 = database.add(client_fields)
            database.close()
        else:
            database = user.User()
            result1 = database.add(user_fields)
            database.close()

            database = healthcare.Healthcare()
            healthcare_fields = ["0", database.getId(username)[0]]
            database.close()
            database = healthcare.Healthcare()
            result2 = database.add(healthcare_fields)
            database.close()


        print(result1," -- ", result2)
        if result1 == True and result2 == True:
            login_up_view = login_logic.Login()
            self.setView(login_up_view)
        else:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText('An error occured. Please check your input.')
            msg.setWindowTitle("Error")
            msg.exec_()
    
    def setView(self, view):
        navigation.close()
        navigation.set(view)
        navigation.show()