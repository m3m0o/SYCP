import socket

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
    try:
        while True:
            message_to_send = input('>>> ')

            client_socket.sendto(f'{message_to_send}\r\n'.encode(), ('127.0.0.1', 2202))

            response = client_socket.recvfrom(1024)

            received_message = response[0].decode().strip()
            received_from_ip = response[1][0]
            received_from_port = response[1][1]

            print(f'{received_from_ip}:{received_from_port}: {received_message}\n', end='')
    except KeyboardInterrupt:
        exit(0)