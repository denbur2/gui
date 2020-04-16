import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

app = QApplication(sys.argv)

w = QWidget()
w.setGeometry(50,50,500,500)
w.setWindowTitle("my Gui")
w.setWindowIcon(QIcon("b.jpg"))
buttonBox = QtWidgets.QDialogButtonBox(Dialog)






w.show()
sys.exit(app.exec_())