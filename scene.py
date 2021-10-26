from math import pi
from manim import *


class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set color and transparency

        square = Square()  # create a square
        square.rotate(PI/4)  # rotate a certain amount

        self.play(Create(square))  # animate the creation of the square
        self.play(Transform(square, circle))  # interpolate the square into the circle
        self.play(FadeOut(square))  # fade out animation


class HelloWorld(Scene):
    def construct(self):
        text = Text("Hello world", font_size=144)
        self.add(text)


class MathTeXDemo(Scene):
    def construct(self):
        rtarrow0 = MathTex(r"\xrightarrow{x^6y^8}", font_size=96)
        rtarrow1 = Tex(r"$\xrightarrow{x^6y^8}$", font_size=96)

        self.add(VGroup(rtarrow0, rtarrow1).arrange(DOWN))


class MovingFrameBox(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        title = Text("Snell's Law", color = BLACK, font_size=180)
        title.generate_target()
        title.target.shift(UP*5)

        text=MathTex(
            "\\frac{n_1}{n_2}",
            "=",
            "\\frac{\\sin{\\theta_2}}{\\sin{\\theta_1}}", color = BLACK, font_size=130
        )

        framebox1 = SurroundingRectangle(text[0], buff = .1, color=RED)
        framebox2 = SurroundingRectangle(text[2], buff = .1, color=RED)

        self.play(Write(title))
        self.play(MoveToTarget(title))
        self.play(Write(text))
        self.play(
            Create(framebox1),
        )
        self.wait()
        self.play(
            ReplacementTransform(framebox1,framebox2),
        )
        self.wait()


class Clock(VGroup):
    CONFIG = {}

    def __init__(self, **kwargs):
        circle = Circle(color=WHITE)
        ticks = []
        for x in range(12):
            alpha = x / 12.
            point = complex_to_R3(
                np.exp(2 * np.pi * alpha * complex(0, 1))
            )
            length = 0.2 if x % 3 == 0 else 0.1
            ticks.append(
                Line(point, (1 - length) * point)
            )
        self.hour_hand = Line(ORIGIN, 0.3 * UP)
        self.minute_hand = Line(ORIGIN, 0.6 * UP)
        # for hand in self.hour_hand, self.minute_hand:
        #     #Balance out where the center is
        #     hand.add(VectorizedPoint(-hand.get_end()))

        VGroup.__init__(
            self, circle,
            self.hour_hand, self.minute_hand,
            *ticks
        )

class m(Scene):
    config.background_color=BLACK
    def construct(self):
        self.add(Clock())

class piadslogowhite(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        colours = ['#c531b0'] + ['#3f0697','#041fa2','#234588','#00afed','#51a84f','#83c079','#fdef29', '#fe8b4e', '#ff5200', '#cd2830', WHITE]
        colours2 = ['#c531b0'] + ['#3f0697','#041fa2','#234588','#00afed','#51a84f','#83c079','#fdef29', '#fe8b4e', '#ff5200', '#cd2830', WHITE]
        
        mobjects = [RoundedRectangle(height = 0.3, width = 0.8, corner_radius=0.15, color= i, fill_opacity = 1, fill_color = i,) for i in colours]
        mobjects2 = [RoundedRectangle(height = 0.3, width = 0.8, corner_radius=0.15, color= i, fill_opacity = 1, fill_color = i,) for i in colours2]
        
        angle1, angle2 = PI/6., PI/6.

        new_mobjects_1 = []
        new_mobjects_2 = []

        for i, (mobject, mobject2) in enumerate(zip(mobjects,mobjects2)):
            if colours[i] !=WHITE:
                mobject = mobject.rotate(angle = angle1, about_point = 2*RIGHT)
                new_mobjects_1.append(mobject)
            if colours2[i] != WHITE:
                mobject2 = mobject2.rotate(angle = -angle2, about_point = 2*LEFT).rotate(angle=PI/3., about_point=ORIGIN)
                mobject2 = mobject2.shift(0.3*DOWN+0.5*LEFT)
                new_mobjects_2.append(mobject2)
            angle2+= PI/6.
            angle1-= PI/6.

        vg1 = VGroup()
        vg2 = VGroup()

        for element in new_mobjects_1:
            vg1.add(element)
        for element in new_mobjects_2:
            vg2.add(element)
        
        vg1.shift(3.5*UP+ 0.5*LEFT)
        vg2.shift(3.5*UP+ 0.5*LEFT)
        
        animations1 = [FadeIn(obj) for obj in vg1]
        animations2 = [FadeIn(obj) for obj in vg2]
        flash_animations1 = [Flash(obj, color=obj.color, line_length=0.2, num_lines=10, flash_radius=0.35, time_width=0.3, run_time=2, rate_func = rush_from) for obj in vg1]
        flash_animations2 = [Flash(obj, color=obj.color, line_length=0.2, num_lines=10, flash_radius=0.35, time_width=0.3, run_time=2, rate_func = rush_from) for obj in vg2]
        
        piads_title1 = Text('EPSRC and SFI Centre ', color= BLACK).scale(2)
        piads_title2 = Text('for Doctoral Training in', color= BLACK).scale(2)
        piads_title3 = Text('Photonic Integration ', color= BLACK).scale(2)
        piads_title4 = Text('and Advanced Data Storage', color= BLACK).scale(2)

        title_whole = VGroup(piads_title1, piads_title2, piads_title3, piads_title4).arrange(direction=DOWN,aligned_edge = LEFT).scale_in_place(0.7)
        title_whole.shift(DOWN*4+RIGHT*0.8)
        self.wait(0.4)  
        self.play(AnimationGroup(*animations1, lag_ratio = 0.2), AnimationGroup(*animations2,lag_ratio= 0.2))
        self.play(AnimationGroup(*flash_animations1, lag_ratio=0), AnimationGroup(*flash_animations2, lag_ratio=0))
        self.play(FadeIn(title_whole))
        self.wait(2)


class piadslogoblack(Scene):
    def construct(self):
        self.camera.background_color = BLACK
        colours = ['#c531b0'] + ['#3f0697','#041fa2','#234588','#00afed','#51a84f','#83c079','#fdef29', '#fe8b4e', '#ff5200', '#cd2830', BLACK]
        colours2 = ['#c531b0'] + ['#3f0697','#041fa2','#234588','#00afed','#51a84f','#83c079','#fdef29', '#fe8b4e', '#ff5200', '#cd2830', BLACK]
        
        mobjects = [RoundedRectangle(height = 0.3, width = 0.8, corner_radius=0.15, color= i, fill_opacity = 1, fill_color = i,) for i in colours]
        mobjects2 = [RoundedRectangle(height = 0.3, width = 0.8, corner_radius=0.15, color= i, fill_opacity = 1, fill_color = i,) for i in colours2]
        
        angle1, angle2 = PI/6., PI/6.

        new_mobjects_1 = []
        new_mobjects_2 = []

        for i, (mobject, mobject2) in enumerate(zip(mobjects,mobjects2)):
            if colours[i] !=BLACK:
                mobject = mobject.rotate(angle = angle1, about_point = 2*RIGHT)
                new_mobjects_1.append(mobject)
            if colours2[i] != BLACK:
                mobject2 = mobject2.rotate(angle = -angle2, about_point = 2*LEFT).rotate(angle=PI/3., about_point=ORIGIN)
                mobject2 = mobject2.shift(0.3*DOWN+0.5*LEFT)
                new_mobjects_2.append(mobject2)
            angle2+= PI/6.
            angle1-= PI/6.

        vg1 = VGroup()
        vg2 = VGroup()

        for element in new_mobjects_1:
            vg1.add(element)
        for element in new_mobjects_2:
            vg2.add(element)
        
        vg1.shift(3.5*UP+ 0.5*LEFT)
        vg2.shift(3.5*UP+ 0.5*LEFT)
        
        animations1 = [FadeIn(obj) for obj in vg1]
        animations2 = [FadeIn(obj) for obj in vg2]
        flash_animations1 = [Flash(obj, color=obj.color, line_length=0.2, num_lines=10, flash_radius=0.35, time_width=0.3, run_time=2, rate_func = rush_from) for obj in vg1]
        flash_animations2 = [Flash(obj, color=obj.color, line_length=0.2, num_lines=10, flash_radius=0.35, time_width=0.3, run_time=2, rate_func = rush_from) for obj in vg2]
        
        piads_title1 = Text('EPSRC and SFI Centre ', color= WHITE).scale(2)
        piads_title2 = Text('for Doctoral Training in', color= WHITE).scale(2)
        piads_title3 = Text('Photonic Integration ', color= WHITE).scale(2)
        piads_title4 = Text('and Advanced Data Storage', color= WHITE).scale(2)

        title_whole = VGroup(piads_title1, piads_title2, piads_title3, piads_title4).arrange(direction=DOWN,aligned_edge = LEFT).scale_in_place(0.7)
        title_whole.shift(DOWN*4+RIGHT*0.8)
        self.wait(0.4)  
        self.play(AnimationGroup(*animations1, lag_ratio = 0.2), AnimationGroup(*animations2,lag_ratio= 0.2))
        self.play(AnimationGroup(*flash_animations1, lag_ratio=0), AnimationGroup(*flash_animations2, lag_ratio=0))
        self.play(FadeIn(title_whole))
        self.wait(2)
