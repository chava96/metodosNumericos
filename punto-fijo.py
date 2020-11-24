#f(x) =  2x^2 - 4x - 5
#xi1 = (2xi0^2 - 5)/4

xi0 = 1.0
Es = 0.01
xi1 = xi0
Ea = 1.0
i = 0

while Ea >= Es:
	xi1 = (2*(xi0**2) - 5) / 4
	Ea = abs((xi1 - xi0)/xi1)
	xi0 = xi1
	print(str(i) + " | " + str(xi1) + " | " + str(Ea*100) + "%")
	i = i + 1