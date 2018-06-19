# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 20:49:53 2017

@author: matteo
"""

from flask import Flask, request, Response


index = ['date','value']


def csv_index(name):
    
    with open('/var/www/html/'+name+'.csv', 'wb') as f:
        
        for line in index:
            f.write(line)
            f.write(',')
            
        f.seek(-1,2)
        f.truncate()
            
            
        f.write('\n')

def csv_data(data, name):
    
    with open('/var/www/html/'+name+'.csv', 'a') as f:
        
        for line in data:
            
            f.write(line)
            f.write(',')
        f.seek(-1,2)
        f.truncate()
        f.write('\n')
        #
#csv_index('temperature')
#csv_index('pressure')
#csv_index('humidity')

app = Flask(__name__)
@app.route("/", methods=['POST'])

def get_data():
    
    def receiver():
        
        post = request.form
        return post
 
        
        
    data = receiver()
    out = [data['date'], data['value']]
    
    if data['name'] == 't': 
        print 'OK'
        csv_data(out, "temperature")
        

    elif data['name'] == 'p':
        
        csv_data(out, "pressure")
        
    elif data['name'] == 'h':
        
       csv_data(out, 'umidity')
       
    elif data['name'] == 'live_data':
        
       with open('/var/www/html/live_data', 'wb') as f:
           
           f.write(out)
        
        
       
       
       
      
        
    return Response(receiver())
    
        
        
        
        
            
    
      
        

    

        
                  



    
    
    
    
    
    

