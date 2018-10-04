import socket 

print("################")
print("#   CLIENTE    #")
print("################")

##ip = input('digite o ip de conexao: ') 
while 1:
	ip = "192.168.0.100"
	port = 7000
	addr = ((ip,port))
	client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client_socket.connect(addr)
	mensagem = input("-> ")
	##msg = byte(mensagem)
	msg = bytes(mensagem, 'utf-8')
	client_socket.send(msg) 	
	print ("mensagem enviada")
	client_socket.close()