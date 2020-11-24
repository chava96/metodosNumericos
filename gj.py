import numpy as np 

#ecuaciones = [[2,1,3],[3,1,2],[2,3,5]]
#soluciones = [2,3,-3]
ecuaciones = [[3,-0.1,-0.2],[0.1,7,-0.3],[0.3,-0.2,10]]
soluciones = [7.85, -19.3,71.4]

a1 = np.array(ecuaciones, float)
b1 = np.array(soluciones, float)


def gaussJordan(a,b):
    n = len(b)
    #a[i,i] == 0 -> Temp = R[i], R[i] = R[i+1], R[i+1] = Temp
    for i in range(n): #iterar en i de 0 hasta n-1
    #PASO 1: ENCONTRAR PIVOTE & DIVIDIR EL RENGLON ENTRE EL VALOR DEL MISMO
    pivote = a[i,i]
    #Tenemos que recorrer todo el renglon-> iterar en cols y dividir entre pivote
    for j in range(n):
        a[i,j] = a[i,j] / pivote
    b[i] = b[i] / pivote

    #PASO 2: ELIMINACION o HACER 0s LOS OTROS VALORES DEL COLUMNA EN LA QUE ESTOY
    for j in range(n):
        if(j != i and a[j,i] != 0):#Asegurarme que no esté en la diagonal ni sea 0
            factor = a[j,i]
            #iterar las cols del mismo renglon, para modificar el renglon: Rj = Rj - factor*Ri
            #(for k in range(n))Rj -> a[j, k] ... Ri -> a[i,k]
            for k in range(n):
                a[j,k] = a[j,k] - (factor*a[i,k])
            b[j] = b[j] - (factor*b[i])
    return a,b

#TODOS LOS CAMBIOS SE GUARDARON EN LA MATRIZ ORIGINAL (a) Y VECTOR DE RESULTADOS (b)
#PASO 3: MOSTRAR LOS RESULTADOS (print)
a2,b2 = gaussJordan(a1,b1)
print("Comprobar diagonal o matriz identidad:")
print(a2)
print("----------------------------")
print("Resultados:")
print(b2)