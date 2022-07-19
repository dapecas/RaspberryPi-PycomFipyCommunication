#Program to open port and obtain the content of a txt located in the Fipy
#Code to use in Fipy:sendTxtToRaspi.py

import serial
import time

info=None

puerto=serial.Serial('/dev/ttyS0', baudrate=115200,
                        parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE,
                        bytesize=serial.EIGHTBITS, timeout=1)
while info==None:
        time.sleep(3)
        if(puerto.inWaiting()):
                print('He escuchado algo')
                info=puerto.read(puerto.inWaiting()).decode('utf-8')
                time.sleep(5)
                data_left=puerto.inWaiting()
                info = info + puerto.read(data_left).decode('utf-8')
        else:
                print('No ha recogido nada')
                time.sleep(1)

time.sleep(3)
print(info)
file=open('/home/pi/pruebasRaspiFipy/TXT/ContenidoDelTxtUbicadoEnFipy.txt', 'w')
file.write(str(info))
file.close()
time.sleep(3)
print('End code')
