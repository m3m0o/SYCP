import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM)as server_socket:
    server_socket.bind(('0.0.0.0', 2205))
    server_socket.listen(5)
    
    while True:
        client_socket, address = server_socket.accept()

        message = client_socket.recv(1024).decode().strip()

        print(f'{address[0]}: {message}')