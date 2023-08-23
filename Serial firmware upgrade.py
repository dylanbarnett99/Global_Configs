import serial
import time

badCommandResponse = b'[BADCOMMAND]\r\n'    # response if a command failed (b makes it into bytes)

#Open serial port
ser = serial.Serial('COM5', 9600, timeout=0.05)

if ser.isOpen(): #  When the port is opened

    print(ser.name + ' open') # Confirm the Port
    
    ser.write(b'*IDN?\n')   # send the standard SCPI identify command

    ser.write(b'Show vlan brief')

    myResponse = ser.readline()    # Read the response

    print('Device Info:' + myResponse) #  Print the unit information

    time.sleep(0.1)    # delay 100ms

    ser.write(b'PHASE?\n')       # try asking for phase

    myResponse = ser.readline() # gather the response

    if myResponse != badCommandResponse:    #is this is not a phase shifter why print the error

        print(b'Phase=' +myResponse)