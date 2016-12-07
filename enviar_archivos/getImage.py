#!/usr/bin/python
# -*- coding: utf-8 -*-

##############################
# Author: @HackerAzteca                                      #
# Licence: Creative Common                                 #
# Web: https://github.com/karlisle                         #
# Share&Help                                                         #
##############################

import cv2

cam = cv2.CaptureFrom(0)

image = cv2.QueryFrame(cam)

cv2.SaveImage("imagen.png", image)
