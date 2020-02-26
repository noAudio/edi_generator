import claim_creator
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QFileDialog
from MainWindow import Ui_MainWindow
import sys

# run the claim creator function
# claim_creator.claim_generator()


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        # draw the ui
        self.setupUi(self)
        # browse for file and folder location
        self.btnAddFileLocation.clicked.connect(self.pickFile)
        self.btnOutputFolder.clicked.connect(self.pickFolder)
        self.launchFolder = self.chkOpenOuputFolder.clicked.connect(
            self.launchFolderWhenComplete)
        # assign path to excel file and path to output folder
        #  to variables
        self.excelpath = self.txtExcelLocation.text()
        self.outputfolder = self.txtOutputLocation.text()
        # run the claim generation script while passing in the
        # paths to the file and output folder and whether to
        # launch the output folder when done
        self.btnGenerateClaims.clicked.connect(
            self.runClaimGenerator)

    def pickFile(self):
        # launch the native file picker dialog
        fileName, _ = QFileDialog.getOpenFileName(
            self, 'QFileDialog.getOpenFileName()', '', 'All Files (*);;Excel Files (*.xlsx)')
        # set the value of the textbox near the browse file
        # button to the user selected file
        self.txtExcelLocation.setText(fileName)
        if fileName:
            print(fileName)

    def pickFolder(self):
        # launch the native file picker dialog and set it
        # to only query directory paths
        folderName = str(QFileDialog.getExistingDirectory(
            self, "Select Directory"))
        # set the value of the textbox near the browse folder
        # button to the user selected path
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

    def runClaimGenerator(self):
        claim_creator.claim_generator(
            self.excelpath, self.outputfolder, self.launchFolder)


app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
