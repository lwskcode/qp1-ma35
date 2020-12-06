from manim import *
import numpy as np
import scipy.stats as stats

class Mittelpunktsregel(GraphScene):
    CONFIG={
        "x_min": -1,
        "x_max": 10,
        "x_axis_width": 9,
        "y_min": -1,
        "y_max": 10,
        "y_axis_height": 6
    }
    def construct(self):
        title=TextMobject("Mittelpunktsregel").scale(1.5)
        subtitle=TextMobject("Verfahren zur numerischen Integration I")
        subtitle.next_to(title, DOWN)
        subtitle_alt=TextMobject("Rechtecke unter dem Graphen von $f$")
        subtitle_alt.next_to(title, DOWN)

        self.play(Write(title), Write(subtitle))
        self.wait(2.5)
        self.play(Transform(subtitle,subtitle_alt))
        self.wait(2.5)
        self.play(FadeOut(title), FadeOut(subtitle))

        self.setup_axes(animate=True)                                           #Koordinatensystem anzeigen

        def func(x):
            return 0.1 * (x + 3 - 5) * (x - 3 - 5) * (x - 5) + 5                #Darzustellende Funktion

        graph = self.get_graph(func, x_min=-1, x_max=10)                        #Graphen erstellen
        graph.set_color(RED)
        graph_label = self.get_graph_label(graph, label = "f")

        self.play(ShowCreation(graph), run_time=3)                              #Graphen anzeigen
        self.play(Write(graph_label))
        self.wait()

        a_grenze = 3
        a_grenze_line = self.get_vertical_line_to_graph(a_grenze, graph, line_class=DashedLine, color=BLUE)
        a_grenze_label = TextMobject("$a$", ).scale(0.75)
        a_grenze_label.next_to(a_grenze_line,DOWN)
        self.play(ShowCreation(a_grenze_line), Write(a_grenze_label))
        self.wait(0.5)

        b_grenze = 6
        b_grenze_line = self.get_vertical_line_to_graph(b_grenze, graph, line_class=DashedLine, color=BLUE)
        b_grenze_label = TextMobject("$b$").scale(0.75)
        b_grenze_label.next_to(b_grenze_line,DOWN)
        self.play(ShowCreation(b_grenze_line), Write(b_grenze_label))
        self.wait(0.5)

        c_mitte = (a_grenze+b_grenze)/2
        c_mitte_line = self.get_vertical_line_to_graph(c_mitte, graph, line_class=DashedLine, color=BLUE)
        c_mitte_label = MathTex(r"c=\frac{a+b}{2}").scale(0.5)
        c_mitte_label.next_to(c_mitte_line,DOWN)
        c_mitte_label2 = MathTex(r"f(c)= f\left( \frac{a+b}{2} \right)").scale(0.5)
        c_mitte_label2.next_to(c_mitte_line,UP)
        self.play(ShowCreation(c_mitte_line), Write(c_mitte_label), Write(c_mitte_label2))

        self.wait(2)

        midInt = self.get_riemann_rectangles(
            graph,
            x_min=a_grenze,
            x_max=b_grenze,
            dx=b_grenze-a_grenze,
            input_sample_type="center",
            fill_opacity=0.5,
            stroke_width=0,
        )

        self.play(FadeIn(midInt))
        self.wait(5)

class Sehentrapezregel(GraphScene):
    CONFIG={
        "x_min": -1,
        "x_max": 10,
        "x_axis_width": 9,
        "y_min": -1,
        "y_max": 10,
        "y_axis_height": 6,
        "default_riemann_start_color": GREEN,
        "default_riemann_end_color": GREEN,
    }
    def construct(self):
        title=TextMobject("Sehnentrapezregel").scale(1.5)
        subtitle=TextMobject("Verfahren zur numerischen Integration II")
        subtitle.next_to(title, DOWN)
        subtitle_alt=TextMobject("Trapeze unter dem Graphen von $f$")
        subtitle_alt.next_to(title, DOWN)

        self.play(Write(title), Write(subtitle))
        self.wait(2.5)
        self.play(Transform(subtitle,subtitle_alt))
        self.wait(2.5)
        self.play(FadeOut(title), FadeOut(subtitle))

        self.setup_axes(animate=True)                                           #Koordinatensystem anzeigen

        def func(x):
            return 0.1 * (x + 3 - 5) * (x - 3 - 5) * (x - 5) + 5                #Darzustellende Funktion

        graph = self.get_graph(func, x_min=-1, x_max=10)                        #Graphen erstellen
        graph.set_color(RED)
        graph_label = self.get_graph_label(graph, label = "f")

        self.play(ShowCreation(graph), run_time=3)                              #Graphen anzeigen
        self.play(Write(graph_label))
        self.wait()

        a_grenze = 3
        a_grenze_line = self.get_vertical_line_to_graph(a_grenze, graph, line_class=DashedLine, color=BLUE)
        a_grenze_label = TextMobject("$a$", ).scale(0.75)
        a_grenze_label.next_to(a_grenze_line,DOWN)
        self.play(ShowCreation(a_grenze_line), Write(a_grenze_label))
        self.wait(0.5)

        b_grenze = 6
        b_grenze_line = self.get_vertical_line_to_graph(b_grenze, graph, line_class=DashedLine, color=BLUE)
        b_grenze_label = TextMobject("$b$").scale(0.75)
        b_grenze_label.next_to(b_grenze_line,DOWN)
        self.play(ShowCreation(b_grenze_line), Write(b_grenze_label))
        self.wait(2)

        a_punkt = ValueTracker(a_grenze)                                        #Punkt in (a|f(a)) zeichnen
        a_punkt_wert = a_punkt.get_value()
        a_punkt_geometrie = Dot().move_to(self.coords_to_point(a_punkt_wert, func(a_punkt_wert)))

        b_punkt = ValueTracker(b_grenze)                                        #Punkt in (b|f(b)) zeichnen
        b_punkt_wert = b_punkt.get_value()
        b_punkt_geometrie = Dot().move_to(self.coords_to_point(b_punkt_wert, func(b_punkt_wert)))
        self.play(FadeIn(a_punkt_geometrie), FadeIn(b_punkt_geometrie))
        self.wait(2)

        x = [a_grenze, b_grenze]
        y = [func(x[0]), func(x[1])]

        lineare_regression = np.poly1d(np.polyfit(x, y, 1))

        trapLine = self.get_graph(lineare_regression, x_min=1, x_max=8, color=GREEN)
        self.play(FadeIn(trapLine))

        self.wait(2)

        trapInt = self.get_riemann_rectangles(
            trapLine,
            x_min=3,
            x_max=6,
            dx=0.001,
            input_sample_type="center",
            fill_opacity=0.5,
            stroke_width=0,
        )
        self.play(FadeIn(trapInt))
        self.wait(5)

class Tangententrapezregel(GraphScene):
    CONFIG={
        "x_min": -1,
        "x_max": 10,
        "x_axis_width": 9,
        "y_min": -1,
        "y_max": 10,
        "y_axis_height": 6,
        "camera_config":{"background_color":"#475147"},
        "default_riemann_start_color": GREEN,
        "default_riemann_end_color": GREEN,
    }
    def construct(self):
        title=TextMobject("Tangententrapezregel").scale(1.5)
        subtitle=TextMobject("Verfahren zur numerischen Integration III")
        subtitle.next_to(title, DOWN)
        subtitle_alt=TextMobject("Trapetze unter einer Tangente durch $(c|f(c))$")
        subtitle_alt.next_to(title, DOWN)

        self.play(Write(title), Write(subtitle))
        self.wait(2.5)
        self.play(Transform(subtitle,subtitle_alt))
        self.wait(2.5)
        self.play(FadeOut(title), FadeOut(subtitle))

        self.setup_axes(animate=True)                                           #Koordinatensystem anzeigen

        def func(x):
            return 0.1 * (x + 3 - 5) * (x - 3 - 5) * (x - 5) + 5                #Darzustellende Funktion

        graph = self.get_graph(func, x_min=-1, x_max=10)                        #Graphen erstellen
        graph.set_color(RED)
        graph_label = self.get_graph_label(graph, label = "f")

        self.play(ShowCreation(graph), run_time=3)                              #Graphen anzeigen
        self.play(Write(graph_label))
        self.wait()

        a_grenze = 3
        a_grenze_line = self.get_vertical_line_to_graph(a_grenze, graph, line_class=DashedLine, color=BLUE)
        a_grenze_label = TextMobject("$a$", ).scale(0.75)
        a_grenze_label.next_to(a_grenze_line,DOWN)
        self.play(ShowCreation(a_grenze_line), Write(a_grenze_label))
        self.wait(0.5)

        b_grenze = 6
        b_grenze_line = self.get_vertical_line_to_graph(b_grenze, graph, line_class=DashedLine, color=BLUE)
        b_grenze_label = TextMobject("$b$").scale(0.75)
        b_grenze_label.next_to(b_grenze_line,DOWN)
        self.play(ShowCreation(b_grenze_line), Write(b_grenze_label))
        self.wait(0.5)

        c_mitte = (a_grenze+b_grenze)/2
        c_mitte_line = self.get_vertical_line_to_graph(c_mitte, graph, line_class=DashedLine, color=BLUE)
        c_mitte_label = MathTex(r"c=\frac{a+b}{2}").scale(0.5)
        c_mitte_label.next_to(c_mitte_line,DOWN)
        c_mitte_label2 = MathTex(r"f(c)= f\left( \frac{a+b}{2} \right)").scale(0.5)
        c_mitte_label2.next_to(c_mitte_line,UP).shift(0.2 * UP)
        self.play(ShowCreation(c_mitte_line), Write(c_mitte_label), Write(c_mitte_label2))
        self.wait(0.5)

        c_punkt = ValueTracker(c_mitte)                                           #Punkt in (c|f(c)) zeichnen
        c_punkt_wert = c_punkt.get_value()
        c_punkt_geometrie = Dot().move_to(self.coords_to_point(c_punkt_wert, func(c_punkt_wert)))
        self.play(FadeIn(c_punkt_geometrie))
        self.wait(2)

        trapLine = self.get_graph(lambda x: -0.825*x+9.15, x_min=1, x_max=8, color=GREEN)
        self.play(FadeIn(trapLine))

        self.wait(2)

        trapInt = self.get_riemann_rectangles(
            trapLine,
            x_min=3,
            x_max=6,
            dx=0.001,
            input_sample_type="center",
            fill_opacity=0.5,
            stroke_width=0,
        )
        self.play(FadeIn(trapInt))
        self.wait(5)

class KeplerscheFassregel(GraphScene):
    CONFIG={
        "x_min": -1,
        "x_max": 10,
        "x_axis_width": 9,
        "y_min": -1,
        "y_max": 10,
        "y_axis_height": 6,
        "camera_config":{"background_color":"#475147"},
        "default_riemann_start_color": GREEN,
        "default_riemann_end_color": GREEN,
    }
    def construct(self):
        title=TextMobject("Simpsonregel/Kepler'sche Fassregel").scale(1.5)
        subtitle=TextMobject("Verfahren zur numerischen Integration IV")
        subtitle.next_to(title, DOWN)
        subtitle_alt=TextMobject("Parabel durch $(a|f(a))$, $(c|f(c))$ und $(b|f(b))$")
        subtitle_alt.next_to(title, DOWN)

        self.play(Write(title), Write(subtitle))
        self.wait(2.5)
        self.play(Transform(subtitle,subtitle_alt))
        self.wait(2.5)
        self.play(FadeOut(title), FadeOut(subtitle))

        self.setup_axes(animate=True)                                           #Koordinatensystem anzeigen

        def func(x):
            return 0.1 * (x + 3 - 5) * (x - 3 - 5) * (x - 5) + 5                #Darzustellende Funktion

        graph = self.get_graph(func, x_min=-1, x_max=10)                        #Graphen erstellen
        graph.set_color(RED)
        graph_label = self.get_graph_label(graph, label = "f")

        self.play(ShowCreation(graph), run_time=3)                              #Graphen anzeigen
        self.play(Write(graph_label))
        self.wait()

        a_grenze = 3
        a_grenze_line = self.get_vertical_line_to_graph(a_grenze, graph, line_class=DashedLine, color=BLUE)
        a_grenze_label = TextMobject("$a$", ).scale(0.75)
        a_grenze_label.next_to(a_grenze_line,DOWN)
        self.play(ShowCreation(a_grenze_line), Write(a_grenze_label))
        self.wait(0.5)

        b_grenze = 6
        b_grenze_line = self.get_vertical_line_to_graph(b_grenze, graph, line_class=DashedLine, color=BLUE)
        b_grenze_label = TextMobject("$b$").scale(0.75)
        b_grenze_label.next_to(b_grenze_line,DOWN)
        self.play(ShowCreation(b_grenze_line), Write(b_grenze_label))
        self.wait(0.5)

        c_mitte = (a_grenze+b_grenze)/2
        c_mitte_line = self.get_vertical_line_to_graph(c_mitte, graph, line_class=DashedLine, color=BLUE)
        c_mitte_label = MathTex(r"c=\frac{a+b}{2}").scale(0.5)
        c_mitte_label.next_to(c_mitte_line,DOWN)
        c_mitte_label2 = MathTex(r"f(c)= f\left( \frac{a+b}{2} \right)").scale(0.5)
        c_mitte_label2.next_to(c_mitte_line,UP)
        self.play(ShowCreation(c_mitte_line), Write(c_mitte_label), Write(c_mitte_label2))
        self.wait(0.5)

        a_punkt = ValueTracker(a_grenze)                                        #Punkt in (a|f(a)) zeichnen
        a_punkt_wert = a_punkt.get_value()
        a_punkt_geometrie = Dot().move_to(self.coords_to_point(a_punkt_wert, func(a_punkt_wert)))

        b_punkt = ValueTracker(b_grenze)                                        #Punkt in (b|f(b)) zeichnen
        b_punkt_wert = b_punkt.get_value()
        b_punkt_geometrie = Dot().move_to(self.coords_to_point(b_punkt_wert, func(b_punkt_wert)))

        c_punkt = ValueTracker(c_mitte)                                           #Punkt in (c|f(c)) zeichnen
        c_punkt_wert = c_punkt.get_value()
        c_punkt_geometrie = Dot().move_to(self.coords_to_point(c_punkt_wert, func(c_punkt_wert)))

        self.play(FadeIn(a_punkt_geometrie), FadeIn(b_punkt_geometrie), FadeIn(c_punkt_geometrie))


        self.wait(2)

        x = [a_grenze, c_mitte, b_grenze]
        y = [func(x[0]), func(x[1]), func(x[2])]

        quadratische_regression = np.poly1d(np.polyfit(x, y, 2))

        parabel = self.get_graph(quadratische_regression, x_min=1, x_max=8, color=GREEN)
        self.play(FadeIn(parabel))

        self.wait(2)

        trapInt = self.get_riemann_rectangles(
            parabel,
            x_min=3,
            x_max=6,
            dx=0.001,
            input_sample_type="center",
            fill_opacity=0.5,
            stroke_width=0,
        )
        self.play(FadeIn(trapInt))
        self.wait(5)
