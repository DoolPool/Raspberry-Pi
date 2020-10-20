<p align="center">
  <a href="https://doolpool.com" target="_blank" rel="noopener noreferrer">
    <img width="100" src="https://doolpool.github.io/DoolPool/imggg.png" alt="DoolPool logo">
  </a>
</p>
<h1 align="center">DoolPool, Inc.</h1>
<h3 align="center">Hello 👋, we are DoolPool, frontend and backend developers located in Peru.</h3>
<hr>

# Raspberry-Pi

## ¡Aprenda a conectar y configurar un receptor GPS a su Raspberry Pi 4 para una variedad de proyectos divertidos!

Muchos proyectos requieren que determine la posición de su Raspberry Pi. A veces, no puede usar una red celular o Wi-Fi para esa tarea. 

En este caso, el GPS puede ser una buena alternativa, especialmente si la Raspberry Pi se usa en exteriores. En este artículo, discutiré cómo puede conectar un módulo GPS común a su Raspberry Pi y usar los datos adquiridos en sus diseños.

## Conexión del receptor GPS y Raspberry Pi

No discutiré los detalles de los receptores GPS y cómo funciona todo el sistema porque muchas otras fuentes ya lo hacen. ¡En lugar de eso, saltemos y conectemos el módulo GPS a la Raspberry Pi! 

El mío usa una conexión en serie simple, por lo que debe estar conectado a los pines TX y RX de la Raspberry Pi:

<p align="center">
    <img width="400" src="https://maker.pro/storage/Pj5hcvo/Pj5hcvoZyKgYOM65ymwmY5jvHOiCBL3HQyU9KtHn.jpeg" alt="img1">
    <p>Conexiones entre el receptor GPS y el Pi 4.</p>
</p>

¡Asegúrese de conectar la entrada RX del módulo a la salida TX de la Raspberry Pi y viceversa! También tenga en cuenta que conecté el módulo GPS a los pines de alimentación de la Raspberry Pi. Asegúrese de utilizar el voltaje correcto para su dispositivo.

## Configuración de Raspberry Pi para GPS

A continuación, debe configurar el sistema operativo de la Raspberry Pi para poder comunicarse con el receptor GPS. Tenga en cuenta que estos pasos se aplican específicamente a Raspbian Jessie o más reciente. Pueden diferir para versiones anteriores. 

También le recomiendo que utilice una instalación nueva del sistema operativo para descartar cualquier problema de configuración cuando pruebe su módulo GPS por primera vez.

Comience ejecutando raspi-config:

```python       
sudo raspi-config
```

Debería ver la siguiente pantalla:

<p align="center">
    <img width="400" src="https://maker.pro/storage/6tMJPDg/6tMJPDg1MG3tNSvbXQCItSYAZObuUtuqohDisW2t.png" alt="img2">
</p>

Aquí debe seleccionar "Opciones de interfaz" y luego "Serie":

<p align="center">
    <img width="400" src="https://maker.pro/storage/m1crFgR/m1crFgRuScTsReJF3DR8xeH2lCrWKsPTQ6Onhjbi.png" alt="img3">
</p>

Luego, desactive la posibilidad de acceder al shell de inicio de sesión a través de una conexión en serie y, en el siguiente paso, elija "Sí" cuando se le pregunte si desea que los puertos en serie permanezcan habilitados:

<p align="center">
    <img width="400" src="https://maker.pro/storage/G2g9fjl/G2g9fjlbcKjQNlGecFn1yekjWx3B3f791dMzyMjY.png" alt="img4">
</p>

Cuando regrese al menú principal del programa raspi-config, elija "Finalizar" y luego reinicie la Raspberry Pi.

## Descarga del software necesario

Instale gpsd y el cliente gpsd:

```python       
sudo apt-get install gpsd gpsd-clients
```

gpsd es un demonio de interfaz para receptores GPS en serie que admite diferentes estándares de comunicación. Lo usaré para obtener una lectura de prueba y verificar que el hardware funcione correctamente. Para obtener más información sobre el programa, puede escribir:

```python  
man gpsd
```

Una vez realizada la instalación, verifique que pueda recibir datos del módulo GPS. Para hacer eso, envíe los datos que envía a través del puerto serie:

```python  
cat /dev/serial0
```

Al principio, la salida debería verse así:

<p align="center">
    <img width="400" src="https://maker.pro/storage/SAsvlxM/SAsvlxMK9CFnougkGAKl1W5TvNVagXwr8dmpFLLK.png" alt="img5">
</p>

No importa qué datos reciba en este momento siempre que reciba algo. Si el puerto se cierra inmediatamente o el Pi no recibe ningún dato, verifique que conectó el módulo correctamente.

Tenga en cuenta que debería poder ejecutar este comando sin ser un superusuario. Si no puede, agregue el usuario pi al grupo de marcado:

```python  
sudo adduser pi dialout
```

## Leer los datos de posición

Ahora finalmente es el momento de determinar la posición de la Raspberry Pi. Escriba el siguiente comando para detener el servicio gpsd que se inició automáticamente cuando instaló gpsd anteriormente. Tienes que hacer esto porque las opciones predeterminadas no son correctas para el Pi:

```python  
sudo systemctl stop gpsd.socket
```

Tenga en cuenta que deberá escribir este comando cada vez que inicie el sistema. Alternativamente, también puede desactivarlo por completo:

```python  
sudo systemctl disable gpsd.socket
```

Inicie una nueva instancia de gpsd que redirija los datos del puerto serie correcto a un socket:

```python  
sudo gpsd /dev/serial0 -F /var/run/gpsd.sock
```

Y luego puede ejecutar cualquiera de los siguientes dos comandos para mostrar los datos del GPS:

```python  
sudo gpsmon
sudo cgps -s
```

Al principio, debería ver algo como esto:

<p align="center">
    <img width="400" src="https://maker.pro/storage/1pMl0Zq/1pMl0ZqClTmHVhc32GMtsoApaGyYivXwwtSQ9CU8.png" alt="img6">
</p>

Sin embargo, después de un tiempo, el módulo debería haber recopilado suficientes datos para mostrar una posición:

<p align="center">
    <img width="400" src="https://maker.pro/storage/Cygp1Iz/Cygp1Iz1alw7IJ85jBUgs7APMMV4Tsf85uhO4n3A.png" alt="img7">
</p>

Tenga en cuenta que pueden pasar hasta 30 minutos hasta que el módulo pueda determinar su posición cuando lo enciende por primera vez, especialmente si está en interiores. Intente apuntar la antena a una ventana o, mejor aún, coloque todo el módulo junto a una ventana o al aire libre.

Pruebe el siguiente comando si obtiene un error cuando ejecuta gpsmon y no hay salida cuando ejecuta cgps:

```python  
sudo systemctl stop serial-getty@serial0.service
```

Entonces deberías poder usar gpsmon también:

<p align="center">
    <img width="400" src="https://maker.pro/storage/9gGOq9p/9gGOq9pX0rB5YTmbANjlN1v1Uo7k4cqg8CiXsDWG.png" alt="img8">
</p>


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
