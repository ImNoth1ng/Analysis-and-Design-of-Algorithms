# codigo para la comunicacion serial con el arduino y python
#Librerias
import serial
import time

#Creamos el objeto Serial
arduino = serial.Serial('COM4', 9600)
time.sleep(2)#Esperamos 2 segundos para que se inicialice el puerto

#Mostramos las opciones
print("Presione 1 para encender el LED y 0 para apagar el LED")

#Creamos un ciclo infinito
while True:
    #Solicitamos la opcion al usuario
    opcion = input("---> ")
    #Si la opcion es 1
    if opcion == '1':
        #Enviamos datos de tipo string por el puerto serial
        arduino.write(b'23.23;42.42;565.6')
        print("Mensaje enviado")
    elif opcion == '0':
        arduino.close()#Cerramos el puerto serial
        print("Puerto cerrado")
        break
