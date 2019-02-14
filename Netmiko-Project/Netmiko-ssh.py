from netmiko import ConnectHandler


cisco_nxos = {
    'device_type': 'cisco_nxos',
    'ip':   ' ',
    'username': ' ',
    'password': ' !',
    'port' : 22,        
    'secret': 'secret',
    'verbose': False,       
}

net_connect = ConnectHandler(**cisco_nxos)

output = net_connect.send_command('show run int g0/30')
print(output)