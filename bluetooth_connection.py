# -*- coding: utf-8 -*-
"""
Created on Fri May 28 19:39:47 2021

@author: Peter
"""
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

control=15

GPIO.setup(control,GPIO.IN)

while True:
    if GPIO.input(control)==GPIO.HIGH:
        print("D")
    else:
        print("R")