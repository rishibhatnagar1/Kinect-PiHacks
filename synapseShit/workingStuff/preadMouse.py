import socket
from pymouse import PyMouse
m = PyMouse()
HOST = '127.0.0.1'                 # Symbolic name meaning all available interfaces
PORT = 5207              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print('Connected by', addr)
while True:
    data = conn.recv(1024)
    if not data: break
    print(data) # inputFromProcessing Script
    # do whatever you need to do with the data
    #move the mouse bro 
    #Data coming in the form of a string from Processing, convert that into float for mouse functions
    m.move(float(data),20)
conn.close()
# optionally put a loop here so that you start 
# listening again after the connection closes
