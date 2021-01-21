“compliance-agent” es una aplicación desarrollada en Python3. 

Está diseñada para recopilar información de equipos, con Linux, en los cuales se ejecute.

Dentro de los datos recopilados, es posible encontrar:


●      Información sobre el procesador.

●      Nombre del sistema operativo.

●      Versión del sistema operativo.

●      Listado de procesos corriendo.

●      Usuarios con una sesión abierta en el sistema.

●      IP del host en el que se ejecuta.  


Esta aplicación usa comandos del Sistema Operativo Linux.

Luego de recopilar los datos, arma una firma .json para enviarla a la aplicación “compliance-api”.

Para correrla es necesario:
·  Tener instalado Python3 y la librería psutil.
·  Inicializar la aplicación “compliance-api” que recibe la información del host en la url: ../api/v1/compliance/systeminfo.
·  Ejecutar el archivo main.py

NOTA: En la carpeta venv se subieron las librerías necesarias para poder ejecutar “compliance-agent”.

Dockerizacion de compliance agent

-Generar imagen del contenedor

sudo docker build -t compliance-agent:latest .

-Correr el contenedor de docker

sudo docker run -p 8081:8081 --link api --name agent compliance-agent

Nota: se vinculan los dos contenedores, si se elige correr ambas aplicaciones dockerizadas, modificar la url seteada en main.py (compliance-agent) por la url = "http://api:5000/api/v1/compliance/system_info" para poder alcanzar al otro contenedor.


