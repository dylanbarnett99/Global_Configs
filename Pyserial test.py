import serial
import time

#
# Make changes to hostname, provision, Vlan200, default gateway, SNMP Locations
#

# Create a serial connection
#Change according to current serial connection
ser = serial.Serial('COM5', baudrate=9600, timeout=1)

# Wait for the serial connection to be ready
time.sleep(2)

#Variables
hostName = "Test_Switch"
vlan200IP = "10.95.200.99"
defaultGateway = "10.95.200.1"
snmpLocation = "POB"

# Send commands to the Cisco switch
#2960X Global config test
commands = [
    'enable',
    'configure terminal',
    'no service pad',
    'service timestamps debug datetime msec',
    'service timestamps log datetime msec',
    'service password-encryption',
    #Change hostname according to switch name
    'hostname {}'.format(hostName),
    #
    'logging console critical',
    'enable secret 5 $1$DQcC$9U0aSXeYZfr7f6.G.Fpmo1',
    'username cmsnetwork password 7 00554733105400085F36',

    'aaa new-model',
    'aaa authentication login default group tacacs+ local',
    'aaa authentication enable default group tacacs+ enable',
    'aaa authorization config-commands',
    'aaa authorization exec default group tacacs+ local',
    'aaa authorization commands 0 default group tacacs+ local',
    "aaa session-id common",

    "clock timezone EST -5 0",
    "clock summer-time EDT recurring",
    #Change according to stack
    "switch 1 provision ws-c2960x-48fps-l",
    #
    "ip domain-name cms.k12.nc.us",
    "vtp mode transparent",

    
    "interface Vlan1",
    "no ip address",
    "shutdown",

    #Change IP accorfing to location
    "interface Vlan200",
    "description Net_Support",
    "ip address {} 255.255.255.0".format(vlan200IP),
    #

    #Change IP according to location
    "ip default-gateway {}".format(defaultGateway),
    #
    "no ip http server",
    "ip http secure-server",

    "ip tacacs source-interface Vlan200",

    "logging host 10.6.60.241",
    "access-list 66 permit 10.188.1.2",
    "access-list 66 permit 10.55.200.2",
    "access-list 66 permit 10.95.1.0 0.0.0.255",
    "access-list 66 permit 10.6.60.0 0.0.0.255",
    "access-list 66 permit 10.6.50.0 0.0.0.255",
    "access-list 66 deny   any log",


    "snmp-server community cmsstg411 RW 66",
    "snmp-server community cmsread411 RO",
    #Change SNMP Location
    "snmp-server location {}".format(snmpLocation),
    #
    "snmp-server host 10.6.60.241 cmsread411",
    "tacacs-server host 10.6.60.238 key 7 15012358541A0401231D6D2A46543147",
    "tacacs-server host 10.6.60.239 key 7 15012358541A0401231D6D2A46543147",
    "tacacs-server directed-request",



    "no vstack",

    "banner motd ^"
    "************************ Warning! Warning! Warning! ***********************"
    "This system is restricted to Charlotte Mecklenburg Schools authorized"
    "users for business purposes.  Unauthorized access is a violation of"
    "the law, and will be prosecuted to the fullest extent of the law."
    "This service may be monitored for administrative and security reasons."
    "By proceeding, you consent to this monitoring."
    "************************ Warning! Warning! Warning! ************************"
    "^",


    "line con 0",
    " session-timeout 10",
    " exec-timeout 15 0",
    " password 7 03075618541F36",
    " logging synchronous",
    "line vty 0 4",
    " session-timeout 10",
    " access-class 66 in",
    " exec-timeout 15 0",
    " password 7 060502321E5E1E",
    " transport input ssh",
    "line vty 5 15",
    " session-timeout 10",
    " access-class 66 in",
    " exec-timeout 15 0",
    " password 7 13061A01591C13",
    " transport input ssh",

    "ntp server 10.1.16.1",

    #Make changes to the vlans
    "vlan 2",
    " name MC_Voice",
    "vlan 10",
    " name MC_Data",
    "vlan 200",
    " name Net_Support",
    "vlan 205",
    " name Video_Conference",
    "vlan 208",
    " name Internal_Wireless",
    "vlan 214",
    " name Security",
    "vlan 232",
    " name Meraki_Wireless",
    "vlan 240",
    " name Wireless_Bonjour",

    'end'
]

for command in commands:
    ser.write(command.encode() + b'\r\n')
    time.sleep(.5)
    output = ser.read_all().decode()
    print(output)

# Close the serial connection
ser.close()
