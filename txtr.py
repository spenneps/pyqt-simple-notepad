from mainwindow import *
from PyQt4.QtGui import QApplication

class Clipper():
    def __init__(self):
        self.window = MainWindow()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Clipper = Clipper()
    Clipper.window.show()
    sys.exit(app.exec_())
    
