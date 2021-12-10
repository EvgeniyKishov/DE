import sys

from DE import *
from BRMC import *
from testf import *

import shutil
shutil.rmtree("DE_plots", ignore_errors=True)
shutil.rmtree("BRMC_plots", ignore_errors=True)

#redirect console output to file
sys.stdout = open("output.txt", "w")

#test function:
test_func = ackley()
#test_func = rastrigin()
#test_func = beale()
#test_func = sphere()
#test_func = rosenbrock()

pop_num = 25

#parameters
de_par = de_param()
de_par.pop_num = pop_num
de_par.xrange = test_func.xrange
de_par.yrange = test_func.yrange
de_par.F = 0.5
de_par.cr = 0.9
de_par.it_num = 20

brmc_par = brmc_param()
brmc_par.xrange = test_func.xrange
brmc_par.yrange = test_func.yrange
brmc_par.best = 0.1
brmc_par.mut = 0.5
brmc_par.rand = 0.1
brmc_par.cross = 0.3
brmc_par.paren = 0.6
brmc_par.pop_num = pop_num
brmc_par.d = 0.3
brmc_par.it_num = 20

plot_par = plot_data()
plot_par.xrange = test_func.xrange
plot_par.yrange = test_func.yrange
plot_par.lines_num = 20
plot_par.step = 0.05
plot_par.plot_pop = True
plot_par.plot_conv = True

x0 = init(test_func.xrange, test_func.yrange, pop_num)

print("### DE ###")
plot_par.alg = "DE"
min_val, x_star, obj_hist_de = de_opt(test_func.f, de_par, plot_par, x0)
print("Min obj. value = {:.3f}, x* = {:.3f}, y* = {:.3f}".
                     format(min_val, x_star.x, x_star.y))
print("Exact solution = {:.3f}, x* = {:.3f}, y* = {:.3f}".
                     format(test_func.minv, test_func.x_star.x, test_func.x_star.y))
print("")
print("### BRMC ###")
plot_par.alg = "BRMC"
min_val, x_star, obj_hist_brmc = brmc_opt(test_func.f, brmc_par, plot_par, x0)
print("Min obj. value = {:.3f}, x* = {:.3f}, y* = {:.3f}".
                     format(min_val, x_star.x, x_star.y))
print("Exact solution = {:.3f}, x* = {:.3f}, y* = {:.3f}".
                     format(test_func.minv, test_func.x_star.x, test_func.x_star.y))
sys.stdout.close()
plot_converg(obj_hist_de, obj_hist_brmc, test_func.minv)

