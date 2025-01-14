from manim import *
from manim_slides import Slide

class Galois(Slide):
    def clear(self):
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )
        
    def slide_1(self):
        def_splitting = Tex(r'Definition: ', r'\textit{the splitting field of a polynomial },' r'$f(x)$ over a field $F$ is the smallest field extension of $F$ that contains all the roots of $f(x)$', color = WHITE, font_size = 35)
        def_galois = Tex(r'Definition: ', r'a field extension $K/F$ is ', r'\textit{Galois}', r' if and only if it is the splitting field of some polynomial over $F$', color = WHITE, font_size = 35)
        def_galois_group = Tex(r'Definition: ', r'the \textit{Galois group}', r' of the extension $K/F$, $\text{Gal}(K/F)$, is the group of all automorphisms of $K$ fixing $F$', color = WHITE, font_size = 35)
        def_fixed_field = Tex(r'Definition: ', r'let $\Gamma \leqslant \text{Gal}(K/F)$, then $K^{\Gamma} = \{ u \in K : \gamma(u) = u \text{ for all }\gamma \in \Gamma\}$', color = WHITE, font_size = 35)
        theorem1 = Tex(r'Theorem 1: ', r'$K^{\text{Gal}(K/F)} = F$', color = WHITE, font_size = 35)
        theorem2 = Tex(r'Theorem 2: ', r'for $\varphi \in \text{Gal}(K/F)$, let $p \in F[x]$ has all its roots $R \subseteq K$, then $\varphi|_R$ is a permutation of $R$', color = WHITE, font_size = 35)
        theorem3 = Tex(r'Theorem 3: ', r'$\text{Gal}(K/F)$ is finite', color = WHITE, font_size = 35)
        theorem1[0].set_color(RED)
        theorem2[0].set_color(RED)
        theorem3[0].set_color(RED)
        def_splitting[0].set_color(LIGHT_BROWN)
        def_splitting[1].set_color(BLUE)
        def_galois[0].set_color(LIGHT_BROWN)
        def_galois[2].set_color(BLUE)
        def_galois_group[0].set_color(LIGHT_BROWN)
        def_galois_group[1].set_color(BLUE)
        def_fixed_field[0].set_color(LIGHT_BROWN)
        
        example1 = Tex(r'The splitting field of $x^2 - 2$ is $\mathbb{Q}(\sqrt{2}) = \{a + b\sqrt{2} : a, b \in \mathbb{Q}\}$', color = YELLOW, font_size = 35)
        example2 = Tex(r'The splitting field of $x^3 - 2$ is $\mathbb{Q}(\sqrt[3]{2}, \omega)$', color = YELLOW, font_size = 35)
        
        def_splitting.to_edge(UP)
        example1.next_to(def_splitting, DOWN)
        def_splitting.to_edge(LEFT)
        example2.next_to(example1, DOWN)
        self.play(Write(def_splitting))
        self.next_slide()
        self.play(Write(example1))
        self.next_slide()
        self.play(Write(example2))
        self.next_slide()
        self.clear()
        self.next_slide()
        
        def_galois.to_edge(UP)
        def_galois.to_edge(LEFT)
        def_galois_group.align_to(def_galois, LEFT)        
        def_galois_group.next_to(def_galois, DOWN)
        def_galois_group.align_to(def_galois, LEFT)

        self.play(Write(def_galois))
        self.next_slide()
        self.play(Write(def_galois_group))
        self.next_slide()
        self.clear()

        def_fixed_field.to_edge(UP)
        def_fixed_field.to_edge(LEFT)
        theorem1.next_to(def_fixed_field, DOWN)
        theorem1.align_to(def_fixed_field, LEFT)
        theorem2.next_to(theorem1, DOWN)
        theorem2.align_to(theorem1, LEFT)
        theorem3.next_to(theorem2, DOWN)
        theorem3.align_to(theorem2, LEFT)

        self.play(Write(def_fixed_field))
        self.next_slide()
        self.play(Write(theorem1))
        self.next_slide()
        self.play(Write(theorem2))
        self.next_slide()
        self.play(Write(theorem3))
            
    def slide_2(self):
        self.clear()
        text = Tex(r'The Setup', color = BLUE, font_size = 45)
        text1 = Tex(r'Let $T : V \to V$ be a linear operator on a complex vector space with algebraic eigenvalues (over $\mathbb{Q}$)', color = WHITE, font_size = 35)
        text2 = Tex(r'Let the distinct eigenvalues be $\lambda_1, \lambda_2, \ldots, \lambda_n \in \mathbb{Q}$', color = WHITE, font_size = 35)
        eq2 = Tex(r'$r_T(x) = (x - \lambda_1)(x - \lambda_2) \ldots (x - \lambda_n) \text{ with coefficients } a_0, a_1, a_2, \dots, a_{n - 1}$', color = YELLOW, font_size = 35)
        eq1 = Tex(r'$E_T = \mathbb{Q}(\lambda_1, \lambda_2, \dots, \lambda_n)$', color = YELLOW, font_size = 35)
        eq3 = Tex(r'$\displaystyle p_T(x) = \text{lcm}_{\varphi \in \text{Gal}\left(\widetilde{E_T}/\mathbb{Q}\right)} \varphi(r_T(x))$', color = YELLOW, font_size = 35)

        text.to_edge(UP)
        text1.next_to(text, DOWN)
        text2.next_to(text1, DOWN)
        eq1.next_to(text2, DOWN)
        eq2.next_to(eq1, DOWN)
        eq3.next_to(eq2, DOWN)
        text1.to_edge(LEFT)
        text2.align_to(text1, LEFT)


        texobjects = [text1, text2, eq1, eq2, eq3]
        self.play(Write(text))
        for tx in texobjects:
            self.next_slide()
            self.play(Write(tx))

    
    def slide_3(self):
        self.clear()
        theorem = Tex(r'Theorem: ', '$p_T \in \mathbb{Q}[x]$ and is separable', font_size = 35)
        theorem[0].set_color(RED)
        theorem[1].set_color(BLUE)
        eq0 = Tex(r'For $\sigma \in \text{Gal}\left(\widetilde{E_T}/\mathbb{Q}\right)$', font_size=30, color=YELLOW)
        eq1 = Tex(r'$\sigma(r_T(x) \text{lcm}_{\varphi \in \text{Gal}\left(\widetilde{E_T}/\mathbb{Q}\right)} \varphi(E_T(x)))$', font_size=30, color=YELLOW)
        eq2 = Tex(r'$r_T(x)\text{lcm}_{\varphi \in \text{Gal}\left(\widetilde{E_T}/\mathbb{Q}\right)} (\sigma \circ \varphi)(E_T(x)))$', font_size=30, color=YELLOW)
        text = Tex(r'$p_T$ is invariant under the action of $\text{Gal}\left(\widetilde{E_T}/\mathbb{Q}\right)$, $p_T \in \mathbb{Q}[x]$', color = WHITE, font_size = 35)
        text2 = Tex(r'Separability comes by minimality of LCM and that $\sigma \in \text{Gal}\left(\widetilde{E_T}/\mathbb{Q}\right)$ permutes roots', color = WHITE, font_size = 35)

        theorem.to_edge(UP)
        eq0.next_to(theorem, DOWN)
        eq1.next_to(eq0, DOWN)
        eq2.next_to(eq0, DOWN)
        text.next_to(eq2, DOWN)
        text2.next_to(text, DOWN)
        theorem.to_edge(LEFT)

        self.play(Write(theorem))
        self.next_slide()
        self.play(Write(eq0))
        self.next_slide()
        self.play(Write(eq1))
        self.next_slide()
        self.play(Transform(eq1, eq2))
        self.next_slide()
        self.play(Write(text))
        self.next_slide()
        self.play(Write(text2))


    def slide_4(self):
        self.clear()
        theorem = Tex(r'Theorem (Converse of Cayley-Hamilton): ', r'\\ let $\lambda$ be an eigenvalue of $T$. If $s \in \mathbb{Q}[x]$ annihilates $T$, then $s(\varphi(\lambda)) = 0$ for all $\varphi \in \text{Gal}\left(\widetilde{E_T} : \mathbb{Q}\right)$. \\[0.2cm] In that case, $p_T(x)$ divides $s(x)$ in $\mathbb{Q}[x]$.', font_size = 35)
        theorem[0].set_color(RED)
        theorem[1].set_color(BLUE)
        
        eq0 = Tex(r'Let $\varphi \in \text{Gal}\left(\widetilde{E_T}/\mathbb{Q}\right)$', font_size=30, color=YELLOW)
        eq11 = Tex(r'Let $s(x) = s_0 + s_1x + s_2x^2 + \dots + s_n x^n, \quad s_0, s_1, \dots, s_n \in \mathbb{Q}$', font_size=30, color=YELLOW)
        eq222 = Tex(r'Since $s(T) = \mathbf{0}$, then $s(\lambda) = 0$ for all eigenvalues $\lambda$', font_size=30, color=YELLOW)
        eq333 = Tex(r'$s_0 + s_1\lambda + \dots + s_n \lambda^n = 0$', font_size=30, color=YELLOW)
        eq444 = Tex(r'$\varphi(s_0 + s_1\lambda + \dots + s_n \lambda^n) = 0$', font_size=30, color=YELLOW)
        eq555 = Tex(r'$s_0 + s_1\varphi(\lambda) + \dots + s_n \varphi(\lambda)^n = 0$', font_size=30, color=YELLOW)
        eq666 = Tex(r'$s(\varphi(\lambda)) = 0$', font_size=30, color=YELLOW)
        
        eq7777 = Tex(r'Thus, $\varphi(r_T(x)) = (x - \varphi(\lambda_1))(x - \varphi(\lambda_2))\dots (x - \varphi(\lambda_n))$ divides $s(x)$ over $E_T$', font_size=30, color=YELLOW)
        eq8888 = Tex(r'$p_T(x)$ divides $s(x)$ over $E_T$', font_size=30, color=YELLOW)
        eq9999 = Tex(r'$s(x) = p_T(x)h(x), \quad h(x) \in E_T[x]$', font_size=30, color=YELLOW)
        eq99999 = Tex(r'$\varphi(s(x)) = \varphi(p_T(x)h(x))$', font_size=30, color=YELLOW)
        eq99999_ = Tex(r'$s(x) = p_T(x)\varphi(h(x))$', font_size=30, color=YELLOW)
        eq99999__ = Tex(r'$h(x) = \varphi(h(x))$', font_size=30, color=YELLOW)
        eq99999___ = Tex(r'$h(x)$ is invariant under $\text{Gal}\left(\widetilde{E_T}/\mathbb{Q}\right)$, $h(x) \in \mathbb{Q}[x]$', font_size=30, color=YELLOW)
        
                
        theorem.to_edge(UP)
        eq0.next_to(theorem, DOWN)
        eq11.next_to(eq0, DOWN)
        eq222.next_to(eq11, DOWN)
        eq333.next_to(eq11, DOWN)
        eq444.next_to(eq11, DOWN)
        eq555.next_to(eq11, DOWN)
        eq666.next_to(eq11, DOWN)
        eq7777.next_to(eq666, DOWN)
        eq8888.next_to(eq666, DOWN)
        eq9999.next_to(eq666, DOWN)
        eq99999.next_to(eq9999, DOWN)
        eq99999_.next_to(eq9999, DOWN)
        eq99999__.next_to(eq9999, DOWN)
        eq99999___.next_to(eq9999, DOWN)
        theorem.to_edge(LEFT)
        
        self.play(Write(theorem))
        self.next_slide()
        self.play(Write(eq0))
        self.next_slide()
        self.play(Write(eq11))
        self.next_slide()
        self.play(Write(eq222))
        self.next_slide()
        self.play(Transform(eq222, eq333))
        self.next_slide()
        self.play(Transform(eq222, eq444))        
        self.next_slide()
        self.play(Transform(eq222, eq555))        
        self.next_slide()
        self.play(Transform(eq222, eq666))        
        self.next_slide()
        self.play(Write(eq7777))
        self.next_slide()
        self.play(Transform(eq7777, eq8888))
        self.next_slide()
        self.play(Transform(eq7777, eq9999))
        self.next_slide()
        self.play(Write(eq99999))
        self.next_slide()
        self.play(Transform(eq99999, eq99999_))
        self.next_slide()
        self.play(Transform(eq99999, eq99999__))
        self.next_slide()
        self.play(Transform(eq99999, eq99999___))
        
    def slide_5(self):
        self.clear()
        theorem = Tex(r'Theorem: ', r'\\ If $\min_{T, \mathbb{Q}}$ is irreducible, then $\min_{T, \mathbb{Q}} = \min_{\lambda, \mathbb{Q}} = p_T$', font_size = 35)
        eq0 = Tex(r'$\min_{T, \mathbb{Q}}$ annihilates $T$ and is in $\mathbb{Q}[x]$', font_size=30, color=YELLOW)
        eq11 = Tex(r'$\min_{T, \mathbb{Q}}(\lambda) = 0$ for any eigenvalue $\lambda$', font_size=30, color=YELLOW)
        eq22 = Tex(r'$\min_{\lambda, \mathbb{Q}} \, | \, \min_{T, \mathbb{Q}}$ for any eigenvalue $\lambda$', font_size=30, color=YELLOW)
        eq33 = Tex(r'$\min_{\lambda, \mathbb{Q}} = \min_{T, \mathbb{Q}}$ by irreducibility', font_size=30, color=YELLOW)
        eq444 = Tex(r'$p_T \, | \, \min_{\lambda, \mathbb{Q}}$ by the Converse of Cayley-Hamilton', font_size=30, color=YELLOW)    
        eq555 = Tex(r'$p_T = \min_{\lambda, \mathbb{Q}}$ by irreducibility', font_size=30, color=YELLOW)
        
        theorem[0].set_color(RED)
        theorem[1].set_color(BLUE)
        theorem.to_edge(UP)
        eq0.next_to(theorem, DOWN)
        eq11.next_to(eq0, DOWN)
        eq22.next_to(eq0, DOWN)
        eq33.next_to(eq0, DOWN)
        eq444.next_to(eq33, DOWN)
        eq555.next_to(eq33, DOWN)
        
        self.play(Write(theorem))
        self.next_slide()
        self.play(Write(eq0))
        self.next_slide()
        self.play(Write(eq11))
        self.next_slide()
        self.play(Transform(eq11, eq22))
        self.next_slide()
        self.play(Transform(eq11, eq33))
        self.next_slide()
        self.play(Write(eq444))
        self.next_slide()
        self.play(Transform(eq444, eq555))
    
    def slide_6(self):
        self.clear()
        theorem1 = Tex(r'Theorem 1: ', 'if $\min_{T, \mathbb{C}}$ is separable, then $T$ is diagonalizable', color = WHITE, font_size = 35)
        theorem2 = Tex(r'Theorem 2: ', 'if $T$ has an irreducible minimal polynomial over $\mathbb{Q}$, then $T$ is diagonalizable', font_size = 35)
        theorem3 = Tex(r'Theorem 3: ', 'if $T$ is diagonalizable and all eigenvalues have the same minimal polynomial over $\mathbb{Q}$, then $\min_{T, \mathbb{Q}}$ is irreducible', color = WHITE, font_size = 35)
        eq0 = Tex(r'Choose an eigenbasis $v_1, v_2, \dots, v_n$ with eigenvalues $\lambda_1, \lambda_2, \dots, \lambda_n$', font_size=30, color=YELLOW)
        eq11 = Tex(r'Let $s$ be the minimal polynomial of the eigenvalues (which is irreducible)', font_size=30, color=YELLOW)
        eq222 = Tex(r'$T(v_i) = \lambda_i v_i$ for all $i$', font_size=30, color=YELLOW)
        eq333 = Tex(r'$(s(T))(v_i) = s(\lambda_i)v_i = 0$ for all $i$', font_size=30, color=YELLOW)
        eq444 = Tex(r'$s(T) = 0$', font_size=30, color=YELLOW)
        eq5555 = Tex(r'$\min_{T, \mathbb{Q}} \, | \, s$', font_size=30, color=YELLOW)
        eq6666 = Tex(r'$\min_{T, \mathbb{Q}} = s$ by irreducibility', font_size=30, color=YELLOW)
        
        
        
        theorem_final = Tex(r'Theorem Boss: ', r'$\min_{T, F}$ is irreducible if and only if $T$ is diagonalizable and all eigenvalues have the same minimal polynomial over $\mathbb{Q}$', color = WHITE, font_size = 35)
        theorem1[0].set_color(RED)
        theorem2[0].set_color(RED)
        theorem2[1].set_color(BLUE)
        theorem3[0].set_color(RED)
        theorem3[1].set_color(BLUE)
        gold = ManimColor.from_rgb((229, 184, 11))
        theorem_final[0].set_color(gold)
        theorem_final[1].set_color(BLUE)
        
        theorem1.to_edge(UP)
        theorem2.next_to(theorem1, DOWN)
        theorem3.next_to(theorem2, DOWN)
        eq0.next_to(theorem3, DOWN)
        eq11.next_to(eq0, DOWN)
        eq222.next_to(eq11, DOWN)
        eq333.next_to(eq11, DOWN)
        eq444.next_to(eq11, DOWN)
        eq5555.next_to(eq444, DOWN)
        eq6666.next_to(eq444, DOWN)
        
        self.play(Write(theorem1))
        self.next_slide()
        self.play(Write(theorem2))
        self.next_slide()
        self.play(Write(theorem3))
        self.next_slide()
        self.play(Write(eq0))
        self.next_slide()
        self.play(Write(eq11))
        self.next_slide()
        self.play(Write(eq222))
        self.next_slide()
        self.play(Transform(eq222, eq333))
        self.next_slide()
        self.play(Transform(eq222, eq444))
        self.next_slide()
        self.play(Write(eq5555))
        self.next_slide()
        self.play(Transform(eq5555, eq6666))
        self.next_slide()
        self.clear()
        self.play(Write(theorem_final))
        self.next_slide()
        self.clear()
        thankyou = Tex(r'Thank you!', color = ORANGE, font_size = 65)
        self.play(Write(thankyou))        

    def construct(self):
        titlE_Tex = Tex(r'Technical Details (with Galois Theory)', color = ORANGE, font_size = 50)
        self.play(Write(titlE_Tex))
        self.next_slide()
        self.play(titlE_Tex.animate.to_edge(UP))
        evariste = ImageMobject("evariste.jpg")
        evariste.scale(0.45)
        self.play(FadeIn(evariste))
        
        galois_text = Tex(r'Evariste Galois', font_size = 35)
        gold = ManimColor.from_rgb((229, 184, 11))
        galois_text.set_color(gold)
        galois_text.next_to(evariste, DOWN)
        self.play(Write(galois_text))
        
        
        self.next_slide()
        self.clear()
        self.next_slide()
        self.slide_1()
        self.next_slide()
        self.slide_2()
        self.next_slide()
        self.slide_3()
        self.next_slide()
        self.slide_4()
        self.next_slide()
        self.slide_5()
        self.next_slide()
        self.slide_6()
        self.next_slide()
        self.clear()