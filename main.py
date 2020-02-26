import claim_creator
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QFileDialog
from MainWindow import Ui_MainWindow
import sys

# run the claim creator function
# claim_creator.claim_generator()


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    launchFolder = False

    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        # run the claim generation script

        # browse for file and folder location
        self.btnAddFileLocation.clicked.connect(self.pickFile)
        self.btnOutputFolder.clicked.connect(self.pickFolder)
        launchFolder = self.chkOpenOuputFolder.clicked.connect(
            self.launchFolderWhenComplete)
        # assign path to excel file and path to output folder
        #  to variables
        excelpath = self.txtExcelLocation.text()
        outputfolder = self.txtOutputLocation.text()

    def pickFile(self):
        fileName, _ = QFileDialog.getOpenFileName(
            self, 'QFileDialog.getOpenFileName()', '', 'All Files (*);;Excel Files (*.xlsx)')
        self.txtExcelLocation.setText(fileName)
        if fileName:
            print(fileName)

    def pickFolder(self):
        folderName = str(QFileDialog.getExistingDirectory(
            self, "Select Directory"))
        self.txtOutputLocation.setText(folderName)
        if folderName:
            print(folderName)

    def launchFolderWhenComplete(self):
        launchfolder = 'Unassigned'
      # check whether to launch folder after claim generation
        if self.chkOpenOuputFolder.isChecked():
            launchfolder = True
            print(launchfolder)
        else:
            launchfolder = False
            print(launchfolder)

        return launchfolder


app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
