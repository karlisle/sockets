#!/usr/bin/python
# -*- coding: utf-8 -*-

##############################
# Author: HackerAzteca                                            #
# Licence: Creative Common                                   #
# Web: hackerazteca.org                                          #
# Share&Help                                                              #
##############################

# Importamos los módulos  necesarios
import socket, os
import getImage

class Cliente():

	def __init__(self):
		# Definimos el puerto de control CPORT y el puerto multimedia MPORT
		self.CPORT = 9091
		self.MPORT = 9090
		pass

	def captura(self):
		# Obtenemos la captura
		get = getImage.Video()
		get.imagen()
		pass

	# Definimos una funcion para transformar un tamaño en bytes en un tamaño más 
	# fácil de leer:
	def humanMode(self, cantidad):
		sufijos = [("B", 2**10), ("K", 2**20),("M", 2**30),("G", 2**40),("T", 2**50)]
		for suf, lim in sufijos:
			if cantidad > lim:
				continue
				pass
			else:
				return round(cantidad/float(lim/2**10), 2).__str__() + suf
				pass
			pass
		pass
	def sendImage(self):
		# Llamamos a la funcion captura, la cual guardara una imagen 
		# obtenida de la webcam

		self.captura()

		print ("Kalhua, pitbull guard!!")

		# Definimos un diccionario con las direcciones IP que queremos usar


		amigos = {	"Kharl": '192.168.1.71',
				"Pi": '192.168.1.110',
				"SERVER" : '192.168.1.71' }

		# Mostramos las diferentes opciones
		#for key, value in amigos.items():
		#	print("--- %s ---: en la dirección     --> %s " %(key, value))
		#	pass

		#seleccion = input("Indica el host al cual conectarse :  ")
		ip = amigos.get("Pi")
		print("Conectandose al host: %s" %(ip))

		# Si hemos elegido "dirs", nos dira la IP's  disponibles

		self.HOST = ip

		# Leer el archivo 
		archivo  = "captura.png"
		# Cambiamos comillas para evitar problemas en loas archivos con espacios
		archivo = archivo.replace('"', '')
		# Creamos un socket que envia la ruta del archivo
		cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		# Se conecta al puerto de control
		cs.connect((self.HOST, self.CPORT))
		# Envia la ruta del archivo
		cs.send(b"SEND" + archivo.encode())
		print("SEND " + archivo)
		cs.close()

		#Otro socket, que envia el archivo
		ms = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		# Se conecta al puerto multimedia 
		ms.connect((self.HOST, self.MPORT))

		# Abrimos el archivo para leerlo:

		f = open(archivo, "rb")
		data = f.read()
		f.close()

		# Obtenemos el tamaño del archivo en bytes:
		enBytes = os.path.getsize(archivo)
		# Usamos la función anterior para convertir el tamaño:
		print ("Archivo", archivo, "leido (", str(self.humanMode(enBytes)), ").")
		# Enviamos los datos del archivo:
		ms.send(data)
		ms.close()
		# Fin
		print("Archivo ", archivo,  " enviado (", str(self.humanMode(enBytes)) ,")." )
		pass
	
	pass

App = Cliente()

App.sendImage()
