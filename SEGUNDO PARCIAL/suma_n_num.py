#Programa que suma n numeros positivos
def suma_n_num(a):
    if a > 0:
        return a + (suma_n_num(a-1))
    else:
        return 0

def recorrido_suma(a):
    suma = str(a)#comenzamos la suma con el valor máximo
    for i in range(1,a):#comenzamos desde 1 para no repetir el máximo
        suma= suma +" + " + str(a-i)#agregamos todos los numeros que componen la suma
    suma = suma + " = " + str(suma_n_num(a))#llamamos la funcion recursiva para añadir el resultado a la suma
    return suma#regresamos la suma completa

if __name__ == "__main__":
    a = int(input("Escribe un numero entero positivo para obtener la suma de los numeros enteros positivos que lo anteceden:"))
    prueba = recorrido_suma(a)

    print(prueba)