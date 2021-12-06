import numpy as np
from manim import *


class rainbow(Scene):
    def construct(self):
        drop = Circle(0.3, color=DARK_BLUE, fill_color=BLUE, fill_opacity=0.5).shift(3*RIGHT)
        drop_edge = drop.get_right()
        drop_label = Text('water droplet', color= BLUE, fill_opacity=0.5).shift(3.5*RIGHT)

        incoming_ray = Line(5*UP + 5*LEFT, drop.get_right(), stroke_width=4, color = YELLOW_B)
        sun = Circle(1, color=RED_A, fill_color=YELLOW_B, fill_opacity=1).shift(5*LEFT + 5*UP)

        rays = []
        colors = [RED, ORANGE, YELLOW_B, GREEN_B, BLUE, PURPLE]

        for i in range(6):
            ray = Line(drop_edge + 0.05*LEFT, 5*DOWN + LEFT*(5+0.2*i), color=colors[i], stroke_width=12)
            rays.append(ray)

        sun_ray = VGroup(sun,incoming_ray)
        vrays = VGroup(*rays)

        self.play(DrawBorderThenFill(sun),run_time=1)
        self.play(Flash(sun, flash_radius=sun.radius*1.5, line_length=0.4, color=YELLOW_B),run_time=0.8)
        self.wait(0.2)
        self.play(Flash(sun, flash_radius=sun.radius*1.5, line_length=0.4, color=YELLOW_B, stay_open=True),run_time=0.8)
        self.wait(0.3)
        self.play(Write(drop_label),run_time=0.5)
        self.play(FadeIn(drop), run_time=0.3)
        # self.play(ScaleInPlace(drop,0.2))
        self.play(Create(incoming_ray),run_time=0.8, )
        self.play(Create(vrays), run_time=2, lag_ratio=0.1)
        self.wait(1)

        # All = VGroup(sun, incoming_ray, drop,vrays)
        All_list = [Uncreate(vrays), Uncreate(incoming_ray), FadeOut(sun), FadeOut(drop), Unwrite(drop_label)]
        self.play(*All_list, run_time=2, lag_ratio=0.1)




if __name__ == '__main__':
    scene = rainbow()
    scene.render()
