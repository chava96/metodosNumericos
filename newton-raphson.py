# f(x) = x^3 + 2x - 1
# f'(x) = 3x^2 + 2
# f''(x) = 6x
#2,4,6,8,10 iteraciones (0,5) [0,5] ... (0,5] o [0,5)

#NEWTON - RAPHSON
xi = -1
xi1 = 0
xr = 0
N = 10
#Por pasos N
for x in range(0,N): #[0,N)
	print(xr)
	xr = xr - ((xr**3 + 2*xr - 1)/(3*(xr**2) + 2))
print("La raiz real es: " + str(xr))

#Hasta que sea igual en la precisión(decimales)
while not(xi1 == xi):
	print(xi1)
	xi = xi1
	xi1 = xi - ((xi**3 + 2*xi - 1)/(3*(xi**2) + 2))
print("La raiz real es: " + str(xi1))