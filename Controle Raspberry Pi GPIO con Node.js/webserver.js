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
