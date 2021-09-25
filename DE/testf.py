def ackley(X, Y):
	import numpy as np
	#Ackley function
	Z = -20.0*np.exp(-0.2*np.sqrt(0.5*(X**2+Y**2))) - \
        np.exp(0.5*(np.cos(2*np.pi*X)+np.cos(2*np.pi*Y))) + np.exp(1) + 20.0
	return Z

def rastrigin(X, Y):
	import numpy as np
	A = 20.0
	n = 2	
	Z = A*n + (X**2 - A*np.cos(2*np.pi*X)) + (Y**2 - A*np.cos(2*np.pi*Y))
	return Z

def sphere(X, Y):
	Z = X**2 + Y**2 
	return Z

def rosenbrock(X, Y):
	Z = 100*(Y - X**2)**2 + (1 - X)**2
	return Z

def beale(X, Y):
	Z = (1.5-X+X*Y)**2 + (2.25-X+X*(Y**2))**2 + (2.625-X+X*(Y**3))**2
	return Z
