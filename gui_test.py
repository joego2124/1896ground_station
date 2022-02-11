from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

connected = False

Form, Window = uic.loadUiType("main.ui")

app = QApplication([])
window = Window()

form = Form()
form.setupUi(window)

def connectClicked():
  print(connected)

form.connectButton.clicked.connect(connectClicked)

window.show()
app.exec_()