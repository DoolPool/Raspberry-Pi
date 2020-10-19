<p align="center">
  <a href="https://doolpool.com" target="_blank" rel="noopener noreferrer">
    <img width="100" src="https://doolpool.github.io/DoolPool/imggg.png" alt="DoolPool logo">
  </a>
</p>
<h1 align="center">DoolPool, Inc.</h1>
<h3 align="center">Hello 👋, we are DoolPool, frontend and backend developers located in Peru.</h3>
<hr>

# Raspberry-Pi

## Instalar Ubuntu

Como sabemos, Raspbian se basa en la distribución Debian, que es el sistema operativo oficial de Raspberry Pi . Es liviano y sigue siendo una de las mejores opciones, y una de las distribuciones de Raspberry Pi Linux más populares. Sin embargo, hay muchas opciones adicionales de escritorio Raspberry Pi.

La instalación de Raspbian también es fácil, pero el problema con Debian son sus ciclos de actualización lentos y sus paquetes más antiguos.

Ejecutar Ubuntu en la Raspberry Pi te brinda una experiencia más rica y un software actualizado. Además, si trabaja con ROS (Robot Operating System), sabrá que el principal sistema operativo compatible es Ubuntu.

Tenemos dos opciones cuando se trata de ejecutar Ubuntu en tu Raspbian Pi.

-Ubuntu MATE

-Ubuntu Server 18.04.4 o 19.10

La primera opción es la más fácil y rápida de configurar, mientras que la segunda opción le da la libertad de instalar el entorno de escritorio de su elección.

En diciembre de 2019, Canonical publicó una hoja de ruta de soporte para la última computadora de placa única Raspberry Pi 4 en su sistema operativo Ubuntu Server y se comprometió a ser totalmente compatible con Ubuntu en todas las placas Raspberry Pi.

Recientemente, el equipo de Ubuntu lanzó la última versión puntual de nuestro sistema operativo 18.04 Long Term Support 18.04.4, y con esa versión viene la compatibilidad con las placas Raspberry Pi. Puede descargar la versión 18.04.4 de Ubuntu desde el sitio web oficial de Ubuntu . Esta es una distribución oficial de Ubuntu Server 18.04.4 para placa Raspberry Pi.

Ubuntu actualmente es compatible con los modelos Raspberry Pi 2, Raspberry Pi 3 y Raspberry Pi 4, y las imágenes están disponibles para Ubuntu 18.04.4 LTS (Bionic Beaver), que es la última versión de LTS (Soporte a largo plazo) compatible hasta abril de 2023, y Ubuntu 19.10 (Eoan Ermine), compatible hasta julio de 2020.

### Requisitos para instalar

1. Una Raspberry Pi 2 o 3

2. Un adaptador de 5 voltios y 2 amperios

3. Convertidor de HDMI a VGA (si utiliza una pantalla LCD sin HDMI)

4. Un teclado y un mouse

5. Una pantalla LCD

6. Una funda de tarjeta SD (para conectar Raspbian a la tarjeta SD)

7. Un dongle Wi-Fi (si usa Raspberry Pi 2)

8. Un cable HDMI

9. Una tarjeta Micro USB de clase 10 (no menos de 8 GB)

### 1. Descarga la imagen del servidor Ubuntu para Raspberry Pi en la tarjeta SD

Primero tienes que descargar la imagen del sistema operativo. Vaya a la página de descarga del sitio web oficial de Ubuntu.

<p align="center">
    <img width="300" src="https://maker.pro/storage/eMV5Vuz/eMV5VuzcrcRP6uKWJeQN6mVlkxXEdgBBI8VV3T8W.png" alt="Raspberry Kit">
</p>

Ahora, desplácese hacia abajo hasta la sección Descargar su imagen de Ubuntu Pi y haga clic en el enlace de descarga para Raspberry Pi 2, Raspberry Pi 3 o Raspberry Pi 4, según la versión de Raspberry Pi que tenga. Tengo Raspberry Pi 4 Model B, así que voy a descargar la imagen de Raspberry Pi 4 con la versión de 64 bits.

### 2. Flasheo de la imagen de Ubuntu en la tarjeta microSD

Puede flashear la imagen de Ubuntu en su tarjeta microSD muy fácilmente en el sistema operativo Windows, Linux y macOS usando Etcher . Etcher es un software realmente fácil de usar para flashear tarjetas microSD para dispositivos Raspberry Pi. Puede descargar Etcher desde el sitio web oficial de Etcher .

Inicie Etcher y seleccione el archivo de imagen y su tarjeta SD.

<p align="center">
    <img width="300" src="https://maker.pro/storage/EnUlh4Q/EnUlh4QRXft3azUBC14oszxlvGyor44jCk9qdIHE.jpeg" alt="Raspberry Kit">
</p>

El proceso tomará unos minutos, así que tenga paciencia. Cuando Etcher haya terminado, puede quitar su tarjeta de la computadora.

### 3. Configuración de la Raspberry Pi

Probablemente ya sepa que necesita algunas cosas para comenzar con Raspberry Pi, como un mouse, teclado, cable HDMI, etc. También puede instalar Raspberry Pi sin teclado ni mouse, pero este tutorial no trata de eso.

- Conecte un mouse y un teclado.

- Conecte el cable HDMI.

- Inserta tu tarjeta MicroSD.

- Conecte su cable Ethernet, si está usando uno.

- Cuando todo lo demás esté configurado, enciéndalo en su Raspberry Pi conectando el cable de alimentación.

### 4. Inicia tu Raspberry Pi

Después de encender su Raspberry Pi, espere a que se complete el proceso de arranque y debería ver el siguiente mensaje en la ventana.

```ubuntu
Ubuntu 18.04.4 LTS ubuntu tty1
ubuntu login:
```

Inicie sesión con el usuario predeterminado. Las credenciales predeterminadas son:

```ubuntu
login: ubuntu
password: ubuntu
```

La primera vez que inicie sesión, se le pedirá que cambie esta contraseña.

```ubuntu
You are required to change your password immediately (root enforced)
Changing password for ubuntu.
(current) UNIX password: _
```

Después de cambiar la contraseña predeterminada, debería recibir un mensaje que confirme que ahora está en Bionic Beaver:

```ubuntu
Last login: Thu Mar 3 13:00:00 UTC 2020 on ***.***.***.*** 
Welcome to Ubuntu 18.04.4 LTS (GNU/Linux 5.3.0-1017-raspi2 aarch64)   
* Documentation:  https://help.ubuntu.com  
* Management:     https://landscape.canonical.com 
* Support:        https://ubuntu.com/advantage

  System information as of Thu Mar 5 15:41:49 UTC 2020

  System load:  0.89                    Processes:        126
  Usage of /:   1.3% of 117.11GB    Users logged in:  0
  Memory usage: 6%                  IP addresss for wlan0:***.***.***.***
  Swape usage:  0%


0 packages can be updated.
0 updates are security updates.

Your Hardware Enablement Stack (HWE) is supported until April 2023.
```

### 5. Configuración de WiFi usando netplan

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

<!--**DoolPool, Inc**-->
