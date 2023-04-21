import socket

server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_address=('localhost',8000)
server_socket.bind(server_address)

server_socket.listen(1)

print(".....Escuchando conexión...")

while True:
    client_socket, client_address=server_socket.accept()
    print('Conexión recibida de',client_address)
    data=client_socket.recv(1024)
    print('Recibido: ',data.decode())

    message="Hola cliente, te saluda el servidor"
    client_socket.sendall(message.encode())
    client_socket.close()
