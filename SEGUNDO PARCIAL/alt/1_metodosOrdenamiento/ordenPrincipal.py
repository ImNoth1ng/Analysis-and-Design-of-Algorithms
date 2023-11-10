# -*- coding: utf-8 -*-

lista=[1,2,3,4,5]

import copy
from time import time
import oord

def leerlista(file):
    lista = []
    with open(file, "r") as f:
        for line in f:
            lista.append(int(line.strip()))
    f.close
    return lista
    

if __name__=="__main__":
    lista=leerlista("peorBurbuja.txt")
    temp=[]
    x=100
    z = len(lista)
    #print(lista)
    for i in range(100,5001,100):
        lista_nueva=copy.deepcopy(lista[:x])
        inicio_tiempo=time()
        #oord.burbuja(lista_nueva)
        #oord.insercion(lista_nueva)
        oord.seleccion(lista_nueva)
        #oord.quicksort(lista_nueva)
        transc=time()-inicio_tiempo
        record=str(x) + ";"+format(transc,'.5f')+"\n"
        temp.append(record)
        oord.graba(temp)
        x=x+100
    
    
    #print(lista_nueva)
#asi con el metodo de insercion; seleccion; mezcla y quick sort