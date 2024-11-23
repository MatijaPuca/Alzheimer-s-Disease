from PyQt5 import QtCore, QtGui, QtWidgets
import presentation.patient_main as patient_main
from data import patient as patient
from businessLogic import navigation, login_logic


class Patient(QtWidgets.QDialog, patient_main.Ui_Dialog):
    def __init__(self,  user, parent=None):
        super(Patient, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Patient Home")
        self.patientId = user[0]
        self.userAll = user
        # close the window
        self.logout.clicked.connect(self.logOut)
        self.btnStartCognitiveTest.clicked.connect(self.startCognitiveTest)
        self.modifyData.clicked.connect(self.addormodifyData)
        self.btnsaveLifestyleData.clicked.connect(self.saveLifestyleData)
        self.getPatientInfo()
        self.age.setText(str(self.patient[4]))
        self.height.setText(str(self.patient[3]))
        self.weight.setText(str(self.patient[2]))
        self.lblgeneticsData.setText(str(self.patient[7]))
        self.result.setText(str(self.patient[1]))
        self.textLifestyleData.setText(str(self.patient[0]))

        database = patient.Patient()
        healthcareProvider = database.getHealthcareProvider(self.patient[6])
        database.close()
        self.healthcareProvider.setText(healthcareProvider[0]+ " "+ healthcareProvider[1])


    def logOut(self):
        login_view = login_logic.Login() # main screen
        self.setView(login_view)

    def getPatientInfo(self):
        database = patient.Patient()
        self.patient = database.get(self.patientId)
        database.close()

    def startCognitiveTest(self):
    #     goals_text = self.goalsTextBox.toPlainText()
          database = patient.Patient()
    #     result = database.update_information([goals_text, self.userAll[0]])
    #     database.close()

    #     if result > 0:
    #             text = "Success"
    #             info = "You have successfully updated your goals."
    #             icon = QtWidgets.QMessageBox.Information
    #     else:
    #             text = "Failure"
    #             info = "Unable to update your goals."
    #             icon = QtWidgets.QMessageBox.Critical

    def addormodifyData(self):
        self.textLifestyleData.setEnabled(True)
        self.btnsaveLifestyleData.setEnabled(True)
        self.modifyData.setEnabled(False)

    def saveLifestyleData(self):
        self.textLifestyleData.setEnabled(False)
        fields = (self.textLifestyleData.toPlainText(), self.patientId)
        database = patient.Patient()
        database.setLifestyleData(fields)
        database.close()
        self.modifyData.setEnabled(True)
        self.btnsaveLifestyleData.setEnabled(False)


    def setView(self, view):
        navigation.close()
        navigation.set(view)
        navigation.show()