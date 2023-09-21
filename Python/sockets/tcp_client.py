import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect(('google.com', 80))

    client_socket.send('GET / HTTP/1.1\nHost: www.google.com\n\n\n'.encode())

    response = client_socket.recv(1024).decode()

    print(response)