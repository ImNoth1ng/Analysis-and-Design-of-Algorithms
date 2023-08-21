#calculando pi con serie de nilakantha
print("Ingresa el numero de iteraciones: ")
n = int(input())

def pi(n):
    pi = 3
    for i in range(1,n):
        pi += 4/((2*i)*(2*i+1)*(2*i+2))*(-1)**(i+1)
    return pi

print("pi es:")
print(pi(n))