from manim import *
from numpy import sqrt

class Snell(Scene):
    def construct(self):
        theta = ValueTracker(np.arctan(1/3)) 
        theta2 = ValueTracker((np.sin(0.75*np.sin(theta.get_value())))) # the refracted angle's value

        midplane = Line(start = (-6,0,0), end = (6,0,0))
        normal = Line(start = (0,-3,0), end = (0,3,0))
        normal = DashedVMobject(normal)
        inc_start = (-6, 2, 0)
        inc_finish = (0,0, 0)
        refrac_start = (0,0,0)
        refrac_fin = (2, -3, 0) # magnitude of this matters but the coordinates really don't...
        in_arrow = Arrow(start = inc_start, end = inc_finish)
        out_arrow = Arrow(start = refrac_start, end = refrac_fin, angle_of_vector = 3*PI/2)
        # ... because the set_angle method effectively changes the coords here, before it is called onscreen
        out_arrow.set_angle(3*PI/2 + np.sin(0.75*np.sin(theta.get_value())))
        left_arc = Arc()
        left_arc.add_updater(
            lambda m: m.become(
                Arc(
            radius = 1.5,
            start_angle = PI/2,
            angle = PI/2 - theta.get_value()
            )))
        right_arc = Arc()
        right_arc.add_updater(
            lambda m: m.become(
                Arc(
            radius = 1.5,
            start_angle = 3*PI/2,
            angle = np.sin(0.75*np.sin(theta.get_value()))
            )))
        label_1 = TexMobject('\\theta_{1}')
        label_2 = TexMobject('\\theta_{2}')
        label_1.add_updater(
            lambda m: m.move_to(left_arc).shift(.165*LEFT+.8*UP))
        label_2.add_updater(
            lambda m: m.move_to(right_arc).shift(.165*RIGHT+.8*DOWN))
        self.add(midplane, normal, in_arrow, left_arc, label_1)
        self.wait()
        self.play(GrowArrow(out_arrow))
        in_arrow.add_updater(
            lambda m: 
            m.become(
                # we use become here because I need to move the arrow's start, which would be fixed if we didn't redefine it like so
                Arrow(start = (-(sqrt(40)*np.cos(theta.get_value())), (sqrt(40)*np.sin(theta.get_value())), 0), end = inc_finish)
                ))
        out_arrow.add_updater(
            # but in this case we can use the set_angle method because all we have to do is rotate it.
            lambda m: m.set_angle(3*PI/2 + np.sin(0.75*np.sin(theta.get_value()))))
        self.play(ShowCreation(right_arc))
        self.play(Write(label_2))
        self.play(theta.increment_value, PI/3- np.arctan(1/3), rate_func = there_and_back, run_time = 2) 
        self.wait()
        self.play(ApplyMethod(in_arrow.rotate, PI))
        self.wait()