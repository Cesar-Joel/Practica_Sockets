import socket

operaciones = {}

ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

cont = 0
port = 1650
ss.bind(("localhost", 1650))
ss.listen(15)
print("Esperando conexión...")

while True:
    if cont < 1:
        cs, addr = ss.accept()
        print("Conexión aceptada desde:", str(addr))
        id = cs.recv(1024)
        operaciones[id.decode('utf-8')] = [addr[0], addr[1]]
        cont += 1
    else:
        cs, addr = ss.accept()
        info = cs.recv(1024)
        operacion = info.decode('utf-8').split(',')
        operandos = operacion[1] + "," + operacion[2]
        
        destino_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        match operacion[0]:
            case "1":
                destino_socket.connect((operaciones["1"][0], operaciones["1"][1]))
            case "2":
                destino_socket.connect((operaciones["2"][0], operaciones["2"][1]))
            case "3":
                destino_socket.connect((operaciones["3"][0], operaciones["3"][1]))
            case "4":
                destino_socket.connect((operaciones["4"][0], operaciones["4"][1]))
            case "5":
                destino_socket.connect((operaciones["5"][0], operaciones["5"][1]))
            case "6":
                destino_socket.connect((operaciones["6"][0], operaciones["6"][1]))
        
        destino_socket.send(operandos.encode('utf-8'))
        resultado = destino_socket.recv(1024)
        cs.send(resultado)
        destino_socket.close()
