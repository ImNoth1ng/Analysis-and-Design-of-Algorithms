#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 03:20:28 2023

@author: csjosh
"""

import pandas as pd
import matplotlib.pyplot as plt

if __name__=="__main__":
    datos=pd.read_csv("m1.csv", sep=";")
    datosDos=pd.read_csv("m2.csv", sep=";")
    x=datos.N
    y=datos.Tiempo
    yy=datosDos.Tiempo
    plt.plot(x,y,x,yy)
    plt.xlabel("N")
    plt.ylabel("Tiempo")
    plt.title("burbuja vs seleccion")
    plt.legend(("burbuja","seleccion"))
    plt.grid
    plt.show