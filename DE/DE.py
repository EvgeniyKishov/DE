from plot import *
import random as rd

#def print_pts(pts):
#    for p in pts:
#        print("{:.2f}, {:.2f}".format(p.x, p.y))

class de_param():
    def __init__(self):
        self.xrange = (-5.0, 5.0)
        self.yrange = (-5.0, 5.0)
        self.F = 0.5
        self.cr = 0.9
        self.it_num = 20
        self.pop_num = 10

def find_min(func, pts):
	min_val = 1.0e30
	p_star = point(0, 0)
	for p in pts:
		f = func(p.x, p.y)
		if f <= min_val:
			min_val = f
			p_star = p
	return min_val, p_star

def compute_rand_ids(pts_num):
    import random as rd
    ids = list(range(0, pts_num))
    r1 = rd.randrange(0, pts_num)
    del ids[r1]
    r2_tmp = rd.randrange(0, pts_num-1)
    r2 = ids[r2_tmp]
    del ids[r2_tmp]
    r3_tmp = rd.randrange(0, pts_num-2)
    r3 = ids[r3_tmp]

    return r1, r2, r3

def init(xrange, yrange, pop_num):
    x_pts = []
    for i in range(0, pop_num):
        p = point(rd.uniform(xrange[0],xrange[1]), rd.uniform(yrange[0],yrange[1]))
        x_pts.append(p)
    return x_pts

def mut(x_pts, de_par):
    v_pts = []
    for i in range(0, de_par.pop_num):
        r1, r2, r3 = compute_rand_ids(de_par.pop_num)
        v = point(0.0, 0.0)
        v.x = x_pts[r1].x + de_par.F*(x_pts[r2].x - x_pts[r3].x)    
        v.y = x_pts[r1].y + de_par.F*(x_pts[r2].y - x_pts[r3].y)
        #imposing box constraints
        v.x = max(de_par.xrange[0], min(v.x, de_par.xrange[1]))
        v.y = max(de_par.yrange[0], min(v.y, de_par.yrange[1]))
        v_pts.append(v)
    return v_pts

def cross(x_pts, v_pts, de_par):
    u_pts = []
    for i in range(0, de_par.pop_num):
        u = point(x_pts[i].x, x_pts[i].y)
        n = rd.randrange(0, 2)
        if (n == 0):
            if (rd.uniform(0.0, 1.0) <= de_par.cr):
                u.x = v_pts[i].x
            if (rd.uniform(0.0, 1.0) <= de_par.cr):
                u.y = v_pts[i].y
        if (n == 1):
            if (rd.uniform(0.0, 1.0) <= de_par.cr):
                u.y = v_pts[i].y                  
        u_pts.append(u)
    return u_pts

def updpop(x_pts, u_pts, func):
    x_pts_new = []
    for p, u in zip(x_pts, u_pts):
        if (func(p.x, p.y) <= func(u.x, u.y)):
            x_pts_new.append(p)
        else:
            x_pts_new.append(u)
    return x_pts_new

def de_opt(func, de_par, plot_par):
    #initial population
    x_pts = init(de_par.xrange, de_par.yrange, de_par.pop_num)
    min_val, x_star = find_min(func, x_pts)
    if plot_par.plot_pop:
        opt_par = opt_data()
        opt_par.it = 0
        opt_par.min_val = min_val
        opt_par.x_star = x_star
        plotf(func, plot_par, x_pts, opt_par)    
    print(0,"{:.3f}".format(min_val),"({:.3f},{:.3f})".format(x_star.x,x_star.y))

    #optimization loop
    obj_hist = [min_val]
    iters = range(1, de_par.it_num)
    for it in iters:
        #mutation (generating children)
        v_pts = mut(x_pts, de_par)
        #crossover
        u_pts = cross(x_pts, v_pts, de_par)
        #update population
        x_pts_new = updpop(x_pts, u_pts, func)
        #assign new points to old one
        x_pts = x_pts_new
        #compute current result
        min_val, x_star = find_min(func, x_pts)
        #plot result
        if plot_par.plot_pop:
            opt_par.it = it
            opt_par.min_val = min_val
            opt_par.x_star = x_star
            plotf(func, plot_par, x_pts, opt_par)  
        #print iteration history

        #save objective history for plotting
        obj_hist.append(min_val)
        print(it,"{:.3f}".format(min_val),"({:.3f},{:.3f})".format(x_star.x,x_star.y))

    print("Number of goal func. evaluation = "+str(de_par.it_num*de_par.pop_num*2))
    if plot_par.plot_conv:
        plot_converg(iters, obj_hist)

    return min_val, x_star
