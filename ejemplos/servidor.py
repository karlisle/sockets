#!/usr/bin/python
# -*- coding: utf-8 -*-
##############################
# Author: HackerAzteca       #
# Licence: Creative Common   #
# Web: hackerazteca.org      #
# Share&Help                 #
##############################

import socket
import sys

# creando el socket TCP/IP

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)	


# Enlace de socket y puerto
server_address = ('localhost', 2001)

print('\nEmpezando a levantar %s puerto %s' % server_address)

sock.bind(server_address)

# Escuchando conexiones entrantes
sock.listen(1)

while True:
	#Esperando conexión
	print('Esperando conexiones...')
	connection, client_address = sock.accept()

	try:
		print('Conexion desde: ', client_address)

		# Recive los datos en trozos y retransmite
		while True:
			data = connection.recv(1024).decode()
			print('Recivido %s' % data)
			if data:
				print('Enviando mensaje de vuelta')
				print("....................................")
				msj = "Successed"
				connection.sendall(msj.encode())
				pass
			elif data == "close":
				break
				pass
			else:
				print('\tNo hay mas datos', client_address)
				break
			pass
		pass
	finally:
		# Cerrando conexion
		connection.close()
		pass
	pass
print("Adios!")
connection.close()





