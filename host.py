import socket
import threading

def send(client):
    while True:
        msg = input("Enter your msg: ")
        client.send(bytes(msg, "utf8"))
    
def recv(client):
    while True:
        recv = client.recv(8192)
        print(f"\n{recv.decode('utf8')}")

def initsend():
    send = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    send.bind(("IP", 8080))
    send.listen(1)
    client, addr = send.accept()
    return client

def initrecv():
    recv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    recv.bind(("IP", 8081))
    recv.listen(1)
    client, addr = recv.accept()
    return client

if __name__ == "__main__":
    print("Waiting for connection")
    client1 = initsend()
    client2 = initrecv()
    sendthread = threading.Thread(target=send, args=(client1,))
    recvthread = threading.Thread(target=recv, args=(client2,))

    sendthread.start()
    recvthread.start()
