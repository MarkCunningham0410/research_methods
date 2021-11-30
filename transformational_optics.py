import numpy as np
from manim import *

def transformation_function():
    return True

class transformation_optic(Scene):
    def construct(self):
        grid = ComplexPlane()
        self.add(grid)

        self.play(Create(grid,run_time=3,lag_ratio = 0.1))

        grid.prepare_for_nonlinear_transform()

        self.play(
            grid.animate.apply_function(
                lambda p: p
                + np.array(
                    [
                        1/(p[1]),
                        1/(p[0]),
                        0,
                    ]
                )
            ),
            run_time = 3
        )
        self.wait()
