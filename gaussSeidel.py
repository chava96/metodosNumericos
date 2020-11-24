import numpy as np 

ecuaciones = [[3,-0.1,-0.2],[0.1,7,-0.3],[0.3,-0.2,10]]
soluciones = [7.85, -19.3,71.4]
iteraciones = 5
a1 = np.array(ecuaciones, float)
b1 = np.array(soluciones, float)

def gaussSeidel(a,b):
    global iteraciones
    n = len(b)
    x = np.zeros(3)
    for steps in range(iteraciones): #Numero de iteraciones que voy a realizar
        for i in range(n):
            x[i] = b[i]
            for j in range(n):
                #Voy a recorrer la matriz, para agarrar las a que NO sean la diagonal... a[i,i]
                if j != i:
                    x[i] = x[i] - (a[i,j]*x[j])
            x[i] = x[i] / a[i,i]
    return x

res = gaussSeidel(a1,b1)
print(res)