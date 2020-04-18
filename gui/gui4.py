import time
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import *
from PyQt5.QtCore import *

class fenster(QWidget):             #!
    def __init__(self):
        super().__init__()
        
        button1 = QPushButton('button1')
        button2 = QPushButton('button2')
        h = QHBoxLayout()                   #horizontal 
        h.addWidget(button1)
        h.addStretch(1)
        h.addWidget(button1)
        h.addWidget(button2)
        v = QVBoxLayout()                   #vertikal
        v.addStretch(1)
        v.addLayout(h)
        self.setLayout(v)
        
        self.setGeometry(25,50,500,500)
        self.setWindowTitle("my Gui")
        self.setWindowIcon(QIcon("b.jpg"))
        #self.statusBar().showMessage('Achtung: diese seite ist nutzlos!')   #status anzeige
        self.show()
app = QApplication(sys.argv)
w = fenster()
sys.exit(app.exec_())