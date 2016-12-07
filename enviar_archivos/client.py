#!/usr/bin/python
# -*- coding: utf-8 -*-

##############################
# Author: HackerAzteca                                            #
# Licence: Creative Common                                   #
# Web: hackerazteca.org                                          #
# Share&Help                                                              #
##############################

# Importamos los módulos  necesarios
import socket, os, sys

# Definimos el puerto de control CPORT y el puerto multimedia MPORT

CPORT = 9091
MPORT = 9090

# Definimos una funcion para transformar un tamaño en bytes en un tamaño más 
# fácil de leer:

def humanMode(cantidad):
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
print ("Enviar archivo por internet")

# Definimos un diccionario con las direcciones IP que queremos usar


amigos = {"Kharl": '192.168.1.71',
		"Pi": '192.168.1.110',
		"SERVER" : '192.168.1.71' }

# Mostramos las diferentes opciones
for key, value in amigos.items():
	print("--- %s ---: en la dirección     --> %s " %(key, value))
	pass

seleccion = input("Indica el host al cual conectarse :  ")
ip = amigos.get(seleccion)
print("Conectandose al host: %s" %(ip))

# Si hemos elegido "dirs", nos dira la IP's  disponibles

HOST = ip

# Leer el archivo 
archivo  = input("Indica el nombre del archivo: ")
# Cambiamos comillas para evitar problemas en loas archivos con espacios
archivo = archivo.replace('"', '')
# Creamos un socket que envia la ruta del archivo
cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Se conecta al puerto de control
cs.connect((HOST, CPORT))
# Envia la ruta del archivo
cs.send(b"SEND" + archivo.encode())
print("SEND " + archivo)
cs.close()

#Otro socket, que envia el archivo
ms = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Se conecta al puerto multimedia 
ms.connect((HOST, MPORT))

# Abrimos el archivo para leerlo:

f = open(archivo, "rb")
data = f.read()
f.close()

# Obtenemos el tamaño del archivo en bytes:
enBytes = os.path.getsize(archivo)
# Usamos la función anterior para convertir el tamaño:
print ("Archivo", archivo, "leido (", str(humanMode(enBytes)), ").")
# Enviamos los datos del archivo:
ms.send(data)
ms.close()
# Fin
print("Archivo ", archivo,  " enviado (", str(humanMode(enBytes)) ,")." )
input("Presione una tecla para terminarl....")
