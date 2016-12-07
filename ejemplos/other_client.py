#!/usr/bin/python
# -*- coding: utf-8 -*-
##############################
# Author: HackerAzteca       #
# Licence: Creative Common   #
# Web: hackerazteca.org      #
# Share&Help                 #
##############################

import socket

# Creamos un objeto para el servidor
s = socket.socket()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = "localhost"
port = 2001
print("Server inicado en " , server + ":", port)

# Nos conectamos al servidor con el metodo connect
s.connect((server, port))

mensaje = input("Mensaje a enviar: ")
s.sendall(mensaje.encode())


print("Adios")
s.close
