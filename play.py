from manim import *
import manim.utils.rate_functions as rf


class LinearTransformationSceneExample(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates = True,
            leave_ghost_vectors = True,
        )

    def construct(self):
        matrix = [[-5, 2],
                  [2, 3]]
        self.apply_matrix(matrix)
        self.wait()


def complex_func(point):
    return complex_to_R3(R3_to_complex(point) ** 2)

class ComplexTransformation(LinearTransformationScene):
    def construct(self):
        square = Square().scale(2)

        self.add_transformable_mobject(square)

        self.apply_nonlinear_transformation(complex_func)

        self.wait()


class CreateStar(Scene):
    def construct(self):
        star = Star(color = YELLOW)
        star.set_fill(PURPLE, opacity = 0.5)
        self.play(DrawBorderThenFill(star))
        self.play(Rotate(star, angle = 2*PI / 5))


class LateXExample(Scene):
    def construct(self):
        e_taylor_series = MathTex(
            r"e^x = x^0 + x^1 + \frac{1}{2} x^2 + \frac{1}{6} x^3 + \cdots + \frac{1}{n!} x^n + \cdots",
            substrings_to_isolate = "x"
        )
        e_taylor_series.set_color_by_tex("x", YELLOW)
        e_complex_exp = MathTex(
            r"e^{i\theta} = \cos(\theta) + i\sin(\theta)"
        )

        self.play(Write(e_taylor_series))
        self.wait()

        self.play(e_taylor_series.animate.shift(UP))
        self.wait()

        e_complex_exp.shift(DOWN)
        self.play(Write(e_complex_exp))


class PlayWithShapes(Scene):
    def construct(self):
        round_rect = RoundedRectangle(color = RED)
        ellipse = Ellipse(color = BLUE)
        triangle = Triangle(color = ORANGE)
        hexagram = Polygram(
            [[0, 2, 0], [-np.sqrt(3), -1, 0], [np.sqrt(3), -1, 0]],
            [[-np.sqrt(3), 1, 0], [0, -2, 0], [np.sqrt(3), 1, 0]],
            color = MAROON
        ).scale(0.5)

        self.play(FadeIn(round_rect))
        self.wait()

        self.play(round_rect.animate.set_fill(PINK, opacity = 0.5))
        self.wait()

        self.play(Rotate(round_rect, angle = 5 * PI, rate_func = rf.ease_in_out_cubic),
                  run_time = 5)
        self.wait()

        self.play(round_rect.animate.shift(2 * LEFT),
                  FadeIn(ellipse),
                  ellipse.animate.shift(2 * RIGHT))
        self.wait()

        self.play(ellipse.animate.set_fill(PURPLE, opacity = 0.5))
        self.wait()

        self.play(Rotate(round_rect, angle = 10 * PI, rate_func = rf.ease_in_out_back),
                  Rotate(ellipse,    angle = 10 * PI, rate_func = rf.ease_in_out_elastic),
                  run_time = 5)
        self.wait()

        self.play(FadeIn(triangle),
                  triangle.animate.shift(2 * UP))
        self.wait()

        self.play(triangle.animate.set_fill(YELLOW, opacity = 0.5))
        self.wait()

        self.play(Rotate(round_rect, angle = 15 * PI, rate_func = rf.ease_in_out_quart),
                  Rotate(ellipse,    angle = 15 * PI, rate_func = rf.ease_in_out_quint),
                  Rotate(triangle,   angle = 15 * PI, rate_func = rf.ease_in_out_expo),
                  run_time = 5)
        self.wait()

        self.play(FadeIn(hexagram),
                  hexagram.animate.shift(2.2 * DOWN))
        self.wait()

        self.play(hexagram.animate.set_fill(GOLD, opacity = 0.5))
        self.wait()

        self.play(Rotate(round_rect, angle = 20 * PI, rate_func = rf.ease_in_out_quad),
                  Rotate(ellipse,    angle = 20 * PI, rate_func = rf.ease_in_out_circ),
                  Rotate(triangle,   angle = 20 * PI, rate_func = rf.ease_in_out_bounce),
                  Rotate(hexagram,   angle = 20 * PI, rate_func = rf.ease_in_out_sine),
                  run_time = 5)
        self.wait()