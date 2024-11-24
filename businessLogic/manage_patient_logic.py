from PyQt5 import QtCore, QtGui, QtWidgets
import presentation.manage_patient as manage_patient
from data import healthcare as healthcare
from businessLogic import navigation, healthcare_logic
from datetime import date

class ManagePatient(QtWidgets.QDialog, manage_patient.Ui_Dialog):
    def __init__(self,  healthcareProvider, patient, parent=None):
        super(ManagePatient, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Manage patient")
        print(patient)
        self.healthcareProviderAll = healthcareProvider
        self.healthcareProviderId = healthcareProvider[0]
        self.patientAll = patient
        self.patientId = patient[0]
        self.patientName.setText(str(patient[2])+" "+str(patient[3]))
        self.lifestyleLabel.setText(str(patient[7]))
        self.age.setText(str(patient[11]))
        self.height.setText(str(patient[10]))
        self.weight.setText(str(patient[9]))
        self.score.setText(str(patient[8]))

        self.genetics.setText(str(patient[14]))

        self.populateCognitiveTest()

        self.assignGeneticsButton.clicked.connect(self.assignGeneticsData)
        self.assignRiskAssesmentButton.clicked.connect(self.assignRiskAssessment)
        self.goBack.clicked.connect(self.cancel)

    def assignGeneticsData(self):
        fields = (self.txtGeneticsData.toPlainText(), self.patientId)
        database = healthcare.Healthcare()
        database.setGeneticsData(fields)
        database.close()
        self.genetics.setText(self.txtGeneticsData.toPlainText())

    def populateCognitiveTest(self):      
        database = healthcare.Healthcare()
        cognitiveTest = database.getPatientCognitiveTest([self.patientId])
        database.close()

        if cognitiveTest and cognitiveTest[0]:
        # cognitiveTest[0][0] is the first (and only) column of the first row
            all_answers = cognitiveTest[0][0]
            if all_answers:
                # Split by '||' to get individual tests, then by '|' to get individual answers
                tests = all_answers.split('||')
                latest_test = tests[0]  # Get the most recent test
                answers = latest_test.split('|')
        
                for row in range(min(len(answers), self.cognitiveTestTable.rowCount())):
                    self.cognitiveTestTable.setItem(row, 1, QtWidgets.QTableWidgetItem(answers[row].strip()))
            else:
                print("No cognitive test data found for this patient.")
        
    def assignRiskAssessment(self):
        fields = (self.txtRiskAssesment.toPlainText(), self.patientId)
        database = healthcare.Healthcare()
        database.addPatientAssessment(fields)
        database.close()
        self.score = self.txtRiskAssesment.toPlainText()


    def cancel(self):
        healthcareProvider_view = healthcare_logic.Healthcare(self.healthcareProviderAll) # main screen
        self.setView(healthcareProvider_view)

    def setView(self, view):
        navigation.close()
        navigation.set(view)
        navigation.show()