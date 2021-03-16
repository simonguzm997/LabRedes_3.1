import socket
import threading
import socketserver
import hashlib
import datetime
from threading import Thread
from socketserver import ThreadingMixIn
from datetime import datetime

# Transfer Info
TCP_IP = '192.168.0.5'
TCP_PORT = 50000
BUFFER_SIZE = 1024
#For logs
testDate = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
print (testDate)

#File options

fileOp1 = "100MBF.txt"
fileOp2 = "250MBF.txt"

#Take inputs
a = True
while a:
    print ("File Options")
    print ("[1] "+fileOp1)
    print ("[2] " + fileOp2)

    fName = input ("Enter File Name: ")
    print (fName != fileOp1)



    if fName != fileOp1 and fName !=fileOp2:
        print("Please chose one of the file options only")
        fName = input ("Enter File Name: ")

    nClients = input ("Enter numer of clients: ")
    if 0 > int(nClients) or int (nClients)>25:
        print ("Please choose less or equal to 25 clients and over 0")
        nClients = input ("Enter numer of clients: ")

    print ("You have chosen the File:", fName, "and want to send to:", nClients, "clients")
    res = input ("Is this correct? Y/N ")
    if res == "Y":
        a = False

# Log file Creation
logFile = open ("./logs/"+testDate+"-log.txt", "w")
logFile.write("Date of the test: "+ testDate+"\n")
logFile.write("Name of the sent file: "+ fName+"\n")
logFile.write("Size of the sent file: "+ str ("100MB" if fName == "100MBF.txt" else "250MB")+"\n")
logFile.write("------------------------------------------\n")

#Hash Creation
Sha256Hash = hashlib.sha256()

def getFileHash ():
    ## TODO Ccambiar segun el input
    #filename2='mytext.txt'
    f2 = open(fName,'rb')
    while True:
        l2 = f2.read(BUFFER_SIZE)
        if not l2:
            break
        Sha256Hash.update(l2)
getFileHash()
print (Sha256Hash.hexdigest())

# Clients list
listaClientes = []

# Class ClientThread
class ClientThread(Thread):
    def __init__(self,ip,port,sock):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.sock = sock
        print (" New thread started for "+ip+":"+str(port))

    def run(self):
        tIniTransm = 0
        tFinTransm = 0
        boolTransEx = False
        numPaquetes = 0
        f = open(fName,'rb')
        self.sock.send(Sha256Hash.hexdigest().encode())
        while True:
            l = f.read(BUFFER_SIZE)
            tIniTransm = datetime.now()
            while (l):
                self.sock.send(l)
                #print('Sent ',repr(l))
                l = f.read(BUFFER_SIZE)
                numPaquetes = numPaquetes +1
            if not l:
                f.close()
                self.sock.close()
                tFinTransm = datetime.now()
                boolTransEx = True
                transferTime = tFinTransm- tIniTransm
                logPClient = "Client ip: "+ self.ip+" port: "+ str(self.port)+ "\n"
                logPClient += "Successfull delivery: "+ str(boolTransEx) +"\n"
                logPClient += "Transfer time: "+ str(transferTime) + "\n"
                logPClient += "Packet Number: "+ str(numPaquetes) + "\n"
                listaClientes.append(logPClient)
                break

#Socket Creation
tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsock.bind((TCP_IP, TCP_PORT))

#print (tcpsock.getpeername())
print (tcpsock.getsockname())
# Threads list
threads = []
Pthreads = []
#Client Counter
tCounter = int(nClients)

# While to listen clients
while True:
    tcpsock.listen(25)
    print ("Waiting for incoming connections...")
    (conn, (ip,port)) = tcpsock.accept()
    print ('Got connection from ', (ip,port))
    newthread = ClientThread(ip,port,conn)
    Pthreads.append(newthread)
    tCounter = tCounter -1
    print (tCounter)
    if tCounter == 0:
        for i in Pthreads:
            i.start()
            threads.append(i)
        break

for t in threads:
    t.join()

logFile.writelines(listaClientes)
logFile.close()
