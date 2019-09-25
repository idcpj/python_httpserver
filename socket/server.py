import socket

def server():
    s = socket.socket()
    HOST='0.0.0.0'
    PORT=6666
    s.bind((HOST, PORT))
    print("ip and port ",HOST,":",PORT)
    s.listen(5)

    while True:
        c,addr = s.accept()
        print("connect addr",addr)
        msg = c.recv(1024)
        c.send(msg)

if __name__ =='__main__':
    print("running")
    server()
