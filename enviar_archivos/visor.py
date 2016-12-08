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

		#Variables globales
		self.contador = 0

		self.next.clicked.connect(self.loadImage)
		self.back.clicked.connect(self.lastImage)
		self.exit.clicked.connect(self.close)
		pass
	# Obtener  el numero de capturas
	def getCont(self):

		f = open('cont.txt', 'r')
		cont = f.readline()
		numCapt = int(cont)
		f.close()
		return numCapt
		pass

	# Cargamos las imagenes en el visor
	def loadImage(self):
		contador = self.getCont()
		nameImage = str(contador-1) + "_192.168.1.110_cap.png"
		self.info.setText("Cargando imagen: %s" %(nameImage))
		self.image.setPixmap(QPixmap('./'+nameImage ))
		pass
	# Cargamos la imagen anterior 
	def  lastImage(self):
		contador -= 1
		nameImage = str(contador) + "_192.168.1.110_cap.png"
		self.info.setText("Cargando imagen: %s" %(nameImage))
		self.image.setPixmap(QPixmap('./' + nameImage))
		pass
	# Salir
	def  close(self):
		exit()
		pass
	pass


#----------- Inicializar la applicacion-----------------------#
App = QApplication(sys.argv)
_visor = Visor()
_visor.show()
App.exec_()
