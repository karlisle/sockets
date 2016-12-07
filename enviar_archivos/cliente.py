#!/usr/bin/python
# -*- coding: utf-8 -*-
##############################
# Author: HackerAzteca       #
# Licence: Creative Common   #
# Web: hackerazteca.org      #
# Share&Help                 #
##############################

from socket import socket

def main():
	s =socket()
	s.connect(("localhost", 2001))

	while True:
		f = open("captura.png", "rb")
		content  = f.read(1024)

		while content:
			s.send(content)
			content = f.read(1024)
			pass
		break
		pass
	try:
		s.send(chr(1))
		pass
	except TypeError:
		s.send(bytes(chr(1), "utf-8"))
		pass
	s.close()
	f.close()
	print("El archivo ha sido enviado correctamente")
	pass

if  __name__ == "__main__":
	main()
	pass
