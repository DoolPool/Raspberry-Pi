<p align="center">
  <a href="https://doolpool.com" target="_blank" rel="noopener noreferrer">
    <img width="100" src="https://doolpool.github.io/DoolPool/imggg.png" alt="DoolPool logo">
  </a>
</p>
<h1 align="center">DoolPool, Inc.</h1>
<h3 align="center">Hello 👋, we are DoolPool, frontend and backend developers located in Peru.</h3>
<hr>

# Raspberry-Pi

## Aprenda a crear una aplicación de pintura simple usando OpenCV en Raspberry Pi.

En este artículo, aprenderá cómo crear una aplicación de pintura simple usando OpenCV. Este tutorial lo ayudará a familiarizarse más con la creación de sus propias interfaces de usuario para cualquier aplicación que esté intentando construir con plataformas como Arduino y Raspberry Pi .

Si es la primera vez que usa OpenCV, consulte mi tutorial anterior sobre cómo configurar OpenCV en una Raspberry Pi .

La aplicación tendrá cuatro barras de seguimiento: tres se usarán para cambiar el color (B, G, R) y la cuarta se usará para seleccionar entre un rectángulo, círculo, línea recta o línea libre.

También es posible utilizar las barras de seguimiento como interruptores. Por defecto, OpenCV no tiene una funcionalidad de botón, pero podemos usar las barras de seguimiento como botones.

Otra función útil que podemos usar en esta aplicación es la función de devolución de llamada del mouse que se ejecutará siempre que se produzca un evento de mouse. 

## Tutorial

## Leer una imagen
La función cv2.imread () se utiliza para leer la imagen y su argumento es el nombre de la imagen. Si la imagen está en el directorio de trabajo, simplemente escriba el nombre de la imagen. De lo contrario, tendrá que proporcionar la ruta completa de la imagen.

Crearemos una ventana y la etiquetaremos como 'imagen'. Todas las barras de seguimiento se adjuntarán a esta ventana.

```python        
img = cv2.imread('obama.jpg')
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
```

## Crear las barras de seguimiento
Para crear las barras de seguimiento, usamos la función cv2.createTrackbar () , que tiene cinco argumentos:

1.El nombre de la barra de seguimiento

2.El nombre de la ventana a la que está adjunta

3.El valor predeterminado

4.El valor máximo

5.La función de devolución de llamada (que se ejecuta cada vez que cambia el valor de la barra de seguimiento)

La función de devolución de llamada siempre tiene un argumento predeterminado que es la posición de la barra de seguimiento. En nuestro caso, la función no hace nada, así que simplemente pasamos.

Creamos tres barras de seguimiento para rojo, verde y azul. Cada barra de seguimiento tiene un valor predeterminado de 0 y un valor máximo de 255 y se adjuntan a la ventana denominada 'imagen'.

A continuación, necesitamos crear una barra de seguimiento para seleccionar entre un rectángulo, círculo, línea recta y línea libre con un valor predeterminado de 0 y un valor máximo de 3. Estableceremos los valores de la siguiente manera:

0: rectángulo

1: círculo

2: línea recta

3: línea libre


```python
# Create trackbars for color change
cv2.createTrackbar('R','image',0,255,nothing)
cv2.createTrackbar('G','image',0,255,nothing)
cv2.createTrackbar('B','image',0,255,nothing)

# Create trackbars for drawing shapes
cv2.createTrackbar('Select', 'image',0,3,nothing)
```

## Función de devolución de llamada del mouse

Ahora podemos crear una función de devolución de llamada del mouse que se ejecuta cuando tiene lugar un evento de mouse. Un evento de mouse puede ser cualquier cosa relacionada con el mouse: botón izquierdo hacia abajo, botón izquierdo hacia arriba, doble clic del botón izquierdo, etc.

La función nos da las coordenadas (x, y) para cada evento del mouse. Con este evento y ubicación, podemos hacer lo que queramos.

La creación de una función de devolución de llamada del mouse tiene un formato específico que es el mismo en todas partes. Solo difiere en lo que hace la función. En nuestro caso, la función de devolución de llamada es la función de dibujo que dibujará un rectángulo, círculo, línea recta o línea libre dependiendo de la posición de la cuarta barra de seguimiento.


```python
def draw(event,x,y,flags,param):
    global ix,iy,drawing
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            if s == 3:
                cv2.circle(img,(x,y),5,(b, g, r),-1)
    elif event == cv2.EVENT_LBUTTONUP:
        if drawing == True:
             if s == 0:
                cv2.rectangle(img,(ix,iy),(x,y),(b, g, r),5)
             elif s == 1:
                cv2.circle(img,(int((ix+x)/2), int((iy+y)/2)),int(math.sqrt( ((ix-x)**2)+((iy-y)**2) )),(b, g, r),5)
             elif s == 2:
                cv2.line(img,(ix,iy),(x,y),(b, g, r),5)
    
        drawing = False
cv2.setMouseCallback('image',draw)
```

## Obtener la posición de la barra de seguimiento

La función Cv2.getTrackbarPos () se utiliza para obtener la posición actual de la barra de seguimiento. El primer argumento que toma es el nombre de la barra de seguimiento que creamos antes y el segundo argumento es el nombre de la ventana a la que se va a adjuntar.

```python
# get current positions of four trackbars
    r = cv2.getTrackbarPos('R','image')
    g = cv2.getTrackbarPos('G','image')
    b = cv2.getTrackbarPos('B','image')
    s = cv2.getTrackbarPos('Select','image')
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
