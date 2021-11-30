from manim import *

class refraction_block(Scene):
    def construct(self):
        self.camera.background_color = GREY

        block_object = Rectangle(height = 1, width = 5, color=BLACK, fill_opacity = 1,  fill_color = BLUE)

        self.play(DrawBorderThenFill(block_object))
        