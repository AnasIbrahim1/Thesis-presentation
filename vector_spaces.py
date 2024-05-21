from manim import *
from manim_slides import Slide

class Vectors(VectorScene, Slide):
    def clear(self):
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )
        
    def slide_add(self):
        plane = NumberPlane()
        plane.add_coordinates()
        self.play(FadeIn(plane))
        self.wait(0)
        self.next_slide()
        v1 = Vector([1, 2], color = YELLOW)
        v2 = Vector([3, -1], color = MAROON_B)
        self.play(Create(v1), run_time=1)
        self.play(Create(v2), run_time=1)
        l1 = self.label_vector(v1, "v")
        l2 = self.label_vector(v2, "w")
        self.wait(0)
        
        vector_group = VGroup(v2, l2)
        self.play(ApplyMethod(vector_group.shift, v1.get_end()), run_time = 1)

        self.wait(0)
        v_sum = Vector(v2.get_end(), color = PINK)
        self.play(Create(v_sum), run_time = 1)
        sum_tex = "\\vec{\\textbf{v}} + \\vec{\\textbf{w}}"
        lsum = self.label_vector(v_sum, sum_tex, rotate = True)
        self.wait(0)
        self.next_slide()
        
        self.play(FadeOut(v_sum), FadeOut(v1), FadeOut(v2), FadeOut(l1), FadeOut(l2), FadeOut(lsum))
        self.wait(0)

        self.next_slide()
        v = Vector([1, 2], color = YELLOW)
        w = Vector(2 * v.get_end(), color = YELLOW)
        self.play(Create(v))
        label = self.label_vector(v, "v")
        self.play(Transform(v, w), FadeOut(label))
        label = self.label_vector(w, MathTex(r"2\vec{\mathbf{v}}", color = YELLOW))
        self.wait(0)
        self.next_slide()
        self.play(FadeOut(v), FadeOut(label))
        self.wait(0)
        self.next_slide()
        
        
                
    def span(self):
        plane = NumberPlane()
        plane.add_coordinates()
        self.play(FadeIn(plane))
        self.wait(0)
        self.next_slide()
        v1 = Vector([2, 1], color = YELLOW)
        self.play(Create(v1), run_time=1)
        label = self.label_vector(v1, "v")
        self.wait(0)
        line = Line(start = v1.get_end()*-3, end = v1.get_end()*3, color = YELLOW)
        self.play(Create(line))
        self.wait(0)
        self.next_slide()
        span_def = MathTex(r"\text{span}(\vec{\mathbf{v}}) = \{c\vec{\mathbf{v}}: c \in \mathbb{R}\}", color = YELLOW)
        span_def.to_edge(UP)
        span_def.shift(DOWN)
        text_box = Rectangle(color=BLACK, fill_color=BLACK, fill_opacity=1)
        text_box.surround(span_def)
        self.play(Create(text_box), Write(span_def))
        self.wait(0)
        self.next_slide()
        self.play(FadeOut(span_def), FadeOut(text_box))
        
        
        v2 = Vector(v1.get_end()*2, color = MAROON_B)
        self.play(Create(v2), run_time = 1)
        label2 = self.label_vector(v2, "w", color = MAROON_B)
        
        self.next_slide()
        text2 = Tex(r'Linearly Dependent', color = YELLOW, font_size = 35)
        text2.to_edge(UP)
        text2.shift(DOWN)
        text_box2 = Rectangle(color=BLACK, fill_color=BLACK, fill_opacity=1)
        text_box2.surround(text2)
        self.play(Create(text_box2), Write(text2))
        
        self.next_slide()
        self.play(FadeOut(text2), FadeOut(text_box2))
        ww = Vector([0, 2], color = MAROON_B)
        self.play(Transform(v2, ww), FadeOut(label2))
        self.wait(0)
    
    def algebraic(self):
        self.clear()
        plane = NumberPlane()
        plane.add_coordinates()
        self.play(FadeIn(plane))
        self.wait(0)
        self.next_slide()
        v1 = Vector([0, 1.414213], color = YELLOW)
        text1 = Tex(r'$\sqrt{2}$', color = YELLOW, font_size = 35)
        text1.next_to(v1.get_end(), 2 * RIGHT)
        textbox = Rectangle(color=BLACK, fill_color=BLACK, fill_opacity=1)
        textbox.surround(text1)
        self.play(Create(v1), Create(textbox), Write(text1))
        self.wait(0)
        self.next_slide()
        
        v2 = Vector([0, 2], color = YELLOW)
        text2 = Tex(r'$2$', color = YELLOW, font_size = 35)
        text2.next_to(v2.get_end(), 2 * RIGHT)
        textbox2 = Rectangle(color=BLACK, fill_color=BLACK, fill_opacity=1)
        textbox2.surround(text2)
        
        self.play(Transform(v1, v2), Transform(text1, text2), Transform(textbox, textbox2))
        
        self.next_slide()
        text3 = Tex(r'$0$', color = YELLOW, font_size = 35)
        textbox3 = Rectangle(color=BLACK, fill_color=BLACK, fill_opacity=1)
        textbox3.surround(text3)
        self.play(FadeOut(v1), Transform(textbox, textbox3), Transform(text1, text3))
        
    def construct(self):
        self.slide_add()
        self.next_slide()
        self.span()
        self.next_slide()
        self.algebraic()
        self.next_slide()
        self.clear()

