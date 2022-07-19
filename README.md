# RaspberryPi-PycomFipyCommunication
Serial communication between Raspberry Pi and Pycom Fipy board

In this repository, there are different codes to carry out the communicaction between Fipy board and Raspberry Pi.

First of all, you have to know how to connect the Fipy board with the Raspberry Pi. The communiaction between devices are serial, so the connection between one device and another will be made from the UART port.

The pinout of Raspberry Pi is this:
![image](https://docs.microsoft.com/es-es/windows/iot-core/media/pinmappingsrpi/rp2_pinout.png)

The pinout of Pycom Fipy is this:
![image](https://user-images.githubusercontent.com/99323067/179707491-77dd4644-39ca-4e1d-b1ef-0915a293bba6.png)

As you can see, the Fipy UART connection is located on the pins P3 and P4. For Raspberry Pi, this connection is located on the pins 8 and 10. Therefore, to perform serial communications, both devices need to be connected through these pins, crossing TX-RX.

Right now, there are 4 folders that contain the necessary files to make a correct serial communication between the devices.
