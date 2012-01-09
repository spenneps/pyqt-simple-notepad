import sys
from PyQt4.QtGui import QMainWindow, QMessageBox
from tabbar import *
from toolbar import *
from document import *

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle("Txtr")
        self.resize(1100, 500)
        self.setDocumentMode(True)
        self.InitLayout()

    
    def InitLayout(self):
        self.tabs = TabWidget()

        self.setCentralWidget(self.tabs)
        toolbar = ToolBar(self)
        self.addToolBar(toolbar)
        
    def AskToSave(self):
        msgBox = QMessageBox(self)
        msgBox.setText("Document has been modified")
        msgBox.setInformativeText("Do you want to save your changes ?")
        msgBox.setStandardButtons(QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)
        msgBox.setDefaultButton(QMessageBox.Save)
        result = msgBox.exec_()
        if result == QMessageBox.Save:
            return True
        elif result == QMessageBox.Discard:
            return False
        elif result == QMessageBox.Cancel:
            return "cancel"
    
        return True

    def closeEvent(self,  event):
        if self.doc.fileName == None and self.doc.toPlainText() == "":
            pass
        elif self.doc.fileName != None or self.doc.toPlainText() != "":
            result = self.AskToSave()
            if result == True:
                self.doc.SaveDocument()
                event.accept()
            if result == False:
                event.accept()
            if result == "cancel":
                event.ignore()
    

