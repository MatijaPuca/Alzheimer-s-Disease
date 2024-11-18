from PyQt5 import QtCore, QtGui, QtWidgets
import presentation.healthcare_main as healthcare_main
from data import healthcare as healthcare
from businessLogic import navigation, login_logic, manage_patient_logic

class Healthcare(QtWidgets.QDialog, healthcare_main.Ui_Dialog):
    def __init__(self,  healthcareProvider, parent=None):
        super(Healthcare, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Healthcare Home")
        self.logout.clicked.connect(self.logOut)
        self.healthcareAll = healthcareProvider
        self.healthcareId = healthcareProvider[0]
        self.populatePatients()
        self.totalClientsLabel.setText(str(self.patientCount()))
        self.manage_client.clicked.connect(self.managePatient)



    def managePatient(self):
        database = healthcare.Healthcare()
        patient = database.getPatient(self.patient_manage_list.currentText())
        print(patient)
        database.close()

        manage_client_view = manage_patient_logic.ManagePatient(healthcareProvider = self.healthcareAll, patient=patient) # main screen
        self.setView(manage_client_view)

    def patientCount(self):
        database = healthcare.Healthcare()
        patientCount = database.getPatientCount(self.healthcareId)
        return patientCount[0]


    def populatePatients(self):
        self.patient_manage_list.clear()
        database = healthcare.Healthcare()
        patients = database.getPatients(self.healthcareId)
        for patient in patients:
             self.patient_manage_list.addItem(patient[0])

    def logOut(self):
        login_view = login_logic.Login() # main screen
        self.setView(login_view)
    

    def setView(self, view):
        navigation.close()
        navigation.set(view)
        navigation.show()