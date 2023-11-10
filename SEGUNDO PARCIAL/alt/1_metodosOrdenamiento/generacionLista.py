# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 21:35:20 2023

@author: callo
"""

import random as rn

def crear_lista(longitud):
    lista=[]
    for i in range(0,longitud):
        lista.append(rn.randint(0,600))
    return lista

if __name__=="__main__":
    lista=crear_lista(2000)
    print(lista)

    with open("promedioQS.txt", "w") as f:
        for s in lista:
            f.write(str(s) +"\n")
        
    f.close()