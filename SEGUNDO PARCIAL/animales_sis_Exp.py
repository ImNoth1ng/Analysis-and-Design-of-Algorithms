import random
import copy

# Variables
H = "HOMBRE"
G = "GALLINA"
L = "LOBO"
M = "MAIZ"
D = "Derecha"
I = "Izquierda"
Bandera = 0 #Bandera para saber si se está moviendo a la izquierda o a la derecha

# Conjunto de hechos iniciales
hechos = {H: I, G: I, L: I, M: I} #estado inicial

objetivo = {H: D, G: D, L: D, M: D} #estado final (objetivo)

recorrido = 1 #contador de recorridos para saber si se está ciclando

# Reglas del acertijo (formato: (antecedentes, consecuencia))
reglas_izquierda = [
    [{H: D}, "El hombre cruza el río solo"],  # Regla 1i: El hombre cruza solo
    [{H: D, G: D}, "El hombre cruza el río con la gallina"],  # Regla 2i: El hombre y la gallina cruzan
    [{H: D, L: D}, "El hombre cruza el río con el lobo"],  # Regla 3i: El hombre y el Lobos cruzan
    [{H: D, M: D}, "El hombre cruza el río con el maíz"],  # Regla 4i: El hombre y el maiz cruzan
    [{H: D, G: D}, "El hombre cruza el río con la gallina"],  # Regla 5i: El hombre y la gallina cruzan
]

reglas_derecha = [
    [{H: I}, "El hombre regresa solo a la orilla izquierda"],  # Regla 1d: El hombre regresa solo
    [{H: I, G: I}, "El hombre regresa a la orilla izquierda con la gallina"],  # Regla 2d: El hombre y la gallina regresan
    [{H: I, L: I}, "El hombre regresa a la orilla izquierda con el lobo"],  # Regla 3d: El hombre y el Lobos regresan
    [{H: I, M: I}, "El hombre regresa a la orilla izquierda con el maiz"],  # Regla 4d: El hombre y el maiz regresan
    [{H: I}, "El hombre regresa solo a la orilla izquierda"],  # Regla 5d: El hombre regresa solo
]

# Reglas extras para evitar que se incumplan las reglas generales
reglas_extras = [
    lambda hechos: hechos[G] != D or hechos[L] != D or hechos[H] != I,  # El Lobos no debe quedarse con la gallina sin el hombre
    lambda hechos: hechos[G] != D or hechos[M] != D or hechos[H] != I,  # La gallina no debe quedarse sola con el maíz sin el hombre
    lambda hechos: hechos[G] != I or hechos[L] != I or hechos[H] != D,  # El Lobos no debe quedarse con la gallina sin el hombre
    lambda hechos: hechos[G] != I or hechos[M] != I or hechos[H] != D,  # La gallina no debe quedarse sola con el maíz sin el hombre
]

# Función para aplicar una regla y actualizar los hechos
def aplicar_regla(hechos, regla):
    antecedentes, consecuencia = regla #antecedentes es una lista de hechos, consecuencia es un string
    nuevos_hechos = hechos.copy() #copiamos los hechos actuales
    nuevos_hechos.update(antecedentes)#actualizamos los hechos con los antecedentes de la regla
    return nuevos_hechos, consecuencia#regresamos los nuevos hechos y la consecuencia de la regla

# Función para verificar las reglas extras
def verificar_reglas_extras(hechos):#recibe los hechos actuales
    for regla_extra in reglas_extras:#para cada regla extra
        if not regla_extra(hechos):#si no se cumple la regla extra
            return False#regresamos falso para indicar que no se cumple
    return True#si se cumplieron todas las reglas extras, regresamos verdadero


# Solución del acertijo
if __name__ == "__main__":
    print("Resolviendo el acertijo del hombre, la gallina, el Lobos y el maíz:")#imprimimos el acertijo
    print("Estado inicial: ", {H: I, G: I, L: I, M: I})#imprimimos el estado inicial
    x=copy.deepcopy(reglas_izquierda)#copiamos las reglas para no modificar las originales y poder reiniciar el recorrido
    y=copy.deepcopy(reglas_derecha)
    print(x)
    print("Recorrido: ", recorrido)#imprimimos el recorrido
    while hechos != objetivo:
        if Bandera == 0:
            if not x:#si la lista de reglas izquierdas está vacía
                print("Una de las listas se vació. Reiniciando recorrido.")
                print("--------------------------------------------------------")
                recorrido = recorrido + 1
                print("Recorrido: ", recorrido)
                hechos = {H: I, G: I, L: I, M: I}#reiniciamos los hechos
                Bandera = 0#reiniciamos la bandera
                x = copy.deepcopy(reglas_izquierda)#copiamos las reglas para no modificar las originales y poder reiniciar el recorrido
                y = copy.deepcopy(reglas_derecha)#copiamos las reglas para no modificar las originales y poder reiniciar el recorrido
                continue
            regla = random.choice(x)#seleccionamos una regla al azar
            x.remove(regla)#la eliminamos de la lista de reglas izquierdas
        else:
            if not y:#si la lista de reglas derechas está vacía
                print("Una de las listas se vació. Reiniciando recorrido.")#imprimimos que se vació una lista
                print("--------------------------------------------------------")
                recorrido = recorrido + 1#incrementamos el recorrido
                print("Recorrido: ", recorrido)
                hechos = {H: I, G: I, L: I, M: I}#reiniciamos los hechos
                Bandera = 0
                x = copy.deepcopy(reglas_izquierda)
                y = copy.deepcopy(reglas_derecha)
                continue
            regla = random.choice(y)
            y.remove(regla)

        hechos, consecuencia = aplicar_regla(hechos, regla)

        print(hechos)
        print()


        if not verificar_reglas_extras(hechos):
            print("Se incumplió una regla general.")
            recorrido = recorrido + 1
            hechos = {H: I, G: I, L: I, M: I}
            Bandera = 0
            print("Reiniciando recorrido.")
            print("--------------------------------------------------------")
            print("Recorrido: ", recorrido)
            x=copy.deepcopy(reglas_izquierda)
            y=copy.deepcopy(reglas_derecha)
        else:
            Bandera = 1 - Bandera  # Cambiar la bandera
            

    print("¡El acertijo está resuelto!")
