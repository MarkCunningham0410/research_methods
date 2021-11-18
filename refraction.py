from manim import *

class refraction_block(Scene):
    def construct(self):

        # Instantiating Block
        block_object = Rectangle(height = 3, width = 8, color=BLACK, fill_opacity = 1,  fill_color = BLUE)
        #halfway_line = DashedLine(start= np.array([-1* block_object.width/2.,0.,0.]),end = np.array([block_object.width/2.,0.,0.]) , dash_length = 0.2)
        normal = DashedLine(start= np.array([0.,block_object.height*1.5,0.]),end = np.array([0.,-1.5*block_object.height,0.]) , dash_length = 0.2, color = BLACK)
        # Instantiating Incident Ray
        rotation_centre = [0., 0.5*block_object.height, 0.]
        
        angle_tracker = ValueTracker(80)
        line_moving = Arrow([-1.5, block_object.height*1.5, 0.], [0., 0.5*block_object.height, 0.])
        line_ref = normal.copy()

        line_moving.rotate(1 * DEGREES, about_point = rotation_centre)
        
        a = Angle(normal, line_moving, radius=0.5, other_angle = False)
        
        line_moving.add_updater(
            lambda x: x.rotate(line_ref.copy()).rotate(
                1*DEGREES, about_point=rotation_centre
            )
        )

        a.add_updater(
            lambda x: x.become(Angle(normal, line_moving, radius=0.5, other_angle=False))
        )

        self.play(FadeIn(block_object))
        #self.play(FadeIn(halfway_line))
        self.play(FadeIn(normal))
        self.add(line_moving, a)
        self.play(angle_tracker.animate.set_value(40))
        self.play(angle_tracker.animate.increment_value(140))
        self.play(angle_tracker.animate.set_value(350))
