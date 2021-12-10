from plot import *
import random as rd

class brmc_param():
    def __init__(self):
        self.xrange = (-5.0, 5.0)
        self.yrange = (-5.0, 5.0)
        self.best = 0.2
        self.mut = 0.3
        self.rand = 0.1
        self.cross = 0.4
        self.paren = 0.1
        self.pop_num = 20
        self.d = 0.3
        self.it_num = 20

def init(xrange, yrange, pop_num):
    x_pts = []
    for i in range(0, pop_num):
        p = point(rd.uniform(xrange[0],xrange[1]), rd.uniform(yrange[0],yrange[1]))
        x_pts.append(p)
    return x_pts

def sort_key(pair):
    return pair[1]

def best(goalv, nbest):    
    goalv.sort(key=sort_key)

    best_pts = []
    for i in range(0, nbest):
        best_pts.append(goalv[i][0])
    return best_pts

def goalf_eval(func, x_pts):
    goalv = []
    for p in x_pts:
        goalv.append((p, func(p.x, p.y)))
    return goalv

def mut(goalv, brmc_par, nmut):
    mut_pts = []

    lx = brmc_par.xrange[1] - brmc_par.xrange[0]
    ly = brmc_par.yrange[1] - brmc_par.yrange[0]
    for i in range(0, nmut):
        p = goalv[i][0]
        mut_p = point(0.0, 0.0)
        mut_p.x = p.x + 0.5*brmc_par.d*lx*rd.uniform(-1.0, 1.0)
        mut_p.y = p.y + 0.5*brmc_par.d*ly*rd.uniform(-1.0, 1.0)
        mut_pts.append(mut_p)

    return mut_pts

def cross(goalv, brmc_par, ncross):
    cross_pts_raw = []
    n = round(brmc_par.paren * brmc_par.pop_num)
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
    for i in range(0, min(ncross, b)):
        cross_pts.append(cross_pts_raw[i][0])
    return cross_pts

def apply_box_constr(x_pts, param):
    x_pts_new = []
    for p in x_pts:
        p.x = min(param.xrange[1],max(param.xrange[0],p.x))
        p.y = min(param.yrange[1],max(param.yrange[0],p.y))
        x_pts_new.append(p)
    return x_pts_new

def brmc_opt(func, brmc_par, plot_par, x0):
    check = brmc_par.best + brmc_par.mut + \
            brmc_par.rand + brmc_par.cross
    if check != 1.0:
        return 0.0, point(0.0, 0.0), [(0.0, 0.0)]

    nbest = round(brmc_par.pop_num * brmc_par.best)
    nmut = round(brmc_par.pop_num * brmc_par.mut)
    nrand = round(brmc_par.pop_num * brmc_par.rand)
    ncross = round(brmc_par.pop_num * brmc_par.cross)

    if x0 == None:
        x_pts = init(brmc_par.xrange, brmc_par.yrange, brmc_par.pop_num)
    else:
        x_pts = x0
    goalv = goalf_eval(func, x_pts)
    best_pts = best(goalv, nbest)
    
    min_val = goalv[0][1]
    x_star = goalv[0][0]
    if plot_par.plot_pop:
        opt_par = opt_data()
        opt_par.it = 0
        opt_par.min_val = min_val
        opt_par.x_star = x_star
        plotf(func, plot_par, x_pts, opt_par)
    print(0,"{:.3f}".format(min_val),"({:.3f},{:.3f})".format(x_star.x,x_star.y))

    #optimization loop
    obj_hist = [(0, min_val)]
    iters = range(1, brmc_par.it_num)
    for it in iters:
        mut_pts = mut(goalv, brmc_par, nmut)
        cross_pts = cross(goalv, brmc_par, ncross)
        if len(cross_pts) != ncross:
            delta = ncross - len(cross_pts)
            rnd_pts = init(brmc_par.xrange, brmc_par.yrange, nrand+delta)  
        else:
            rnd_pts = init(brmc_par.xrange, brmc_par.yrange, nrand)  
        x_pts_raw = best_pts + mut_pts + rnd_pts + cross_pts
        x_pts = apply_box_constr(x_pts_raw, brmc_par)

        goalv = goalf_eval(func, x_pts)
        best_pts = best(goalv, nbest)
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