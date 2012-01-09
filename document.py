from PyQt4.QtGui import QTextEdit, QFileDialog

class Document(QTextEdit):
    def  __init__(self):
        QTextEdit.__init__(self)
        self.setFocus()
        self.lastSaved = None
        self.fileName = None
        self.ensureCursorVisible()
        self.defaultWeight = self.fontWeight()
    
    def CheckBeforeClosing(self):
        if self.toPlainText() != self.lastSaved:
            self.AskToSave()

    
    def SaveDocument(self):
        if self.fileName == None:
            self.fileName = QFileDialog.getSaveFileName(self,"Save File")

        f = open(self.fileName,  'w+')
        f.write(self.toPlainText())
        self.lastSaved = self.toPlainText()
        f.close()

    def JustifyLeft(self):
        self.setAlignment(Qt.AlignLeft)
        
    def JustifyCenter(self):
        self.setAlignment(Qt.AlignCenter)
        
    def JustifyRight(self):
        self.setAlignment(Qt.AlignRight)
        
    def FormatUnderline(self):
        if self.fontUnderline() == False:
            self.setFontUnderline(True)
        elif self.fontUnderline() == True:
            self.setFontUnderline(False)
    def FormatItalic(self):
        if self.fontItalic() == False:
            self.setFontItalic(True)
        elif self.fontItalic() == True:
            self.setFontItalic(False)
    def FormatBold(self):
        if self.fontWeight() < 100:
            self.setFontWeight(100)
        else:
            self.setFontWeight(self.defaultWeight)

