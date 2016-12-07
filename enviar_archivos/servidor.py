#!/usr/bin/python
# -*- coding: utf-8 -*-
##############################
# Author: HackerAzteca       #
# Licence: Creative Common   #
# Web: hackerazteca.org      #
# Share&Help                 #
##############################

from socket import socket, error

def main():
	s =  socket()

	s.bind(("localhost", 2001))
	print("Localhost, escuchando en el puerto: 2001")
	s.listen(0)
	conn, addr = s.accept()

	f = open("captura_recv.png", "wb")

	while True:
		try:
			input_data = conn.recv(1024)
			pass
		except error:
			print("Error de lectura")
			break
		else:
			if (input_data):
				if(isinstance(input_data, bytes)):
					end = input_data[0] ==1
					pass
				else:
					end = input_data == chr(1)
					pass
				if not end:
					f.write(input_data)
					pass
				else:
					break
				pass
	print("El archivo se ha recivido correctamente.")
	f.close()
	pass

if __name__ == "__main__":
	main()
