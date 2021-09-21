from DE import *
import random as rd

def print_pts(pts):
    for p in pts:
        print("{:.2f}, {:.2f}".format(p.x, p.y))

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

def mut(pts, F):
    v = []
    for p in pts["p"]:
        r1, r2, r3 = compute_rand_ids(pop_num)
        v_tmp = point(0.0, 0.0)
        v_tmp.x = pts["p"][r1].x + F*(pts["p"][r2].x - pts["p"][r3].x)    
        v_tmp.y = pts["p"][r1].y + F*(pts["p"][r2].y - pts["p"][r3].y)
        #imposing box constraints
        v_tmp.x = max(param.min, min(v_tmp.x, param.max))
        v_tmp.y = max(param.min, min(v_tmp.y, param.max))

        v.append(v_tmp)

    pts.update({"v": v})
    return pts

def cross(pts, cr):
    u = []
    for i in range(0, pop_num):
        u_tmp = point(pts["p"][i].x, pts["p"][i].y)
        n = rd.randrange(0, 2)
        if (n == 0):
            if (rd.uniform(0.0, 1.0) <= cr):
                u_tmp.x = pts["v"][i].x
            if (rd.uniform(0.0, 1.0) <= cr):
                u_tmp.y = pts["v"][i].y
        if (n == 1):
            if (rd.uniform(0.0, 1.0) <= cr):
                u_tmp.y = pts["v"][i].y    
        u.append(u_tmp)

    pts.update({"u": u})
    return pts

#parameters
pop_num = 10
min_val = -5
max_val = 5
F = 0.5
cr = 0.9
param = plot_data()

#initial population
pts = init(min_val, max_val, pop_num)
plotf(f, param, pts)

#mutation (generating children)
pts = mut(pts, F)
plotf(f, param, pts)

#crossover
pts = cross(pts, cr)
plotf(f, param, pts)

#update population
