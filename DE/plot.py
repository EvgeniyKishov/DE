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
		self.alg = 'DE'
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
	import numpy as np
	import os

	fig, ax = plt.subplots()	
	fig.set_size_inches(12.0, 9.0)
	X = np.arange(plot_par.xrange[0]-0.5, plot_par.xrange[1]+0.5, plot_par.step)
	Y = np.arange(plot_par.yrange[0]-0.5, plot_par.yrange[1]+0.5, plot_par.step)
	X, Y = np.meshgrid(X, Y)

	Z = func(X, Y)

	surf = ax.contour(X, Y, Z, levels = plot_par.lines_num)
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
	folder = plot_par.alg + "_plots"
	if not os.path.exists(folder):
		os.makedirs(folder)
	plt.savefig(folder+'\\'+'iter = '+str(opt_par.it)+'.png', dpi=100)
	plt.close(fig)

def plot_converg(obj_hist_de, obj_hist_brmc, minv):
	import matplotlib.pyplot as plt
	fig, ax = plt.subplots()
	fig.suptitle("Convergence plot")
	fig.set_size_inches(12.0, 9.0)
	ax.set_xlabel('Iterations')
	ax.set_ylabel('Goal function values')

	iters_de = []
	obj_de = []	
	for o in obj_hist_de:
		iters_de.append(o[0])
		obj_de.append(o[1])
	iters_brmc = []
	obj_brmc = []
	for o in obj_hist_brmc:
		iters_brmc.append(o[0])
		obj_brmc.append(o[1])
	if len(iters_de) >= len(iters_brmc):
		plt.xticks(iters_de)
		iters_exact = iters_de
	else:
		plt.xticks(iters_brmc)
		iters_exact = iters_brmc
	
	exact = []
	for it in iters_exact:
		exact.append(minv)

	plt.plot(iters_de, obj_de, 'bo-', label='DE')
	plt.plot(iters_brmc, obj_brmc, 'r*-', label='BRMC')
	plt.plot(iters_exact, exact, 'g--', label='Exact')
	plt.legend()
	plt.savefig('convergence.png')
	plt.show()