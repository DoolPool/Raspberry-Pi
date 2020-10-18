<p align="center">
  <a href="https://doolpool.com" target="_blank" rel="noopener noreferrer">
    <img width="100" src="https://doolpool.github.io/DoolPool/imggg.png" alt="DoolPool logo">
  </a>
</p>
<h1 align="center">DoolPool, Inc.</h1>
<h3 align="center">Hello 👋, we are DoolPool, frontend and backend developers located in Peru.</h3>
<hr>

# Raspberry-Pi

## Aprenda a cómo puede usar la GUI estándar de Python, Tkinter, para controlar los pines GPIO en su Raspberry Pi a través de Raspbian.

Este apartado le mostrará cómo crear una aplicación de interfaz gráfica de usuario (GUI) simple que controlará los pines GPIO de Raspberry Pi utilizando Tkinter, la GUI estándar de Python. Antes de sumergirse en Tkinter, familiarícese con Python como lenguaje de programación . La aplicación GUI tendrá tres botones: dos controlarán los pines GPIO 20 y 21 y el tercero será el botón de salida.

Si bien hay muchas opciones de aplicaciones GUI para Python, Tkinter es la forma más común, más fácil de usar y más rápida de crear una aplicación GUI. Además, está integrado en el sistema operativo Raspberry Pi, Raspbian.

## Componentes requeridos
Para este proyecto, necesitará:

• Raspberry Pi

• 2 x LED

• Cables de salto

• Tablero de circuitos (Breadboard)

## Diagrama de circuito y explicación
El diagrama del circuito es muy simple. Solo tenemos que conectar dos LED a GPIO 20 y 21 en nuestra Raspberry Pi utilizando resistencias de 220 ohmios. Conecte los pines al lado positivo de cada LED y conecte el lado negativo de cada LED con las resistencias de 220 ohmios a tierra.

<p align="center">
    <img width="200" src="https://raw.githubusercontent.com/DoolPool/Raspberry-Pi/main/Python%2C%20Tkinter%2C%20controlar%20los%20pines%20GPIO/circuito.png" alt="Circuito">
</p>

## Tutorial de código
Echemos un vistazo al código y veamos qué hace cada sección para el proyecto en su conjunto.

En primer lugar, importamos las bibliotecas necesarias para este proyecto. La biblioteca Tkinter nos ayuda a crear la aplicación GUI y la biblioteca RPi.GPIO controla los pines GPIO de Raspberry Pi.

```python
import Tkinter as tk 
import RPi.GPIO as GPIO
from time import sleep
```
Luego, inicializamos los pines GPIO 21 y 20 para nuestros LED usando la numeración de pines BCM y declarando estos pines como salida.

```python        
GPIO21 = 21
GPIO20 = 20
GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO21, GPIO.OUT)
GPIO.setup(GPIO20, GPIO.OUT)
```
    
Después de eso, creamos el widget raíz Tk. Solo puede haber un widget raíz y debe crearse antes que cualquier otro widget.

Luego cambiamos el nombre del título de esta ventana y definimos su tamaño.

```python       
master = tk.Tk()
master.title("GPIO Control")
master.geometry("300x100")
```
    
Cuando se presiona el botón GPIO 21, buscará el estado anterior. Si el estado anterior es verdadero (estado alto), lo hará falso (estado bajo) y viceversa.

También hay una etiqueta al lado del botón que nos dirá si el LED es ALTO o BAJO.

```python        
def GPIO21button():
	global GPIO21_state
	if GPIO21_state == True:
		GPIO.output(GPIO21, GPIO21_state)
		GPIO21_state = False
		ONlabel = tk.Label(master, text="Turned ON", fg="green")
		ONlabel.grid(row=0, column=1)
	else:
		GPIO.output(GPIO21, GPIO21_state)
		GPIO21_state = True
		ONlabel = tk.Label(master, text="Turned OFF", fg="red")
		ONlabel.grid(row=0, column=1)
```
    
El botón GPIO 20 funciona de manera similar:

```python       
def GPIO20button():
	global GPIO20_State
	if GPIO20_State == True:
		GPIO.output(GPIO20, GPIO20_State)
		GPIO20_State = False
		OFFlabel = tk.Label(master, text="Turned ON", fg="green")
		OFFlabel.grid(row=1, column=1)
	else:
		GPIO.output(GPIO20, GPIO20_State)
		GPIO20_State = True
		OFFlabel = tk.Label(master, text="Turned OFF", fg="red")
		OFFlabel.grid(row=1, column=1)
```
    
Al final, creamos tres botones. Dos de ellos controlan los pines GPIO 20 y 21 y el tercero es el botón de salida.

```python        
ONbutton = tk.Button(master, text="GPIO 21", bg="blue", command=GPIO21button)
ONbutton.grid(row=0, column=0)

OFFbutton = tk.Button(master, text="GPIO 20",bg="blue" , command=GPIO20button)
OFFbutton.grid(row=1, column=0)

Exitbutton = tk.Button(master, text="Exit",bg="red", command=master.destroy)
Exitbutton.grid(row=2, column=0)
```
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
