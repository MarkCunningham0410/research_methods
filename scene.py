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