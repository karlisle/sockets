#!/usr/bin/python
# -*- coding: utf-8 -*-
##############################
# Author: HackerAzteca       #
# Licence: Creative Common   #
# Web: hackerazteca.org      #
# Share&Help                 #
##############################

import socket

def get_constant(prefix):
	""" Create a dictionary mapping socket module constants to ther names"""
	return dict((getattr(socket, n), n)
		for n in dir(socket)
			if n.startswith(prefix)
			)
	pass

families = get_constant('AF')
types = get_constant('SOCK_')
protocols = get_constant('IPPROTO_')

sock = socket.create_connection(('localhost', 2001))

print('Family: ', families[sock.family])
print('Type: ', types[sock.type])
print('Protocol: ', protocols[sock.proto])

try:
	message = b"This is the message. It will be repeated"
	print('Sending...%s' %message)
	sock.sendall(message)
	amount_received = 0
	amount_expected = len(message)

	while amount_received < amount_expected:
		data = sock.recv(16)
		amount_received += len(data)
		print('Receiven "%s' % data)
		pass
	pass
finally:
	print('Closing socket....')
	sock.close()
	pass
