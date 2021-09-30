import socket
import threading

def send(client):
    while True:
        msg = input("Enter your msg: ")
        client.send(bytes(msg, "utf8"))
    
def recv(client):
    while True:
        recv = client.recv(8192)
        print(recv.decode("utf8"))

def initsend():
    while True:
        try:
            send = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            send.connect(("HOST_IP", 8080))
            return send
        except:
            print("Send connection failed, trying again")

def initrecv():
    while True:
        try:
            recv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            recv.connect(("HOST_IP", 8081))
            return recv
        except:
            print("Recv connetion failed, trying again")

if __name__ == "__main__":
    print("Connecting")
    client1 = initsend()
    client2 = initrecv()
    sendthread = threading.Thread(target=send, args=(client2,))
    recvthread = threading.Thread(target=recv, args=(client1,))
    sendthread.start()
    recvthread.start()
