import socket
import os

os.system('color 02')

print("################")
print("#   SERVIDOR   #")
print("################")


host = '' 
port = 7000
addr = (host, port)

while True:
	serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	serv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
	serv_socket.bind(addr) 
	serv_socket.listen(10) 
	print ("aguardando conexao")
	con, cliente = serv_socket.accept() 
	print ("conectado") 
	print ("aguardando Comando") 
	recebe = con.recv(1024) 
	msg = str(recebe, 'utf-8')
	retorno = os.system(msg)
	#print ("mensagem recebida: " + msg)
	serv_socket.close()
	pass