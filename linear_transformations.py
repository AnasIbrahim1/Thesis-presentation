from manim import *
from manim_slides import Slide

shear = [[1, 1], [0, 1]]
normal = [[1, 2],
          [1, 0]]

def matrix_multiply(m1, m2):
    result = [[0 for _ in range(len(m2[0]))] for _ in range(len(m1))]
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            for k in range(len(m2)):
                result[i][j] += m1[i][k] * m2[k][j]
    return result

def convert_to_tex(matrix):
    res = r'$\begin{bmatrix}'
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            res += str(matrix[i][j])
            if j != len(matrix[0]) - 1:
                res += ' & '
        if i != len(matrix) - 1:
            res += r' \\ '
    res += r'\end{bmatrix}$'
    return res

class Matrix(LinearTransformationScene, Slide):
    def clear(self):
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )

    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=True,
            show_basis_vectors=True
        )
        
    def wait(self, *args, **kwargs):
        w = Wait(*args, **kwargs)
        self.play(w)
        self.remove(w.mobject)
        self.moving_mobjects.remove(w.mobject)

    def construct(self):
        self.next_slide()
        self.apply_matrix(normal)
        self.next_slide()
        
        ttt = Tex(r'$A = \begin{bmatrix} 1 & 2 \\ 1 & 0 \end{bmatrix}$', color = WHITE, font_size = 35)
        ttt.to_edge(UL)
        ttt.add_background_rectangle()
        self.play(Create(ttt))
        self.add_background_mobject(ttt)
        
        self.next_slide()
        self.apply_matrix(normal)
        ttt2 = Tex(r'$A^2 = $' + convert_to_tex(matrix_multiply(normal, normal)), color = WHITE, font_size = 35)
        ttt2.to_edge(UL)
        ttt2.add_background_rectangle()
        self.play(Transform(ttt, ttt2))
        self.add_background_mobject(ttt2)
        
        self.clear()
        
        
        
        
        
