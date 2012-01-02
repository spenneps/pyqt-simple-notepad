#! /usr/bin/python

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
from PyQt4 import  uic



class MainWindow(QMainWindow):
	#text = ""
	def __init__(self):
		QMainWindow.__init__(self)
		uic.loadUi('test.ui', self)



	
   

app = QApplication(sys.argv)
main = MainWindow()
main.show()
sys.exit(app.exec_())
	
