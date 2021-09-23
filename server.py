#!/home/juan/anaconda3/bin/ python3
import socket
import sys
import Crypto
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP as pk
host = '127.0.0.1'
port = int(sys.argv[1])
port2 =int(sys.argv[2])
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
add = (host,port)
sock.bind(add)
sock.listen(5)
client1,address= sock.accept()
llave = client1.recv(300)
print("Llave del cliente 1:")
print(llave)
sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
add2 = (host,port2)
sock2.bind(add2)
sock2.listen(5)
client2,address2 = sock2.accept()
client2.sendall(llave)
llave2 = client2.recv(300)
print("Llave del cliente 2:")
print(llave2)
client1.sendall(llave2)
def generarLLaveAjena(llaveImportada):
    llaveRecibida = RSA.importKey(llaveImportada)
    key = pk.new(llaveRecibida)
    return key
llaveC1 = generarLLaveAjena(llave)
llaveC2 = generarLLaveAjena(llave2)
while True:
    mensaje1=client1.recv(300)
    print("Mensaje para 2\n" + str(mensaje1))
    #Intentar decodificar mensaje con llave publica
    #decodificacion = llaveC1.decrypt(mensaje1)
    #print(str(decodificacion))
    client2.sendall(mensaje1)
    print(mensaje1)
    mensaje2=client2.recv(300)
    #Intentar decodificar mensaje con llave publica
    #decodificacion = llaveC2.decrypt(mensaje2)
    #print(str(decodificacion))
    client1.sendall(mensaje2)
    print("Mensaje para 1 \n" + str(mensaje2))


