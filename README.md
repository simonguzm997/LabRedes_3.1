# LabRedes_3.1

## Pasos para correr la aplicación: 
* Abrir los archivos client.py y serverMilty.py en su editor de texto preferido
* Editar el atributo TCP_IP por la dirección IP asociado a la maquina Ubuntu del servidor

### Servidor:
1. Transferir la carpeta "Servidor" con todos sus contenidos a la maquina Ubuntu del servidor
2. Entrar en la carpeta donde esta ubicado el archivo serverMilty.py
3. Usar el comando: python3 serverMilty.py
4. Ingrese el nombre del archivo según las opciones presentadas
5. Ingrese la cantidad de usuarios (valor entre 1 y 25)
6. Ingrese Y si esta de acuerdo o N en caso contrario
7. Espere las conexiones del cliente

### Cliente:
1. Entrar a la carpeta donde esta ubicado el archivo client.py
2. Usar el comando python client.py
3. Ingresar el numero total de clientes
4. Ingresar el num del cliente actual
5. Esperar que el servidor reciba los clientes necesarios.
6. Repetir este paso según la cantidad de clientes deseada
