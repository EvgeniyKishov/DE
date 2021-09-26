from DE import *
from testf import *

#parameters
de_par = de_param()
de_par.pop_num = 20
de_par.xrange = (-5.0, 5.0)
de_par.yrange = (-5.0, 5.0)
de_par.F = 0.5
de_par.cr = 0.9
de_par.it_num = 25

plot_par = plot_data()
plot_par.max = 5.0
plot_par.min = -5.0
plot_par.lines_num = 20
plot_par.plot_pop = True
plot_par.plot_conv = True

min_val, x_star = de_opt(ackley, de_par, plot_par)
print("Min obj. value = {:.3f}, x* = {:.3f}, y* = {:.3f}".
                     format(min_val, x_star.x, x_star.y))
