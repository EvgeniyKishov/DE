from DE import *
from testf import *

#parameters
de_par = de_param()
de_par.pop_num = 20
de_par.min_val = -4.5
de_par.max_val = 4.5
de_par.F = 0.5
de_par.cr = 0.9
de_par.it_num = 5

plot_par = plot_data()
plot_par.max = 5.0
plot_par.min = -5.0
plot_par.lines_num = 20
plot_par.plot_pop = False
plot_par.plot_conv = False

min_val, p_star = de_opt(ackley, de_par, plot_par)
print("Min obj. value = {:.3f}, x* = {:.3f}, y* = {:.3f}".
                     format(min_val, p_star.x, p_star.y))
