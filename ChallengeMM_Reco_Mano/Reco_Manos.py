
# -*- coding: latin-1 -*-

import cv2
import mediapipe as mp
import numpy as np
from math import sqrt
import pandas as pd
import os
from os import remove
from os import path
import tkinter as tk
from tkinter import messagebox
#import lock


# variables globales
# ------------------
props_dict={}

def init(props):
    global props_dict

    print("Python: Enter in init")
    
    #props es un diccionario
    props_dict= props
     # Ejecución del challenge para ver si funciona (no se comprueba la clave)
    #executeChallenge()

    # Fake de la ejecución
    if props_dict["mode"] == "parental":
        resultado = ('\0', 1)

    else: # Modo no parental
        resultado = ('1', 1)

    # Comprobación de que la longitud del resultado es mayor que cero (ejecución sin problemas)
    if (resultado[1] > 0):
        return 0
    else:
        return -1
    



def calcularDistancia (x1,y1,x2,y2): 
    return sqrt((x1-x2)**2 + (y1-y2)**2)



def executeChallenge():
    print("Starting execute")
    
    resul=[]
    def cerrar():
        ventana.destroy()

    ca=messagebox.askquestion(title= "Reco_Manos", message="Tines escaner vinculado al PC para obtener una imagen de tu mano derecha")
    print (ca)
    
    if (ca=="no"):
        ventana= tk.Tk()
        ventana.geometry('450x100')
        tk.Label(ventana,text='Necesitas un escaner para comprobar la imagen', font = "Calibri 16").pack()
        #Botón para cerrar ventana una vez que el usuario introdujo su nombre y apellidos
        button1 = tk.Button(ventana, text = "OK", command = cerrar).pack(side= tk.BOTTOM)
        ventana.mainloop()
        rmse=-1

    else: 
        
        d_Path=os.environ['SECUREMIRROR_CAPTURES']

        print ("storage folder is :",d_Path)
    
        ventana= tk.Tk()
        ventana.geometry('750x150')
        tk.Label(ventana,text='Antes de pulsar OK crea una carpeta llamada:  MANO (si aún no la has creado) \n en la ruta '  + d_Path + ' \n y guarde en ella una imagen escaneada de la palma de la mano derecha\n ', font = "Calibri 16").pack()
        #Botón para cerrar ventana una vez que el usuario introdujo su nombre y apellidos
        button1 = tk.Button(ventana, text = "OK", command = cerrar).pack(side= tk.BOTTOM)
        ventana.mainloop()

        dataPath = d_Path + '/' + 'MANO' #Cambia a la ruta donde se almacene la imagen diaria

        #comprobando que el directorio de la carpeta MANO no está vacio
        direct = os.listdir(dataPath) 
        if len(direct) != 0: 

            for fileName in os.listdir(dataPath):
            
                mp_drawing = mp.solutions.drawing_utils
                mp_hands = mp.solutions.hands
                with mp_hands.Hands(
                    static_image_mode=True,
                    max_num_hands=1,
                    min_detection_confidence=0.5) as hands:

                    image_R = cv2.imread(dataPath + "/" + fileName)
                    image_R=cv2.resize(image_R,(400,400),interpolation=cv2.INTER_CUBIC)
                    height, width, _ = image_R.shape
                    image = cv2.flip(image_R, 1)

                    image_rgb =cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

                    results = hands.process(image_rgb)

       

                if results.multi_hand_landmarks is not None:
                    for idx, hand_handedness in enumerate(results.multi_handedness): 
                        if hand_handedness.classification[0].label == "Left": 
                            rmse=-1
                            ventana= tk.Tk()
                            ventana.geometry('450x100')
                            tk.Label(ventana,text='Entre una imagen de la mano derecha', font = "Calibri 16").pack()
                            #Botón para cerrar ventana una vez que el usuario introdujo su nombre y apellidos
                            button1 = tk.Button(ventana, text = "OK", command = cerrar).pack(side= tk.BOTTOM)
                            ventana.mainloop()

                            
                        elif hand_handedness.classification[0].label == "Right":
                            print('Dentro de right')
                            # Dibujando los puntos y las conexiones mediante mp_drawing  
                            for hand_landmarks in results.multi_hand_landmarks:
                                mp_drawing.draw_landmarks(
                                    image, hand_landmarks, mp_hands.HAND_CONNECTIONS,
                                    mp_drawing.DrawingSpec(color=(255,255,0), thickness=4, circle_radius=2), 
                                    mp_drawing.DrawingSpec(color=(255,0,255), thickness=2))
                                x0 = int(hand_landmarks.landmark[0].x * width)
                                y0 = int(hand_landmarks.landmark[0].y * height)
                                x6 = int(hand_landmarks.landmark[20].x * width)
                                y6 = int(hand_landmarks.landmark[20].y * height)
                                x61 = int(hand_landmarks.landmark[17].x * width)
                                y61 = int(hand_landmarks.landmark[17].y * height)
                                x7 = int(hand_landmarks.landmark[16].x * width)
                                y7 = int(hand_landmarks.landmark[16].y * height)
                                x71 = int(hand_landmarks.landmark[13].x * width)
                                y71 = int(hand_landmarks.landmark[13].y * height)
                                x8 = int(hand_landmarks.landmark[12].x * width)
                                y8 = int(hand_landmarks.landmark[12].y * height)
                                x81 = int(hand_landmarks.landmark[9].x * width)
                                y81 = int(hand_landmarks.landmark[9].y * height)
                                x9 = int(hand_landmarks.landmark[8].x * width)
                                y9 = int(hand_landmarks.landmark[8].y * height)
                                x91 = int(hand_landmarks.landmark[5].x * width)
                                y91 = int(hand_landmarks.landmark[5].y * height)
                                x10 = int(hand_landmarks.landmark[4].x * width)
                                y10 = int(hand_landmarks.landmark[4].y * height)
                                x101 = int(hand_landmarks.landmark[2].x * width)
                                y101 = int(hand_landmarks.landmark[2].y * height)

                                dis6= calcularDistancia(x6,y6,x0,y0)
                                dis61= calcularDistancia(x61,y61,x0,y0)
                                dis7= calcularDistancia(x7,y7,x0,y0)
                                dis71= calcularDistancia(x71,y71,x0,y0)
                                dis8= calcularDistancia(x8,y8,x0,y0)
                                dis81= calcularDistancia(x81,y81,x0,y0)
                                dis9= calcularDistancia(x9,y9,x0,y0)
                                dis91= calcularDistancia(x91,y91,x0,y0)
                                dis10= calcularDistancia(x10,y10,x0,y0)
                                dis101= calcularDistancia(x101,y101,x0,y0)
                        
                                # Dibujando los puntos de interés
                                cv2.circle(image, (x0, y0), 3,(255,0,0),3)
                                cv2.circle(image, (x6, y6), 3,(255,0,0),3)
                                cv2.circle(image, (x61, y61), 3,(255,0,0),3)
                                cv2.circle(image, (x7, y7), 3,(255,0,0),3)
                                cv2.circle(image, (x71, y71), 3,(255,0,0),3)
                                cv2.circle(image, (x8, y8), 3,(255,0,0),3)
                                cv2.circle(image, (x81, y81), 3,(255,0,0),3)
                                cv2.circle(image, (x9, y9), 3,(255,0,0),3)
                                cv2.circle(image, (x91, y91), 3,(255,0,0),3)
                                cv2.circle(image, (x10, y10), 3,(255,0,0),3)
                                cv2.circle(image, (x101, y101), 3,(255,0,0),3)
             
                  
                            resul=[fileName,dis6,dis61,dis7,dis71,dis8,dis81,dis9,dis91,dis10,dis101, results] #Se almacena una lista de los resultados de las distancias entre los puntos y el valor de  multi_hand_landmarks que me permite saber si la imagen es de una mano derecha o izquierda
                        
                            data= {'Nombre': [(resul[0])]
                                        , 'Dist 20-0': [(resul[1])]
                                        , 'Dist 17-0': [(resul[2])]
                                        , 'Dist 16-0': [(resul[3])]
                                        ,'Dist 13-0': [ (resul[4])]
                                        ,'Dist 12-0': [(resul[5])]
                                        ,'Dist 9-0': [ (resul[6])]
                                        ,'Dist 8-0': [(resul[7])]
                                        ,'Dist 5-0': [(resul[8])]
                                        ,'Dist 4-0': [(resul[9])]
                                        ,'Dist 2-0': [(resul[10])]}

                        
                            # Creación DataFrame:
                            tab_result = pd.DataFrame(data)
                        

                            df=pd.read_csv(d_Path + '/' + 'datos.csv')
                            rmse= sqrt((((tab_result.iloc[0, 1]-df.iloc[0, 1])**2)+((tab_result.iloc[0, 2]-df.iloc[0, 2])**2)+((tab_result.iloc[0, 3]-df.iloc[0, 3])**2)+((tab_result.iloc[0, 4]-df.iloc[0, 4])**2)+((tab_result.iloc[0, 5]-df.iloc[0, 5])**2)+((tab_result.iloc[0, 6]-df.iloc[0, 6])**2)+((tab_result.iloc[0, 7]-df.iloc[0, 7])**2)+((tab_result.iloc[0, 8]-df.iloc[0, 8])**2)+((tab_result.iloc[0, 9]-df.iloc[0, 9])**2)+((tab_result.iloc[0, 10]-df.iloc[0, 10])**2))/10)
                            
                            #Eliminando imagen de la carpeta MANO para que el usuario tenga que guardarla cada vez que se ejecute el challenge
                            remove(dataPath + "/" + fileName)
                image = cv2.flip(image, 1)
                cv2.imshow("Image",image)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
            

              

        else:
            ventana= tk.Tk()
            ventana.geometry('850x100')
            tk.Label(ventana,text='Debes guardar una imagen de la palma de la mano derecha escaneada en una carpeta llamada: \n MANO en la ruta '  + d_Path + ' ', font = "Calibri 16").pack()
            #Botón para cerrar ventana una vez que el usuario introdujo su nombre y apellidos
            button1 = tk.Button(ventana, text = "OK", command = cerrar).pack(side= tk.BOTTOM)
            ventana.mainloop()
            rmse=-1

    
    # Get the mode from the properties dictionary (global variable)
    mode = props_dict["mode"]    
    
   # Construcción de la respuesta
    if mode == "parental":
        if rmse >= 0 and rmse <= df.iloc[0,11]:   cad = '\0'
        else:                                     cad = '\u0001'
        
    else:   # Modo no parental 
        print(rmse)
        print(df.iloc[0,11]) 
        if rmse<0:                                        resp=0
        elif rmse >= 0 and rmse <= df.iloc[0,11]:         resp=1
        elif rmse > df.iloc[0,11] and rmse <= 20:         resp=2 
        elif rmse > 20 and rmse <= 25:                    resp=3
        elif rmse > 25 and rmse <= 30:                    resp=4
        elif rmse > 30 and rmse <= 35:                    resp=5
        elif rmse > 35 and rmse <= 40:                    resp=6    
        elif rmse > 40 and rmse <= 45:                    resp=7
        elif rmse > 45 and rmse <= 50:                    resp=8
        elif rmse > 50 and rmse <= 55:                    resp=9
        elif rmse > 55 and rmse <= 60:                    resp=10
        elif rmse > 60 and rmse <= 65:                    resp=11
        elif rmse > 65:                                   resp=12   
    
    
        cad="%d"%(resp)

    key = bytes(cad,'utf-8')
    key_size = len(key)
    result =(key, key_size)
    print ("result:",result)
    return result
    
    #mecanismo de lock END
    #-----------------------
    lock.lockOUT("Reco_Manos")

if __name__ == "__main__":
    midict={"mode": "parental"}
    print(init(midict))
    print(executeChallenge())
