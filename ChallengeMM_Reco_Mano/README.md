# ChallengeMM_Reco_Mano

# DESCRIPCION y FIABILIDAD
Reco_Mano es un challenge multimedia que cuenta con dos modos de funcionamiento:

1. Modo Parental, comprueba que el usuario es una persona adulta de la que se han extraido características de sus manos previamente.
2. Modo no parental, comprueba si el usuario es un usuario habitual (empleado de la empresa).

Se calculan las distancias de la geometría de la mano donde da como resultado 1 si es un usuario habitual, sino puede dar valores de 0 (si el challenge no se ejecuta por falta de escáner, o si no detecta una mano derecha en la captura), también puede dar un valor de 2 a 12 si la mano detectada no coincide con el usuario habitual, con una cardinalidad igual a 13. Este challenge tiene una fiabilidad media porque el usuario malicioso puede tener las dimensiones de su mano similar al usuario habitual y es difícil que tenga una imagen de la mano derecha del usuario habitual escaneada para engañar al challenge. 

# FUNCIONAMIENTO
Este challenge requiere un proceso inicial de recopilación de datos, esto se hace con el archivo CrearBD_Manos.py, donde se le pide  al usuario que guarde 5 imágenes de su mano derecha escaneada, en la ubicación de la variable de entorno SECUREMIRROR_CAPTURES, luego se calcula la media de las distancias entre los puntos situados en los dedos y la palma de la mano (mediante la librería mediapipe de python), obtenidas de las 5 imágenes almacenadas. Posteriormente se crea el fichero datos.csv con las medias de las distancias de los puntos obtenidas.
El challenge se encuentra en el fichero Reco_Manos.py donde se pide al usuario que se escanee la mano derecha y la almacene en una ubicación determinada, dentro de la ruta de la variable de entorno SECUREMIRROR_CAPTURES. 

Importante: La imagen almacenada en dicha ubicación se eliminará automáticamente una vez que se ejecute el challenge para garantizar que el usuario haga la operación cada vez que necesite ejecutarlo, disminuyendo así el riesgo de plagio de la imagen.

Una vez que la imagen se encuentra en la ubicación, se calculan las distancias y error medio cuadrático (RMSE) entre las distancias de la imagen y las medias almacenadas y se compara con un Umbral obtenido de la mayor diferencia entre las imágenes de entrenamiento. La clave resultante para el modo parental será 0 ó 1, y en el modo no parental estará desde 0 hasta 12, siendo 1 el valor correcto en ambos casos.


# Requisitos:
La variable de entorno SECUREMIRROR_CAPTURES debe existir y apuntar al path donde el server bluetooth deposita las capturas.
Importante: Instalar el framework MediaPipe https://mediapipe.dev/, actualmente disponible hasta la versión 3.10.8. 
Importante: Hacer fotos escaneadas de la mano derecha en el escáner que utiliza habitualmente para tomar la imagen a comparar. 

# Librerías utilizadas:

- Mediapipe para los modelos de detección de manos y ubicación de los puntos de interés (mp.solutions.HANDS y handlandmarks). para instalar mediapipe simplmente: pip install mediapipe

- Opencv para la entrada de las imagen y configuración de sus dimensiones  (la librería mediapipe también instala opencv): https://www.geeksforgeeks.org/opencv-python-tutorial
 
Importante:Tras instalar opencv, la dll python3.dll de instalación de python cambia, debes darle acceso al programa que haga uso de este challenge ubicándola en un directorio al que pueda acceder. Para aprender opencv https://www.geeksforgeeks.org/opencv-python-tutorial 

- Tkinter para las GUI de interacción con el usuario. Para instalar el módulo tkinter simplemente: pip install tkinter. Para aprender tkinter: https://www.pythontutorial.net/tkinter/ . Para instalar el módulo tkinter simplemente: pip install tkinter
 
- os para crear directorios y listar archivos. https://docs.python.org/es/3.10/library/os.html

# Configuración para validar el challenge:

El valor del campo "FileName" debe ser "challenge_loader_python.dll". Dentro del campo "Props" debe haber varios pares clave-valor:

"module_python": Debe contener el nombre del archivo del módulo de python  (sin incluir ".py"). En este caso: "Reco_Manos".

"validity_time": el tiempo de validez del challenge en segundos (entero).

"refresh_time": el tiempo en segundos (entero) entre ejecuciones automáticas del challenge.

"modo": determina el modo de ejecución. El modo parental se selecciona si su valor es "parental". De lo contrario, se utiliza el modo no parental.

Otros campos como "Description" y "Requirements" son opcionales e informativos.

# EJEMPLO:
Ejemplo de configuración del challenge para el modo parental:

{ 	"FileName": "challenge_loader_python.dll",
	
	"Props": {
		"module_python": "Reco_Manos",
		"validity_time": 3600,
		"refresh_time": 3000,
		"mode": "parental",
		
	},
	"Requirements": "none"
}

A continuación se presenta una configuración en modo no parental, para el caso de uso en empresas. 

{	"FileName": "challenge_loader_python.dll",
	
	"Props": {
		"module_python": "Reco_MAnos",
		"validity_time": 3600,
		"refresh_time": 3000,
		"mode": "normal",
		
	},
	"Requirements": "none"
}



