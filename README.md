## Smart_Floor_Hanger
## 基于树莓派的智能天气衣架 

### 2018广东省大学生电子设计大赛项目代码  
硬件需求：树莓派，单片机，亚克力板，直流电机驱动模块和电机，DHT11，蓝牙HC-05，光线传感器  

#### The repository contains codes of my design in 2018 GuangDong Undergraduate Electronic Design Competition

##### Hardware requirements: Raspberry 4B, Arduino uno r3, ACRYLIC board, DC motor, DHT11 Sensor, Bluetooth HC-05, Light Sensor, Ultrasonic distance sensor

If you want to make the all system, you can design and order an ACRYLIC board. We provide our ACRYLIC.SLDPRT(open through Solidwork) as reference.

1.Download "Blink" app on your phone and register  
  
2.Register to "心知天气" and get your key (you will get weather service through the api,or you can replace it to another api if you want) 
  
3.Replace the "auth" to your key(blinker's key) in MQTT.py  
  
4.Replace the "key to your key(weather's key) in get_weather.py
  
5.connect your Arduino with Raspberry  
  
6.run .ino file on your Arduino  
  
7.run .py files on your Raspberry  
  
8.Enjoy it! Control your hanger through your phone or let your hanger control itself automatically!

### APP on your phone(you can design your own UI)
![image](https://github.com/LY4C49/Smart_Floor_Hanger/blob/main/APP.jpg)

### Hanger
![image](https://github.com/LY4C49/Smar_Floor_Hanger/blob/main/Results.jpg)



