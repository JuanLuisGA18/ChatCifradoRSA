#!/home/juan/anaconda3/bin/ python3
import socket
import sys
import Crypto
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP as pk
from Crypto import Random
host = '127.0.0.1'
port = int(sys.argv[1])
tipo = int(sys.argv[2])
add = (host,port)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor =sock.connect(add)
def generarLLavePropia():
    generadorAleatorio = Random.new().read
    #Llave privada
    llave = RSA.generate(1024,generadorAleatorio)
    #Llave publica
    llavePublica = llave.publickey()
    llaveMens = llavePublica.export_key()
    return llave, llavePublica, llaveMens
def generarLLaveAjena(llaveImportada):
    llaveRecibida = RSA.importKey(llaveImportada)
    key = pk.new(llaveRecibida)
    return key

llaveRecibida = 0
encriptadorPropio = 0
if tipo == 0:
    llaves = generarLLavePropia()
    encriptadorPropio = pk.new(llaves[0])
    print("Mi llave como cliente 1 es:")
    print(llaves[2])
    sock.sendall(llaves[2])
    llaveImportada = sock.recv(300)
    llaveRecibida = generarLLaveAjena(llaveImportada)
else:
    llaveImportada = sock.recv(300)
    llaveRecibida = generarLLaveAjena(llaveImportada)
    llaves = generarLLavePropia()
    print("Mi llave como cliente 2 es:")
    print(llaves[2])
    encriptadorPropio = pk.new(llaves[0])
    sock.sendall(llaves[2])
while True:
    if tipo ==0:
        mensaje = input("Ingrese el mensaje a enviar ")
        mensajeEncriptado=llaveRecibida.encrypt(mensaje.encode())
        sock.sendall(mensajeEncriptado)
        print("Esperando Respuesta")
        Respuesta = sock.recv(300)
        mensaje=encriptadorPropio.decrypt(Respuesta)
        print("El mensaje recibido es: ")
        print(str(mensaje))
    else:
        print("Esperando Respuesta")
        Respuesta = sock.recv(300)
        mensaje=encriptadorPropio.decrypt(Respuesta)
        print("El mensaje recibido es: ")
        print(str(mensaje))
        mensaje = input("Ingrese el mensaje a enviar ")
        mensajeEncriptado=llaveRecibida.encrypt(mensaje.encode())
        sock.sendall(mensajeEncriptado)
