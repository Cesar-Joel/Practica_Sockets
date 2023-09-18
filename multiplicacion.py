import socket

port = 1613
id = "3"

info_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
info_socket.bind(("localhost", port))
info_socket.connect(("localhost", 1650))
info_socket.send(id.encode('utf-8'))
info_socket.close()

ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss.bind(("localhost", port))
ss.listen(5)

while True:
    cs, addr = ss.accept()
    operacion = cs.recv(1024)
    operandos = operacion.decode('utf-8').split(",")
    resultado = int(operandos[0]) * int(operandos[1])
    cs.send(str(resultado).encode('utf-8'))