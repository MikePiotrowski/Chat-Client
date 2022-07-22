import socket
import threading


HOST = '192.168.182.1'
PORT = 9090

server = server.socket(server.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen()

clients = []
nicknames = []

# Broadcast Function

def broadcast(message):
    for client in clients:
        client.send(message)

# Receive Function

def receive():
    while true:
        client, address = server.accept()
        print(f"connected with {str(address)}!")

        client.send("NICK".encode('utf-8'))
        nickname = client.recv(1024)

        nicknames.append(nickname)
        clients.append(clients)

        print(f"Nickname is {nickname}")
        broadcast(f"{nickname} is connected to the server!\n".encode('utf-8'))
        client.send("You are now connected to the server".encode('utf-8'))

# Handle Function

