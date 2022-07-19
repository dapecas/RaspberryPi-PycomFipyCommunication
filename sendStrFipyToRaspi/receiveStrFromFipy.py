#Program to open port and obtain the content of a string sent from the Fipy
#Code to use in Fipy:sendStrToRaspi.py

import serial
import time

info=None

puerto=serial.Serial('/dev/ttyS0', baudrate=115200,
                        parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE,
                        bytesize=serial.EIGHTBITS, timeout=1)
while info==None:
        time.sleep(3)
        if(puerto.inWaiting()):
                print('I heard something')
                info=puerto.read(puerto.inWaiting()).decode('utf-8')
                time.sleep(5)
                data_left=puerto.inWaiting()
                info = info + puerto.read(data_left).decode('utf-8')
        else:
                print('has not collected anything')
                time.sleep(1)

time.sleep(3)
print(info)
file=open('/home/pi/pruebasRaspiFipy/TXT/ContenidoDelTxtUbicadoEnFipy.txt', 'w')  #Create a file on the path
file.write(str(info))
file.close()
time.sleep(3)
print('End code')
