#Programa que grafica los tiempos de ejecución de los algoritmos de ordenamiento de datos
import csv
import matplotlib.pyplot as plt
import os

def leer_csv(nombre):
    with open(nombre, mode='r', newline='') as archivo_csv:
        lector_csv = csv.reader(archivo_csv)
        lista = []
        for linea in lector_csv:
            lista.append(linea)
    return lista
