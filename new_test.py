import numpy as np 

x = np.array([1,2,3,4,5,6,7])
y = np.array([0.5,2.5,2.0,4.0,3.5,6.0,5.5])

n = np.size(x)

def promedio(arr):
	suma = 0
	for i in arr:
		suma += i
	suma /= np.size(arr)
	return suma

x_prom = promedio(x)
y_prom = promedio(y)

def suma_arr(arr):
	suma = 0
	for i in arr:
		suma += i
	return suma

def mult_arr(arr1,arr2):
	new_arr = np.array([])
	for i in range(np.size(arr1)):
		new_arr = np.append(new_arr, (arr1[i]*arr2[i]))
	return new_arr

suma_x = suma_arr(x)
suma_y = suma_arr(y)
suma_xy = suma_arr(mult_arr(x,y))
suma_xx = suma_arr(mult_arr(x,x))
cuad_suma_x = suma_x ** 2

a1 = ((n*suma_xy) - (suma_x*suma_y)) / ((n*suma_xx) - (cuad_suma_x))
a0 = y_prom - (a1*x_prom)

print("y = "+str(a0)+" - " + str(a1)+"x")