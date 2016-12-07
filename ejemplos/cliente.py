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

# creando un socket TCP/IP

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 2001)
print( 'Conectando a %s por el puerto %s' % server_address)

sock.connect(server_address)
while True:
	try:
		# enviando datos
		message = input("Mensaje >> ")
		print( 'Enviando...%s' % message)
		sock.sendall(message.encode())

		if message == "close":
			print("Se termino el juego...")
			break
			pass

		#Buscando respuesta
		amount_received = 0
		amount_expected = len(message)

		while amount_received < amount_expected:
			data = sock.recv(1024).decode()
			amount_received += len(data)
			print( 'Reciviendo %s' % data)
			print("....................................")
			pass
		pass
	finally:
		#print( ' Cerrando socket...')
		#sock.close()
		pass
	pass

#print("Cerrando socket!")
#sock.close()

class Hola(object):
	"""docstring for Hola"""
	def __init__(self, arg):
		super(Hola, self).__init__()
		self.arg = arg
		pass
	pass


		
