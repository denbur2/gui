import time
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import *
from PyQt5.QtCore import *

class fenster(QWidget):             #!
    def __init__(self):
        super().__init__()
        grid = QGridLayout()
        namen = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        posis = [(i, j) for i in range(3) for j in range(3)]
        for pos, name in zip(posis, namen):
            button = QPushButton(name)
            grid.addWidget(button, *pos)
        self.setLayout(grid)

        self.setGeometry(25,50,500,500)
        self.setWindowTitle("my Gui")
        self.setWindowIcon(QIcon("b.jpg"))
        #self.statusBar().showMessage('Achtung: diese seite ist nutzlos!')   #status anzeige
        self.show()
app = QApplication(sys.argv)
w = fenster()
sys.exit(app.exec_())