from PyQt5 import QtCore, QtGui, QtWidgets
from businessLogic import first_screen_logic
from businessLogic import navigation

if __name__ == "__main__":
    import sys
    
    app = QtWidgets.QApplication(sys.argv)
    first_screen_view = first_screen_logic.FirstScreen()
    navigation.set(first_screen_view)
    navigation.show()

    sys.exit(app.exec_())