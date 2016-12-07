#!/usr/bin/python
# -*- coding: utf-8 -*-
##############################
# Author: HackerAzteca       #
# Licence: Creative Common   #
# Web: hackerazteca.org      #
# Share&Help                 #
##############################

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = "localhost"
port = 9999
print("Server inicado en " , server + ":", port)

s.bind((server, port))

s.listen(5)

print("Servidor iniciado y escuchando...\n>>>")
while True:
	(sc, addr) = s.accept()
	print("Conexion encontrada\n")
	recivido = sc.recv(1024).decode()

	if recivido == "close":
		break
		pass

	print("Datos: ", recivido)
	r = "Correcto!"
	sc.send(r.encode())
	pass

print("Adios!!")
sc.close()
s.close()
