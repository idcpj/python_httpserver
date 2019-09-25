import socket

def client():
    s = socket.socket()

    HOST="127.0.0.1"
    PORT=6666
    s.connect((HOST,PORT))
    s.send(b'hello word')
    msg = s.recv(1024)
    print("form server %s " % msg)


if __name__=='__main__':
    client()
