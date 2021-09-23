# ChatCifradoRSA
Un chat con dos clientes y un servidor cifrado con el algoritmo RSA de la libreria Pycrtpyo implementado en python
Para correr desde un terminal use el comando (interprete) client.py/server.py (puertos tcp/ip 1 para cliente 2 para servidor) (0 o 1 para escoger el cliente)
ejemplo de ejecución para correr en 3 terminales impoertante seguir el orden
terminal 1:
python server.py 12345 12346
terminal 2:
python client.py 12345 0
terminal 3:
python client.py 12346 1
