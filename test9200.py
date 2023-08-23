import serial
import time

#Create a serial connection
#Change according to current serial connection
ser = serial.Serial('COM5', baudrate=9600, timeout=1)

# Wait for the serial connection to be ready
time.sleep(2)

#Variables
hostName = "8461_9200L-MC-stack"
vlan200IP = "10.207.200.3"
defaultGateway = "10.207.200.1"
snmpLocation = "Lincoln Heights"

commands = [
'enable',
'configure terminal'

]

for command in commands:
    ser.write(command.encode() + b'\r\n')
    time.sleep(1)
    output = ser.read_all().decode()
    print(output)

# Close the serial connection
ser.close()