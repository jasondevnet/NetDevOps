
from netmiko import ConnectHandler
import getpass
import subprocess

user = raw_input('Username: ')
password = getpass.getpass()


cisco_nxos = {
'device_type': 'cisco_nxos',
'ip': '10.100.248.53',
'username': user,
'password': password,
}

net_connect = ConnectHandler(**cisco_nxos)
output = net_connect.send_command('show run int g1')
print(output)