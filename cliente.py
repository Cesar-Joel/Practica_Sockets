import socket

ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss.connect(("localhost", 1650))

num1 = input("Ingrese el primer valor: ")
num2 = input("Ingrese el segundo valor: ")
operacion = str(2) + "," + str(num1) + "," + str(num2)
ss.send(operacion.encode('utf-8'))
resultado = ss.recv(1024)
ss.close()
print(f"{num1} + {num2} = {resultado.decode('utf-8')}")
