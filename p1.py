#algoritmo babilonico para raiz quadrada

x = print("Ingresa un numero positivo: ")
x = float(input())

def raiz(x):
    r = x
    while r*r > x:
        r = (r + x/r) / 2
    return r

print("raiz quadrada de x:")
print(raiz(x))
