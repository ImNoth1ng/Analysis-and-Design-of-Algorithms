import numpy as np
import copy as cp

def Num_rand(cantidad_maxima_de_numeros, rango_minimo, rango_maximo):
    lista_enteros = np.random.randint(rango_minimo, rango_maximo, cantidad_maxima_de_numeros)
    return lista_enteros

#Algoritmos de ordenamiento que reciben un arreglo de números enteros y retornan el arreglo ordenado
#bubble sort
def bubble_sort(arr):
    n = len(arr)#n es la longitud del arreglo
    for i in range(n):
        for j in range(0, n - i - 1):#se recorre el arreglo de 0 a n-i-1
            if arr[j] > arr[j+1] :#si el elemento en la posición j es mayor al elemento en la posición j+1
                arr[j], arr[j + 1] = arr[j + 1], arr[j]#se intercambian los elementos
    return arr#se retorna el arreglo ordenado

#insertion sort
def insertion_sort(arr):#se recibe un arreglo
    for i in range(1, len(arr)):#se recorre el arreglo desde la posición 1 hasta la longitud del arreglo
        key = arr[i]#se guarda el elemento en la posición i en la variable key
        j = i - 1#se guarda la posición anterior a i en la variable j
        while j >= 0 and key < arr[j]:#mientras j sea mayor o igual a 0 y el elemento en la posición key sea menor al elemento en la posición j
            arr[j + 1] = arr[j]#se intercambian los elementos
            j -= 1#se disminuye en 1 la variable j
        arr[j + 1] = key#se guarda el elemento en la posición key en la posición j+1
    return arr#se retorna el arreglo ordenado
#selection sort

def selection_sort(arr):#se recibe un arreglo
    for i in range(len(arr)):#se recorre el arreglo desde la posición 0 hasta la longitud del arreglo
        min_idx = i#se guarda la posición i en la variable min_idx
        for j in range(i + 1, len(arr)):#se recorre el arreglo desde la posición i+1 hasta la longitud del arreglo
            if arr[j] < arr[min_idx]:#si el elemento en la posición j es menor al elemento en la posición min_idx
                min_idx = j#se guarda la posición j en la variable min_idx
        arr[i], arr[min_idx] = arr[min_idx], arr[i]#se intercambian los elementos
    return arr#se retorna el arreglo ordenado

#merge sort
def merge_sort(arr):#se recibe un arreglo
    if len(arr) <= 1:#si la longitud del arreglo es menor o igual a 1
        return arr#se retorna el arreglo

    def merge(left, right):#se define la función merge que recibe dos arreglos
        result = []#se crea un arreglo vacío
        i = j = 0#se inicializan las variables i y j en 0

        while i < len(left) and j < len(right):#mientras i sea menor a la longitud del arreglo left y j sea menor a la longitud del arreglo right
            if left[i] < right[j]:#si el elemento en la posición i del arreglo left es menor al elemento en la posición j del arreglo right
                result.append(left[i])#se agrega el elemento en la posición i del arreglo left al arreglo result
                i += 1#se aumenta en 1 la variable i
            else:
                result.append(right[j])#se agrega el elemento en la posición j del arreglo right al arreglo result
                j += 1#se aumenta en 1 la variable j

        result.extend(left[i:])#se agrega al arreglo result los elementos del arreglo left desde la posición i hasta el final
        result.extend(right[j:])#se agrega al arreglo result los elementos del arreglo right desde la posición j hasta el final
        return result#se retorna el arreglo result

    mid = len(arr) // 2#se guarda la longitud del arreglo dividida en 2 en la variable mid
    left = arr[:mid]#se guarda en el arreglo left los elementos desde la posición 0 hasta la posición mid
    right = arr[mid:]#se guarda en el arreglo right los elementos desde la posición mid hasta el final

    left = merge_sort(left)#se llama a la función merge_sort con el arreglo left
    right = merge_sort(right)#se llama a la función merge_sort con el arreglo right

    return list(merge(left, right))#se retorna el arreglo ordenado

#quick sort
def quick_sort(arr):#se recibe un arreglo
    if len(arr) <= 1:#si la longitud del arreglo es menor o igual a 1
        return arr#se retorna el arreglo

    pivot = arr[len(arr) // 2]#se guarda el elemento en la posición len(arr)//2 en la variable pivot
    left = [x for x in arr if x < pivot]#se guarda en el arreglo left los elementos del arreglo arr que sean menores al elemento en la posición len(arr)//2
    middle = [x for x in arr if x == pivot]#se guarda en el arreglo middle los elementos del arreglo arr que sean iguales al elemento en la posición len(arr)//2
    right = [x for x in arr if x > pivot]#se guarda en el arreglo right los elementos del arreglo arr que sean mayores al elemento en la posición len(arr)//2

    return quick_sort(left) + middle + quick_sort(right)#se retorna el arreglo ordenado



if __name__ == "__main__":
    num = np.array(Num_rand(100, 1, 100))
    numInsertion = cp.deepcopy(num)
    numBubble = cp.deepcopy(num)
    numSelection = cp.deepcopy(num)
    numMerge = cp.deepcopy(num)
    numQuick = cp.deepcopy(num)

    print("Arreglo desordenado: ", num)

    sortedBubble = bubble_sort(numBubble)
    print("Arreglo ordenado con Bubble Sort: ", sortedBubble)

    sortedInsertion = insertion_sort(numInsertion)
    print("Arreglo ordenado con Insertion Sort: ", sortedInsertion)

    sortedSelection = selection_sort(numSelection)
    print("Arreglo ordenado con Selection Sort: ", sortedSelection)

    sortedMerge = merge_sort(numMerge)
    print("Arreglo ordenado con Merge Sort: ", sortedMerge)

    sortedQuick = quick_sort(numQuick)
    print("Arreglo ordenado con Quick Sort: ", sortedQuick)

    #comparación de de igualdad entre los arreglos ordenados
    if np.array_equal(sortedBubble, sortedInsertion) and np.array_equal(sortedBubble, sortedSelection) and np.array_equal(sortedBubble, sortedMerge) and np.array_equal(sortedBubble, sortedQuick):
        print("Todos los algoritmos ordenaron el arreglo de igual manera")
