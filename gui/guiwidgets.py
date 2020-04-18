import time
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import *
from PyQt5.QtCore import *

class fenster(QWidget):             #!
    def __init__(self):
        super().__init__()

        text = QLabel('das ist sind tolle widgets', self)
        text.move(20,20)

        bild = QLabel(self)
        bild.setPixmap(QPixmap('b.jpg'))
        bild.move(20,35)

        link = QLabel(self)
        link.setText("<a href='https://www.google.com'>zu google</a>")
        link.linkHovered.connect(self.clicked)
        link.move(300,35)

        box = QCheckBox("check me", self)
        box.move(20,300)
        box.stateChanged.connect(self.clicked)

        togglebtn = QPushButton('clickme', self)
        togglebtn.setCheckable(True)
        togglebtn.clicked[bool].connect(self.clicked)



        self.setGeometry(25,50,500,500)
        self.setWindowTitle("my Gui")
        self.setWindowIcon(QIcon("b.jpg"))
        #self.statusBar().showMessage('Achtung: diese seite ist nutzlos!')   #status anzeige
        self.show()

    def clicked(self, down):
        if down:
            print('down')
        else:
            print('up')

app = QApplication(sys.argv)
w = fenster()
sys.exit(app.exec_())