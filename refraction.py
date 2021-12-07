from manim import *
import numpy as np
from numpy.core.shape_base import block

def snell_law(incident_angle, n1, n2):
    refractive_angle = np.arcsin((n1/n2) * np.sin(incident_angle))
    return refractive_angle

class refraction_block_positive(Scene):
    def construct(self):
        n2 = ValueTracker(2.5) #refractive index
        # Instantiating Block
        block_object = Rectangle(
            height=0.01, width=12, color=BLUE, fill_opacity=0.5, fill_color=BLUE
        )
        
        normal = DashedLine(
            start=-3 * UP,
            end=3 * UP,
            dash_length=0.2,
            color=RED,
            stroke_width = 5
        )
        rotation_centre = ORIGIN

        angle_tracker = ValueTracker(0.00001)  # initial angle from normal
        
        line_moving = Line(
            start=3 * UP, # <-- change this,
            end= ORIGIN,   # <-- and this instead of block_object.height
            buff = 0,
            color = YELLOW_B,
            stroke_width = 8
        )
        
        line_refract = Line(
            start=ORIGIN,
            end=3*DOWN,
            buff=0,
            color=YELLOW_B,
            stroke_width=8
        )
        triangle_incident = Triangle(fill_color=YELLOW_D, fill_opacity=1, stroke_width=0).scale(0.2)


        line_moving.rotate(
            angle_tracker.get_value() * DEGREES,
            about_point=rotation_centre,
        )
        
        line_refract.rotate(
            angle_tracker.get_value() * DEGREES,
            about_point=rotation_centre,
        )
        
        
        
        triangle_incident.move_to(line_moving.get_center()).rotate(180 * DEGREES)
        # line_refract = line_moving.copy().rotate(PI, about_point = rotation_centre)
        
        line_ref = line_moving.copy()
        line_ref1 = line_refract.copy()
        
        triangle_ref = triangle_incident.copy()
        
        triangle_refract = triangle_incident.copy().move_to(line_refract.get_center())
        triangle_ref1 = triangle_refract.copy()

        a = Angle(
            normal,
            line_moving.copy().scale(-1),
            quadrant=(1, 1),
            radius=1,
            other_angle=False if angle_tracker.get_value() > 0 else True,
        )
        
        a1 = Angle(
            normal,
            line_refract.copy(),
            quadrant=(-1, -1),
            radius=1,
            other_angle=False if angle_tracker.get_value() > 0 else True,
        )
        
        tex_incident = MathTex(r"\theta_i").move_to(a.point_from_proportion(0.5))
        tex_refract = MathTex(r"\theta_r").move_to(a1.point_from_proportion(0.5))
        
        # updaters
        line_moving.add_updater(
            lambda x: x.become(line_ref.copy()).rotate(
                angle_tracker.get_value() * DEGREES, about_point=rotation_centre
            )
        )

        triangle_incident.add_updater(
            lambda x: x.become(triangle_ref.copy()).rotate(
                angle_tracker.get_value() * DEGREES, about_point=rotation_centre
            )
        )
        
        line_refract.add_updater(
            lambda x: x.become(line_ref1.copy()).rotate(
                np.arcsin(np.sin(angle_tracker.get_value()*DEGREES)/n2.get_value()), about_point=rotation_centre
            )
        )
        
        triangle_refract.add_updater(
            lambda x: x.become(triangle_ref1.copy()).rotate(
                np.arcsin(np.sin(angle_tracker.get_value()*DEGREES)/n2.get_value()), about_point=rotation_centre
            )
        )

        a.add_updater(
            lambda x: x.become(
                Angle(
                    normal,
                    line_moving.copy().scale(-1),
                    quadrant=(1, 1),
                    radius=1,
                    other_angle=False if angle_tracker.get_value() > 0 else True,
                )
            )
        )
        
        a1.add_updater(
            lambda x: x.become(
                Angle(
                    normal,
                    line_refract.copy(),
                    quadrant=(-1, 1),
                    radius=1,
                    other_angle=False if (angle_tracker.get_value()>0 and n2.get_value()> 0) or (angle_tracker.get_value()<0 and n2.get_value()<0) 
                    else True,
                )
            )
        )
        
        
        tex_incident.add_updater(
            lambda x: x.move_to(
                a.point_from_proportion(0.5) + UP*0.4
            )
        )
        
        tex_refract.add_updater(
            lambda x: x.move_to(
                a1.point_from_proportion(0.5) + DOWN*0.4
            )
        )

        n1_text = MathTex(r"n_1 = 1", color= RED).shift(RIGHT*4 + UP)
        n2_text = MathTex(r"n_2 = {}".format(str(n2.get_value())[0:4]), color= RED).shift(RIGHT*4 + DOWN*0.5)

        n2_text.add_updater(
            lambda x: x.become(MathTex(r"n_2 = {}".format(str(n2.get_value())[0:4]), color= RED).shift(RIGHT*4 + DOWN*0.5)
        ))





        snells_words = Text("Snell's Law", font_size=100)
        snells_words.generate_target()
        snells_words.move_to(4*UP)
        snells_words.target.move_to(5*UP)

        snells_eq=MathTex(
            "\\frac{n_1}{n_2}",
            "=",
            "\\frac{\\sin{\\theta_2}}{\\sin{\\theta_1}}", font_size=80
        )
        snells_eq.generate_target()
        snells_eq.move_to(3*RIGHT + 3*UP)
        snells_eq.target.move_to(UP*5 + 3*RIGHT)

        # framebox1 = SurroundingRectangle(text[0], buff = .1, color=RED)
        # framebox2 = SurroundingRectangle(text[2], buff = .1, color=RED)






        self.play(FadeIn(block_object), run_time=0.5)
        self.play(FadeIn(normal), run_time=0.5)

        #


        self.play(AnimationGroup(
            FadeIn(line_refract),
            FadeIn(line_moving),
            FadeIn(triangle_incident),
            FadeIn(triangle_refract),
        ), run_time=0.5
                 )
        #2.5 sec

        # self.play(angle_tracker.animate.increment_value(0.002))
        self.play(angle_tracker.animate.increment_value(25), run_time=0.75)
        self.play(FadeIn(a),
                  FadeIn(a1), run_time=0.75)
        self.wait(0.75)

        #4 sec

        #UP TO HERE
        #Snell's law words and equation appear and move
        self.play(angle_tracker.animate.increment_value(60))
        self.play(angle_tracker.animate.set_value(-50))
        self.play(Write(snells_words))
        self.play(MoveToTarget(snells_words))
        self.play(Write(snells_eq))
        self.wait(1)
        self.play(Indicate(snells_eq[0],color=WHITE))
        self.play(FadeOut(snells_words))
        self.play(MoveToTarget(snells_eq))

        self.play(AnimationGroup(FadeIn(n1_text), FadeIn(n2_text)))
        self.wait()


        self.play(FadeIn(tex_incident), FadeIn(tex_refract))
        self.play(n2.animate.increment_value(2))
        self.wait()
        self.play(n2.animate.increment_value(-2))
        self.wait(2)
        self.play(Indicate(snells_eq[0],color=WHITE))

        self.play(FadeToColor(snells_eq[0], color=RED_C))
        self.wait(0.5)
        self.play(FadeToColor(snells_eq[0], color=BLUE_D))
        self.wait(2)



class refraction_block_negative(Scene):
    def construct(self):
        n2 = ValueTracker(-1) #refractive index
        # Instantiating Block
        block_object = Rectangle(
            height=0.01, width=12, color=BLUE, fill_opacity=0.5, fill_color=BLUE
        )

        normal = DashedLine(
            start=-3 * UP,
            end=3 * UP,
            dash_length=0.2,
            color=RED,
            stroke_width = 5
        )
        rotation_centre = ORIGIN

        angle_tracker = ValueTracker(0.00001)  # initial angle from normal

        line_moving = Line(
            start=3 * UP, # <-- change this,
            end= ORIGIN,   # <-- and this instead of block_object.height
            buff = 0,
            color = YELLOW_B,
            stroke_width = 8
        )

        line_refract = Line(
            start=ORIGIN,
            end=3*DOWN,
            buff=0,
            color=YELLOW_B,
            stroke_width=8
        )
        triangle_incident = Triangle(fill_color=YELLOW_D, fill_opacity=1, stroke_width=0).scale(0.2)


        line_moving.rotate(
            angle_tracker.get_value() * DEGREES,
            about_point=rotation_centre,
            )

        line_refract.rotate(
            angle_tracker.get_value() * DEGREES,
            about_point=rotation_centre,
            )



        triangle_incident.move_to(line_moving.get_center()).rotate(180 * DEGREES)
        # line_refract = line_moving.copy().rotate(PI, about_point = rotation_centre)


        NegRefText = Text("Negative Refraction", font_size=100)
        NegRefText.move_to(4*UP)


        line_ref = line_moving.copy()
        line_ref1 = line_refract.copy()

        triangle_ref = triangle_incident.copy()

        triangle_refract = triangle_incident.copy().move_to(line_refract.get_center())
        triangle_ref1 = triangle_refract.copy()

        a = Angle(
            normal,
            line_moving.copy().scale(-1),
            quadrant=(1, 1),
            radius=1,
            other_angle=False if angle_tracker.get_value() > 0 else True,
        )

        a1 = Angle(
            normal,
            line_refract.copy(),
            quadrant=(-1, -1),
            radius=1,
            other_angle=False if angle_tracker.get_value() > 0 else True,
        )

        tex_incident = MathTex(r"\theta_i").move_to(a.point_from_proportion(0.5))
        tex_refract = MathTex(r"\theta_r").move_to(a1.point_from_proportion(0.5))

        # updaters
        line_moving.add_updater(
            lambda x: x.become(line_ref.copy()).rotate(
                angle_tracker.get_value() * DEGREES, about_point=rotation_centre
            )
        )

        triangle_incident.add_updater(
            lambda x: x.become(triangle_ref.copy()).rotate(
                angle_tracker.get_value() * DEGREES, about_point=rotation_centre
            )
        )

        line_refract.add_updater(
            lambda x: x.become(line_ref1.copy()).rotate(
                np.arcsin(np.sin(angle_tracker.get_value()*DEGREES)/n2.get_value()), about_point=rotation_centre
            )
        )

        triangle_refract.add_updater(
            lambda x: x.become(triangle_ref1.copy()).rotate(
                np.arcsin(np.sin(angle_tracker.get_value()*DEGREES)/n2.get_value()), about_point=rotation_centre
            )
        )

        a.add_updater(
            lambda x: x.become(
                Angle(
                    normal,
                    line_moving.copy().scale(-1),
                    quadrant=(1, 1),
                    radius=1,
                    other_angle=False if angle_tracker.get_value() > 0 else True,
                )
            )
        )

        a1.add_updater(
            lambda x: x.become(
                Angle(
                    normal,
                    line_refract.copy(),
                    quadrant=(-1, 1),
                    radius=1,
                    other_angle=False if (angle_tracker.get_value()>0 and n2.get_value()> 0) or (angle_tracker.get_value()<0 and n2.get_value()<0)
                    else True,
                )
            )
        )


        tex_incident.add_updater(
            lambda x: x.move_to(
                a.point_from_proportion(0.5) + UP*0.4
            )
        )

        tex_refract.add_updater(
            lambda x: x.move_to(
                a1.point_from_proportion(0.5) + DOWN*0.4
            )
        )

        n1_text = MathTex(r"n_1 = 1", color= RED).shift(RIGHT*4 + UP)
        n2_text = MathTex(r"n_2 = {}".format(str(n2.get_value())[0:4]), color= BLUE_D).shift(RIGHT*4 + DOWN*0.5)

        n2_text.add_updater(
            lambda x: x.become(MathTex(r"n_2 = {}".format(str(n2.get_value())[0:4]), color= RED).shift(RIGHT*4 + DOWN*0.5)
                               ))

        self.play(FadeIn(block_object), run_time=0.2)
        self.play(FadeIn(normal), run_time=0.2)

        self.play(AnimationGroup(
            FadeIn(line_refract),
            FadeIn(line_moving),
            FadeIn(triangle_incident),
            FadeIn(triangle_refract),
            FadeIn(n1_text),
            FadeIn(n2_text)
        ), run_time=0.2
        )

        self.play(angle_tracker.animate.increment_value(0.002), run_time=0.2)
        self.play(FadeIn(a),
                  FadeIn(a1), run_time=0.2)

        self.play(angle_tracker.animate.increment_value(10))

        self.play(FadeIn(tex_incident), FadeIn(tex_refract))
        self.wait()
        self.play(angle_tracker.animate.increment_value(30))
        self.play(angle_tracker.animate.set_value(-50))
        self.wait(2)

        self.play(n2.animate.increment_value(-1.5))
        self.wait()
        self.play(AnimationGroup(
        n2.animate.increment_value(1.5), Write(NegRefText)), run_time = 1.2
        )
        self.wait(3)
