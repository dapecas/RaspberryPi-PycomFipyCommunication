#Program that sends the content of a TXT file.
#Code to use in Raspi: receiveTxtFromFipy.py

import time
import pycom
from machine import UART

with open('/flash/urraca.txt', 'r') as dataBirds:
    txtContent=dataBirds.read()
    dataBirds.close()

uart1=UART(1, 115200)
uart1.init(115200, bits=8, parity=None, stop=1, pins=('P3', 'P4'))
x=1

while True:
    for dataChunk in txtContent:
        uart1.write(bytes(dataChunk, 'utf-8'))
    else:
        print('Mensaje mandado numero: '+str(x))
        x+=1
