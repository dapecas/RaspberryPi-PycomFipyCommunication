#Program to send a txt file to Fipy and save it
#Code to use in Fipy: recibirTXTdeRaspi

import serial
import time

puerto = serial.Serial('/dev/ttyS0', baudrate=115200,
                        parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE,
                        bytesize=serial.EIGHTBITS, timeout=1)

path = '/home/pi/pruebasRaspiFipy/TXT/urraca.txt'

f=open(path, 'r')
txtContent=f.read()
f.close()

x=0
y=1

while x<1:
        for dataChunk in txtContent:
                puerto.write(bytes(dataChunk, 'utf-8'))
        else:
                print('Mensaje mandado numero: '+str(y))
                y+=1
                x+=1

print('End of code')
