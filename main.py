# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 22:41:25 2017

@author: matteo
"""

#!/usr/bin/python
#

from sensors import *
import  time
import schedule
import lcddriver
import threading
import requests


lcd = lcddriver.lcd()


def save_data(value, name):
                       
    month = time.strftime("%m")
    day = time.strftime("%d")
    year = time.strftime("%Y")
    hour = time.strftime("%H")
    minute = time.strftime("%M")
    
    date_format = year+'/'+month+'/'+day+" "+hour+':'+minute
    print date_format
    

 
    dict = {"name":name, "value" : value, "date":date_format}
  
    
   
    try:
        
        r = requests.post("http://192.168.0.6:5000", data = dict)

    except:
        
        pass
        print 'request not send'
        
    finally:
        
        print value

        
def job():
    
    
    a = bmp()
    b = DHT22()
    
    
            #########################################################################
            # QUI ANDRANNO MESSE TUTTE LE INIZIALIZZAZIONI DELLE CLASSI DEI SENSORI#
            #########################################################################
    
    t_value = a.temperature('c')
    p_value = a.pressure('atm')
    h_value = b.humidity()
    
    save_data(t_value, 't')
    save_data(p_value, 'p')
    save_data(h_value, 'h')
    
    return t_value
    
    
def scheduler():
    
    hours = ['6:00', '12:00', '18:00', '00:00']
    
    for i in hours:
                    
            schedule.every().day.at(i).do(job)
    
    while True:
        
        schedule.run_pending() 
        time.sleep(1)
        

    
def display():
    lcd = lcddriver.lcd()
    
    
    lcd.lcd_clear()
            
    lcd.lcd_display_string('temp =', 1)

    lcd.lcd_display_string('C', 1,12)

    lcd.lcd_display_string('press = ',2)

    lcd.lcd_display_string('atm', 2,12)
    lcd.lcd_display_string('hum = ', 3)
    lcd.lcd_display_string('%', 3, 12)
    
    lcd.lcd_display_string('wind = ', 4)
    lcd.lcd_display_string('km/h', 4, 13)
    
    


def check():
    
    try:
        
        a = bmp()
        a.temperature('c')
        
        return 1 
        
    except:
        pass 
        return 10 
        
    try:
        
        
        b =  DHT22()
        b.humidity()
        
        return 2
        
    except:
        
        pass 
        return 20
        
        
        
def loading():
    lcd = lcddriver.lcd()
    lcd.lcd_clear()
    
    lcd.lcd_display_string('loading......', 1)
    
    time.sleep(5)
     

        

          

def lcd():
    lcd = lcddriver.lcd()
           
    display()
    

    while True:

        t_p = bmp()
        h = DHT22()

        
        
        c = check()
        
        
        
        
                    
          #  
            
            
            
        if c == 10:
            lcd.lcd_display_string('no sensor', 1)
            lcd.lcd_display_string('no sensor', 2)

        if c == 20:

            lcd.lcd_display_string('no sensor', 3) 
            
            
        else:


            temp = str(t_p.temperature('c'))
            
            press = "{0:.2f}".format(t_p.pressure('atm'))
            hum = str(h.humidity())

            
            lcd.lcd_display_string(temp, 1, 7)
            
            lcd.lcd_display_string(press, 2, 8)
            lcd.lcd_display_string(hum, 3, 7)
            
            
            
            live_data = [temp, press, hum]
            out = {'name': 'live_data', 'values':live_data}
            
            r = requests.post("http://192.168.0.6:5000", data = out)
            


        time.sleep(20)
        
        
def wind():
    
    lcd = lcddriver.lcd()
    
    while True:  
        
        w = wind_arduino()
        v_w = w.wind()
        lcd.lcd_display_string(v_w, 4,8)
        
        time.sleep(1)
    





        
if __name__ == '__main__':
    
    loading()
    
    
    try:
        
        LCD = threading.Thread(name='lcd', target=lcd)
        WIND = threading.Thread(name='wind', target=wind)
        SCHEDULER = threading.Thread(name='scheduler', target=scheduler)
        
        
        LCD.start()
        WIND.start()
        SCHEDULER.start()
        
        
    except:
        pass
        
    


        
    
    
    
    
    



        
        
        
        

        
        

    

    
        
        
        

    
    
