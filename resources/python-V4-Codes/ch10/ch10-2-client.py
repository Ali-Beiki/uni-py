import socket
PORT = 150
HOST = socket.gethostname()
s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
NICK = input("Welcom, Enter your name : ")
while True :
    MSG = input(">> ")
    MSG = NICK + ":" + MSG
    if MSG.strip()[4:] == "exit" :
        break
    s.send(MSG.encode("Utf-8"))
    data = s.recv(1024)
    print(data)
s.close()
