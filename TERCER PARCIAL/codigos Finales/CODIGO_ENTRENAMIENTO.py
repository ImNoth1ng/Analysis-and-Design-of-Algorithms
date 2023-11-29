'''
Código en Python para entrenar un perceptrón que recibe datos de color.

Para efectos de este entrenamiento, los puntos, p1, p2 y p3 se almacenan como una tupla, y
posteriormente, el enlace entre el dato y su correspondiente valor de escalon se almacena
como un diccionario. En este tenor, la sintaxis del tratamiento de datos es la siguiente:

	(p1,p2,p3):Z
	
	Donde:
p1 es el valor entero recibido del sensor correspondiente al color ROJO.
p2 es el valor entero recibido del sensor correspondiente al color VERDE.
p3 es el valor entero recibido del sensor correspondiente al color AZUL.
Z es el valor entero de la función escalón que nosotros le hemos asignado a ese valor RGB, limitado a ser 0 o 1.

Para hacer una correcta diferenciación de tres frutas, hemos decidido poner dos perceptrones.
Y bajo estas circunstancias, el valor RGB procedente del sensor tiene dos funciones de
activación asignadas. A continuación, se muestran las funciones de activación que se han
asignado a cada fruta. Tome en cuenta que Z1 y Z2 son el primer y segundo perceptrón,
respectivamente.

    Fruta;      Z1; Z2
    Manzana:    0;  0
    Limón:      1;  0
    Mandarina:  0;  1

Dicho esto, es evidente que se tienen que formular dos vectores de pesos, y por lo tanto,
se tiene que hacer el entrenamiento dos veces. Pero ajustando los valores que se formularon
previamente en el siguiente código.


'''
import pandas as pd

def escalon(k,pesos,b):
    n=-b
    for i in range(len(k)):
        n=n+( k[i]*pesos[i])
    if(n>=0):
        return 1
    else:
        return 0
'''Para obtener los valores de la funcion escalon, se encesita el punto de prueba(k), el
vector de pesos y el bias. Dará como resultado el valor denominado Z que es la función escalón.
'''


def entrenar_perceptron(datos_ent,pesos,b,lamda):
    epocas=0
    errores=True
    while errores and epocas<4000:
        epocas=epocas+1
        print()
        print("Epoca: ",epocas)
        errores=False
        for k,y in datos_ent.items():
            n=escalon(k,pesos,b)
            if(n!=y):
                print("Hay ajuste")
                print("p1:",k[0],"p2:",k[1],"p3:",k[2])
                errores=True
                e=(y-n)
                delta_b=-(lamda*e)
                print("b:",b,"e",e,"delta_b",delta_b)
                for i in range(len(k)):
                    delta_w=lamda*e*k[i]
                    pesos[i]=pesos[i]+delta_w
                    print("Pesos",i,pesos[i])
            else:
                print("No hay Ajuste")
                print("p1:",k[0],"p2:",k[1],"p3:",k[2])
                e=(y-n)
                delta_b=-(lamda*e)
                print("b:",b,"e",e,"delta_b",delta_b)
    return pesos,b

def clasificar(entrada,pesos,b):
    return escalon(entrada,pesos,b)
    


'''
Para efectos de alimentarse de los datos, hemos decidido leer los tres datos en formato CSV,
cada uno correspondiente a una fruta. Así, guardamos todos los datos de una sola vez.

'''
def insertar_datos(archivo,archivo2,archivo3):
    datos=pd.read_csv(archivo, sep=",",
                      header=None)
    datos2=pd.read_csv(archivo2, sep=",",
                      header=None)
    datos3=pd.read_csv(archivo3, sep=",",
                      header=None)
    #recolección de datos de los archivos CSV correspondientes a cada fruta.
    
    lst = datos.values.tolist()
    lst2 = datos2.values.tolist()
    lst3 = datos3.values.tolist()
    #Se guardan los datos en una lista.
    
    #Se conviertentodos los elementos guardados a tuplas.
    new_lst = [tuple(x) for x in lst]
    new_lst2 = [tuple(x) for x in lst2]
    new_lst3 = [tuple(x) for x in lst3]
    dataa={}    
    
    '''
    cada uno de los datos correspondientes a cada fruta se guardan en un diccionario
    asignándole como clave la función escalón que hemos formulado.
    Estos valores son del primer entrenamiento; cuando se haga el segundo entrenamiento
    se deberán modificar los datos a los especificados en la tabla de arriba.
    '''
    for i in new_lst:
        dataa[i]=0
    for i in new_lst2:
        dataa[i]=1
    for i in new_lst3:
        dataa[i]=0
    return dataa

if __name__=="__main__":
    
    datos_ent=insertar_datos("./tratamientoDatos/csv/NuevaManzana1.csv",
                             "./tratamientoDatos/csv/Mandarina.csv",
                             "./tratamientoDatos/csv/Limon1.csv")
    pesos=[.2,.6,.1]
    b=0.4
    lamda=0.2
    pesos,b=entrenar_perceptron(datos_ent,pesos,b,lamda)
    print("-------------")
    print("Pesos finales: ",pesos)
    print("Bias Final: ",b)
    prueba=(45,60,92)
    print("Probando perceptron: ",str(prueba)+str(clasificar(prueba,pesos,b)))
    

'''
Ejecute este código para probar sus propios valores RGB. Añada los pesos y bias generados
por el entrenamiento, y ambos perceptrones deberían dar dos valores de salida.
'''

prueba=(132,152,189)
print("UNO: ",str(prueba)+str(clasificar(prueba, [42.80000000000001, 4.600000000000016, -28.899999999999984]
,0.4)))
print("DOS: ",str(prueba)+str(clasificar(prueba,[-225.6000000000002, 123.80000000000007, -1.6999999999999886],0.4)))