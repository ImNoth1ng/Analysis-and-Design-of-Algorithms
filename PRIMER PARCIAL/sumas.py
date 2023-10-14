def maxsuma1(s, n):# s es el arreglo y n es el tamaño del arreglo
    suma = [[0] * (n + 1) for _ in range(n + 1)]# se crea una matriz de n+1 x n+1

    for i in range(1, n + 1):
        for j in range(1, i):
            suma[i][j] = suma[i - 1][j] + s[i - 1]# se llena la matriz con la suma de los elementos del arreglo
            suma[i][i] = s[i - 1]# se llena la diagonal con los elementos del arreglo

    # Encontrar el máximo
    max_sum = 0
    for i in range(1, n + 1):# se recorre la matriz
        for j in range(1, i):
            if suma[i][j] > max_sum:
                max_sum = suma[i][j]

    return max_sum# se retorna el valor máximo

def maxsuma2(s, n):# s es el arreglo y n es el tamaño del arreglo
    max_sum = 0# se inicializa la variable max_sum en 0

    for i in range(1, n + 1):# se recorre el arreglo
        suma = s[i - 1]# se inicializa la variable sumaii con el primer elemento del arreglo
        if suma > max_sum:# se compara si sumaii es mayor que max_sum
            max_sum = suma# se asigna el valor de sumaii a max_sum

        for j in range(1, i):
            suma = s[j - 1] + sum(s[j:i])# se suma el elemento j-1 con la suma de los elementos desde j hasta i
            if suma > max_sum:# se compara si sumaii es mayor que max_sum
                max_sum = suma# se asigna el valor de sumaii a max_sum

    return max_sum

def maxsuma3(s, n):
    max_sum = 0# se inicializa la variable max_sum en 0
    suma = 0# se inicializa la variable suma en 0

    for i in range(n):# se recorre el arreglo
        if suma + s[i] > 0:# se compara si la suma de la variable suma con el elemento i del arreglo es mayor que 0
            suma += s[i]# se suma el elemento i del arreglo a la variable suma
        else:
            suma = 0# se asigna 0 a la variable suma

        if suma > max_sum:# se compara si la variable suma es mayor que max_sum
            max_sum = suma# se asigna el valor de suma a max_sum

    return max_sum# se retorna el valor máximo

# Ejemplo de uso
s = [27, 6, -50, 21, -3, 14, 16, -8, 42, 33, -21, 9]# se inicializa el arreglo
n = len(s)# se obtiene el tamaño del arreglo
resultado = maxsuma1(s, n)# se llama a la función maxsuma1
print("La suma máxima 1 es:", resultado)# se imprime el resultado
resultado = maxsuma2(s, n)
print("La suma máxima 2 es:", resultado)
resultado = maxsuma3(s, n)
print("La suma máxima 3 es:", resultado)

