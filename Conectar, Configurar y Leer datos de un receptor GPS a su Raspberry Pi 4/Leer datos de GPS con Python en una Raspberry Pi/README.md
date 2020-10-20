<p align="center">
  <a href="https://doolpool.com" target="_blank" rel="noopener noreferrer">
    <img width="100" src="https://doolpool.github.io/DoolPool/imggg.png" alt="DoolPool logo">
  </a>
</p>
<h1 align="center">DoolPool, Inc.</h1>
<h3 align="center">Hello 👋, we are DoolPool, frontend and backend developers located in Peru.</h3>
<hr>

# Raspberry-Pi

## Recopilar datos del Sistema de posicionamiento global y cómo usarlos en sus proyectos en una Raspberry Pi

Recientemente les mostraba cómo puede conectar un módulo GPS común a su Raspberry Pi y qué se necesita para configurar el hardware para que pueda determinar la posición GPS de la computadora.

Sin embargo, conectar el módulo GPS es solo el primer paso y, debido a que debe ingresar comandos manualmente, no es muy útil en muchos proyectos. Por lo tanto, en este artículo, explicaré cómo usar Python para obtener los datos de posicionamiento del módulo GPS y usarlos en sus propios proyectos.

## Lectura de datos GPS sin procesar desde el puerto serie

La mayoría de los módulos GPS se comunican con la Raspberry Pi a través de una simple conexión en serie. Envían cadenas que contienen datos GPS y otros mensajes de estado. Estas cadenas se denominan sentencias NMEA . Puede acceder a esos comandos leyendo directamente el puerto serie al que está conectado el módulo GPS escribiendo:

```python       
sudo cat /dev/serial0
```

Este comando le dará algo como esto:

<p align="center">
    <img width="400" src="https://maker.pro/storage/L6gkVyN/L6gkVyNugmSoiZMKqXXB7ybIZvjpLm07mIABDTyD.png" alt="DoolPool logo">
</p>

Tenga en cuenta que tendrá que hacer esto antes de abrir un socket gpsd. De lo contrario, los datos en serie se redirigen al socket. El comando GPGGA contiene los datos de localización de GPS, que incluyen la posición. Si el módulo GPS no puede determinar la posición, lo más probable es que devuelva campos vacíos (como se muestra en la imagen) o devuelva cero.

Para utilizar los datos GPS en Python, puede leer directamente las cadenas que el módulo envía al puerto serie de la Raspberry Pi. Sin embargo, tendrá que hacer todo el análisis y el manejo de errores usted mismo. Adjunté un breve programa de ejemplo que lee las sentencias NMEA directamente desde el puerto serie e imprime la posición en la consola, al final de este artículo. La salida de este programa de ejemplo se ve así:

<p align="center">
    <img width="400" src="https://maker.pro/storage/Oj5qhmc/Oj5qhmc0cX0pHtElaBLmx81s86SnI7M3lJi9IMTq.png" alt="DoolPool logo">
</p

Este enfoque funciona y le recomiendo que lo utilice para aplicaciones no críticas. Además, con este método, no es necesario instalar ningún software adicional. Sin embargo, si necesita que su aplicación sea más confiable y no desea manejar todos los errores y otras oraciones NMEA, le recomiendo que use una biblioteca preconstruida bien probada que haga todo eso por usted.

## Instalación del módulo gpsd-clients

Si siguió el proyecto de "Conectar y configurar un receptor GPS a su Raspberry Pi 4" , entonces gpsd y el marco del cliente ya deberían estar configurados y funcionando sin problemas. Si no lo hizo, use el siguiente comando para instalar todas las bibliotecas y programas necesarios:

```python        
sudo apt-get install gpsd gpsd-clients
```
    
Esto debería permitirle importar los módulos necesarios cuando abre una consola Python:

<p align="center">
    <img width="400" src="https://maker.pro/storage/wY3pufb/wY3pufbZBCR6iuDbkrsU8cYZw7yc8weHEj666Oix.png" alt="DoolPool logo">
</p>

Si obtiene un error al importar el módulo GPS, asegúrese de que todos los paquetes necesarios se hayan instalado correctamente.

## Uso de la biblioteca de Python para analizar datos GPS

La biblioteca que instalamos en el último paso le permite comunicarse con el demonio GPS que luego se comunica con el receptor GPS. gpsd usa objetos JSON para comunicarse con sus clientes, por lo que recibirá dichos objetos JSON cuando use la biblioteca gpsd-clients, que puede analizar en su secuencia de comandos de Python.

En este tutorial, no estamos interesados ​​en enviar solicitudes al receptor GPS. En cambio, solo estamos mirando las respuestas. Las respuestas contienen clases y sus nombres corresponden al tipo de mensaje NMEA. Es importante tener en cuenta que estos objetos JSON pueden estar incompletos si un valor no está definido. Esto puede suceder cuando el receptor GPS no conoce su posición. En tal caso, el campo simplemente se omite. Puede encontrar una lista completa de comandos y descripciones más detalladas en la documentación oficial .

De todos modos, ahora sabemos que estas respuestas son objetos JSON simples donde se pueden omitir algunos campos. Por lo tanto, es una simple cuestión de leer y analizar los campos JSON para obtener los datos de posición:

```python 
def getPositionData(gps):
	nx = gpsd.next()
	if nx['class'] == 'TPV':
    	    latitude = getattr(nx, 'lat', "Unknown")
                longitude = getattr(nx, 'lon', "Unknown")
    	    print "Your position: lon = " + str(longitude) + ", lat = " + str(latitude)
```
Puede encontrar el script Python completo al final de este artículo. Si recibe un error al ejecutar el script, asegúrese de que el servidor gpsd se esté ejecutando y de que esté vinculado al puerto serie correcto. Si todo funciona correctamente, debería ver algo como esto:

<p align="center">
    <img width="400" src="https://maker.pro/storage/fkWwawy/fkWwawyC4vEo1uJQMpwLwrgaq6eNRssCOO6sA1ob.png" alt="DoolPool logo">
</p>

Como puede ver, es bastante fácil leer los valores proporcionados por el receptor GPS. No es necesario instalar ningún paquete adicional. Sin embargo, le recomiendo que utilice una biblioteca, como el paquete gpsd-client, para comunicarse con el receptor GPS, ya que esto facilita el manejo de muchos comandos diferentes y situaciones inesperadas.

<hr> 
<p align="center">
   <a alt="play doolpool" href="https://doolpool.com/play">Play DoolPool</a>
 • <a alt="red doolpool" href="https://doolpool.com/red/">Red DoolPool</a>
 • <a alt="music doolpool" href="https://doolpool.com/music">Music DoolPool</a>
</p> 
<p align="center"> © 2018-2020 DoolPool Inc. <br>All right reserved in <a href="https://doolpool.com/docs/">Documentation</a>.</p>
           
<p align="center">
  <a href="https://twitter.com/dool_pool" target="blank">
    <img align="center" src="https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/twitter.svg" alt="dool_pool" height="15" width="15" />
  </a>
  <a href="https://fb.com/doolpool.company" target="blank">
    <img align="center" src="https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/facebook.svg" alt="doolpool.company" height="15" width="15" />
  </a>
  <a href="https://instagram.com/doolpool.company" target="blank">
    <img align="center" src="https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/instagram.svg" alt="doolpool.company" height="15" width="15" />
  </a>
  <a href="https://www.youtube.com/channel/uc1jwir5d3pgcdaxb2brdh3w" target="blank"> 
    <img align="center" src="https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/youtube.svg" alt="https://www.youtube.com/channel/uc1jwir5d3pgcdaxb2brdh3w" height="15" width="15" />
  </a>
</p>

<!--
**DoolPool, Inc**
-->
