import claim_creator
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QFileDialog
from MainWindow import Ui_MainWindow
import sys

# run the claim creator function
# claim_creator.claim_generator()

launchfolder = False


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        # assign path to excel file and path to output folder
        #  to variables
        excelpath = self.txtExcelLocation.text()
        outputfolder = self.txtOutputLocation.text()
        # check whether to launch folder after claim generation
        if self.chkOpenOuputFolder == True:
            launchfolder = True

        # run the claim generation script

        self.setupUi(self)

    def pick_folder(self):
        fileName, _ = QFileDialog.getOpenFileName(
            self, 'QFileDialog.getOpenFileName()', '', 'All Files (*);;Excel Files (*.xlsx)')
        if fileName:
            print(fileName)


app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
