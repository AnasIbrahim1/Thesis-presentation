from manim import *
from manim_slides import Slide

class LinearText(Slide):
    def clear(self):
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )

    def construct(self):       
        eq1 = Tex(r'$A\mathbf{v} = \lambda \mathbf{v}$', color = YELLOW, font_size = 35)
        eq2 = Tex(r'$(a_{n - 1}A^{n - 1} + a_{n - 2}A^{n - 2} + \dots + a_1A + a_0I)(\mathbf{v})$', color = YELLOW, font_size = 35)
        eq3 = Tex(r'$a_{n - 1}\lambda^{n - 1} + a_{n - 2}\lambda^{n - 2} + \dots a_1\lambda + a_0$', color = YELLOW, font_size = 35)
        eq4 = Tex(r'$p(A)\mathbf{v} = p(\lambda)$', color = YELLOW, font_size = 35)
        eq5 = Tex(r'$p(A) = O \iff p(\lambda) = 0$', color = YELLOW, font_size = 35)
        
        self.play(Write(eq1))
        self.play(eq1.animate.to_edge(UP))
        self.next_slide()
        
        eq2.next_to(eq1, DOWN)
        self.play(Write(eq2))
        self.next_slide()
        
        eq3.next_to(eq1, DOWN)
        self.play(Transform(eq2, eq3))
        self.next_slide()
        
        eq4.next_to(eq3, DOWN)
        self.play(Write(eq4))
        self.next_slide()
        
        eq5.next_to(eq4, DOWN)
        self.play(Write(eq5))
        self.next_slide()
        
        something = Tex(r'To annihilate both $\sqrt{2}$ and $\sqrt{3}$, the smallest polynomial is $(x^2 - 2)(x^2 - 3)$', color = YELLOW, font_size = 35)
        something.next_to(eq5, 2 * DOWN)
        self.play(Write(something))
        self.next_slide()
        self.play(FadeOut(something))
        
        
        text = Tex(r'$A$ is algebraic over $\mathbb{Q}$ if and only if all its eigenvalues are algebraic', color = RED, font_size = 35)
        text.to_edge(DOWN)
        self.play(Write(text))
        self.next_slide()
        
        text2 = Tex(r'if $\text{min}_{A, \mathbb{Q}}$ is irreducible, then all eigenvalues have the same minimal polynomial', color = RED, font_size = 35)
        text2.next_to(text, UP)
        self.play(Write(text2))
        self.next_slide()
        self.clear()