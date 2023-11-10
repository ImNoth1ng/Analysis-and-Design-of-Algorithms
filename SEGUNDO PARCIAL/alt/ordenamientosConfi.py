#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 21:37:36 2023

@author: luis
"""

def crea_archivo(nombre):
    archivo=open(nombre + ".csv", "w")
    archivo.write(nombre + "\nN;Tiempo\n")
    archivo.close()
    global nmm
    nmm =nombre + ".csv"

def graba(cont):
    with open(nmm, "a") as archivo:
        archivo.writelines(cont)

def metodo_burbuja(lista):
    crea_archivo("BURBUJA")
    for i in range(1, len(lista)):
        for j in range(0, len(lista)-i):
            if(lista[j]>lista[j+1]):
                aux=lista[j]
                lista[j]=lista[j+1]
                lista[j+1]=aux


def metodo_insercion_directa(lista):
    crea_archivo("INSERC_DIRECTA")
    for j in range(1, len(lista)):
        i=j-1
        x=lista[j]
        while (x<lista[i] and i>=0):
            lista[i+1]=lista[i]
            i=i-1
        lista[i+1]=x

#------------------------------------
def particion_quick(lista):
    crea_archivo("QuickSortPart")
    pivote=lista[0]
    menores=[]
    mayores=[]
    
    for i in range(1, len(lista)):
        if lista[i]<pivote:
            menores.append(lista[i])
        else:
            mayores.append(lista[i])
#-------------------------------------

def quicksort(lista):
    crea_archivo("QuickSort")
    if len(lista)<2:
        return lista
    menores, pivote, mayores=particion_quick(lista)
    return quicksort(menores)+[pivote]+quicksort(mayores)

#----------------------------------------------

def seleccion(lista):
    crea_archivo("seleccion")
    longitud=len(lista)
    for i in range(longitud-1):
        menor=i
        print("El indice actual para comparar es: ",menor)
        for j in range(i+1, longitud):
            if lista[j]<lista[menor]:
                menor=j
                print("Recorriendo la lista. El indice menor es: ", menor)
        temporal= lista[menor]
        lista[menor]= lista[i]
        lista[i]= temporal
        print("Cambiamos el elemento: ", lista[menor], "por el elemento", lista[i])


def merge_sort(lista):
    crea_archivo("merge")
    if len(lista)>1:
        mitad=len(lista)//2
        prime_mitad= lista[:mitad]
        second_mitad= lista[mitad:]
        
        merge_sort(prime_mitad)
        merge_sort(second_mitad)
        i=0
        j=0
        k=0
        
        while i<len(prime_mitad) and j<len(second_mitad):
            if prime_mitad[i]<second_mitad[j]:
                lista[k]= prime_mitad[i]
                i+=1
            else:
                lista[k]= second_mitad[j]
                j+=1
            k+=1
                
        while i<len(prime_mitad):
            lista[k]= prime_mitad[i]
            i+=1
            k+=1
            
        while j<len(second_mitad):
            lista[k]= second_mitad[j]
            j+=1
            k+=1
