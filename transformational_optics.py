import numpy as np
from manim import *
# To open the movie after render.
from manim.utils.file_ops import open_file as open_media_file
\

radius = 3 # radius inside which circle becomes empty

def transf(p):
    # print(p)
    x, y, z = p[0], p[1], p[2]
    xv, yv = abs(x), abs(y)

    r = np.sqrt(x**2 + y**2)
    d_r = np.exp(- (r**2) / radius**2 ) # delta r

    cs = xv / (r) # cos and sin of angle to project delta_r
    sn = yv / (r)

    return [x + np.sign(x)*cs*d_r, y + np.sign(y)*sn*d_r, 0]

color

class transformation_optic(Scene):
    def construct(self):
        xrange = (-7, 7, 1)
        yrange = (-7, 7, 1)
        grid = NumberPlane(xrange, yrange, background_line_style={"stroke_color":YELLOW_B}, hide_x_axis=True, hide_y_axis=True)
        # https://docs.manim.community/en/stable/reference/manim.utils.color.Colors.html?highlight=colors
        print(grid.axis_config)
        xax = grid.get_x_axis()
        # xax.z_index = -1
        # grid.x_axis_config.update({"stroke_opacity": 0, "stroke_color": RED}) #doesn't work
        yax = grid.get_y_axis()
        # yax.z_index = -1

        # line = Line([-2,1,0],[2,1,0],).set_color(RED)
        # self.add(grid, line)

        # self.play(Create(grid,run_time=3,lag_ratio = 0.1))
        self.play(Create(grid,run_time=0.5,lag_ratio = 0.1))
        grid.prepare_for_nonlinear_transform()

        self.play(
            *[grid.animate.apply_function(transf)], run_time = 3
        )
        # self.play(line.animate.apply_function(transf), run_time = 2)
        self.wait()



if __name__ == '__main__':
    scene = transformation_optic()
    scene.render()  # That's it!

    # Here is the extra step if you want to also open
    # the movie file in the default video player
    # (there is a little different syntax to open an image)
    open_media_file(scene.renderer.file_writer.movie_file_path)