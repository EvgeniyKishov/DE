from testf import *
from common import *

class plot_data:
	def __init__(self):
		self.xrange = (-5.0, 5.0)
		self.yrange = (-5.0, 5.0)
		self.step = 0.05
		self.lines_num = 20
		self.x_style = 'o'
		self.v_style = 'v'
		self.u_style = '*'
		self.plot_pop = True
		self.plot_conv = True

class opt_data:
	def __init__(self):
		self.it = 0
		self.min_val = 0.0
		self.x_star = point(0.0, 0.0)

def plot_pts(func, x_pts, plt, ax, style):
	for p in x_pts:
		plt.plot(p.x, p.y, style)
		text = "{:.2f}".format(func(p.x, p.y))
		ax.annotate(text, (p.x, p.y), fontsize=12)

def plotf(func, plot_par, x_pts, opt_par):
	import matplotlib.pyplot as plt
	from matplotlib import cm
	import numpy as np

	fig, ax = plt.subplots()	
	fig.set_size_inches(12.0, 9.0)
	X = np.arange(plot_par.xrange[0]-0.5, plot_par.xrange[1]+0.5, plot_par.step)
	Y = np.arange(plot_par.yrange[0]-0.5, plot_par.yrange[1]+0.5, plot_par.step)
	X, Y = np.meshgrid(X, Y)

	Z = func(X, Y)

	surf = ax.contour(X, Y, Z, plot_par.lines_num)
	fig.colorbar(surf, shrink=0.5, aspect=10)

	plot_pts(func, x_pts, plt, ax, plot_par.x_style)
	
	min_val = opt_par.min_val
	x_star = opt_par.x_star
	text = "Min. goal func. value from current population = {:.3f}".format(min_val)
	ax.annotate(text, xy=(0.0, 1.1), xycoords='axes fraction', fontsize=12)
	text = "Best candidate point = ({:.3f},{:.3f})".format(x_star.x, x_star.y)
	ax.annotate(text, xy=(0.0, 1.05), xycoords='axes fraction', fontsize=12)
	#arrow
	ax.annotate('min', xy=(x_star.x, x_star.y), xytext=(x_star.x-1, x_star.y-1),
                 arrowprops=dict(facecolor='red', shrink=0.05))
	
	#plt.get_current_fig_manager().window.state('zoomed')
	#plt.show()
	plt.savefig('iter = '+str(opt_par.it)+'.png', dpi=100)
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