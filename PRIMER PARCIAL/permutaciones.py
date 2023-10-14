def generate_permutations(elements):# se crea la funcion
    if len(elements) == 0:# se compara si el tamaño del arreglo es 0
        return [[]]# se retorna un arreglo vacio

    first_element = elements[0]# se obtiene el primer elemento del arreglo
    remaining_elements = elements[1:]# se obtienen los elementos restantes del arreglo
    permutations_without_first = generate_permutations(remaining_elements)# se llama a la función recursivamente

    all_permutations = []# se crea un arreglo vacio
    for permutation in permutations_without_first:# se recorre el arreglo
        for i in range(len(permutation) + 1):# se recorre el arreglo
            new_permutation = permutation[:i] + [first_element] + permutation[i:]# se crea una nueva permutación
            all_permutations.append(new_permutation)# se agrega la nueva permutación al arreglo

    return all_permutations# se retorna el arreglo

# Ejemplo de uso
input_elements = [1, 2, 3]# se inicializa el arreglo
permutations = generate_permutations(input_elements)# se llama a la función
for p in permutations:# se recorre el arreglo
    print(p)
print(permutations)


from itertools import permutations# se importa la libreria itertools para obtener las permutaciones

def generate_permutations(elements):
    all_permutations = list(permutations(elements))# se obtienen todas las permutaciones
    return all_permutations

# Ejemplo de uso
input_elements = [1, 2, 3]# se inicializa el arreglo
permutations = generate_permutations(input_elements)
for p in permutations:
    print(p)


def calculate_permutations(n, r):# se crea la función calculate_permutations con los parámetros n y r que son el número total de elementos y el número de elementos tomados de r en r
    if n < r:# se compara si n es menor que r
        return 0# se retorna 0

    result = 1# se inicializa la variable result en 1
    for i in range(n, n - r, -1):# se recorre el arreglo
        result *= i# se multiplica el valor de result por el valor de i
    return result# se retorna el valor de result

if __name__ == "__main__":

    # Ejemplo de uso
    n = 5  # Número total de elementos
    r = 3  # Elementos tomados de r en r
    permutations = calculate_permutations(n, r)
    print(f"El número de permutaciones posibles de {n} elementos tomados de {r} en {r} es {permutations}.")
