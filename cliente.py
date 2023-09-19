import socket

ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss.connect(("localhost", 1650))

print("- M E N U -")
print("1.- Suma.")
print("2.- Resta.")
print("3.- Multiplicación.")
print("4.- División.")
print("5.- Módulo.")
print("6.- Potencia.")
print("7.- Salir.")
opc = int(input("Seleccione una opción: "))

if opc in [1, 2, 3, 4, 5, 6]:
    num1 = input("Ingrese el primer valor: ")
    num2 = input("Ingrese el segundo valor: ")
else:
    ss.close()
    exit()

while (opc == 4 or opc == 5) and num2 == 0:
    num2 = input("No se permiten divisiones entre 0, ingrese otro número: ")

match opc:
    case 1:
        operacion = str(1) + "," + str(num1) + "," + str(num2)
    case 2:
        operacion = str(2) + "," + str(num1) + "," + str(num2)
    case 3:
        operacion = str(3) + "," + str(num1) + "," + str(num2)
    case 4:
        operacion = str(4) + "," + str(num1) + "," + str(num2)
    case 5:
        operacion = str(5) + "," + str(num1) + "," + str(num2)
    case 6:
        operacion = str(6) + "," + str(num1) + "," + str(num2)
 
ss.send(operacion.encode('utf-8'))
resultado = ss.recv(1024)
ss.close()

match opc:
    case 1:
        print(f"{num1} + {num2} = {resultado.decode('utf-8')}")
    case 2:
        print(f"{num1} - {num2} = {resultado.decode('utf-8')}")
    case 3:
        print(f"{num1} * {num2} = {resultado.decode('utf-8')}")
    case 4:
        print(f"{num1} / {num2} = {resultado.decode('utf-8')}")
    case 5:
        print(f"{num1} % {num2} = {resultado.decode('utf-8')}")
    case 6:
        print(f"{num1} ** {num2} = {resultado.decode('utf-8')}")
