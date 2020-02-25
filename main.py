import claim_creator
from PyQt5 import QtWidgets, uic
from MainWindow import Ui_MainWindow
import sys

# run the claim creator function
# claim_creator.claim_generator()

launch_folder = False


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)


app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
