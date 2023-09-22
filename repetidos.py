import numpy as np


def contar_numero_en_lista(lista, numero):# se crea la función contar_numero_en_lista con los parámetros lista y numero
    contador = 0# se inicializa la variable contador en 0
    for elemento in lista:# se recorre la lista
        if elemento == numero:# se compara si el elemento es igual al número
            contador += 1# se incrementa el contador en 1
    return contador# se retorna el valor del contador

# Ejemplo de uso
lista_enteros = [2, 4, 2, 6, 8, 2, 10, 2]# se inicializa la lista
numero_buscar = 2# se inicializa el número a buscar
resultado = contar_numero_en_lista(lista_enteros, numero_buscar)# se llama a la función contar_numero_en_lista
print(f"El número {numero_buscar} aparece {resultado} veces en la lista.")# se imprime el resultado

# Ejemplo de uso con numpy
cantidad_maxima_de_numeros = 600
rango_minimo = 1
rango_maximo = 500

lista_enteros = np.random.randint(rango_minimo, rango_maximo, cantidad_maxima_de_numeros)# se inicializa la lista con números aleatorios
numero_buscar = input(f"Ingrese un número entre {rango_minimo} y {rango_maximo}: ")# se pide al usuario que ingrese un número
resultado = contar_numero_en_lista(lista_enteros, int(numero_buscar))# se llama a la función contar_numero_en_lista
print(f"El número {numero_buscar} aparece {resultado} veces en la lista.")# se imprime el resultado