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

#initial population
pop_num = 10
param = plot_data()
p = []
for i in range(0, pop_num):
    pt = point(rd.uniform(-5,5), rd.uniform(-5,5))
    p.append(pt)

pts = {"p": p}
plotf(f, param, pts)

#generating children
v = []
F = 0.5
for p in pts["p"]:
    r1, r2, r3 = compute_rand_ids(pts_num)
    v_tmp = point(0.0, 0.0)
    v_tmp.x = pts["p"][r1].x + F*(pts["p"][r2].x - pts["p"][r3].x)    
    v_tmp.y = pts["p"][r1].y + F*(pts["p"][r2].y - pts["p"][r3].y)
    #imposing box constraints
    v_tmp.x = max(param.min, min(v_tmp.x, param.max))
    v_tmp.y = max(param.min, min(v_tmp.y, param.max))

    v.append(v_tmp)

pts.update({"v": v})
plotf(f, param, pts)






