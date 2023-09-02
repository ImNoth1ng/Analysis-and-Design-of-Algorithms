def generate_permutations(elements):
    if len(elements) == 0:
        return [[]]

    first_element = elements[0]
    remaining_elements = elements[1:]
    permutations_without_first = generate_permutations(remaining_elements)

    all_permutations = []
    for permutation in permutations_without_first:
        for i in range(len(permutation) + 1):
            new_permutation = permutation[:i] + [first_element] + permutation[i:]
            all_permutations.append(new_permutation)

    return all_permutations

# Ejemplo de uso
input_elements = [1, 2, 3]
permutations = generate_permutations(input_elements)
for p in permutations:
    print(p)
print(permutations)


from itertools import permutations

def generate_permutations(elements):
    all_permutations = list(permutations(elements))
    return all_permutations

# Ejemplo de uso
input_elements = [1, 2, 3]
permutations = generate_permutations(input_elements)
for p in permutations:
    print(p)


def calculate_permutations(n, r):
    if n < r:
        return 0

    result = 1
    for i in range(n, n - r, -1):
        result *= i
    return result

if __name__ == "__main__":

    # Ejemplo de uso
    n = 5  # Número total de elementos
    r = 3  # Elementos tomados de r en r
    permutations = calculate_permutations(n, r)
    print(f"El número de permutaciones posibles de {n} elementos tomados de {r} en {r} es {permutations}.")
