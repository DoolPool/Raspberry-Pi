<p align="center">
  <a href="https://doolpool.com" target="_blank" rel="noopener noreferrer">
    <img width="100" src="https://doolpool.github.io/DoolPool/imggg.png" alt="DoolPool logo">
  </a>
</p>
<h1 align="center">DoolPool, Inc.</h1>
<h3 align="center">Hello 👋, we are DoolPool, frontend and backend developers located in Peru.</h3>
<hr>

# Raspberry-Pi

## Aprenda a controlar un pin GPIO de Raspberry Pi desde un servidor web usando Node.js y socket.io.

En este Proyecto, aprenderá a controlar un pin GPIO en una Raspberry Pi desde un servidor web usando Node.js y socket.io. Crearemos botones en la página web que encenderán o apagarán el LED conectado.

Antes de crear el servidor web, tenemos que instalar algunos paquetes.

## Instalación de Node.js en Raspberry Pi

Lo primero que debe hacer es actualizar su Raspberry Pi.

```node.js      
sudo apt-get update
```
Luego escriba el siguiente comando para actualizar los paquetes instalados a la última versión.

```node.js      
sudo apt-get dist-upgrade
```

Escriba el siguiente comando para instalar la última versión de Node en Raspberry pi.

```node.js      
curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash -
```

Ahora, con el repositorio del paquete NodeSource cargado, podemos continuar e instalar Node.js

```node.js      
sudo apt-get install -y nodejs
```

Para verificar si Node.js se instaló correctamente, escriba el siguiente comando, que debería mostrarle la versión de Node.js

```node.js      
node -v
```

## Instalación del módulo onoff

Para controlar los pines GPIO de la Raspberry Pi usando Node.js, tendremos que instalar el módulo “onoff”. Escriba el siguiente comando para instalarlo.

```node.js      
npm install onoff
```

## Instalación de socket.io para Node.js

Ahora instalamos el módulo de socket web para Node.js que nos permitirá controlar el pin GPIO de Raspberry Pi desde la página web.

```node.js      
npm install socket.io --save
```

## Crear el servidor web y el archivo HTML

Ahora hemos instalado todos los paquetes necesarios y es el momento de crear el servidor web y el archivo html. Ambos archivos deben estar en el mismo directorio.

### Index.html

Primero hagamos el archivo html que creará los botones en el navegador web. Cree el archivo html escribiendo index.html y pegue el siguiente código en él o descarge el archivo de este repositorio.

```html 
<!DOCTYPE html>
<html>
	<title>GPIO Control</title>
	<body>
    		<h2>Control GPIO 4</h2>
    		<button type="button" id="state" onclick="LEDOn()" style="background-color:green;">ON</button>
    		<button type="button" id="state" onclick="LEDOff()" style="background-color:red;">OFF</button>
    		<script src="https://cdnjs.cloudflare.com/ajax/libs/socket.io/2.0.3/socket.io.js"></script>
    		<script>
        		var socket = io.connect(); //cargar socket.io-client y conectarse al host
        		function LEDOn() { 
				socket.emit("state", 1); //enviar el estado del botón al servidor
			}

       			function LEDOff() {
            			socket.emit("state", 0); //enviar el estado del botón al servidor
        		}
    		</script>

	</body>
</html>
```
<p align="center">
    nota: tambien puedes descargar los archivos ya creados de este repositorio
</p>

## Conectando el LED a Raspberry Pi

Ahora conecte el LED a GPIO 4 usando una resistencia de 220 ohmios como se muestra en el siguiente diagrama:

<p align="center">
    <img width="400" src="https://maker.pro/storage/k8EOwqa/k8EOwqaPCH9ri3oSwsYqh9gQP0IFmwmOYtG1rpaI.png" alt="img1">
</p>

## Crear el servidor web

¡Ahora configuremos un servidor web !. El archivo Node.js abrirá el archivo solicitado y devolverá el contenido del archivo y, si algo sale mal, arrojará un error 404.

Cree el archivo escribiendo nano webserver.js y pegue el siguiente código en él o descarge el archivo de este repositorio.


```js
var Gpio = require('onoff').Gpio; //requiere onoff para controlar GPIO
var LEDPin = new Gpio(4, 'out'); //declara GPIO4 como salida
var fs = require('fs'); //requiere que el sistema de archivos lea archivos html
var http = require('http').createServer(function handler(req, res) { //crear servidor
  fs.readFile(__dirname + '/index.html', function (err, data) { //leer archivo html
    if (err) {
      res.writeHead(500);
      return res.end('Error al cargar socket.io.html');
    }
    res.writeHead(200);
    res.end(data);
  });
});

var io = require('socket.io')(http) //requiere el módulo socket.io y pasa el objeto http

http.listen(8080); //escuchar el puerto 8080

io.sockets.on('connection', function (socket) {// Conexión WebSocket
  var buttonState = 0; //variable para almacenar el estado del botón

  socket.on('state', function (data) { //obtener el estado del botón del cliente
    buttonState = data;
    if (buttonState != LEDPin.readSync()) { //Cambiar el estado del LED si se cambia el estado del botón
      LEDPin.writeSync(buttonState); //encender o apagar el LED
    }
  });
});
```
<p align="center">
    nota: tambien puedes descargar los archivos ya creados de este repositorio
</p>

Hemos creado tanto el servidor web como los archivos HTML, por lo que es hora de ejecutar el servidor web y controlar el pin GPIO de la Raspberry Pi.

Escriba el siguiente comando en la terminal para iniciar el servidor web:

```js
node webserver.js
```

Luego vaya a su navegador y abra la página web usando [Raspberrypi-ip]: 8080

En mi caso, es 192.168.4.1:8080

Debería ver dos botones en su pantalla y cuando presione estos botones, el LED conectado a GPIO4 de la Raspberry Pi se encenderá o apagará.

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
