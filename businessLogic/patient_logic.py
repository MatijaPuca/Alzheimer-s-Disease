import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
import presentation.patient_main as patient_main
from data import patient, cognitive_test
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
        self.btnSubmitCognitiveTest.clicked.connect(self.submitCognitiveTest)
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
        self.cognitiveTestBox.setEnabled(True)
        self.btnStartCognitiveTest.setEnabled(False)

    def submitCognitiveTest(self):
        test_answer = "|".join([answer.text() for answer in self.answers])
        date_taken = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        fields = (self.patientId, test_answer, date_taken)
        database = cognitive_test.Cognitive_Tests()
        self.cognitive_test = database.add(fields)
        database.close()
        self.cognitiveTestBox.setEnabled(False)

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