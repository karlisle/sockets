#!/usr/bin/python
# -*- coding: utf-8 -*-

##############################
# Author: @HackerAzteca                                      #
# Licence: Creative Common                                 #
# Web: https://github.com/karlisle                         #
# Share&Help                                                         #
##############################

import sys

import numpy as np
import  sqlite3
import  csv
import operator
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog, QPushButton, QLabel, QMessageBox
from PyQt5 import uic



class Visor(QMainWindow):
	def __init__(self):
		#Iniciar el objeto QMainWindow
		QMainWindow.__init__(self)
		# Cargar el archivo de interfaz
		uic.loadUi("visor.ui", self)

		self.next.clicked.connect(self.loadImage)
		pass
	# Cargamos las imagenes en el visor
	def loadImage(self):
		self.info.setText("Cargando imagen")
		self.image.setPixmap(QPixmap("./captura.png"))
		pass

	pass


#----------- Inicializar la applicacion-----------------------#
App = QApplication(sys.argv)
_visor = Visor()
_visor.show()
App.exec_()
