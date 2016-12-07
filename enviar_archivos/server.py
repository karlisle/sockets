#!/usr/bin/python
# -*- coding: utf-8 -*-

##############################
# Author: @HackerAzteca                                      #
# Licence: Creative Common                                 #
# Web: https://github.com/karlisle                         #
# Share&Help                                                         #
##############################

# Importamos algunos modulos

import os
import socket, time, string, sys
from urllib.parse import urlparse
from threading import *


# Creamos un objeto de tipo StreamHandler:

class StreamHandler(Thread):
	def __init__(self):
		Thread.__init__(self)
		pass

	def run(self):
		# Aquí tenemos un método que nos puestra que esmops trabajando con objetos de tipo socket

		self.process() 		
		pass
	def bindmsock(self):
		# Creamos un objeto de socket
		self.msock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		# Estas banderas son para evitar que marque el siguiente error:
		# socket.error: [Errno 98] Address already in use
		# basicamnete le dice al kernel que no espere y reuse inmediatamente el puerto 
		self.msock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		# Enlazamos el self al puerto 9090 (multimedia)
		self.msock.bind(('', 9090))
		self.msock.listen(1)
		print('[INTR] Esperando al puerto 9090') 
		#pass
		#def acceptcsock(self):
		# Acceptamos la conexión
		self.mconn, self.maddr = self.msock.accept()
		print("[INTR] Usuario", self.maddr , " conectado.")
		pass
	def bindcsock(self):
		# Enlazamos al puerto 9091 (control)
		self.csock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.csock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.csock.bind(('', 9091))
		self.csock.listen(1)
		print("[CTRL] esperando en el puerto 9091")
		pass
	def acceptmsock(self):
		# Aceptamos
		self.filename = 'No_name'
		self.cconn, self.maddr = self.csock.accept()
		print("[CTRL] Usuario %s conectado." %(self.maddr[0]))

		while 1:
			# Capturamos los datos
			self.data = self.cconn.recv(1024).decode()
			print(self.data)
			if not self.data:
				print("\n\t NO DATA")
				break
				pass
			# Si los datos comeinzan con SENDm captamos el nombre de archivo 
			elif (self.data[0:4] == "SEND"):
				self.filename = self.data[4:]

				print("[CTRL] Preparado para recivir %s" %(self.filename))
				break
				pass
			pass
		#pass
		#def transfer(self):
		print("[INTR] Transfiriendo datos de %s" % (self.filename))
		# Obtenemos el nombre del archivo y su extención
		finalName = os.path.basename(self.filename)
		print("\n\t Nombre final", finalName, "\n")

		# Lo guardamos en el directorio recivido
		print
		f = open('rcv_' + finalName, "wb")
		# Ahora el bucle que captura los datos del archivo
		while True:
			data = self.mconn.recv(1024)
			if not data:
				break
				pass
			f.write(data)
			pass
		f.close()
		# Hemos escrito los datos en el nuevo archivo
		print("[Media] Recivido %s" % self.filename)
		print("[Media] Cerrando el flujo de %s" % self.filename)
		self.csock.close()
		self.cconn.close()
		pass
	def close(self):
		# Cerramos todos los sockets:
		self.csock.close()
		self.cconn.close()
		self.mconn.close()
		self.msock.close()
		pass
	def process(self):
		# Siempre aceptamos las conexiones
		while True:
			self.bindcsock()
			#self.acceptcsock()
			self.bindmsock()
			self.acceptmsock()
			#self.transfer()
			self.close()
			pass
		pass
	pass

s = StreamHandler()
s.run()
