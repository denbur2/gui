import time
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import *
from PyQt5.QtCore import *

class fenster(QWidget):

    def __init__(self):
        super().__init__()
        self.initme()
    def initme(self):
        self.setGeometry(25,50,500,500)
        self.setWindowTitle("my Gui")
        self.setWindowIcon(QIcon("b.jpg"))
        button = QPushButton('drück mich', self)
        button.move(50,50)
        QToolTip.setFont(QFont('Arial', 14))
        button.setToolTip('this is a <b>Great</b> button <b>!</b>')
        self.setToolTip('das hier ist ein fenster')

        button.clicked.connect(self.pressed)
        #button.clicked.connect(QtCore.QCoreApplication.instance().quit)


        self.show()

    def pressed(self):
        a = 100
        print('button wurde gedrückt')
        sender = self.sender()
        sender.move(a,a)

    def keyPressEvent(cls, self, QKeyEvent):
        if QKeyEvent == Qt.Key_W:
            self.close()
        #return super().keyPressEvent(self, QKeyEvent)   



app = QApplication(sys.argv)
w = fenster()
sys.exit(app.exec_())