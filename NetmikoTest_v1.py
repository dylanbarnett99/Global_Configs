import re
from netmiko import ConnectHandler
from getpass import getpass

# Switch details
switch_ip = '10.95.200.99'
switch_username = 'dylant.barnett'
switch_password = getpass()
firmware_file = 'firmware_image.bin'

# Connect to the switch
device = {
    'device_type': 'cisco_ios',
    'ip': switch_ip,
    'username': switch_username,
    'password': switch_password,
}

try:
    net_connect = ConnectHandler(**device)
    net_connect.enable()

    # Get the current firmware version
    output = net_connect.send_command('show version')
    #current_version_match = re.search(r'^.*Version\s+(.*?)$', output, flags=re.M)
    #if current_version_match:
        #current_version = current_version_match.group(1)
        #print(f"Current firmware version: {current_version}")
    #else:
        #print("Unable to retrieve current firmware version.")

    # Schedule the firmware upgrade for overnight
    #scheduled_time = '02:00:00'  # Adjust the time as needed
    #command = f'archive download-sw /overwrite /force-reload tftp://{tftp_server}/{firmware_file} flash:/{firmware_file} prompt-timeout'
    #output = net_connect.send_command_timing(command, strip_prompt=False, strip_command=False)
    #if 'Do you want to proceed?' in output:
    #    output += net_connect.send_command_timing('yes', strip_prompt=False, strip_command=False)
    #    if 'scheduled for' in output:
    #        print(f"Firmware upgrade scheduled for overnight at {scheduled_time}")
    #    else:
    #        print("Unable to schedule the firmware upgrade.")
    #else:
    #    print("Firmware upgrade is not required.")

    net_connect.disconnect()

except Exception as e:
    print(f"An error occurred: {str(e)}")