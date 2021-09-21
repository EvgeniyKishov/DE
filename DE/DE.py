class plot_data:
	def __init__(self):
		self.min = -5.0
		self.max = 5.0
		self.step = 0.05
		self.lines_num = 20
		self.p_style = 'o'
		self.v_style = 'v'
		self.u_style = '*'

class point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

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

def f(X, Y):
	#return ackley(X, Y)
	#return rastrigin(X, Y)
	#return sphere(X, Y)
	#return rosenbrock(X, Y)
	return beale(X, Y)

def find_min(func, pts):
	min_val = 1.0e30
	p_star = point(0, 0)
	for p in pts:
		f = func(p.x, p.y)
		if f <= min_val:
			min_val = f
			p_star = p
	return min_val, p_star

def plot_pts(func, pts, plt, ax, style):
	for p in pts:
		plt.plot(p.x, p.y, style)
		text = "{:.2f}".format(func(p.x, p.y))
		ax.annotate(text, (p.x, p.y), fontsize=12)

def plotf(func, param, pts, it):
	import matplotlib.pyplot as plt
	from matplotlib import cm
	import numpy as np

	fig, ax = plt.subplots()	
	fig.set_size_inches(12.0, 9.0)
	X = np.arange(param.min-0.5, param.max+0.5, param.step)
	Y = np.arange(param.min-0.5, param.max+0.5, param.step)
	X, Y = np.meshgrid(X, Y)

	Z = func(X, Y)

	surf = ax.contour(X, Y, Z, param.lines_num)
	fig.colorbar(surf, shrink=0.5, aspect=10)

	if "p_new" in pts:
		plot_pts(func, pts["p_new"], plt, ax, param.p_style)
		min_val, p_star = find_min(f, pts["p_new"])
	else:
		if "p" in pts:
			plot_pts(func, pts["p"], plt, ax, param.p_style)
			min_val, p_star = find_min(f, pts["p"])
		if "v" in pts:
			plot_pts(func, pts["v"], plt, ax, param.v_style)
			min_val, p_star = find_min(f, pts["v"])
		if "u" in pts:
			plot_pts(func, pts["u"], plt, ax, param.u_style)
			min_val, p_star = find_min(f, pts["u"])
	
	text = "Min. goal func. value from current population = {:.3f}".format(min_val)
	ax.annotate(text, xy=(0.0,1.1), xycoords='axes fraction', fontsize=12)
	text = "Best candidate point = ({:.3f},{:.3f})".format(p_star.x, p_star.y)
	ax.annotate(text, xy=(0.0,1.05), xycoords='axes fraction', fontsize=12)
	#arrow
	ax.annotate('min', xy=(p_star.x, p_star.y), xytext=(p_star.x-1, p_star.y-1),
                 arrowprops=dict(facecolor='red', shrink=0.05))
	
	#plt.get_current_fig_manager().window.state('zoomed')
	#plt.show()
	plt.savefig('iter = '+str(it)+'.png', dpi=100)
	plt.close(fig)

def plot_converg(iters, obj_hist):
	import matplotlib.pyplot as plt
	fig = plt.figure()
	fig.suptitle("Convergence plot")
	fig.set_size_inches(12.0, 9.0)
	plt.xticks([0] + list(iters))
	plt.plot([0] + list(iters), obj_hist, color='tab:blue', marker='o')
	plt.savefig('convergence.png')
	plt.show()