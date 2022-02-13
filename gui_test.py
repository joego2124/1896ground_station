import sys
from time import sleep
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from python_socket_test.DroneClients import DroneClients

Form, Window = uic.loadUiType("main.ui")

app = QApplication([])
window = Window()

form = Form()
form.setupUi(window)


def startDroneClient():
	map = 0  # get_map
	telemetry = 0 #get_telemetry
	stop_threads = False

	# map object, telemetry object, SERVER, PORT
	drone_clients = DroneClients(map, telemetry,"192.168.1.108", 5050 )
	drone_clients.run()
	drone_clients.send_command("START")
	drone_clients.send_command("STOP")
	drone_clients.send_command("ARM")
	drone_clients.send_command("DISARM")
	print('done')

form.connectButton.clicked.connect(startDroneClient)

window.show()
app.exec_()
