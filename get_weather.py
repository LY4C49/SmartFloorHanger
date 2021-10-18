# -*- coding: utf-8 -*-
"""
Created on Thu May 27 15:37:39 2021

@author: Peter
"""
import requests
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

FOUT=19
FIN=26
GPIO.setup(FOUT,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(FIN,GPIO.IN)

key='SilAvUA3kkSTh8Sck'

currentWeatherAPI='https://api.seniverse.com/v3/weather/now.json'
LOCATION = requests.get('https://checkip.amazonaws.com').text.strip()#获取本机ip地址
LANGUAGE = 'zh-Hans'
UNIT = 'c'  # 单位摄氏度

weather='weather.txt'



def get_weather():
    
    result = requests.get(currentWeatherAPI, params={
        'key': key,
        'location': LOCATION,
        'language': LANGUAGE,
        'unit': UNIT
    }, timeout=2)
    result = eval(result.text)
    weather= result['results'][0]['now']['text']
    print(weather)
    
    return weather


while True:
    current_time=time.localtime(time.time())
    minutes=current_time.tm_min
    if minutes%15==0:
        current_weather=get_weather()
    while GPIO.input(FIN)==GPIO.HIGH:
        continue
    GPIO.output(FOUT,GPIO.HIGH)
    f=open(weather,'w+')
    f.write(current_weather)
    f.close()
    GPIO.output(FOUT,GPIO.LOW)
    
        
        





