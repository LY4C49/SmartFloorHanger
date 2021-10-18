# -*- coding: utf-8 -*-
"""
Created on Thu May 27 13:38:59 2021

@author: Peter
"""


import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

AM='AM.txt'
DR='DR.txt'
H='H.txt'
weather='weather.txt'


lumination=17

control=14


GPIO.setup(lumination,GPIO.IN)

FOUT=19
FIN=26
GPIO.setup(FOUT,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(FIN,GPIO.IN)

GPIO.setup(control,GPIO.OUT,initial=GPIO.LOW)

state=0
operation=0
SR=0


while True:
    
    if GPIO.input(FIN)==GPIO.HIGH:
        continue
    else:
        GPIO.output(FOUT,GPIO.HIGH)
        
    f=open(AM,'w+')
    state=f.readline()
    print(state)
    f.close()
    
    f=open(DR,'w+')
    operation=f.readline()
    print(operation)
    f.close()
    
    f=open(H,'w+')
    H_data=f.readline()
    H_data=eval(H_data)
    print(H_data)
    f.close()
    
    f=open(weather,'w+')
    SR=f.readline()
    f.close()
    print(SR)

    time.sleep(.1)
    GPIO.output(FOUT,GPIO.LOW)

    
    if state=='A':

    
        key_word='雨'
        
        if key_word in SR:
            GPIO.output(control,GPIO.LOW)
            print("收回")
        else:
            if GPIO.input(lumination)==GPIO.HIGH:
                GPIO.output(control,GPIO.HIGH)
                print("推出")
            else:
                GPIO.output(control,GPIO.LOW)
                print("收回")
    
    else:
        if operation=='R':
            GPIO.output(control,GPIO.LOW)
            print("收回")
        else:
            GPIO.output(control,GPIO.HIGH)
            print("推出")
    
    time.sleep(5)
            

    
    
    
    
    
    

    




