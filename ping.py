import os
#
ip = '192.168.34.81' # нужный айпи
ping_file = "ping.txt"
response = os.popen(f'ping {ip} > "{ping_file}"').read()
with open(ping_file, 'r', encoding='cp866') as file:
    ping = file.read()
print(ping)