import serial
import time

#Create a serial connection
#Change according to current serial connection
ser = serial.Serial('COM5', baudrate=9600, timeout=1)

# Wait for the serial connection to be ready
time.sleep(2)

commands = [

]

for command in commands:
    ser.write(command.encode() + b'\r\n')
    time.sleep(.5)
    output = ser.read_all().decode()
    print(output)

# Close the serial connection
ser.close()