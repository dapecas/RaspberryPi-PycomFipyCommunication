#code to use in Fipy: recibirStrDeRaspi
#Program to send a str from Raspi to FiPy

import serial #Required to use serial port
import time

info=None

#Serial port initialization
puerto=serial.Serial('/dev/ttyS0', baudrate=115200,
                        parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE,
                        bytesize=serial.EIGHTBITS, timeout=1)
contenido = 'Hello'
x=1
while True:
        for dataChunk in contenido:
                puerto.write(bytes(dataChunk, 'utf-8'))
        else:
                print('Mensaje mandado numero: '+str(x))
                x+=1
