import sys  
from PyQt4 import QtGui 
from  document  import *
  
class TabWidget(QtGui.QTabWidget):  
	def __init__(self, parent=None):  
		super (TabWidget, self).__init__(parent)  
		self.setTabsClosable(True)  
		self.tabCloseRequested.connect(self.closeTab)  
		self.setMovable(True)
		self.setTabShape(self.Rounded)
		self.addNewTab()

	def tabInserted(self, index):  
		self.tabBar().setVisible(self.count() > 1)  
		

	def tabRemoved(self, index):  
		self.tabBar().setVisible(self.count() > 1)  


	def getCurrentWidget(self):
		return self.currentWidget()

	def closeTab(self,index):
		self.last_closed_doc =  self.widget(index)
		self.removeTab(index)
	def addNewTab(self,title = "Untitled"):
		self.addTab(Document(), title)  

