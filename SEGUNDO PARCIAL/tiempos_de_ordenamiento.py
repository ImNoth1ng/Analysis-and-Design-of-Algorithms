import csv
import time
import numpy as np
import os

import ordenamientos as ord

# Función para generar una lista de datos aleatorios
def generar_datos(cantidad):
    cantidad = np.random.randint(0, 1000, cantidad)
    return cantidad

# Función para escribir en el archivo CSV
def escribir_csv(tiempo, cantidad_datos, algoritmo, nombre):
    with open(nombre, mode='a', newline='') as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)
        escritor_csv.writerow([cantidad_datos, tiempo])

def generar_csv(datos, algoritmo, pasos, nombre):
    for cantidad_datos in range(pasos, len(datos) + pasos, pasos):
        datos_ordenados = datos[:cantidad_datos].copy()

        inicio_tiempo = time.time()
        if algoritmo == 1:  # bubble sort
            ord.bubble_sort(datos_ordenados)
            algoritmo_nombre = "burbuja"
        elif algoritmo == 2:  # insertion sort
            ord.insertion_sort(datos_ordenados)
            algoritmo_nombre = "insercion"
        elif algoritmo == 3:  # selection sort
            ord.selection_sort(datos_ordenados)
            algoritmo_nombre = "seleccion"
        elif algoritmo == 4:  # merge sort
            ord.merge_sort(datos_ordenados)
            algoritmo_nombre = "mezcla"
        elif algoritmo == 5:  # quick sort
            ord.quick_sort(datos_ordenados)
            algoritmo_nombre = "rapido"
        fin_tiempo = time.time()

        tiempo_transcurrido = fin_tiempo - inicio_tiempo

        print(f"Datos ordenados: {cantidad_datos}, Tiempo: {tiempo_transcurrido} segundos")

        if cantidad_datos % pasos == 0:
            escribir_csv(tiempo_transcurrido, cantidad_datos, algoritmo, nombre)

    print(f"Proceso completado. Los tiempos han sido escritos en {nombre}")

if __name__ == "__main__":
    ubicacion_tiempos = "./tiempos"
    os.makedirs(ubicacion_tiempos, exist_ok=True)

    cantidad_total_datos = int(input("Escribe la cantidad total de datos a ordenar: "))
    pasos = int(input("Escribe el número de pasos: "))
    algoritmo = int(input("Escribe el número del algoritmo a utilizar:\n1. Bubble sort\n2. Insertion sort\n3. Selection sort\n4. Merge sort\n5. Quick sort\n6.-TODOS (puede tomar mucho tiempo) ----> "))
    nombre = str(input("Escribe el nombre del archivo donde se guardarán los tiempos (sin extensión): "))
    nombre_archivo = os.path.join(ubicacion_tiempos, f"{nombre}_tiempos.csv")

    datos = generar_datos(cantidad_total_datos)
    if algoritmo == 6:
        for i in range(1, 6):
            if i == 1:
                nombre_archivo = os.path.join(ubicacion_tiempos, f"{nombre}_tiempos_burbuja.csv")
            elif i == 2:
                nombre_archivo = os.path.join(ubicacion_tiempos, f"{nombre}_tiempos_insercion.csv")
            elif i == 3:
                nombre_archivo = os.path.join(ubicacion_tiempos, f"{nombre}_tiempos_seleccion.csv")
            elif i == 4:
                nombre_archivo = os.path.join(ubicacion_tiempos, f"{nombre}_tiempos_mezcla.csv")
            elif i == 5:
                nombre_archivo = os.path.join(ubicacion_tiempos, f"{nombre}_tiempos_rapido.csv")
            generar_csv(datos, i, pasos, nombre_archivo)
    elif algoritmo in range(1, 6):
        generar_csv(datos, algoritmo, pasos, nombre_archivo)
    else:
        print("Algoritmo no válido")