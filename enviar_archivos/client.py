#!/usr/bin/python
# -*- coding: utf-8 -*-

##############################
# Author: HackerAzteca                                            #
# Licence: Creative Common                                   #
# Web: hackerazteca.org                                          #
# Share&Help                                                              #
##############################

# Importamos los módulos  necesarios
import socket, os, time
import getImage

class Cliente():

	def __init__(self):
		# Definimos el puerto de control CPORT y el puerto multimedia MPORT
		self.CPORT = 9091
		self.MPORT = 9090
		self.cont = 0
		pass
	# Obtenemos el ultimo valor del contador de capturas
	def getCont(self):
		f = open("cont.txt", "r")
		cont = f.readline()
		f.close()
		return cont
		pass
	#Guardamos el contador en el archivo
	def setCont(self, value):
		f = open("cont.txt", "w")
		f.write(str(value))
		f.close()
		pass

	def captura(self, host):
		# Obtenemos el contador de capturas almacenado
		value = self.getCont()
		# Quitamos los saltos de linea
		value = value.rstrip("\n")
		# Incrementamos en 1 el valor del contador
		self.cont = int(value) + 1
		# Guardamos el nuevo valor del contador de capturas
		self.setCont(self.cont)
		# Instanciamos un objeto de Video
		get = getImage.Video()
		# Capturamos una  imagen, para esto enviamos dos parametros
		# 1.- la direccion del host
		# 2.- el valor del contador de capturas
		get.imagen(host, self.cont)
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

		self.captura(self.HOST)

		# Leer el archivo 
		archivo  = "cap.png"
		# Cambiamos comillas para evitar problemas en loas archivos con espacios
		archivo = archivo.replace('"', '')
		# Creamos un socket que envia la ruta del archivo
		cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		# Se conecta al puerto de control
		cs.connect((self.HOST, self.CPORT))
		# Envia la ruta del archivo
		archivo =str(self.cont) + '_' + self.HOST+ "_" + archivo
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

while True:
	App.sendImage()
	time.sleep(10)
	pass


