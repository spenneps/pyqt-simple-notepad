from PyQt4.QtGui import QToolBar,  QComboBox,  QFontComboBox, QIcon, QLineEdit,  QToolButton,  QColorDialog,  QColor, QFileDialog
from PyQt4.QtCore import Qt
import txtr
#import Settings

class ToolBar(QToolBar):
    def __init__(self, mainWindow):
        QToolBar.__init__(self)
        self.mainWindow = mainWindow
        self.doc = mainWindow.tabs.getCurrentWidget()
        self.Items()
        self.Layout()
        self.Signals()
 #       settings = Settings.Settings()
        
    
    def Items(self):
        self.Item_FontControls()
        self.Item_SearchBox()
        
        
    def Item_FontControls(self):   
        self.fontComboBox = QFontComboBox()
        self.fontSize = QComboBox()
        self.fontSize.setEditable(True)
        fontSizes = ("72","60","48","36","24","18","16","12","11")
        for i in fontSizes:
            self.fontSize.addItem(i)
        self.fontSize.setCurrentIndex(7)
        

    def Item_SearchBox(self):
        self.searchBox = QLineEdit()
        self.searchBox.setMaximumWidth(200)
        self.searchBox.setAlignment(Qt.AlignLeft)
        self.searchBox.setPlaceholderText("Type To Search ...")

    def Layout(self):
        self.newFile = self.addAction(QIcon("icons/document-new.svg"), "New File")
        self.openFile = self.addAction(QIcon("icons/document-open.svg"), "Open File")
        self.saveFile = self.addAction(QIcon("icons/document-save.svg"), "Save File")
        self.addSeparator()
        self.undo = self.addAction(QIcon("icons/undo.svg"), "Undo")
        self.redo = self.addAction(QIcon("icons/redo.svg"), "Redo")
        self.addSeparator()
        self.cut = self.addAction(QIcon("icons/edit-cut.png"), "Cut")
        self.copy = self.addAction(QIcon("icons/edit-copy.png"), "Copy")
        self.paste = self.addAction(QIcon("icons/edit-paste.png"), "Paste")
        self.selectAll = self.addAction(QIcon("icons/edit-select-all.svg"), "Select All")
        self.addSeparator()
        self.justifyLeft = self.addAction(QIcon("icons/align-horizontal-left.svg"), "Justify Left")
        self.justifyCenter = self.addAction(QIcon("icons/align-horizontal-center.svg"), "Justify Center")
        self.justifyRight = self.addAction(QIcon("icons/align-horizontal-right.svg"), "Justify Right")
        self.addSeparator()
        self.bold = self.addAction(QIcon("icons/format-text-bold.png"), "Bold")
        self.italic = self.addAction(QIcon("icons/format-text-italic.png"), "Italic")
        self.underline = self.addAction(QIcon("icons/format-text-underline.png"), "Underline")
        self.addWidget(self.fontComboBox)
        self.addWidget(self.fontSize)
        self.fontColor = self.addAction(QIcon("icons/color.svg"),  "Font Color")
        self.addSeparator()
        self.addWidget(self.searchBox)
        self.addAction(QIcon("icons/stock_properties.svg"), "Settings")
        self.saveFile.setEnabled(False)
        self.cut.setEnabled(False)
        self.undo.setEnabled(False)
        self.redo.setEnabled(False)
        self.doc.textChanged.connect(self.EnableActions)
            
    def EnableActions(self):
        self.saveFile.setEnabled(True)
        self.cut.setEnabled(True)
        self.undo.setEnabled(True)
        self.redo.setEnabled(True)
        
    def DisableActions(self):
        self.saveFile.setEnabled(False)
        self.cut.setEnabled(False)
        self.undo.setEnabled(False)
        self.redo.setEnabled(False)

    def StartNewWindow(self):
#        main()
	 self.mainWindow.tabs.addNewTab()
        
    def fontColorDialog(self):
        self.cDialog = QColorDialog()
        colorDialog = QColorDialog.open(self.cDialog,self.FormatFontColor)
        
    def OpenFile(self):
        if self.doc.fileName != None:
            #new Window
            pass
        elif self.doc.fileName == None:
            self.doc.fileName = QFileDialog.getOpenFileName(self,"Open File")
            f = open(self.doc.fileName, "r")
            data = f.read()
            self.doc.setText(data)
            f.close()
            fileNameOnly = self.getFileName()
            self.mainWindow.setWindowTitle(self.mainWindow.windowTitle()+" => "+fileNameOnly)
            self.DisableActions()
    
    def getFileName(self):
        fileinit = self.doc.fileName.split("/")
        fileNameOnly = fileinit[-1:]
        fileNameOnly = fileNameOnly[0]
        return fileNameOnly

    def Signals(self):        
        self.newFile.activated.connect(self.StartNewWindow)
        self.openFile.activated.connect(self.OpenFile)
        self.saveFile.activated.connect(self.doc.SaveDocument)
        self.saveFile.activated.connect(lambda: self.saveFile.setEnabled(False))
        self.undo.activated.connect(self.doc.undo)
        self.redo.activated.connect(self.doc.redo)
        self.copy.activated.connect(self.doc.copy)
        self.cut.activated.connect(self.doc.cut)
        self.paste.activated.connect(self.doc.paste)
        self.selectAll.activated.connect(self.doc.selectAll)
        self.justifyLeft.activated.connect(lambda: self.doc.setAlignment(Qt.AlignLeft))
        self.justifyCenter.activated.connect(lambda: self.doc.setAlignment(Qt.AlignCenter))
        self.justifyRight.activated.connect(lambda: self.doc.setAlignment(Qt.AlignRight))
        self.bold.activated.connect(self.doc.FormatBold)
        self.italic.activated.connect(self.doc.FormatItalic)
        self.underline.activated.connect(self.doc.FormatUnderline)
        self.fontComboBox.currentFontChanged.connect(lambda: self.doc.setFont(self.fontComboBox.currentFont()))
        self.fontSize.currentIndexChanged.connect(lambda: self.doc.setFontPointSize(int(self.fontSize.currentText())) )
        self.fontColor.activated.connect(self.fontColorDialog)
        self.searchBox.textChanged.connect(self.Search)
        
    def Search(self):
        searchFor  = self.searchBox.text()
        result = self.doc.find(searchFor)
        if result == True:
            self.doc.setTextBackgroundColor(QColor("#ccc"))

    def FormatFontColor(self):
        self.doc.setTextColor(self.cDialog.currentColor())
