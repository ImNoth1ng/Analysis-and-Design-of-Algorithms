# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 09:18:19 2023

@author: callo
"""
def crea_archivo(nombre):
    archivo=open(nombre + ".txt", "w")
    archivo.write(nombre + "\nN;Tiempo\n")
    archivo.close()
    global nmm
    nmm =nombre + ".txt"

def graba(cont):
    with open(nmm, "a") as archivo:
        archivo.writelines(cont)

def burbuja(lista):
    crea_archivo("BURBUJA")
    for i in range(1,len(lista)):
        for j in range(0,len(lista)-i):
            if(lista[j]>lista[j+1]):
                aux=lista[j]
                lista[j]=lista[j+1]
                lista[j+1]=aux

def quicksort(lista):
    crea_archivo("QuickSort")

    if len(lista)<=1:
        return lista
    else:
        piv = lista.pop()
        
    listaMayor=[]
    listaMenor=[]
    
    for item in lista:
        if item>piv:
            listaMayor.append(item)
        else:
            listaMenor.append(item)
    return quicksort(listaMenor) + [piv] + quicksort(listaMayor)
    
def insercion(lista):
 
    # Traverse through 1 to len(arr)
    for i in range(1, len(lista)):
        crea_archivo("Insercion")
        key = lista[i]
 
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >= 0 and key < lista[j] :
                lista[j + 1] = lista[j]
                j -= 1
        lista[j + 1] = key
 
def seleccion(lista):
    crea_archivo("Seleccion")
    tamanyo=len(lista)
    for step in range(tamanyo):
        min_idx = step

        for i in range(step + 1, tamanyo):
         
            # to sort in descending order, change > to < in this line
            # select the minimum element in each loop
            if lista[i] < lista[min_idx]:
                min_idx = i
         
        # put min at the correct position
        (lista[step], lista[min_idx]) = (lista[min_idx], lista[step])

if __name__=="__main__":
    ls=[3,56,7,99,6,1,888,35,37,85]
    seleccion(ls)
    print(ls)
    
        