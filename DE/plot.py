from testf import *
from common import *

class plot_data:
	def __init__(self):
		self.min = -5.0
		self.max = 5.0
		self.step = 0.05
		self.lines_num = 20
		self.p_style = 'o'
		self.v_style = 'v'
		self.u_style = '*'
		self.plot_pop = True
		self.plot_conv = True

class opt_data:
	def __init__(self):
		self.it = 0
		self.min_val = 0.0
		self.p_star = point(0.0, 0.0)

def plot_pts(func, pts, plt, ax, style):
	for p in pts:
		plt.plot(p.x, p.y, style)
		text = "{:.2f}".format(func(p.x, p.y))
		ax.annotate(text, (p.x, p.y), fontsize=12)

def plotf(func, param, pts, opt_data):
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
	else:
		if "p" in pts:
			plot_pts(func, pts["p"], plt, ax, param.p_style)
		if "v" in pts:
			plot_pts(func, pts["v"], plt, ax, param.v_style)
		if "u" in pts:
			plot_pts(func, pts["u"], plt, ax, param.u_style)
	
	min_val = opt_data.min_val
	p_star = opt_data.p_star
	text = "Min. goal func. value from current population = {:.3f}".format(min_val)
	ax.annotate(text, xy=(0.0, 1.1), xycoords='axes fraction', fontsize=12)
	text = "Best candidate point = ({:.3f},{:.3f})".format(p_star.x, p_star.y)
	ax.annotate(text, xy=(0.0, 1.05), xycoords='axes fraction', fontsize=12)
	#arrow
	ax.annotate('min', xy=(p_star.x, p_star.y), xytext=(p_star.x-1, p_star.y-1),
                 arrowprops=dict(facecolor='red', shrink=0.05))
	
	#plt.get_current_fig_manager().window.state('zoomed')
	#plt.show()
	plt.savefig('iter = '+str(opt_data.it)+'.png', dpi=100)
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