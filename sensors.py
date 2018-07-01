# -*- cod\ing: utf-8 -*-
"""
Created on Wed Sep  6 22:29:32 2017

@author: matteo
"""

#!/usr/bin/python

import Adafruit_BMP.BMP085 as BMP085
import time, json
import numpy as np
import matplotlib.pyplot as plt
import RPi.GPIO as GPIO
import Adafruit_DHT as DHT
import serial


sensor_bmp = BMP085.BMP085()


GPIO.setmode(GPIO.BOARD)

DHT22_GPIO = 16




class bmp(): #defing class that it will be used for the temperature misered by the BMP180 sensor

   
          
   
    def temperature(self, misure_unity):
        
        if misure_unity == 'c':
            
        
            tmp_c = float(sensor_bmp.read_temperature())
            return tmp_c
            
        elif misure_unity == 'f':
            
            tmp = float(sensor_bmp.read_temperature())
            tmp_f = float(1.8*tmp+32)
            return tmp_f
            
        elif misure_unity == 'k':
            
            tmp = float(sensor_bmp.read_temperature())
            tmp_k = float(tmp+273.15)
            return tmp_k
            

    def pressure(self, misure_unity):
        
        if misure_unity == 'pa':
            
            press_pa = float(sensor_bmp.read_pressure())
            return press_pa

        elif misure_unity == 'atm':
        
            press = float(sensor_bmp.read_pressure())
            press_atm = float(press/101325)
            return press_atm
            
        elif misure_unity == 'bar':
            
            press = float(sensor_bmp.read_pressure())
            press_bar = float(press/(10^(-5)))
            return press_bar
            
            

       

class DHT22():
    
    def humidity(self):
        
        dht22 = DHT.read_retry(DHT.DHT22, DHT22_GPIO)
        
        h = "{0:.2f}".format(dht22[0])
        
 
        return h
        
        
        
        
class wind_arduino():
    
    
    
    
    def wind(self):
        
        ser = serial.Serial('/dev/ttyACM0', 9600)
        
        value = float(ser.readline())
        value = "{0:.2f}".format(value)
        
        return value
            
            




            
                        
            
            
            
            
            
            
            
            
        
        
        

        
        
        

        
        
        
        
        
        
        
        
        
        
        
        
    
        
        
        
        

        
    
        
        
            
            
            
            
            
            
            
            
            
            
        
        
        
        

        

        
        
        
        
        
        
        
        
        
        
        
        
    




                
        
                    
                    
                    
                
                    
                    
                    
                
                    
                    
                    
                    
                
                    

        
                    
                    
        
                    
            
            
            
        
        
        

            