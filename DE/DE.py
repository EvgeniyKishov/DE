class fun_data:
	def __init__(self):
		self.min = -5.0
		self.max = 5.0
		self.step = 0.05
		self.lines_num = 20

class point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

def f(X, Y):
	import numpy as np
	#Ackley function
	Z = -20.0*np.exp(-0.2*np.sqrt(0.5*(X**2+Y**2))) - \
        np.exp(0.5*(np.cos(2*np.pi*X)+np.cos(2*np.pi*Y))) + np.exp(1) + 20.0
	return Z

def plotf(func, param, pts):
	import matplotlib.pyplot as plt
	from matplotlib import cm
	import numpy as np

	fig, ax = plt.subplots()

	X = np.arange(param.min, param.max, param.step)
	Y = np.arange(param.min, param.max, param.step)
	X, Y = np.meshgrid(X, Y)

	Z = func(X, Y)

	surf = ax.contour(X, Y, Z, param.lines_num)
	#ax.clabel(surf, inline=True, fontsize=10)
	fig.colorbar(surf, shrink=0.5, aspect=10)

	min_val = 1.0e30
	p_star = point(0, 0)
	for p in pts:
		f = func(p.x, p.y)
		if f <= min_val:
			min_val = f
			p_star = p

		plt.plot(p.x, p.y, 'ko')
		text = "{:.2f}".format(f)
		ax.annotate(text, (p.x, p.y), fontsize=12)
	
	text = "Min. goal func. value from current population = {:.3f}".format(min_val)
	ax.annotate(text, xy=(0.0,1.1), xycoords='axes fraction', fontsize=12)
	text = "Best candidate point = ({:.3f},{:.3f})".format(p_star.x, p_star.y)
	ax.annotate(text, xy=(0.0,1.05), xycoords='axes fraction', fontsize=12)
	#arrow
	ax.annotate('min', xy=(p_star.x, p_star.y), xytext=(p_star.x-1, p_star.y-1),
                 arrowprops=dict(facecolor='red', shrink=0.05))

	plt.show()