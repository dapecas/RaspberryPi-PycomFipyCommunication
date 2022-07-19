#Code to use in Raspi: sendTXTfromRaspi.py
#Program that collects the content of a TXT and saves it in a TXT.

import time
import pycom as py
from machine import UART

txtContent=None

uart1=UART(1, 115200)
uart1.init(115200, bits=8, parity=None, stop=1, pins=('P3', 'P4'))

while txtContent==None:
    if uart1.any():
        txtContent=uart1.read().decode('utf-8') #Fipy read all data from Raspi
        time.sleep(1)
    else:
        print('No ha recogido nada')
        time.sleep(1)

with open('/flash/prueba.txt', 'w') as data:
    data.write(txtContent)
    uart1.deinit()
    py.rgbled(0x00FF00) #Green
    data.close()
