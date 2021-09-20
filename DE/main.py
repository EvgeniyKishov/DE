from DE import *
import random as rd

param = fun_data()
pts = []
for i in range(0, 10):
    p = point(rd.uniform(-5,5), rd.uniform(-5,5))
    pts.append(p)
plotf(f, param, pts)
