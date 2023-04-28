import socket
#socket.AF_INET es para usar IPv4
cliente_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server_address=('localhost',8000)

cliente_socket.connect(server_address)

message='Hola, servidor'

cliente_socket.sendall(message.encode())

data=cliente_socket.recv(1024)
print('Mensaje recibido desde el servidor: ', data.decode())

cliente_socket.close()
