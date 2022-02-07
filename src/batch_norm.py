# original work on colab: https://colab.research.google.com/drive/11pVYtpCAclAmaB5ryc7biRWKa4jhSzhz?usp=sharing
import itertools
from manim import *

def create_node(scene, label, pos=[]):
  if pos:
    node = Circle(radius=0.5, color=BLUE).shift(*pos)
    anno = MathTex(label).shift(*pos)
  else:
    node = Circle(radius=0.5, color=BLUE)
    anno = MathTex(label)

  # scene.play(Create(node), Write(anno))
  return node, anno, Create(node), Write(anno)

# create lines pair-wise; start_nodes * end_nodes
# returns a list containing the lines created
def create_edges(scene, start_nodes, end_nodes):
  edges = list(map(lambda pair: Line(start=pair[0].get_right(), 
                                end=pair[1].get_left(), 
                                stroke_width=2), 
                   list(itertools.product(start_nodes, end_nodes))))

  scene.play(*map(lambda x: Create(x), edges))
  return edges

# input used for the video
x1 = [3.0, 5.0, 6.0, 4.0, 7.0, 9.0, 2.0, 1.0, 8.0]
x2 = [0.8, 0.9, 0.6, 0.7, 0.5, 0.0, 0.2, 0.3, 0.1]
x = list(zip(x1, x2))

class BN(MovingCameraScene):
    def construct(self):
        title = Text("Batch Normalization", gradient=(BLUE, GREEN)).scale(1.5)
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))


        feature_colors = [RED, BLUE]
        # the input X
        X = Matrix(x).shift(LEFT*3)
        X.set_column_colors(*feature_colors)

        # 3 batches
        batch_1_m = Matrix(x[:3]).set_column_colors(*feature_colors).shift(RIGHT*3, UP*2.5).scale(0.75)
        batch_1_label = Text("Batch 1").shift(batch_1_m.get_center(), LEFT*2.5).scale(0.75)

        batch_2_m = Matrix(x[3:6]).set_column_colors(*feature_colors).shift(RIGHT*3).scale(0.75)
        batch_2_label = Text("Batch 2").shift(batch_2_m.get_center(), LEFT*2.5).scale(0.75)

        batch_3_m = Matrix(x[6:9]).set_column_colors(*feature_colors).shift(RIGHT*3, DOWN*2.5).scale(0.75)
        batch_3_label = Text("Batch 3").shift(batch_3_m.get_center(), LEFT*2.5).scale(0.75)

        buckets = VGroup(batch_1_m, 
                         batch_2_m, 
                         batch_3_m)

        input_x = MathTex('x=').shift(X.get_left(), LEFT)
        self.play(Create(input_x), Create(X))
        self.wait()

        self.play(FadeOut(input_x), 
                  FadeTransform(X, buckets))
        
        self.play(Write(batch_1_label), 
                  Write(batch_2_label), 
                  Write(batch_3_label))

        self.wait()
        self.play(FadeOut(buckets), 
                  FadeOut(batch_1_label), 
                  FadeOut(batch_2_label), 
                  FadeOut(batch_3_label))


        batch_1_anno = Text("Batch 1").shift(UP*2)
        self.play(FadeIn(batch_1_anno))

        batch_1_m = Matrix(x[:3])
        self.play(Create(batch_1_m))
        self.play(batch_1_m.animate.shift(LEFT*5), 
                  batch_1_anno.animate.shift(LEFT*5))

        # highlight x1
        self.play(Circumscribe(SurroundingRectangle(batch_1_m.get_rows()[0])))
        self.wait(0.5)
        batch_1_1_m = Matrix([[x[0][0]], [x[0][1]]]).shift(LEFT*2)
        self.play(Create(batch_1_1_m))

        # highlight x2
        self.play(Circumscribe(SurroundingRectangle(batch_1_m.get_rows()[1])))
        self.wait(0.5)
        batch_1_2_m = Matrix([[x[1][0]], [x[1][1]]]).shift(LEFT*0.5)
        self.play(Create(batch_1_2_m))

        # highlight x3
        self.play(Circumscribe(SurroundingRectangle(batch_1_m.get_rows()[2])))
        self.wait(0.5)
        batch_1_3_m = Matrix([[x[2][0]], [x[2][1]]]).shift(RIGHT)
        self.play(Create(batch_1_3_m))

        self.play(self.camera.frame.animate.shift(RIGHT*4))

        # move the 3 inputs to UL
        self.play(batch_1_1_m.animate.shift(UP*2.5), 
                  batch_1_2_m.animate.shift(UP*2.5),
                  batch_1_3_m.animate.shift(UP*2.5))

        # the NN
        x_1_node, x_1_anno, x_1_node_ani, x_1_anno_ani = create_node(self, "x_1", [UP, LEFT * 2])
        x_2_node, x_2_anno, x_2_node_ani, x_2_anno_ani = create_node(self, "x_2", [DOWN, LEFT * 2])
        h_1_node, h_1_anno, h_1_node_ani, h_1_anno_ani = create_node(self, "h_1", [UP])
        h_2_node, h_2_anno, h_2_node_ani, h_2_anno_ani = create_node(self, "h_2", [DOWN])

        z_node, z_anno, z_node_ani, z_anno_ani = create_node(self, "z", [RIGHT*2])

        self.play(x_1_node_ani, x_1_anno_ani, 
                  x_2_node_ani, x_2_anno_ani, 
                  h_1_node_ani, h_1_anno_ani, 
                  h_2_node_ani, h_2_anno_ani, 
                  z_node_ani, z_anno_ani)


        W1 = create_edges(self, [x_1_node, x_2_node], [h_1_node, h_2_node])
        W2 = create_edges(self, [h_1_node, h_2_node], [z_node])

        # using weights: [0.5, 3, 0.1, 0.2]
        h1_1 = MathTex('3.9').shift(h_1_anno.get_center())
        h2_1 = MathTex('.46').shift(h_2_anno.get_center())

        h1_2 = MathTex('5.2').shift(h_1_anno.get_center())
        h2_2 = MathTex('.68').shift(h_2_anno.get_center())

        h1_3 = MathTex('4.8').shift(h_1_anno.get_center())
        h2_3 = MathTex('.71').shift(h_2_anno.get_center())

        self.wait()

        # highlight the first input
        self.play(Indicate(batch_1_1_m))

        input1 = MathTex(str(x[0][0])).shift(x_1_anno.get_center())
        input2 = MathTex(str(x[0][1])).shift(x_2_anno.get_center())

        self.play(Transform(x_1_anno, input1), Transform(x_2_anno, input2))
        self.play(Indicate(x_1_anno), Indicate(x_2_anno))
        self.play(*map(lambda l: Indicate(l, scale_factor=1), W1))

        self.play(Transform(x_1_anno, input1), Transform(x_2_anno, input2))
        self.play(Indicate(h_1_anno), Indicate(h_2_anno))

        # first calc
        # transform labels of hidden layers into the actual values after calc
        self.play(Transform(h_1_anno, h1_1), Transform(h_2_anno, h2_1))
        self.play(Indicate(h_1_anno), Indicate(h_2_anno))

        # add a new entry to the right of the inputs
        hidden_1 = Matrix([[3.9], ['.46']]).set_color(GREEN).shift(UP*2.5, RIGHT*3)
        self.play(Create(hidden_1))
        self.play(Indicate(hidden_1), Indicate(h_1_anno), Indicate(h_2_anno))
        self.wait()

        # second calc
        self.play(Indicate(batch_1_2_m))

        input1 = MathTex(str(x[1][0])).shift(x_1_anno.get_center())
        input2 = MathTex(str(x[1][1])).shift(x_2_anno.get_center())

        self.play(Transform(x_1_anno, input1), Transform(x_2_anno, input2))
        self.play(Indicate(x_1_anno), Indicate(x_2_anno))
        self.play(*map(lambda l: Indicate(l, scale_factor=1), W1))

        # transform labels of hidden layers into the actual values after calc
        self.play(Transform(h_1_anno, h1_2), Transform(h_2_anno, h2_2))
        self.play(Indicate(h_1_anno), Indicate(h_2_anno))

        # add a new entry to the right of the inputs
        hidden_2 = Matrix([[5.2], ['.68']]).set_color(GREEN).shift(UP*2.5, RIGHT*4.5)
        self.play(Create(hidden_2))
        self.play(Indicate(hidden_2), Indicate(h_1_anno), Indicate(h_2_anno))
        self.wait()

        # third calc
        self.play(Indicate(batch_1_3_m))

        input1 = MathTex(str(x[2][0])).shift(x_1_anno.get_center())
        input2 = MathTex(str(x[2][1])).shift(x_2_anno.get_center())

        self.play(Transform(x_1_anno, input1), Transform(x_2_anno, input2))
        self.play(Indicate(x_1_anno), Indicate(x_2_anno))
        self.play(*map(lambda l: Indicate(l, scale_factor=1), W1))

        # transform labels of hidden layers into the actual values after calc
        self.play(Transform(h_1_anno, h1_3), Transform(h_2_anno, h2_3))
        self.play(Indicate(h_1_anno), Indicate(h_2_anno))

        # add a new entry to the right of the inputs
        hidden_3 = Matrix([[4.8], ['.71']]).set_color(GREEN).shift(UP*2.5, RIGHT*6)
        self.play(Create(hidden_3))
        self.play(Indicate(hidden_3), Indicate(h_1_anno), Indicate(h_2_anno))
        self.wait()

        # push the orignal inputs out of the way;
        # hides all the past values in the NN
        self.play(batch_1_1_m.animate.shift(LEFT*5), 
                  batch_1_2_m.animate.shift(LEFT*5), 
                  batch_1_3_m.animate.shift(LEFT*5), 
                  hidden_1.animate.shift(LEFT*5),
                  hidden_2.animate.shift(LEFT*5),
                  hidden_3.animate.shift(LEFT*5), 
                  FadeOut(x_1_anno), 
                  FadeOut(x_2_anno), 
                  FadeOut(h_1_anno), 
                  FadeOut(h_2_anno))
        
        self.wait()

        # formula expansions
        mean_formula = MathTex(r"\mu_i = \frac{\sum_j^{m}h_{i,j}}{m}").shift(UP*3,RIGHT*5)
        variance_formula = MathTex(r"\sigma_i^2 = \frac{\sum_j{(h_{i,j}-\mu_i)^2}}{m}").shift(UP*1.5, RIGHT*5)

        mu_1_formula = MathTex(r"\mu_1 = \frac{\sum_j^{m}h_{1,j}}{m}").shift(mean_formula.get_center())
        mu_2_formula = MathTex(r"\mu_2 = \frac{\sum_j^{m}h_{2,j}}{m}").shift(mean_formula.get_center(), DOWN*1.5)

        var_1_formula = MathTex(r"\sigma_1 = \sqrt{\frac{\sum_j{(h_{1,j}-\mu_1)^2}}{m}}").shift(variance_formula.get_center(), DOWN*2)
        var_2_formula = MathTex(r"\sigma_2 = \sqrt{\frac{\sum_j{(h_{2,j}-\mu_2)^2}}{m}}").shift(variance_formula.get_center(), DOWN*4)

        self.play(Write(mu_1_formula), 
                  Write(mu_2_formula),
                  Write(var_1_formula),
                  Write(var_2_formula))

        self.wait(3)

        # expand mu1
        self.play(Circumscribe(SurroundingRectangle(VGroup(*map(lambda x: x.get_rows()[0], 
                                                                [hidden_1, hidden_2, hidden_3])))))
        mu_1_expanded = MathTex(r"\mu_1 = \frac{3.9+5.2+4.8}{3}=4.6").shift(mu_1_formula.get_center())

        self.play(Transform(mu_1_formula, mu_1_expanded))

        self.wait(2)

        # expand mu2
        self.play(Circumscribe(SurroundingRectangle(VGroup(*map(lambda x: x.get_rows()[1], 
                                                                [hidden_1, hidden_2, hidden_3])))))
        mu_2_expanded = MathTex(r"\mu_2 = \frac{.46+.68+.72}{3}=.62").shift(mu_2_formula.get_center())

        self.play(Transform(mu_2_formula, mu_2_expanded))
        self.wait(2)

        mu_1 = MathTex(r'\mu_1 = 4.6').shift(mu_1_expanded.get_center(), LEFT)
        mu_2 = MathTex(r'\mu_2 = .62').shift(mu_2_expanded.get_center(), LEFT)
        self.play(Transform(mu_1_formula, mu_1), Transform(mu_2_formula, mu_2))

        self.wait(2)

        self.play(Indicate(var_1_formula))
        # highlight first input
        self.play(Circumscribe(SurroundingRectangle(VGroup(*map(lambda x: x.get_rows()[0], 
                                                        [hidden_1, hidden_2, hidden_3])))))
        
        self.play(Circumscribe(SurroundingRectangle(mu_1)))


        var_1_expanded = MathTex(r"\sigma_1 = \sqrt{\frac{(3.0-4.6)^2 + (5.0-4.6)^2 + (6.0-4.6)^2}{3}} = \sqrt{1.56}").scale(0.6).shift(var_1_formula.get_center(), RIGHT)
        var_1 = MathTex(r"\sigma_1=\sqrt{1.6}").shift(mu_2.get_center(), DOWN*1.5)
        self.play(Transform(var_1_formula, var_1_expanded))
        self.wait(2)
        self.play(Transform(var_1_formula, var_1))
        self.wait(2)

        # highlight second input and substitute the values in
        self.play(Indicate(var_2_formula))
        self.play(Circumscribe(SurroundingRectangle(VGroup(*map(lambda x: x.get_rows()[1], 
                                                        [hidden_1, hidden_2, hidden_3])))))
        
        self.play(Circumscribe(SurroundingRectangle(mu_2)))


        var_2_expanded = MathTex(r"\sigma_2 = \sqrt{\frac{(.46-.62)^2 + (.68-.62)^2 + (.72-.62)^2}{3}} = \sqrt{.11}").scale(0.6).shift(var_2_formula.get_center(), RIGHT)
        var_2 = MathTex(r"\sigma_2=\sqrt{1.6}").shift(var_1.get_center(), DOWN*1.5)
        self.play(Transform(var_2_formula, var_2_expanded))
        self.wait(2)
        self.play(Transform(var_2_formula, var_2))

        h_1_norm = MathTex(r"\hat{h_1} = \frac{h_1 - \mu_1}{\sigma_1}").shift(mu_1.get_center(), RIGHT*3)
        h_2_norm = MathTex(r"\hat{h_2} = \frac{h_2 - \mu_2}{\sigma_2}").shift(mu_2.get_center(), RIGHT*3)
        self.play(Write(h_1_norm), Write(h_2_norm))
        self.wait(2)
        h_1_norm_sub = MathTex(r"\hat{h_1} = \frac{h_1 - 4.6}{1.25}=").shift(mu_1.get_center(), RIGHT*3)
        h_2_norm_sub = MathTex(r"\hat{h_2} = \frac{h_2 - .62}{1.28}=").shift(mu_2.get_center(), RIGHT*3)

        self.play(Transform(h_1_norm, h_1_norm_sub))
        self.play(Transform(h_2_norm, h_2_norm_sub))
        self.wait(2)


        self.play(FadeOut(mu_1_formula), FadeOut(mu_2_formula), FadeOut(var_1_formula), FadeOut(var_2_formula))
        self.play(h_1_norm.animate.shift(LEFT*2), h_2_norm.animate.shift(LEFT*2))
        self.wait(2)

        # fill in the node anno for norm
        h1_hat_anno = MathTex(r"\hat{h_1}").shift(h_1_anno.get_center())
        h2_hat_anno = MathTex(r"\hat{h_2}").shift(h_2_anno.get_center())

        self.play(Write(h1_hat_anno), Write(h2_hat_anno))
        self.wait(2)

        # norm begins
        self.play(Indicate(hidden_1))
        self.play(Indicate(h_1_norm), 
                  Indicate(h_2_norm), 
                  Indicate(h1_hat_anno), 
                  Indicate(h2_hat_anno))
        h_1_1 = MathTex('-.56').shift(h_1_norm.get_right(), RIGHT)
        h_1_2 = MathTex('−1.1').shift(h_2_norm.get_right(), RIGHT)
        self.play(Write(h_1_1), Write(h_1_2))

        self.play(Indicate(h_1_node), Indicate(h_2_node))

        self.play(FadeOut(h1_hat_anno), FadeOut(h2_hat_anno))

        self.play(h_1_1.scale(0.8).animate.move_to(h_1_anno.get_center()), 
                  h_1_2.scale(0.8).animate.move_to(h_2_anno.get_center()))
        
        self.play(*map(lambda w: Indicate(w, scale_factor=1), W2))
        self.play(Indicate(z_anno), Indicate(z_node))
        self.wait()

        self.play(FadeOut(h_1_1), 
                  FadeOut(h_1_2))


        # norm the second hidden values
        self.play(Indicate(hidden_2))
        self.play(Indicate(h_1_norm), Indicate(h_2_norm))

        h_2_1 = MathTex('.48').shift(h_1_norm.get_right(), RIGHT)
        h_2_2 = MathTex('−0.95').shift(h_2_norm.get_right(), RIGHT)
        self.play(Write(h_2_1), Write(h_2_2))

        self.play(Indicate(h_1_node), Indicate(h_2_node))
        self.play(h_2_1.scale(0.8).animate.move_to(h_1_anno.get_center()), 
                  h_2_2.scale(0.8).animate.move_to(h_2_anno.get_center()))
        
        self.play(*map(lambda w: Indicate(w, scale_factor=1), W2))
        self.play(Indicate(z_anno), Indicate(z_node))
        self.wait()

        self.play(FadeOut(h_2_1), 
                  FadeOut(h_2_2))


        # norm the third hidden values
        self.play(Indicate(hidden_3))
        self.play(Indicate(h_1_norm), Indicate(h_2_norm))

        h_3_1 = MathTex('.16').shift(h_1_norm.get_right(), RIGHT)
        h_3_2 = MathTex('−.92').shift(h_2_norm.get_right(), RIGHT)
        self.play(Write(h_3_1), Write(h_3_2))

        self.play(Indicate(h_1_node), Indicate(h_2_node))
        self.play(h_3_1.scale(0.8).animate.move_to(h_1_anno.get_center()), 
                  h_3_2.scale(0.8).animate.move_to(h_2_anno.get_center()))
        
        self.play(*map(lambda w: Indicate(w, scale_factor=1), W2))
        self.play(Indicate(z_anno), Indicate(z_node))

        self.wait()