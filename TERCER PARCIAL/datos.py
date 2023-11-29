import numpy as np

def leer_datos(archivo):
    lista_datos = []
    with open(archivo, 'r') as archivo:
        for linea in archivo:
            partes = linea.strip().split(',')
            # Convierte las partes numéricas a enteros
            numeros = [int(part) for part in partes[1::2]]
            # Crea una tupla con los valores R, G, B y agrega a la lista
            tupla = tuple(numeros)
            lista_datos.append(tupla)
    lista_datos = [tupla for tupla in lista_datos if tupla]
    return lista_datos

def escalon(n):
    return 1 if n >= 0 else 0

def entrenar_perceptron(datos_entrada, pesos, b, lamda):
    epocas = 0
    error = True
    while error:
        epocas += 1
        print("Época:", epocas)
        error = False
        for k, y in datos_entrada:
            n = escalon(np.dot(k, pesos) + b)
            if n != y:
                print("¡Hay ajuste!")
                error = True
                e = y - n
                delta_b = -lamda * e
                print("b:", b, "e:", e, "delta:", delta_b)
                for i in range(len(k)):
                    delta_w = lamda * e * k[i]
                    pesos[i] = pesos[i] + delta_w
                    print("Peso", i, ":", pesos[i])
            else:
                print("No hay ajuste.")
    return pesos, b, epocas

def clasificar(entrada, pesos, b):
    return escalon(np.dot(entrada, pesos) + b)

if __name__ == "__main__":
    manzana = leer_datos('NuevaManzana1.txt')
    limon = leer_datos('Limon1.txt')
    mandarina = leer_datos('NuevaMandarina1.txt')

    # Agregar etiquetas a los datos
    manzana = [(tupla, 1) for tupla in manzana]
    limon = [(tupla, 2) for tupla in limon]
    mandarina = [(tupla, 3) for tupla in mandarina]

    # Combina los conjuntos de datos
    datos_entrada = manzana + limon + mandarina

    # Inicialización de pesos y bias para el perceptrón 1
    pesos1 = [0.5, 0.5]
    b1 = 1
    lamda1 = 0.6

    # Entrenar perceptrón 1
    pesos1, b1, epocas1 = entrenar_perceptron(datos_entrada, pesos1, b1, lamda1)

    # Inicialización de pesos y bias para el perceptrón 2
    pesos2 = [0.5, 0.5]
    b2 = 1
    lamda2 = 0.6

    # Entrenar perceptrón 2
    pesos2, b2, epocas2 = entrenar_perceptron(datos_entrada, pesos2, b2, lamda2)

    # Resultados del perceptrón 1
    print("----------------")
    print("Pesos finales perceptrón 1:", pesos1)
    print("Bias final perceptrón 1:", b1)
    print("Épocas de entrenamiento perceptrón 1:", epocas1)

    # Resultados del perceptrón 2
    print("----------------")
    print("Pesos finales perceptrón 2:", pesos2)
    print("Bias final perceptrón 2:", b2)
    print("Épocas de entrenamiento perceptrón 2:", epocas2)

    # Pruebas
    print("----------------")
    print("Probando perceptrón 1 en (1, 0):", clasificar((1, 0), pesos1, b1))
    print("Probando perceptrón 1 en (0, 1):", clasificar((0, 1), pesos1, b1))
    print("Probando perceptrón 2 en (1, 0):", clasificar((1, 0), pesos2, b2))
    print("Probando perceptrón 2 en (0, 1):", clasificar((0, 1), pesos2, b2))
