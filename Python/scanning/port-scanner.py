import socket
import sys

ports_options = {
    'all': range(65535),
    'std': range(4000)
}

try:
    _, host, ports_range = sys.argv
except ValueError:
    print('Usage: python port-scanner.py <host> <ports> (std | all | 22, 80, 3306,...)')
    exit(1)

if ports_range in ports_options:
    ports = ports_options[ports_range]
else:
    ports = [int(port) for port in ports_range.split(',')]

for port in ports:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.settimeout(1)

        connection_result_code = client_socket.connect_ex((host, port))

        if connection_result_code == 0:
            print(f'[+] port {port} is open')