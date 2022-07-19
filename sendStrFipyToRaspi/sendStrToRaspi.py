import time
import pycom
from machine import UART

pycom.heartbeat(False)

uart1=UART(1, 115200)
uart1.init(115200, bits=8, parity=None, stop=1, pins=('P3', 'P4'))

x=1

while True:
    uart1.write(b'Hello')
    print('Sent message number: '+str(x))
    x+=1
