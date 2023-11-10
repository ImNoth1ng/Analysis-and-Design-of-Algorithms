# -*- coding: utf-8 -*-

lista=[1,2,3,4,5]

import copy
from time import time
import random as rn
import oord
import ordenamientosConfi as oc

def crear_lista(longitud):
    lista=[]
    for i in range(0,longitud):
        lista.append(rn.randint(0,200))
    return lista

if __name__=="__main__":
    lista=crear_lista(500)
    temp=[]
    x=100
    z = len(lista)
    print(lista)
    for i in range(100,501,100):
        lista_nueva=copy.deepcopy(lista[:x])
        inicio_tiempo=time()
        oord.burbuja(lista_nueva)
        #oord.quicksort(lista)
        #oord.seleccion(lista)
        oord.insercion(lista_nueva)
        #oc.metodo_burbuja(lista)
        transc=time()-inicio_tiempo
        record=str(x) + ";"+format(transc,'.5f')+"\n"
        temp.append(record)
        oord.graba(temp)
        x=x+100
    
    print(lista_nueva)
#asi con el metodo de insercion; seleccion; mezcla y quick sort