# Proyecto de Cálculo Distribuido
## Descripción General
Esta aplicación de cálculo distribuido permite a un cliente realizar diversas operaciones matemáticas (suma, resta, multiplicación, división, módulo y potencia) utilizando un servidor central como intermediario para enrutar las solicitudes a servidores específicos de operaciones. Cada operación (suma, resta, etc.) se implementa en un servidor dedicado, y el cliente se comunica con el servidor central para solicitar el cálculo deseado.

## Arquitectura de la Aplicación
Cliente (cliente.py):
+ Inicia una conexión con el servidor central.
+ Muestra un menú que permite al usuario seleccionar una operación matemática y proporcionar los operandos.
+ Envía los datos de la operación y los operandos al servidor central.
+ Recibe el resultado de la operación del servidor central y lo muestra.
Servidor Central (servidor_nombre.py):
+ Actúa como intermediario entre el cliente y los servidores de operaciones.
+ Acepta conexiones de clientes y registra las operaciones que solicitan.
+ Enruta las solicitudes a los servidores de operaciones correspondientes.
+ Recibe los resultados de los servidores de operaciones y los devuelve al cliente.
Servidores de Operaciones (suma.py, resta.py, multiplicacion.py, division.py, modulo.py, potencia.py):
+ Cada servidor de operaciones está especializado en una operación matemática específica.
+ Espera conexiones de otros servidores y de la información del servidor central.
+ Realiza la operación correspondiente en los operandos proporcionados y envía el resultado al servidor central.
## Ejecución de la Aplicación
1. Configuración Inicial: Asegurarse de tener Python 3 instalado en el sistema.
2. Ejecución del Servidor Central: Ejecutar servidor_nombre.py en una terminal. Este servidor central será el encargado de enrutar las solicitudes a los servidores de operaciones.
3. Ejecución de los Servidores de Operaciones: Ejecutar cada uno de los servidores de operaciones (suma.py, resta.py, multiplicacion.py, division.py, modulo.py, potencia.py) en terminales separadas. Cada uno escuchará en su puerto correspondiente.
4. Ejecución del Cliente: Ejecutar cliente.py en otra terminal. El cliente mostrará un menú y permitirá al usuario seleccionar una operación matemática y proporcionar operandos.
## Diagrama de Arquitectura
![image](https://github.com/Cesar-Joel/Practica_Sockets/assets/79111276/7e16e1de-c7f0-41de-8d4e-1e03f9c93e30)
## Guía de Uso
1. Iniciar la aplicación ejecutando en diferentes terminales de comandos el servidor central junto con los servidores de operaciones en el siguiente orden: suma.py, resta.py, multiplicacion.py, division.py, modulo.py, potencia.py. Luego ejecutar el cliente para empezar a usar la aplicación.
2. Seleccionar una opción del menú del cliente (suma, resta, etc.).
3. Proporcionar los operandos requeridos.
4. El cliente enviará la solicitud al servidor central, que a su vez la enruta al servidor de operaciones correspondiente.
5. El servidor de operaciones realizará la operación y enviará el resultado de vuelta al cliente a través del servidor central.
6. El cliente mostrará el resultado de la operación en pantalla.
7. Repetir los pasos 2-6 según sea necesario.
## Datos de prueba.
Suma: 3 + 4
+ Resultado esperado: 7
+ Salida de la aplicación:

![image](https://github.com/Cesar-Joel/Practica_Sockets/assets/79111276/7ab674e7-e9a0-4438-b5cd-872c04380bef)

Resta: 3 − 4
+ Resultado esperado: -1
+ Salida de la aplicación:

![image](https://github.com/Cesar-Joel/Practica_Sockets/assets/79111276/569b21d3-47b5-41af-9dda-e04cb352e593)

Multiplicación: 3 ∗ 4
+ Resultado esperado: 12
+ Salida de la aplicación:

![image](https://github.com/Cesar-Joel/Practica_Sockets/assets/79111276/ab6e64e3-6df0-4c90-8223-e013bb8c2495)

División: 3/4
+ Resultado esperado: 0.75
+ Salida de la aplicación:

![image](https://github.com/Cesar-Joel/Practica_Sockets/assets/79111276/8d6276c2-d5f0-417c-acc6-5989516359ee)

Modulo: 6/4
+ Resultado esperado: 2
+ Salida de la aplicación:

![image](https://github.com/Cesar-Joel/Practica_Sockets/assets/79111276/4fb7c03f-c168-40b0-a25d-6d56b8e92d41)

Potencia: 3^4
+ Resultado esperado: 81
+ Salida de la aplicación:

![image](https://github.com/Cesar-Joel/Practica_Sockets/assets/79111276/b8506fc1-ef2d-4943-8b90-9a8796654ad1)
