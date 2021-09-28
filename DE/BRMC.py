from plot import *
import random as rd

class brmc_param():
    def __init__(self):
        self.xrange = (-5.0, 5.0)
        self.yrange = (-5.0, 5.0)
        self.nbest = 3
        self.nmut = 2
        self.nrand = 1
        self.ncross = 1
        self.d = 0.2
        self.it_num = 20
        self.pop_num = 0

def find_min(func, x_pts):
	min_val = 1.0e30
	x_star = point(0, 0)
	for p in x_pts:
		f = func(p.x, p.y)
		if f <= min_val:
			min_val = f
			x_star = p
	return min_val, x_star

def init(xrange, yrange, pop_num):
    x_pts = []
    for i in range(0, pop_num):
        p = point(rd.uniform(xrange[0],xrange[1]), rd.uniform(yrange[0],yrange[1]))
        x_pts.append(p)
    return x_pts

def sort_key(pair):
    return pair[1]

def best(goalv, opt_par):    
    goalv.sort(key=sort_key)

    best_pts = []
    for i in range(0, opt_par.nbest):
        best_pts.append(goalv[i][0])
    return best_pts

def goalf_eval(func, x_pts):
    goalv = []
    for p in x_pts:
        goalv.append((p, func(p.x, p.y)))
    return goalv

def mut(goalv, brmc_par):
    mut_pts = []

    lx = brmc_par.xrange[1] - brmc_par.xrange[0]
    ly = brmc_par.yrange[1] - brmc_par.yrange[0]
    for i in range(0, brmc_par.nmut):
        p = goalv[i][0]
        mut_p = point(0.0, 0.0)
        mut_p.x = p.x + 0.5*brmc_par.d*lx*rd.uniform(-1.0, 1.0)
        mut_p.y = p.y + 0.5*brmc_par.d*ly*rd.uniform(-1.0, 1.0)
        mut_pts.append(mut_p)

    return mut_pts

def cross(goalv, brmc_par):
    best_pairs = []
    for i in range(0, brmc_par.nbest):
        best_pairs.append(goalv[i])

    cross_pts_raw = []
    n = round(brmc_par.paren_pct * brmc_par.pop_num)
    for i in range(0, n):
        for k in range(i+1, n):
            cross_p = point(0.0, 0.0)
            cross_p.x = 0.5*(goalv[i][0].x + goalv[k][0].x)
            cross_p.y = 0.5*(goalv[i][0].y + goalv[k][0].y)
            q = 0.5*(goalv[i][1] + goalv[k][1])
            cross_pts_raw.append((cross_p, q))
    cross_pts_raw.sort(key=sort_key)

    cross_pts = []
    b = int(0.5*(n**2 - n))
    for i in range(0, min(brmc_par.ncross, b)):
        cross_pts.append(cross_pts_raw[i][0])
    return cross_pts

def brmc_opt(func, brmc_par, plot_par):
    brmc_par.pop_num = brmc_par.nbest + brmc_par.nmut + \
                       brmc_par.nrand + brmc_par.ncross

    x_pts = init(brmc_par.xrange, brmc_par.yrange, brmc_par.pop_num)
    goalv = goalf_eval(func, x_pts)
    best_pts = best(goalv, brmc_par)
    
    min_val = goalv[0][1]
    x_star = goalv[0][0]
    if plot_par.plot_pop:
        opt_par = opt_data()
        opt_par.it = 0
        opt_par.min_val = min_val
        opt_par.x_star = x_star
        plotf(func, plot_par, x_pts, opt_par)
    
    #optimization loop
    obj_hist = [(0, min_val)]
    iters = range(1, brmc_par.it_num)
    for it in iters:
        mut_pts = mut(goalv, brmc_par)   
        rnd_pts = init(brmc_par.xrange, brmc_par.yrange, brmc_par.nrand)  
        cross_pts = cross(goalv, brmc_par)
        x_pts = best_pts + mut_pts + rnd_pts + cross_pts

        goalv = goalf_eval(func, x_pts)
        best_pts = best(goalv, brmc_par)
        min_val = goalv[0][1]
        x_star = goalv[0][0]
        #plot result
        if plot_par.plot_pop:
            opt_par.it = it
            opt_par.min_val = min_val
            opt_par.x_star = x_star
            plotf(func, plot_par, x_pts, opt_par)  
        #save objective history for plotting
        obj_hist.append((it, min_val))
        print(it,"{:.3f}".format(min_val),"({:.3f},{:.3f})".format(x_star.x,x_star.y))

    print("Number of goal func. evaluation = "+str(brmc_par.it_num*brmc_par.pop_num))
    #if plot_par.plot_conv:
    #    plot_converg(iters, obj_hist)

    return min_val, x_star, obj_hist