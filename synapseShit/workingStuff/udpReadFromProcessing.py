import socket
#from pymouse import PyMouse()
#m = PyMouse()

HOST = '127.0.0.1'                 # Symbolic name meaning all available interfaces
PORTrx = 5200              # Arbitrary non-privileged port
PORTry = 5201
PORTlx = 5202
PORTly = 5203
PORTcx = 5204
PORTcy = 5205

rx = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ry = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
rx.bind((HOST, PORTrx))
ry.bind((HOST, PORTry))
rx.listen(1)
ry.listen(1)
connrx, addrrx = rx.accept()
connry, addrry = ry.accept()
print('Connected by rx', addrrx)
print('Connected by ry', addrry)

lx = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ly = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
lx.bind((HOST,PORTlx))
ly.bind((HOST,PORTly))
lx.listen(1)
ly.listen(1)
connlx, addrlx = lx.accept()
connly, addrly = ly.accept()
print('Connected by ly', addrly)
print('Connected by lx', addrlx)
'''
cx = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cy = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cx.bind((HOST,PORTcx))
cy.bind((HOST,PORTcy))
cx.listen(1)
cy.listen(1)
conncx,addrcx = cx.accept()
conncy,addrcy = cy.accept()

print('Connected by cx', addrcx)


print('Connected by cy', addrcy)
'''
while True:
	
	datarx = connrx.recv(1024)
	datary = connry.recv(1024)
	
	datalx = connlx.recv(1024)
	dataly = connly.recv(1024)
	'''
	datacx = conncx.recv(1024)
	datacy = conncy.recv(1024)
	'''
# do whatever you need to do with the data

connrx.close()
connry.close()

connlx.close()
connly.close()
'''
conncx.close()
conncy.close()
'''
# optionally put a loop here so that you start 
# listening again after the connection closes
