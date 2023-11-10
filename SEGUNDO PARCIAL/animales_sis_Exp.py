import random

# Variables
H = "HOMBRE"
G = "GALLINA"
Z = "ZORRO"
M = "MAIZ"
D = "Derecha"
I = "Izquierda"
Bandera = 0

# Conjunto de reglas (formato: (antecedentes, consecuencia))
reglas_izquierda = [
    ({H: D}, "El hombre cruza el río solo"),  # Regla 1i: El hombre cruza solo
    ({H: D, G: D}, "El hombre cruza el río con la gallina"),  # Regla 2i: El hombre y la gallina cruzan
    ({H: D, Z: D}, "El hombre cruza el río con el zorro"),  # Regla 3i: El hombre y el zorro cruzan
    ({H: D, M: D}, "El hombre cruza el río solo con el maíz"),  # Regla 4i: El hombre y el maiz cruzan
    ({H: D, G: D}, "El hombre cruza el río con la gallina"),  # Regla 5i: El hombre y la gallina cruzan
]

reglas_derecha = [
    ({H: I}, "El hombre regresa solo a la orilla izquierda"),  # Regla 1d: El hombre regresa solo
    ({H: I, G: I}, "El hombre regresa a la orilla izquierda con la gallina"),  # Regla 2d: El hombre y la gallina regresan
    ({H: I, Z: I}, "El hombre regresa a la orilla izquierda con el zorro"),  # Regla 3d: El hombre y el zorro regresan
    ({H: I, M: I}, "El hombre regresa a la orilla izquierda con el maiz"),  # Regla 4d: El hombre y el maiz regresan
    ({H: I}, "El hombre regresa solo a la orilla izquierda"),  # Regla 5d: El hombre regresa solo
]

# Reglas extras
reglas_extras = [
    lambda hechos: hechos[G] != D or hechos[Z] != D or hechos[H] != I,  # El zorro no debe quedarse con la gallina sin el hombre
    lambda hechos: hechos[G] != D or hechos[M] != D or hechos[H] != I,  # La gallina no debe quedarse sola con el maíz sin el hombre
    lambda hechos: hechos[G] != I or hechos[Z] != I or hechos[H] != D,  # El zorro no debe quedarse con la gallina sin el hombre
    lambda hechos: hechos[G] != I or hechos[M] != I or hechos[H] != D,  # La gallina no debe quedarse sola con el maíz sin el hombre
]

# Función para aplicar una regla y actualizar los hechos
def aplicar_regla(hechos, regla):
    antecedentes, consecuencia = regla
    nuevos_hechos = hechos.copy()
    nuevos_hechos.update(antecedentes)
    return nuevos_hechos, consecuencia

# Función para verificar las reglas extras
def verificar_reglas_extras(hechos):
    for regla_extra in reglas_extras:
        if not regla_extra(hechos):
            return False
    return True

# Conjunto de hechos iniciales
hechos = {H: I, G: I, Z: I, M: I}

objetivo = {H: D, G: D, Z: D, M: D}

# Solución del acertijo
print("Resolviendo el acertijo del hombre, la gallina, el zorro y el maíz:")
print("Estado inicial: ", {H: I, G: I, Z: I, M: I})
print()

while hechos != objetivo:
    if Bandera == 0:
        regla = random.choice(reglas_izquierda)
    else:
        regla = random.choice(reglas_derecha)
    
    hechos, consecuencia = aplicar_regla(hechos, regla)
    print(f"Regla seleccionada: {consecuencia}")

    print(hechos)
    print()

    if not verificar_reglas_extras(hechos):
        print("Se incumplió una regla general.")
        hechos = {H: I, G: I, Z: I, M: I}
        Bandera = 0
        print("Reiniciando recorrido.")
        print("--------------------------------------------------------")
        print()
    else:
        Bandera = 1 - Bandera  # Cambiar la bandera

print("¡El acertijo está resuelto!")