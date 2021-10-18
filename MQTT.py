
# -*- coding: utf-8 -*-
"""
Created on Thu May 27 16:37:41 2021

@author: Peter
"""

from Blinker import Blinker, BlinkerButton, BlinkerNumber
from Blinker.BlinkerDebug import *
import RPi.GPIO as GPIO
import time

auth = '5ae7a5b5503a'

GPIO.setmode(GPIO.BCM)

AM='AM.txt'
DR='DR.txt'
H='H.txt'
T='T.txt'
weather='weather.txt'

FOUT=19
FIN=26
GPIO.setup(FOUT,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(FIN,GPIO.IN)


# GPIO.setup(P221,GPIO.IN)
# GPIO.setup(PH21,GPIO.IN)

# GPIO.setup(P122,GPIO.OUT,initial=GPIO.LOW)
# GPIO.setup(P12H,GPIO.OUT,initial=GPIO.LOW)


BLINKER_DEBUG.debugAll()

Blinker.mode("BLINKER_WIFI")
Blinker.begin(auth)

btn_am = BlinkerButton("btn-am")
btn_dr = BlinkerButton("btn-dr")

num_tmp=BlinkerNumber("num-tmp")
num_humi=BlinkerNumber("num-humi")

def btn_am_callback(state):
    
    BLINKER_LOG('get button state: ', state)
    
    if state=='on':
        btn_am.text('AUTO')
        btn_am.print(state)
        while GPIO.input(FIN)==GPIO.HIGH:
            continue
        GPIO.output(FOUT,GPIO.HIGH)
        f=open(AM,'w+')
        f.write("A")
        f.close()
        GPIO.output(FOUT,GPIO.LOW)
    else:
        btn_am.text('Manual')
        btn_am.print(state)
        GPIO.output(FOUT,GPIO.HIGH)
        f=open(AM,'w+')
        f.write('M')
        f.close()
        GPIO.output(FOUT,GPIO.LOW)

def btn_dr_callback(state):
    
    BLINKER_LOG('get button state: ', state)
    

    if state=='on':
        btn_dr.text('D')
        btn_dr.print(state)
        while GPIO.input(FIN)==GPIO.HIGH:
            continue
        GPIO.output(FOUT,GPIO.HIGH)
        f=open(DR,'w+')
        f.write("D")
        f.close()
        GPIO.output(FOUT,GPIO.LOW)
    else:
        btn_dr.text('R')
        btn_dr.print(state)
        while GPIO.input(FIN)==GPIO.HIGH:
            continue
        GPIO.output(FOUT,GPIO.HIGH)
        f=open(AM,'w+')
        f.write('R')
        f.close()
        # time.sleep(.2)
        GPIO.output(FOUT,GPIO.LOW)


def heartbeat_callback():
    while GPIO.input(FIN)==GPIO.HIGH:
        continue
    GPIO.output(FOUT,GPIO.HIGH)
    f=open(T,'r')
    temp=f.readline()
    f.close()
    
    f=open(H,'r')
    humi=f.readline()
    f.close()
    GPIO.output(FOUT,GPIO.LOW)
    temp=eval(temp)
    humi=eval(humi)
    print("flag")
    
    num_humi.print(humi)
    num_tmp.print(temp)

Blinker.attachHeartbeat(heartbeat_callback)
btn_am.attach(btn_am_callback)
btn_dr.attach(btn_dr_callback)

if __name__ == '__main__':

    while True:
        Blinker.run()


