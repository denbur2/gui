import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon

class fenster(QWidget):

    def __ini__(self):
        super().__init__()
        self.initme()
    def initme(self):
        self.setGeometry(50,50,500,500)
        self.setWindowTitle("my Gui")
        self.setWindowIcon(QIcon("b.jpg"))
        self.button = QPushButton('drück mich', self)
        self.show()

app = QApplication(sys.argv)
w = fenster()
sys.exit(app.exec_())