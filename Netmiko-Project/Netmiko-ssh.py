from netmiko import ConnectHandler

cisco_nxos = {
    'device_type': 'cisco_nxos',
    'ip':   'IP ADDRESS',
    'username': '',
    'password': '',
    'port' : 22,        
    'secret': 'secret',
    'verbose': False,       
}

net_connect = ConnectHandler(**cisco_nxos)

output = net_connect.send_command('show run int e1/1')
print(output)