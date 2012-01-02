#! /usr/bin/python

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
from PyQt4 import  uic
import os


class MainWindow(QMainWindow):
	
	filepath  = ""
	rootpath  = "/home"
	last_saved = ""

	def __init__(self):

		QMainWindow.__init__(self)
		uic.loadUi('interface.ui', self)

		self.file_new.activated.connect(self.file_new_func)
		self.file_open.activated.connect(self.file_open_func)
		self.file_save.activated.connect( self.file_save_func)
		self.file_saveas.activated.connect( self.file_saveas_func)
		self.file_print.activated.connect( self.file_print_func)
		self.file_preview.activated.connect( self.file_preview_func)

	def save_request(self):
		content  =  self.textEdit.toPlainText()
		if content != self.last_saved and content != "" :
			result  = self.msg_box()
			if result == QMessageBox.Save:
				self.file_save_func()
				return True
			elif result == QMessageBox.Discard:
				return True
			elif result == QMessageBox.Cancel:
				return False


		return True
			

	def closeEvent(self,event):

		result = self.save_request()
	
		if result:
			event.accept()
		else:
			event.ignore()

	def file_new_func(self):

		if self.save_request():

			self.textEdit.clear()	
			self.filepath = ""
			self.statusbar.showMessage("new file")

	def file_open_func(self):
		fname = QFileDialog.getOpenFileName(self, 'Open file',self.rootpath,"Text files (*.txt);")	
		f = open(fname, 'r')
		self.filepath = f        
		with f:        
			data = f.read()
			self.textEdit.setText(data) 

		self.statusbar.showMessage("file opened : "+fname)

	def file_save_func(self):

		
		if self.filepath == "":
			fname = QFileDialog.getSaveFileName(self, 'Save file',self.rootpath,"Text files (*.txt);")		
			self.filepath = fname   

		
		content  =  self.textEdit.toPlainText()
		filepath = self.filepath
		
		self.save_my_file(filepath,content)

	def file_saveas_func(self):

		fname = QFileDialog.getSaveFileName(self, 'Save file',self.rootpath,"Text files (*.txt);")		
		self.filepath = fname   		
		content  =  self.textEdit.toPlainText()
		filepath = self.filepath
		
		self.save_my_file(filepath,content)


	def file_print_func(self):
		dialog = QPrintDialog()
		if dialog.exec_() == QDialog.Accepted:
			self.textEdit.document().print_(dialog.printer())


	def file_preview_func(self):
	        dialog = QPrintPreviewDialog()
	        dialog.paintRequested.connect(self.textEdit.print_)
	        dialog.exec_()




	def save_my_file(self,filepath,content):

	
		try:	
			f = open(filepath,"a+")
			f.write(content)
			f.close()
			self.statusbar.showMessage("file saved : "+filepath)			
			self.last_saved = content

			
		except IOError as (errno, strerror):
			self.statusbar.showMessage(strerror)			
		except:
			pass

	def msg_box(self):
		msgBox = QMessageBox(self)
		msgBox.setText("The document has been modified.");
		msgBox.setInformativeText("Do you want to save your changes?");
		msgBox.setStandardButtons(QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel);
		msgBox.setDefaultButton(QMessageBox.Save);
		msgBox.setText("The document has been modified.")
		result = msgBox.exec_()
		
		return result
	
app = QApplication(sys.argv)
main = MainWindow()
main.show()
sys.exit(app.exec_())
	
