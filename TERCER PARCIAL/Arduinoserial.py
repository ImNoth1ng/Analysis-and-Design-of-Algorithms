# codigo para la comunicacion serial con el arduino y python
#Librerias
import serial
import time

#Creamos el objeto Serial
arduino = serial.Serial('COM4', 9600)
time.sleep(2)#Esperamos 2 segundos para que se inicialice el puerto

#Mostramos las opciones
print("Mistrando datos del arduino")

#Creamos un ciclo infinito
while True:
    #Leemos y convertimos a cadena el valor leido
    dato = str(arduino.readline())
    #Mostramos el valor leido y eliminamos el salto de linea del final
    print(dato)
    #Hacemos una pausa de medio segundo
    time.sleep(1)
    dato = "" #Limpiamos la variable dato

