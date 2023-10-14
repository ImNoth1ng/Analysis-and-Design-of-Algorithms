#obteniendo el minimo de iteraciones para que pi sea 3.14159 con un error de 0.00001

def pi(n):
    pi = 3
    for i in range(1,n):
        pi += 4/((2*i)*(2*i+1)*(2*i+2))*(-1)**(i+1)
    return pi
i = 1
cal = 3
for i in range(1,100):
    print(i)
    print(pi(i))

