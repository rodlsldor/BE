

import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

def Attente_de_communication(Host,Port):
    Serveur_Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    Serveur_Socket.bind((Host,Port))
    Serveur_Socket.listen()
    return Serveur_Socket

def reception(Serveur_Socket):
    conn, addr = Serveur_Socket.accept()
    with conn:
        print(f"Connected by {addr}")
        message = conn.recv(1024)
        print("test1")
    return message

def emision(Serveur_Socket,message):
    Serveur_Socket.sendall(message)

ServeurSocket = Attente_de_communication(HOST,PORT)
message = reception(ServeurSocket)
print(message)
ServeurSocket.sendall(message)
emision(ServeurSocket,message)

