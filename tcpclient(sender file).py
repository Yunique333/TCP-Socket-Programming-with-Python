import socket


TCP_IP = "192.168.100.27"
FILE_PORT = 5005
DATA_PORT = 5006
buf = 1024
file_name = "V6 - Change The World.mp3"


try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((TCP_IP, FILE_PORT))
    sock.send(file_name)
    sock.close()

    print "Sending %s ..." % file_name

    f = open(file_name, "rb")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((TCP_IP, DATA_PORT))
    data = f.read()
    sock.send(data)

finally:
    sock.close()
    f.close()