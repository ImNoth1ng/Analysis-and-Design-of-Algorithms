import csv
import time
import numpy as np

import ordenamientos as ord
# Función para generar una lista de datos aleatorios
def generar_datos(cantidad):
    cantidad = np.random.randint(0, 1000, cantidad)
    return cantidad

# Función para escribir en el archivo CSV
def escribir_csv(tiempo, cantidad_datos, algoritmo,nombre):
    with open(nombre_archivo, mode='a', newline='') as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)
        escritor_csv.writerow([cantidad_datos, tiempo])

def generar_csv(datos, algoritmo, pasos, nombre):
    for cantidad_datos in range(pasos, len(datos) + pasos, pasos):
        datos_ordenados = datos[:cantidad_datos].copy()

        inicio_tiempo = time.time()
        if algoritmo == 1:#bubble sort
            ord.bubble_sort(datos_ordenados)
            algoritmo_nombre = "burbuja"
        elif algoritmo == 2:#insertion sort
            ord.insertion_sort(datos_ordenados)
            algoritmo_nombre = "insercion"
        elif algoritmo == 3:#selection sort
            ord.selection_sort(datos_ordenados)
            algoritmo_nombre = "seleccion"
        elif algoritmo == 4:#merge sort
            ord.merge_sort(datos_ordenados)
            algoritmo_nombre = "mezcla"
        elif algoritmo == 5:#quick sort
            ord.quick_sort(datos_ordenados)
            algoritmo_nombre = "rapido"
        fin_tiempo = time.time()


        tiempo_transcurrido = fin_tiempo - inicio_tiempo

        print(f"Datos ordenados: {cantidad_datos}, Tiempo: {tiempo_transcurrido} segundos")

        if cantidad_datos % pasos == 0:
            escribir_csv(tiempo_transcurrido, cantidad_datos, algoritmo, nombre)
        nombre_archivo = nombre
    print("Proceso completado. Los tiempos han sido escritos en " + nombre_archivo)

if __name__ == "__main__":
    cantidad_total_datos = int(input("Escribe la cantidad total de datos a ordenar: "))
    pasos = int(input("Escribe el número de pasos: "))
    algoritmo = int(input("Escribe el número del algoritmo a utilizar:\n1. Bubble sort\n2. Insertion sort\n3. Selection sort\n4. Merge sort\n5. Quick sort\n ----> "))
    nombre = str(input("Escribe el nombre del archivo donde se guardarán los tiempos:\n --------> "))
    if ".csv" in nombre:
        nombre_archivo = nombre
    else:
        nombre_archivo = nombre + ".csv"

    datos = generar_datos(cantidad_total_datos)
    generar_csv(datos, algoritmo, pasos, nombre_archivo)

