from DE import *
from BRMC import *
from testf import *

import shutil
shutil.rmtree("/DE")
shutil.rmtree("/BRMC")

#test function:
#test_func = ackley()
#test_func = rastrigin()
test_func = beale()

#parameters
de_par = de_param()
de_par.pop_num = 20
de_par.xrange = test_func.xrange
de_par.yrange = test_func.yrange
de_par.F = 0.5
de_par.cr = 0.9
de_par.it_num = 2

brmc_par = brmc_param()
brmc_par.xrange = test_func.xrange
brmc_par.yrange = test_func.yrange
brmc_par.nbest = 2*2
brmc_par.nmut = 3*2
brmc_par.nrand = 1*2
brmc_par.ncross = 4*2
brmc_par.paren_pct = 0.1
brmc_par.d = 0.3
brmc_par.it_num = 3

plot_par = plot_data()
plot_par.xrange = test_func.xrange
plot_par.yrange = test_func.yrange
plot_par.lines_num = 20
plot_par.step = 0.05
plot_par.plot_pop = True
plot_par.plot_conv = True

print("### DE ###")
plot_par.alg = "DE"
min_val, x_star, obj_hist_de = de_opt(test_func.f, de_par, plot_par)
print("Min obj. value = {:.3f}, x* = {:.3f}, y* = {:.3f}".
                     format(min_val, x_star.x, x_star.y))
print("Exact solution = {:.3f}, x* = {:.3f}, y* = {:.3f}".
                     format(test_func.minv, test_func.x_star.x, test_func.x_star.x))
print("")
print("### BRMC ###")
plot_par.alg = "BRMC"
min_val, x_star, obj_hist_brmc = brmc_opt(test_func.f, brmc_par, plot_par)
print("Min obj. value = {:.3f}, x* = {:.3f}, y* = {:.3f}".
                     format(min_val, x_star.x, x_star.y))
print("Exact solution = {:.3f}, x* = {:.3f}, y* = {:.3f}".
                     format(test_func.minv, test_func.x_star.x, test_func.x_star.x))
plot_converg(obj_hist_de, obj_hist_brmc, test_func.minv)