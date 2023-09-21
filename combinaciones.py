import itertools

def obtener_combinaciones(arreglo):
    combinaciones = []
    for r in range(1, len(arreglo) + 1):
        combinaciones.extend(itertools.combinations(arreglo, r))
    return combinaciones

# Arreglo de ejemplo
arreglo_ejemplo = [1, 2, 3]

# Obtener combinaciones
todas_combinaciones = obtener_combinaciones(arreglo_ejemplo)

# Mostrar las combinaciones obtenidas
print("Todas las combinaciones posibles del arreglo son:")
for combinacion in todas_combinaciones:
    print(combinacion)

print("-----------------------------")

### SIN LIBRERIA ITERTOOLS ###

def obtener_combinaciones(arreglo):
    n = len(arreglo)
    # Lista para almacenar las combinaciones
    combinaciones = []

    def generar_combinaciones(indice, combinacion_actual):
        # Añade la combinación actual a la lista de combinaciones
        combinaciones.append(combinacion_actual[:])

        # Genera combinaciones para cada elemento restante
        for i in range(indice, n):
            combinacion_actual.append(arreglo[i])
            generar_combinaciones(i + 1, combinacion_actual)
            combinacion_actual.pop()

    # Genera las combinaciones
    generar_combinaciones(0, [])

    return combinaciones

# Ejemplo de uso
arreglo = [1, 2, 3]
todas_combinaciones = obtener_combinaciones(arreglo)

# Imprime todas las combinaciones
for combinacion in todas_combinaciones:
    print(combinacion)
