from plot import *
import random as rd

#def print_pts(pts):
#    for p in pts:
#        print("{:.2f}, {:.2f}".format(p.x, p.y))

class de_param():
    def __init__(self):
        self.xmin = -5.0
        self.xmax = 5.0
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

def init(min_val, max_val, pop_num):
    p = []
    for i in range(0, pop_num):
        pt = point(rd.uniform(min_val, max_val), rd.uniform(min_val, max_val))
        p.append(pt)

    pts = {"p": p}
    return pts

def mut(pts, de_par):
    v = []
    for p in pts["p"]:
        r1, r2, r3 = compute_rand_ids(de_par.pop_num)
        v_tmp = point(0.0, 0.0)
        v_tmp.x = pts["p"][r1].x + de_par.F*(pts["p"][r2].x - pts["p"][r3].x)    
        v_tmp.y = pts["p"][r1].y + de_par.F*(pts["p"][r2].y - pts["p"][r3].y)
        #imposing box constraints
        v_tmp.x = max(de_par.xmin, min(v_tmp.x, de_par.xmax))
        v_tmp.y = max(de_par.xmin, min(v_tmp.y, de_par.xmax))

        v.append(v_tmp)

    pts.update({"v": v})
    return pts

def cross(pts, de_par):
    u = []
    for i in range(0, de_par.pop_num):
        u_tmp = point(pts["p"][i].x, pts["p"][i].y)
        n = rd.randrange(0, 2)
        if (n == 0):
            if (rd.uniform(0.0, 1.0) <= de_par.cr):
                u_tmp.x = pts["v"][i].x
            if (rd.uniform(0.0, 1.0) <= de_par.cr):
                u_tmp.y = pts["v"][i].y
        if (n == 1):
            if (rd.uniform(0.0, 1.0) <= de_par.cr):
                u_tmp.y = pts["v"][i].y    
        u.append(u_tmp)

    pts.update({"u": u})
    return pts

def updpop(pts, func):
    p_new = []
    for p, u in zip(pts["p"], pts["u"]):
        if (func(p.x, p.y) <= func(u.x, u.y)):
            p_new.append(p)
        else:
            p_new.append(u)

    pts.update({"p_new": p_new})
    return pts

def de_opt(func, de_par, plot_par):
    #initial population
    pts = init(de_par.xmin, de_par.xmax, de_par.pop_num)
    min_val, p_star = find_min(func, pts["p"])
    if plot_par.plot_pop:
        opt_par = opt_data()
        opt_par.it = 0
        opt_par.min_val = min_val
        opt_par.p_star = p_star
        plotf(func, plot_par, pts, opt_par)    
    print(0,"{:.3f}".format(min_val),"({:.3f},{:.3f})".format(p_star.x,p_star.y))

    #optimization loop
    obj_hist = [min_val]
    iters = range(1, de_par.it_num)
    for it in iters:
        #mutation (generating children)
        pts = mut(pts, de_par)
        #crossover
        pts = cross(pts, de_par)
        #update population
        pts = updpop(pts, func)
        #assign new points to old one
        pts.update({"p": pts["p_new"]})
        #compute current result
        min_val, p_star = find_min(func, pts["p"])
        #plot result
        if plot_par.plot_pop:
            opt_par.it = it
            opt_par.min_val = min_val
            opt_par.p_star = p_star
            plotf(func, plot_par, pts, opt_par)  
        #print iteration history

        #save objective history for plotting
        obj_hist.append(min_val)
        print(it,"{:.3f}".format(min_val),"({:.3f},{:.3f})".format(p_star.x,p_star.y))

    print("Number of goal func. evaluation = "+str(de_par.it_num*de_par.pop_num*2))
    if plot_par.plot_conv:
        plot_converg(iters, obj_hist)

    return min_val, p_star
