import numpy as np
from manim import *

radius = 1 # radius inside which circle becomes empty
radius2 = 2

def transf(p):
    # print(p)
    x, y, z = p[0], p[1], p[2]
    xv, yv = abs(x), abs(y)
    # EPSILON = 1e-6
    # if abs(x) < EPSILON: x = 0
    # if abs(y) < EPSILON: y = 0

    r = np.sqrt(x**2 + y**2)
    d_r = np.exp(- (r**2) / radius2**2 ) # delta r

    # d_r = 1 / (1 + r**2) # delta_r -> too sharp for all powers
    # d_r = 1/abs(x + y) if (x!= 0 and y != 0) else 0  # delta_r -> doesn't work

    cs = xv / (r) # cos and sin of angle to project delta_r
    sn = yv / (r)

    return [x + np.sign(x)*cs*d_r, y + np.sign(y)*sn*d_r, 0]


    # return [x + np.sign(x)*cs*np.exp(-x**2), y + np.sign(y)*sn*np.exp(-y**2), 0]

    # def singlecos(x):
    #     # if -np.pi / (2*radius) < x < np.pi / (2*radius):
    #     if -radius/4 < x < radius/4:
    #         return np.cos(2*np.pi*x / radius)
    #     else:
    #         return 0


    # k = 3 # decay rate of amplitude
    # amp=0.4
    # return [x + singlecos(y)/(k*x), y + singlecos(x)/(k*y), 0]
    # return [x + amp*np.sign(x)*singlecos(y)/(1+xv), y + amp*np.sign(y)*singlecos(x)/(1+yv), 0]


class transformation_optic(Scene):
    def construct(self):
        xrange = (-7, 7, 0.5)
        yrange = (-4, 4, 0.5)
        grid = NumberPlane(xrange, yrange, background_line_style={"stroke_color":YELLOW_B})
        # https://docs.manim.community/en/stable/reference/manim.utils.color.Colors.html?highlight=colors
        # grid.axis_config.update({ "include_ticks":True})
        line = Line([-2,1,0],[2,1,0],).set_color(RED)
        self.add(grid, line)

        # self.play(Create(grid,run_time=3,lag_ratio = 0.1))
        self.play(Create(grid,run_time=0.5,lag_ratio = 0.1))
        grid.prepare_for_nonlinear_transform()

        self.play(
            grid.animate.apply_function(transf), run_time = 3
        )
        self.play(
            line.animate.apply_function(transf), run_time = 2
        )
        self.wait()
