from manim import *
from manim_slides import Slide

class Intro(Slide):
    def clear(self):
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )
        
    def slide_1(self):
        title_tex = Tex(r'On Algebraicity of Complex Matrices over $\mathbb{Q}$', color = ORANGE, font_size = 50)
        title_tex.shift(2 * UP)
        self.play(Write(title_tex))
                
        author = Tex(r'Author: {Anas A. Ibrahim}', color = GREEN, font_size = 32)
        gold = ManimColor.from_rgb((229, 184, 11))
        supervisors = Tex(r'Supervisors: {Dr. Eslam Badr, Dr. Daoud Siniora}', color = gold, font_size = 42)
        author.next_to(title_tex, DOWN)
        author.shift(DOWN)
        supervisors.next_to(author, DOWN)
        self.play(Write(author))
        self.play(Write(supervisors))


        senior_thesis = Tex(r'\textit{Mathematics Senior Thesis}', color = WHITE, font_size = 30)
        senior_thesis.next_to(supervisors, DOWN)
        senior_thesis.shift(DOWN)
        auc = Tex(r'{The American University in Cairo}', color = WHITE, font_size = 30)
        auc.next_to(senior_thesis, DOWN)
        self.play(Write(senior_thesis)) 
        self.play(Write(auc))
        
    def slide_2(self):
        self.clear()
        game_tex = Tex(r'Let’s play a game!', color = BLUE, font_size = 45)
        game_tex.to_edge(UP)
        game_tex.to_edge(LEFT)
        game_tex.shift(DOWN)
        self.play(Write(game_tex))
        self.next_slide()
        
        given = Tex(r'Given a number $x$ and you can do 3 operations:', color = ORANGE, font_size = 35)
        given.next_to(game_tex, DOWN)
        given.align_to(game_tex, LEFT)
        option1 = Tex(r'1. Multiply your number by $x$', color = ORANGE, font_size = 35)
        option1.next_to(given, DOWN)
        option1.align_to(game_tex, LEFT)
        option2 = Tex(r'2. Multiply your number by a rational number (like $\frac{2}{3}$)', color = ORANGE, font_size = 35)
        option2.next_to(option1, DOWN)
        option2.align_to(game_tex, LEFT)
        option3 = Tex(r'3. Add a rational number to your number', color = ORANGE, font_size = 35)
        option3.next_to(option2, DOWN)
        option3.align_to(game_tex, LEFT)
        option4 = Tex(r'Your goal is to reach 0', color = ORANGE, font_size = 35)
        option4.next_to(option3, DOWN)
        option4.align_to(game_tex, LEFT)
        
        
        self.play(Write(given))
        self.next_slide()
        self.play(Write(option1))
        self.next_slide()
        self.play(Write(option2))
        self.next_slide()
        self.play(Write(option3))
        self.next_slide()
        self.play(Write(option4))
        self.next_slide()
        
        eq1 = Tex(r'$\sqrt{2}$', color = YELLOW, font_size = 35)
        eq1.to_edge(DOWN)
        eq1.shift(UP)
        eq2 = Tex(r'$(\sqrt{2})^2$', color = YELLOW, font_size = 35)
        eq3 = Tex(r'$2$', color = YELLOW, font_size = 35)
        eq4 = Tex(r'$2 - 2$', color = YELLOW, font_size = 35)
        eq5 = Tex(r'$0$', color = YELLOW, font_size = 35)
        eq6 = Tex(r'\textit{Algebraic Number over $\mathbb{Q}$}', color = BLUE, font_size = 35)
        
        eqlist = [eq2, eq3, eq4, eq5, eq6]
        
        for eq in eqlist:
            eq.to_edge(DOWN)
            eq.shift(UP)
            
        self.play(Write(eq1))
        for eq in eqlist:
            self.next_slide()
            self.play(Transform(eq1, eq))
            
        self.next_slide()
        eqq = Tex(r'$x$', color = YELLOW, font_size = 35)
        eqq.to_edge(DOWN)
        eqq.shift(UP)
        self.play(Transform(eq1, eqq))
        
        eq2 = Tex(r'$ax$', color = YELLOW, font_size = 35)
        eq3 = Tex(r'$ax + b$', color = YELLOW, font_size = 35)
        eq4 = Tex(r'$x(ax + b)$', color = YELLOW, font_size = 35)
        eq5 = Tex(r'$ax^2 + bx$', color = YELLOW, font_size = 35)
        eq6 = Tex(r'$ax^2 + bx + c$', color = YELLOW, font_size = 35)
        eq7 = Tex(r'$x(ax^2 + bx + c)$', color = YELLOW, font_size = 35)
        eq8 = Tex(r'$ax^3 + bx^2 + cx$', color = YELLOW, font_size = 35)
        eq9 = Tex(r'$ax^3 + bx^2 + cx + d$', color = YELLOW, font_size = 35)
        eq10 = Tex(r'$a_nx^n + a_{n - 1}x^{n - 1} + \dots + a_1 x + a_0$ (a polynomial)', color = YELLOW, font_size = 35)
        
        eqlist = [eq2, eq3, eq4, eq5, eq6, eq7, eq8, eq9, eq10]
        
        
        for eq in eqlist:
            eq.to_edge(DOWN)
            eq.shift(UP)
        
        for eq in eqlist:
            self.next_slide()
            self.play(Transform(eq1, eq))
            
    def slide_3(self):
        self.clear()
        def1 = Tex(r'Definition: ', r'a complex number $\alpha$ is said to be ', r'\textit{algebraic over $\mathbb{Q}$}', r' if there exists a polynomial $f(x)$ with rational coefficients such that $f(\alpha) = 0$', font_size = 35)
        def1[0].set_color(LIGHT_BROWN)
        def1[2].set_color(BLUE)
        eq1 = Tex(r'$f(x) = a_nx^n + a_{n - 1}x^{n - 1} + \dots + a_1 x + a_0, \quad a_n, a_{n - 1}, \dots, a_1, a_0 \in \mathbb{Q}$', color = YELLOW, font_size = 35)
        eq2 = Tex(r'$f(\alpha) = a_n\alpha^n + a_{n - 1}\alpha^{n - 1} + \dots + a_1 \alpha + a_0 = 0$', color = YELLOW, font_size = 35)
        def2 = Tex(r'Definition: ', r'\textit{the minimal polynomial of $\alpha \in \mathbb{C}$ over $\mathbb{Q}$}', r' ($\min_{\alpha, \mathbb{Q}}$) is the monic polynomial $p \in \mathbb{Q}[x]$ of lowest degree $p(\alpha) = 0$', font_size = 35)
        def2[0].set_color(LIGHT_BROWN)
        def2[1].set_color(BLUE)
        
        example = Tex(r'$\min_{\sqrt{2}, \mathbb{Q}}(x) = x^2 - 2$', color = YELLOW, font_size = 35)
        
        texte = Tex(r'$\min_{\alpha, \mathbb{Q}}(x)$ is', r' \textit{irreducible}', font_size = 35)
        texte[1].set_color(BLUE)
        
        eqe = Tex(r'$\min_{\alpha, \mathbb{Q}}(x) \ne p(x)q(x) \quad \deg p, \deg q \ge 1$', color = YELLOW, font_size = 35)
        eqe2 = Tex(r'$\min_{\alpha, \mathbb{Q}}(\alpha) = p(\alpha)q(\alpha)$', color = YELLOW, font_size = 35)
        eqe3 = Tex(r'$0 = p(\alpha)q(\alpha)$', color = YELLOW, font_size = 35)
        eqe4 = Tex(r'$p(\alpha) = 0 \text{ or } q(\alpha) = 0$', color = YELLOW, font_size = 35)
        
        text1 = Tex(r'What if we extend a dimension?', color = BLUE, font_size = 35)
        eq3 = Tex(r'$(x_1, y_1), (x_2, y_2) \in \mathbb{C}^2$', color = YELLOW, font_size = 30)
        eq4 = Tex(r'$(x_1, y_1) + (x_2, y_2) = (x_1 + y_1, x_2 + y_2)$', color = YELLOW, font_size = 30)
        eq44 = Tex(r'$(x_1, y_1) \cdot (x_2, y_2) = (x_1 \cdot y_1, x_2 \cdot y_2)$', color = YELLOW, font_size = 30)
        eq5 = Tex(r'$a(x, y) = (ax, ay)$', color = YELLOW, font_size = 30)
        eq6 = Tex(r'$a_n(x, y)^n + a_{n - 1}(x, y)^{n - 1} + \dots + a_1(x, y) + a_0 = (0, 0)$', color = YELLOW, font_size = 30)
        eq7 = Tex(r'$a_n(x^n, y^n) + a_{n - 1}(x^n, y^{n - 1}) + \dots + a_1(x, y) + a_0 = (0, 0)$', color = YELLOW, font_size = 30)
        
        text2 = Tex(r'Matrices!', color = BLUE, font_size = 35)
        eq8 = Tex(r'$\begin{bmatrix} x_1 & 0 \\ 0 & y_1 \end{bmatrix} + \begin{bmatrix} x_2 & 0 \\ 0 & y_2 \end{bmatrix} = \begin{bmatrix} x_1 + x_2 & 0 \\ 0 & y_1 + y_2 \end{bmatrix}$', color = YELLOW, font_size = 30)
        eq9 = Tex(r'$\begin{bmatrix} x_1 & 0 \\ 0 & y_1 \end{bmatrix} \cdot \begin{bmatrix} x_2 & 0 \\ 0 & y_2 \end{bmatrix} = \begin{bmatrix} x_1 \cdot x_2 & 0 \\ 0 & y_1 \cdot y_2 \end{bmatrix}$', color = YELLOW, font_size = 30)
        eq10 = Tex(r'$a\begin{bmatrix} x & 0 \\ 0 & y \end{bmatrix} = \begin{bmatrix} ax & 0 \\ 0 & ay \end{bmatrix}$', color = YELLOW, font_size = 30)
        eq11 = Tex(r'$p\left(\begin{bmatrix} a_1 & a_2 \\ b_1 & b_1 \end{bmatrix}\right) = \begin{bmatrix} 0 & 0 \\ 0 & 0 \end{bmatrix}$', color = YELLOW, font_size = 30)
        
        text33 = Tex(r'Research Questions:', color = BLUE, font_size = 35)
        text3 = Tex(r'\begin{enumerate} \item When is a matrix $A$ algebraic over $\mathbb{Q}$? \item What does its minimal polynomial look like? (irreducibility) \end{enumerate}', color = WHITE, font_size = 35)
        
        # Now aligning the text and equations geometrically
        
        def1.to_edge(UP)
        def1.to_edge(LEFT)
        eq1.next_to(def1, DOWN)
        eq2.next_to(def1, DOWN)
        def2.next_to(def1, DOWN)
        def2.to_edge(LEFT)
        
        self.play(Write(def1))
        self.next_slide()
        self.play(Write(eq1))
        self.next_slide()
        self.play(FadeOut(eq1))
        self.play(Write(eq2))
        self.next_slide()
        self.play(FadeOut(eq2))
        self.play(Write(def2))
        self.next_slide()
        
        example.to_edge(DOWN)
        example.shift(2 * UP)
        self.play(Write(example))
        texte.move_to(example.get_center())
        eqe.move_to(example.get_center())
        eqe2.move_to(example.get_center())
        eqe3.move_to(example.get_center())
        eqe4.move_to(example.get_center())
        self.next_slide()
        self.play(Transform(example, texte))
        self.next_slide()
        self.play(Transform(example, eqe))
        self.next_slide()
        self.play(Transform(example, eqe2))
        self.next_slide()
        self.play(Transform(example, eqe3))
        self.next_slide()
        self.play(Transform(example, eqe4))
        
        self.next_slide()
        self.play(Write(text1))
        self.play(FadeOut(def1), FadeOut(def2), FadeOut(example))
        self.play(text1.animate.to_edge(UP))
        self.next_slide()
        eq3.next_to(text1, DOWN)
        eq4.next_to(eq3, DOWN)
        eq44.next_to(eq4, DOWN)
        eq5.next_to(eq44, DOWN)
        eq6.next_to(eq5, DOWN)
        eq7.next_to(eq5, DOWN)
        text2.to_edge(DOWN)
        text2.shift(UP)
        
        eqlist = [eq3, eq4, eq44, eq5, eq6]
        for eq in eqlist:
            self.play(Write(eq))
            self.next_slide()
        self.play(Transform(eq6, eq7))
        self.next_slide()
        self.play(Write(text2))
        
        self.next_slide()
        self.play(FadeOut(text1), FadeOut(eq3), FadeOut(eq4), FadeOut(eq44), FadeOut(eq5), FadeOut(eq6), FadeOut(eq7))
        self.play(text2.animate.to_edge(UP))

        eq8.next_to(text2, DOWN)
        eq9.next_to(eq8, DOWN)
        eq10.next_to(eq9, DOWN)
        eq11.next_to(eq10, DOWN)
        self.next_slide()
        self.play(Write(eq8))
        self.play(Write(eq9))
        self.play(Write(eq10))
        self.next_slide()
        self.play(Write(eq11))
        
        texte2 = Tex(r'There is a problem!', color = BLUE, font_size = 35)
        texte2.to_edge(DOWN)
        self.next_slide()
        self.play(Write(texte2))
        self.play(FadeOut(eq8), FadeOut(eq9), FadeOut(eq10), FadeOut(eq11), FadeOut(text2))
        self.play(texte2.animate.to_edge(UP))
        
        eqe5 = Tex(r'$\begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix} \cdot \begin{bmatrix} 0 & 0 \\ 0 & 1 \end{bmatrix} = \begin{bmatrix} 0 & 0 \\ 0 & 0 \end{bmatrix}$', color = YELLOW, font_size = 35)
        eqe6 = Tex(r'$AB = O \nRightarrow A = O \text{ or } B = O$!', color = YELLOW, font_size = 35)
        texte3 = Tex(r'$\min_{A, \mathbb{Q}}$ can be reducible!', color = WHITE, font_size = 35)
        
        self.play(Write(eqe5))
        self.next_slide()
        self.play(Transform(eqe5, eqe6))
        self.next_slide()
        self.play(Transform(eqe5, texte3))
        self.next_slide()
        self.play(eqe5.animate.shift(2 * UP))
        
        eqe7 = Tex(r'$A = \begin{bmatrix} 1 & i \\ 0 & 0 \end{bmatrix}$', color = YELLOW, font_size = 35)
        eqe8 = Tex(r'$aA + bI \ne O \quad { for }a, b \in \mathbb{Q}$', color = YELLOW, font_size = 35)
        eqe9 = Tex(r'$A^2 = A$', color = YELLOW, font_size = 35)
        eqe10 = Tex(r'$\min_{A, \mathbb{Q}}(x) = x^2 - x = x(x - 1)$ which is not irreducible', color = YELLOW, font_size = 35)
        self.play(Write(eqe7))
        eqe8.next_to(eqe7, DOWN)
        self.next_slide()
        self.play(Write(eqe8))
        eqe9.next_to(eqe8, DOWN)
        self.next_slide()
        self.play(Write(eqe9))
        eqe10.next_to(eqe9, DOWN)
        self.next_slide()
        self.play(Write(eqe10))
        
        
        
        self.next_slide()
        self.clear()
        self.play(Write(text33))
        self.play(text33.animate.to_edge(UP))
        text3.next_to(text33, DOWN)
        self.play(Write(text3))
        
    def slide_4(self):
        self.clear()
        vertical_line = Line(5 * UP, 5 * DOWN)
        text1 = Tex(r'Linear Algebraic \\ Perspective', color = BLUE, font_size = 60)
        text2 = Tex(r'Technical Perspective \\ (with Galois Theory)', color = ORANGE, font_size = 60)
        text1.next_to(vertical_line, 6.5 * LEFT)
        text2.next_to(vertical_line, 5 * RIGHT)
        self.play(Create(vertical_line), Write(text1), Write(text2))
        self.next_slide()
        self.play(FadeOut(text2), FadeOut(vertical_line), text1.animate.move_to(ORIGIN))
        
    def construct(self):
        self.slide_1()
        self.next_slide()
        self.slide_2()
        self.next_slide()
        self.slide_3()
        self.next_slide()
        self.slide_4()
        self.next_slide()
        self.clear()
        
        
        
# “” ‘’
