#!/usr/bin/python
# -*- coding: utf-8 -*-

##############################
# Author: @HackerAzteca                                      #
# Licence: Creative Common                                 #
# Web: https://github.com/karlisle                         #
# Share&Help                                                         #
##############################

import cv2, time

class Video():
	def __init__(self):
		pass
	def imagen(self, host, number):
		print("Obteniendo captura....")

		cap = cv2.VideoCapture(1)
		time.sleep(5)
		cont = 0
		while cont <= 10:
			ret, frame = cap.read()
			cv2.imwrite(str(number) + '_' + host + "_cap.png", frame)
			#cv2.imshow("frame", frame)
			#cv2.waitKey(1)
			cont += 1
		pass
		cap.release()
		cv2.destroyAllWindows()
		pass
	pass
