import numpy as np


def contar_numero_en_lista(lista, numero):
    contador = 0
    for elemento in lista:
        if elemento == numero:
            contador += 1
    return contador

# Ejemplo de uso
lista_enteros = [2, 4, 2, 6, 8, 2, 10, 2]
numero_buscar = 2
resultado = contar_numero_en_lista(lista_enteros, numero_buscar)
print(f"El número {numero_buscar} aparece {resultado} veces en la lista.")

# Ejemplo de uso con numpy
cantidad_maxima_de_numeros = 600
rango_minimo = 1
rango_maximo = 500

lista_enteros = np.random.randint(rango_minimo, rango_maximo, cantidad_maxima_de_numeros)
numero_buscar = input(f"Ingrese un número entre {rango_minimo} y {rango_maximo}: ")
resultado = contar_numero_en_lista(lista_enteros, int(numero_buscar))
print(f"El número {numero_buscar} aparece {resultado} veces en la lista.")