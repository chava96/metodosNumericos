import numpy as np 

ecuaciones = [[3,-0.1,-0.2],[0.1,7,-0.3],[0.3,-0.2,10]]
soluciones = [7.85, -19.3,71.4]

a = np.array(ecuaciones, float)
b = np.array(soluciones, float)
x = np.zeros(3)

# x1 = b1 - a12*x2 - a13*x3
# x2 = b2 - a21*x1 - a23*x3
# x3 = b3 - a31*x1 - a32*x2

n = len(b)

for steps in range(5):
    for i in range(n):
        x[i] = b[i]
        for j in range(n):
            if j != i:
                x[i] -= (a[i,j]*x[j]) #Es lo mismo a x[i] = x[i] - (a[i,j]*x[j])
        x[i] /= a[i,i]
    print("Step " + str(steps) + ":")
    print(x)
