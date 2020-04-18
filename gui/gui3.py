import time
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import *
from PyQt5.QtCore import *

class fenster(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(25,50,500,500)
        self.setWindowTitle("my Gui")
        self.setWindowIcon(QIcon("b.jpg"))
        self.statusBar().showMessage('Achtung: diese seite ist nutzlos!')   #status anzeige
        
        exitme = QAction(QIcon('b.jpg'), '&exit', self)
        exitme.setShortcut('ctrl+e')
        exitme.setStatusTip('exit')
        exitme.triggered.connect(self.close)

        menubar = self.menuBar()
        file = menubar.addMenu('file')
        file.addAction(exitme)

        toolbar = self.addToolBar('exit')
        toolbar.addAction(exitme)

        self.show()

app = QApplication(sys.argv)
w = fenster()
sys.exit(app.exec_())