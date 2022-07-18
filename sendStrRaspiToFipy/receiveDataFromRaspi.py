#code to use in raspi: enviarHolaMundo.py
#Program that collects the content of a str and saves it in a TXT.

import time
import pycom as py
from machine import UART

txtContent=None

uart1=UART(1, 115200)
uart1.init(115200, bits=8, parity=None, stop=1, pins=('P3', 'P4'))  #Initialization of UART port 1

while txtContent==None:
    if uart1.any():
        txtContent=uart1.read(10).decode('utf-8')   #Fipy read only 10 characters
        time.sleep(1)
    else:
        print('No ha recogido nada')
        time.sleep(1)

with open('/flash/prueba.txt', 'w') as data:  #Create a txt file to save all data
    data.write(txtContent)
    uart1.deinit()
    py.rgbled(0x00FF00) #Green
    data.close()
