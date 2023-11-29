import pandas as pd

def escalon(k, pesos, b):
    n = -b
    for i in range(len(k)):
        n = n + (k[i] * pesos[i])
    if n >= 0:
        return 1
    else:
        return 0

def entrenar_perceptron(datos_ent, pesos, b, lamda):
    epocas = 0
    errores = True
    while errores and epocas < 4000:
        epocas = epocas + 1
        print()
        print("Epoca: ", epocas)
        errores = False
        for k, y in datos_ent.items():
            n = escalon(k, pesos, b)
            if n != y:
                print("Hay ajuste")
                print("p1:", k[0], "p2:", k[1], "p3:", k[2])
                errores = True
                e = (y - n)
                delta_b = -(lamda * e)
                print("b:", b, "e", e, "delta_b", delta_b)
                for i in range(len(k)):
                    delta_w = lamda * e * k[i]
                    pesos[i] = pesos[i] + delta_w
                    print("Pesos", i, pesos[i])
            else:
                print("No hay Ajuste")
                print("p1:", k[0], "p2:", k[1], "p3:", k[2])
                e = (y - n)
                delta_b = -(lamda * e)
                print("b:", b, "e", e, "delta_b", delta_b)
    return pesos, b

def clasificar(entrada, pesos, b):
    return escalon(entrada, pesos, b)

def insertar_datos(archivo, archivo2, archivo3):
    # Leemos el contenido de los archivos de texto
    with open(archivo, 'r') as file:
        data = [tuple(map(int, line.strip().split())) for line in file.readlines()]

    with open(archivo2, 'r') as file:
        data2 = [tuple(map(int, line.strip().split())) for line in file.readlines()]

    with open(archivo3, 'r') as file:
        data3 = [tuple(map(int, line.strip().split())) for line in file.readlines()]

    # Convertimos los datos a un formato de diccionario
    dataa = {point: 0 for point in data}
    dataa.update({point: 1 for point in data2})
    dataa.update({point: 0 for point in data3})

    return dataa

if __name__ == "__main__":
    datos_ent = insertar_datos("NuevaManzana1.txt", "Limon1.txt", "NuevaMandarina1.txt")
    pesos = [0.2, 0.6, 0.1]
    b = 0.4
    lamda = 0.2
    pesos, b = entrenar_perceptron(datos_ent, pesos, b, lamda)
    print("-------------")
    print("Pesos finales: ", pesos)
    print("Bias Final: ", b)
    prueba = (45, 60, 92)
    print("Probando perceptron: ", str(prueba) + str(clasificar(prueba, pesos, b)))

    # Bloque adicional de prueba
    prueba1 = (132, 152, 189)
    prueba2 = (100, 50, 30)

    print("UNO: ", str(prueba1) + str(clasificar(prueba1, [42.8, 4.6, -28.9], 0.4)))
    print("DOS: ", str(prueba2) + str(clasificar(prueba2, [-225.6, 123.8, -1.7], 0.4)))
