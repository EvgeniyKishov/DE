from common import *

class ackley:
	def __init__(self):
		self.x_star = point(0.0, 0.0)
		self.minv = 0.0
		self.xrange = (-5.0, 5.0)
		self.yrange = (-5.0, 5.0)

	@staticmethod
	def f(X, Y):
		import numpy as np
		#Ackley function
		Z = -20.0*np.exp(-0.2*np.sqrt(0.5*(X**2+Y**2))) - \
			np.exp(0.5*(np.cos(2*np.pi*X)+np.cos(2*np.pi*Y))) + np.exp(1) + 20.0
		return Z

class rastrigin:
	def __init__(self):
		self.x_star = point(0.0, 0.0)
		self.minv = 0.0
		self.xrange = (-5.12, 5.12)
		self.yrange = (-5.12, 5.12)
	
	@staticmethod
	def f(X, Y):
		import numpy as np
		A = 20.0
		n = 2	
		Z = A*n + (X**2 - A*np.cos(2*np.pi*X)) + (Y**2 - A*np.cos(2*np.pi*Y))
		return Z

class sphere:
	def __init__(self):
		self.x_star = point(0.0, 0.0)
		self.minv = 0.0
		self.xrange = (-5.0, 5.0)
		self.yrange = (-5.0, 5.0)
	
	@staticmethod
	def f(X, Y):
		Z = X**2 + Y**2 
		return Z

class rosenbrock:
	def __init__(self):
		self.x_star = point(1.0, 1.0)
		self.minv = 0.0
		self.xrange = (-2.0, 2.0)
		self.yrange = (-1.0, 3.0)

	@staticmethod
	def f(X, Y):
		Z = 100*(Y - X**2)**2 + (1 - X)**2
		return Z

class beale:
	def __init__(self):
		self.x_star = point(3.0, 0.5)
		self.minv = 0.0
		self.xrange = (-4.5, 4.5)
		self.yrange = (-4.5, 4.5)

	@staticmethod
	def f(X, Y):
		Z = (1.5-X+X*Y)**2 + (2.25-X+X*(Y**2))**2 + (2.625-X+X*(Y**3))**2
		return Z
