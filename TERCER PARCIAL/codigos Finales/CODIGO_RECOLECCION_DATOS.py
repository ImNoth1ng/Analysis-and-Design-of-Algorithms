import os
import serial
import time

def arduino_read_data(file):
    encoding = "utf-8"
    #Iniciando la conexion serial
    arduinoPort = serial.Serial('COM7',9600,timeout=1) #Cambiar la entrada del arduino en Windows
    f = open(file,"w") #Abre el archivo dependiendo del valor que se manda, nombre el archivo txt

    #Retardo para establecer la conexion serial
    time.sleep(.3)  #Retardo para leer los datos, preferentemente debe ser igual al delay del código del arduino
    for i in range (500):
        getSerialValue = arduinoPort.readline()
        print(getSerialValue)
        f.write(getSerialValue.decode(encoding))

    #Cerrando el puerto serial
    arduinoPort.close()
    f.close()
	

arduino_read_data("Limon2.txt")
#Guardando los datos en un archivo.