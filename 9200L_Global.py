import serial
import time

#Create a serial connection
#Change according to current serial connection
ser = serial.Serial('COM5', baudrate=9600, timeout=1)

# Wait for the serial connection to be ready
time.sleep(2)

#Variables
hostName = "4435_9200L-IC2-stack"
vlan200IP = "10.207.200.4"
defaultGateway = "10.207.200.1"
snmpLocation = "Trillium Springs at Lincoln Heights IC2"
location_octet = "207"
ntpServer = "10.1.13.1"

commands = [
'enable',
'configure terminal',
"service timestamps debug datetime msec",
"service timestamps log datetime msec",
"service call-home",
"platform punt-keepalive disable-kernel-core",
####
"hostname {}".format(hostName),
"vrf definition Mgmt-vrf",

" address-family ipv4",
" exit-address-family",

" address-family ipv6",
" exit-address-family",

"logging console critical",
"enable secret 9 $9$mAFPRrPb49/cek$IwkdQK8Y4lYKY6/Ed4gavVf5qUbJi0eDArb/FopE9Vw",

"aaa new-model",

"aaa authentication login default group tacacs+ local",
"aaa authentication enable default group tacacs+ enable",
"aaa authorization config-commands",
"aaa authorization exec default group tacacs+ local",
"aaa authorization commands 0 default group tacacs+ local",
"aaa authorization commands 1 default group tacacs+ local",
"aaa authorization commands 15 default group tacacs+ local",
"aaa accounting exec default start-stop group tacacs+",
"aaa accounting commands 15 default start-stop group tacacs+",

"aaa session-id common",
"clock timezone EST -5 0",
"clock summer-time EDT recurring",
"software auto-upgrade enable",

#Change Provision
"switch 1 provision c9200l-48p-4g",
"switch 2 provision c9200l-48p-4g",

"vtp mode transparent",

"no ip domain lookup",
"ip domain name cms.k12.nc.us",

"license boot level network-essentials addon dna-essentials",

"diagnostic bootup level minimal",

"spanning-tree mode rapid-pvst",
"spanning-tree extend system-id",
"memory free low-watermark processor 10626",

"errdisable recovery cause bpduguard",
"errdisable recovery interval 1800",
"username cmsnetwork secret 9 $9$suYSmIhVGYbLHk$jwywoMHyNpOWRznp6HgFhx9QiQR09hghwazpNHPGHGg",


"redundancy",
" mode sso",


"transceiver type all",
" monitoring",

#Change Vlans

"vlan 21",
"name MC_Admin",

"vlan 22",
"name MC_Voice",

"vlan 24",
"name MC_Student",

"vlan 200",
"name Network_Support",

"vlan 204",
"name CMPD",

"vlan 205",
"name Safari_Montage",

"vlan 208",
"name Cisco_Wireless",

"vlan 214",
"name Security_Cam",

"vlan 232",
"name Meraki_Wireless",

"vlan 240",
"name Flexconnect",

"lldp run",


"interface Vlan1",
" no ip address",
" shutdown",


"interface Vlan200",
" description NetSupport",
" ip address {} 255.255.255.0".format(vlan200IP),
" no ip route-cache",


"ip default-gateway {}".format(defaultGateway),
"ip forward-protocol nd",
"no ip http server",
"ip http secure-server",
"ip tacacs source-interface Vlan200",
"ip ssh version 2",


"logging host 10.95.1.55",
"logging host 10.6.60.241",
"ip access-list standard 66",
" 10 permit 10.{}.200.1".format(location_octet),
" 20 permit 10.188.1.2",
" 30 permit 10.95.1.0 0.0.0.255",
" 40 permit 10.6.60.0 0.0.0.255",
" 50 permit 10.6.50.0 0.0.0.255",
" 60 deny   any log",


"snmp-server community cmsstg411 RW 66",
"snmp-server community cmsread411 RO",
"snmp-server location {}".format(snmpLocation),
"snmp-server host 10.6.60.241 cmsstg411",
"tacacs-server directed-request",
"tacacs server 1_TACACS-SERVER",
" address ipv4 10.6.60.238",
" key 7 15012358541A0401231D6D2A46543147",
"tacacs server 2_TACACS-SERVER",
" address ipv4 10.6.60.239",
" key 7 15012358541A0401231D6D2A46543147",


"control-plane",
" service-policy input system-cpp-policy",


"banner motd ^CC",
"************************ Warning! Warning! Warning! ***********************",
"This system is restricted to Charlotte Mecklenburg Schools authorized",
"users for business purposes.  Unauthorized access is a violation of",
"the law, and will be prosecuted to the fullest extent of the law.",
"This service may be monitored for administrative and security reasons.",
"By proceeding, you consent to this monitoring.",
"************************ Warning! Warning! Warning! ************************",
"^C",


"line con 0",
" session-timeout 10",
" exec-timeout 15 0",
" password 7 03075618541F36",
" logging synchronous",
" stopbits 1",
"line aux 0",
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

"ntp server {}".format(ntpServer),
"call-home",

"crypto key generate rsa modulus 1024",
]

for command in commands:
    ser.write(command.encode() + b'\r\n')
    time.sleep(1)
    output = ser.read_all().decode()
    print(output)

# Close the serial connection
ser.close()