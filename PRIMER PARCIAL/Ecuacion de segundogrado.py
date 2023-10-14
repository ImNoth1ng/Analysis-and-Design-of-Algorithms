#formula general sin bibliotecas
print("Ingresa el valor de a: ")
a = float(input())
print("Ingresa el valor de b: ")
b = float(input())
print("Ingresa el valor de c: ")
c = float(input())

#validado a != 0
if a == 0:
    print("a debe ser diferente de 0")
    exit()

#formula general


def formula(a,b,c):
    x1 = (-b + (b**2 - 4*a*c)**(1/2))/(2*a)
    x2 = (-b - (b**2 - 4*a*c)**(1/2))/(2*a)
    return x1,x2

print("x1 y x2 son:")
print(formula(a,b,c))
