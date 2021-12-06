import numpy as np
from manim import *
# To open the movie after render.
from manim.utils.file_ops import open_file as open_media_file
from manim.mobject.geometry import ArrowTriangleFilledTip


radius = 4 # radius inside which circle becomes empty
# bg_color = config.background_color
timings = [1.5, 1, 2, 2.7,3,1]

def transf(p):
    # print(p)
    x, y, z = p[0], p[1], p[2]
    xv, yv = abs(x), abs(y)
    r = np.sqrt(x**2 + y**2)
    d_r = np.exp(- (r**2) / (radius**2) ) # delta r

    cs = xv / (r) # cos and sin of angle to project delta_r
    sn = yv / (r)

    rad_in = np.exp(-1/(radius**2))

    xnew = x + np.sign(x)*cs*d_r
    ynew = y + np.sign(y)*sn*d_r
    return [xnew, ynew, 0]


class transformation_optic(Scene):
    def construct(self):
        xrange = (-7, 7, 1)
        yrange = (-7, 7, 1)
        grid = NumberPlane(xrange, yrange, background_line_style={"stroke_color":YELLOW_B},
                           axis_config={"stroke_color":RED}) # hide_x_axis=True, hide_y_axis=True
        # https://docs.manim.community/en/stable/reference/manim.utils.color.Colors.html?highlight=colors
        print(grid)
        xax = grid.get_x_axis()
        # xax.z_index = -1
        # grid.x_axis_config.update({"stroke_color": RED}) #doesn't work
        yax = grid.get_y_axis()
        # yax.z_index = -1

        # line = Line([-2,1,0],[2,1,0],).set_color(RED)
        # self.add(grid, line)

        # self.play(Create(grid,run_time=3,lag_ratio = 0.1))

        tip_left_coord = 3.5
        # create arrow heads
        tips = []
        for i in [2,4,-2,-4]:
            tip = ArrowTriangleFilledTip(length = 0.3, start_angle=0, color=YELLOW_B)
            tip.shift(tip_left_coord*LEFT, i*UP)
            tips.append(tip)

        text_ray = Text('light rays', color= YELLOW_B).scale(1.2).shift(4.5*LEFT,2.5*UP)


        self.play(Create(grid,run_time=timings[0],lag_ratio = 0.1))
        self.play(*[Create(tipp) for tipp in tips], run_time=timings[1])
        self.play(Create(text_ray),run_time = timings[1])

        self.play(*[tipp.animate.shift(12*RIGHT) for tipp in tips], run_time=1.5)
        self.play(Uncreate(text_ray), run_time=1)
        grid.prepare_for_nonlinear_transform()


        self.wait(timings[2])

        self.play(grid.animate.apply_function(transf), run_time = timings[3])
        # self.play(line.animate.apply_function(transf), run_time = 2)
        self.wait(timings[4])
        self.play(Uncreate(grid,run_time=timings[5],lag_ratio = 0.1))




if __name__ == '__main__':
    scene = transformation_optic()
    scene.render()  # That's it!

    # Here is the extra step if you want to also open
    # the movie file in the default video player
    # (there is a little different syntax to open an image)
    open_media_file(scene.renderer.file_writer.movie_file_path)
