def maxsuma1(s, n):
    suma = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, i):
            suma[i][j] = suma[i - 1][j] + s[i - 1]
            suma[i][i] = s[i - 1]

    # Encontrar el máximo
    max_sum = 0
    for i in range(1, n + 1):
        for j in range(1, i):
            if suma[i][j] > max_sum:
                max_sum = suma[i][j]

    return max_sum

def maxsuma2(s, n):
    max_sum = 0

    for i in range(1, n + 1):
        sumaii = s[i - 1]
        if sumaii > max_sum:
            max_sum = sumaii

        for j in range(1, i):
            sumaji = s[j - 1] + sum(s[j:i])
            if sumaji > max_sum:
                max_sum = sumaji

    return max_sum

def maxsuma3(s, n):
    max_sum = 0
    suma = 0

    for i in range(n):
        if suma + s[i] > 0:
            suma += s[i]
        else:
            suma = 0

        if suma > max_sum:
            max_sum = suma

    return max_sum

# Ejemplo de uso
s = [27, 6, -50, 21, -3, 14, 16, -8, 42, 33, -21, 9]
n = len(s)
resultado = maxsuma1(s, n)
print("La suma máxima 1 es:", resultado)
resultado = maxsuma2(s, n)
print("La suma máxima 2 es:", resultado)
resultado = maxsuma3(s, n)
print("La suma máxima 3 es:", resultado)

