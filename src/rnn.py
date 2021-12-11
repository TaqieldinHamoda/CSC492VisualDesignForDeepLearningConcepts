# original work on colab: https://colab.research.google.com/drive/1izlTyOY-b1uPXlTsMy3jOWNIIOtYiSfL?usp=sharing

from manim import *


class Rnn(MovingCameraScene):
  def construct(self):
    title = Text('Recurrent Neural Network', gradient=(BLUE, GREEN))
    subtitle = Text('Forward Pass (training)').shift(DOWN).scale(0.5)
    embedding_look_up_subtitle = Text('Embedding look up')

    self.play(Write(title))
    self.play(FadeIn(subtitle))
    self.wait()
    self.play(FadeOut(title), FadeOut(subtitle))
    # display 3 words
    word1 = Text("I").shift(LEFT * 2.5)
    word2 = Text("feel").next_to(word1)
    word3 = Text("thankful").next_to(word2)
    VGroup(word1, word2, word3).move_to(ORIGIN)

    self.play(Write(embedding_look_up_subtitle))
    self.play(embedding_look_up_subtitle.animate.shift(UP*3.5).scale(0.5))

    self.play(Write(word1), Write(word2), Write(word3))
    self.play(word1.animate.shift(LEFT * 2, DOWN*2),
              word2.animate.shift(DOWN*2),
              word3.animate.shift(RIGHT*2, DOWN*2))
    
    embedding_text = Text("Embedding", font_size=20)
    embedding = VGroup(embedding_text, 
                       Rectangle(height=embedding_text.height + 0.2, width=embedding_text.width + 8))

    # display the embedding
    self.play(Create(embedding))

    # show word -> vector
    word1_to_emb = Line(start=word1.get_top(), 
                         end=[word1.get_top()[0], embedding.get_bottom()[1], 0], 
                        buff=0.2).add_tip()
    word2_to_emb = Line(start=word2.get_top(), 
                         end=[word2.get_top()[0], embedding.get_bottom()[1], 0], 
                        buff=0.2).add_tip()
    word3_to_emb = Line(start=word3.get_top(), 
                         end=[word3.get_top()[0], embedding.get_bottom()[1], 0], 
                        buff=0.2).add_tip()

    word1_vector = Matrix([[1.1], [-0.9]]).move_to([word1.get_top() + UP*4]).scale(0.8)
    word2_vector = Matrix([[-0.8], [1.0]]).move_to([word2.get_top() + UP*4]).scale(0.8)
    word3_vector = Matrix([[3.1], [2.9]]).move_to([word3.get_top() + UP*4]).scale(0.8)

    # word1 -> word1 vec
    self.play(Create(word1_to_emb))
    self.play(Indicate(embedding, scale_factor=1, color=BLUE))

    word1_emb = MathTex(r'... \text{``I"}: \begin{bmatrix} 1.1 \\ -0.9 \end{bmatrix} ...').scale(0.25).move_to([word1_vector.get_center()[0], embedding_text.get_center()[1], 0])

    self.camera.frame.save_state()

    self.play(self.camera.frame.animate.move_to(word1_emb).set(height=embedding.height*1.5), FadeIn(word1_emb))
    self.wait(2)
    self.play(Restore(self.camera.frame), FadeOut(word1_emb))

    emb_to_word1_vec = Line(start=[word1.get_top()[0], embedding.get_top()[1], 0], end=word1_vector.get_bottom(), buff=0.2).add_tip()

    self.play(Create(emb_to_word1_vec))
    self.play(Create(word1_vector))

    # word2 -> word1 vec
    self.play(Create(word2_to_emb))
    self.play(Indicate(embedding, scale_factor=1, color=BLUE))

    word2_emb = MathTex(r'... \text{``feel"}: \begin{bmatrix} -0.8 \\ 1.0 \end{bmatrix} ...').scale(0.25).move_to([word2_vector.get_center()[0], embedding_text.get_center()[1], 0])

    self.camera.frame.save_state()

    self.play(self.camera.frame.animate.move_to(word2_emb).set(height=embedding.height*1.5), FadeIn(word2_emb), FadeOut(embedding_text))
    self.wait(2)
    self.play(Restore(self.camera.frame), FadeOut(word2_emb), FadeIn(embedding_text))


    emb_to_word2_vec = Line(start=[word2.get_top()[0], embedding.get_top()[1], 0], end=word2_vector.get_bottom(), buff=0.2).add_tip()

    self.play(Create(emb_to_word2_vec))
    self.play(Create(word2_vector))

    # word3 -> word1 vec
    self.play(Create(word3_to_emb))
    self.play(Indicate(embedding, scale_factor=1, color=BLUE))

    word3_emb = MathTex(r'... \text{``thankful"}: \begin{bmatrix} 3.1 \\ 2.9 \end{bmatrix} ...').scale(0.25).move_to([word3_vector.get_center()[0], embedding_text.get_center()[1], 0])

    self.camera.frame.save_state()

    self.play(self.camera.frame.animate.move_to(word3_emb).set(height=embedding.height*1.5), FadeIn(word3_emb))
    self.wait(2)
    self.play(Restore(self.camera.frame), FadeOut(word3_emb))

    emb_to_word3_vec = Line(start=[word3.get_top()[0], embedding.get_top()[1], 0], end=word3_vector.get_bottom(), buff=0.2).add_tip()

    self.play(Create(emb_to_word3_vec))
    self.play(Create(word3_vector))

    # Calculation scene ---------------------------------------------------------------------------------

    # remove all but the word vec
    self.play(*map(lambda x: FadeOut(x), 
                   [word1, word2, word3, 
                    word1_to_emb, word2_to_emb, word3_to_emb, 
                    embedding, 
                    emb_to_word1_vec, emb_to_word2_vec, emb_to_word3_vec, 
                    embedding_look_up_subtitle]))

    # move all the vectors to the bottom
    self.play(word1_vector.animate.move_to(ORIGIN).shift(DOWN*3, LEFT*4), 
              word2_vector.animate.move_to(ORIGIN).shift(DOWN*3), 
              word3_vector.animate.move_to(ORIGIN).shift(DOWN*3, RIGHT*4))
    
    x1_label = MathTex('x^{(1)}', color=BLUE).move_to(word1_vector.get_top() + UP *0.5)
    x2_label = MathTex('x^{(2)}', color=BLUE).move_to(word2_vector.get_top() + UP *0.5)
    x3_label = MathTex('x^{(3)}', color=BLUE).move_to(word3_vector.get_top() + UP *0.5)

    self.play(Write(x1_label), Write(x2_label), Write(x3_label))


    forward_pass_title = Text('Forward pass calculation')
    self.play(Write(forward_pass_title))
    self.wait()
    self.play(forward_pass_title.animate.shift(UP*3.5).scale(0.5))

    

    self.wait()

    # the target
    t = MathTex(r't=').shift(UP*2, LEFT*5)
    target_vector = Matrix([[1], [0]]).next_to(t)
    target = VGroup(t, 
                    target_vector, 
                    MathTex(r' = \text{happy}').next_to(target_vector))
    self.play(Create(target))
    self.wait()
    
    h1_label = MathTex('h^{(1)}', color=RED).move_to(x1_label.get_top()).shift(UP*2)
    h2_label = MathTex('h^{(2)}', color=RED).move_to(x2_label.get_top()).shift(UP*2)
    h3_label = MathTex('h^{(3)}', color=RED).move_to(x3_label.get_top()).shift(UP*2)

    h1_label_with_value = MathTex(r'{{ h^{(1)} }} = {{ \begin{bmatrix} 1.1 \\ -0.2 \end{bmatrix} }}', color=GREEN).scale(0.7).move_to(h1_label) # h0->h1 need to be spaced out properly
    h2_label_with_value = MathTex(r'{{ h^{(2)} }} = {{ \begin{bmatrix} 0.3 \\ -0.4 \end{bmatrix} }}', color=GREEN).scale(0.7).move_to(h2_label) 
    h3_label_with_value = MathTex(r'{{ h^{(3)} }} = {{ \begin{bmatrix} 3.4 \\ -6.4 \end{bmatrix} }}', color=GREEN).scale(0.7).move_to(h3_label) 

    # h0 has 2 labels due to spacing issues
    h0_label = MathTex(r'h^{(0)}={{ \begin{bmatrix} 0 \\ 0 \end{bmatrix} }}', color=GREEN).scale(0.7).move_to([h1_label.get_left()]).shift(LEFT*4)
    h0_label_overview = MathTex(r'h^{(0)}={{ \begin{bmatrix} 0 \\ 0 \end{bmatrix} }}', color=GREEN).scale(0.7).move_to([h1_label.get_left()]).shift(LEFT*2)

    h0_to_h1 = Line(start=h0_label.get_right(), end=h1_label_with_value.get_left(), buff=0.2).add_tip()
    h0_to_h1_overview = Line(start=h0_label_overview.get_right(), end=h1_label_with_value.get_left(), buff=0.2).add_tip()
    h1_to_h2 = Line(start=h1_label_with_value.get_right(), end=h2_label_with_value.get_left(), buff=0.2).add_tip()
    h2_to_h3 = Line(start=h2_label_with_value.get_right(), end=h3_label_with_value.get_left(), buff=0.2).add_tip()

    x1_to_h1 = Line(start=x1_label, end=h1_label_with_value.get_bottom(), buff=0.2).add_tip()
    x2_to_h2 = Line(start=x2_label, end=h2_label_with_value.get_bottom(), buff=0.2).add_tip()
    x3_to_h3 = Line(start=x3_label, end=h3_label_with_value.get_bottom(), buff=0.2).add_tip()

    time_step_frame = SurroundingRectangle(VGroup(word1_vector, h1_label), buff=0.3, color=GREY_D)

    self.camera.frame.save_state()

    self.play(Create(time_step_frame))
    self.play(self.camera.frame.animate.move_to(time_step_frame).shift(LEFT*2).set(height=time_step_frame.height*1.1))
    self.wait(0.3)

    self.play(Create(h0_label))

    self.play(Create(x1_to_h1), Create(h0_to_h1))
    self.play(Create(h1_label))

    # calculation for h1
    h1_calculation = MathTex(r'{{ h^{(1)} }} = {{ V }} \cdot {{ h^{(0)} }} + {{ W }} \cdot {{ x^{(1)} }}').scale(0.6).move_to(time_step_frame).shift(LEFT*5, UP)
    h1_calculation.set_color_by_tex('h^{(1)}', RED)
    h1_calculation.set_color_by_tex('h^{(0)}', GREEN)
    h1_calculation.set_color_by_tex('x^{(1)}', BLUE)

    h1_sub = MathTex(r'= {{ \begin{bmatrix} 1 & 0\\0 & 1 \end{bmatrix} }} \cdot {{ \begin{bmatrix} 0 \\ 0 \end{bmatrix} }} +' \
                     + r'{{ \begin{bmatrix} 1 & 0\\-1 & -1 \end{bmatrix} }} \cdot {{ \begin{bmatrix} 1.1\\-0.9 \end{bmatrix} }}').scale(0.6).align_to(h1_calculation.submobjects[1], LEFT).shift(DOWN*1.25)
    h1_sub.set_color_by_tex(r'\begin{bmatrix} 0 \\ 0 \end{bmatrix}', GREEN)
    h1_sub.set_color_by_tex(r'\begin{bmatrix} 1.1\\-0.9 \end{bmatrix}', BLUE)

    h1_final_val = MathTex(r'= {{ \begin{bmatrix} 1.1 \\ -0.2 \end{bmatrix} }}').scale(0.6).align_to(h1_sub.submobjects[0], LEFT).shift(DOWN*2.25)


    self.play(Write(h1_calculation))
    self.wait(3)
    self.play(Write(h1_sub))
    self.wait(3)
    self.play(Write(h1_final_val))

    self.wait(3)

    # move to calculation of h_2
    h2_calculation = MathTex(r'{{ h^{(2)} }} =  {{ V }} \cdot {{ h^{(1)} }} + {{ W }} \cdot {{ x^{(2)} }}').scale(0.6).move_to(h1_calculation)
    h2_calculation.set_color_by_tex('h^{(2)}', RED)
    h2_calculation.set_color_by_tex('h^{(1)}', GREEN)
    h2_calculation.set_color_by_tex('x^{(2)}', BLUE)

    self.play(Transform(h1_label, h1_label_with_value))
    self.wait(2)

    self.play(time_step_frame.animate.shift(x2_label.get_center() - x1_label.get_center()), 
              self.camera.frame.animate.shift(x2_label.get_center() - x1_label.get_center()),
              h1_calculation.animate.become(h2_calculation).shift(x2_label.get_center() - x1_label.get_center()),
              FadeOut(h0_to_h1),
              FadeOut(h0_label),
              FadeOut(x1_label),
              FadeOut(x1_to_h1), 
              FadeOut(word1_vector),
              FadeOut(h1_sub),
              FadeOut(h1_final_val))
    
    h2_sub = MathTex(r'= {{ \begin{bmatrix} 1 & 0\\0 & 1 \end{bmatrix} }} \cdot {{ \begin{bmatrix} 1.1 \\ -0.2 \end{bmatrix} }} +' \
                     + r'{{ \begin{bmatrix} 1 & 0\\-1 & -1 \end{bmatrix} }} \cdot {{ \begin{bmatrix} -0.8\\1.0 \end{bmatrix} }}').scale(0.5).align_to(h1_calculation.submobjects[1], LEFT).shift(DOWN*1.25)

    h2_sub.set_color_by_tex(r'\begin{bmatrix} 1.1 \\ -0.2 \end{bmatrix}', GREEN)
    h2_sub.set_color_by_tex(r'\begin{bmatrix} -0.8\\1.0 \end{bmatrix}', BLUE)

    h2_final_val = MathTex(r'= {{ \begin{bmatrix} 0.3 \\ -0.4 \end{bmatrix} }}').scale(0.6).align_to(h2_sub.submobjects[0], LEFT).shift(DOWN*2.25)


    self.play(Create(x2_to_h2), Create(h1_to_h2))
    self.play(Write(h2_label))
    self.wait()

    self.play(Write(h2_sub))
    self.wait(3)
    self.play(Write(h2_final_val))

    self.wait(3)

    # move to calculation of h_3
    h3_calculation = MathTex(r'{{ h^{(3)} }} =  {{ V }} \cdot {{ h^{(2)} }} + {{ W }} \cdot {{ x^{(3)} }}').scale(0.6).move_to(h1_calculation)
    h3_calculation.set_color_by_tex('h^{(3)}', RED)
    h3_calculation.set_color_by_tex('h^{(2)}', GREEN)
    h3_calculation.set_color_by_tex('x^{(3)}', BLUE)

    self.play(Transform(h2_label, h2_label_with_value))
    self.wait(2)

    self.play(time_step_frame.animate.shift(x3_label.get_center() - x2_label.get_center()), 
              self.camera.frame.animate.shift(x3_label.get_center() - x2_label.get_center()), 
              h1_calculation.animate.become(h3_calculation).shift(x3_label.get_center() - x2_label.get_center()),
              FadeOut(x2_label),
              FadeOut(x2_to_h2), 
              FadeOut(word2_vector),
              FadeOut(h2_sub),
              FadeOut(h2_final_val))

    h3_sub = MathTex(r'=  {{ \begin{bmatrix} 1 & 0\\0 & 1 \end{bmatrix} }} \cdot {{ \begin{bmatrix} 0.3 \\ -0.4 \end{bmatrix} }}+' \
                     + r' {{ \begin{bmatrix} 1 & 0\\-1 & -1 \end{bmatrix} }} \cdot {{ \begin{bmatrix} 3.1\\2.9 \end{bmatrix} }}').scale(0.5).align_to(h1_calculation.submobjects[1], LEFT).shift(DOWN*1.25)

    h3_sub.set_color_by_tex(r'\begin{bmatrix} 0.3 \\ -0.4 \end{bmatrix}', GREEN)
    h3_sub.set_color_by_tex(r'\begin{bmatrix} 3.1\\2.9 \end{bmatrix}', BLUE)

    h3_final_val = MathTex(r'= {{ \begin{bmatrix} 3.4 \\ -6.4 \end{bmatrix} }}').scale(0.6).align_to(h3_sub.submobjects[0], LEFT).shift(DOWN*2.25)


    self.play(Create(x3_to_h3), Create(h2_to_h3))
    self.play(Write(h3_label))
    self.wait()

    self.play(Write(h3_sub))
    self.wait(3)
    self.play(Write(h3_final_val))

    self.wait(3)

    self.play(Transform(h3_label, h3_label_with_value))
    self.wait(2)

    self.play(Restore(self.camera.frame),
              FadeOut(h1_calculation),
              FadeOut(h3_sub),
              FadeOut(h3_final_val),
              FadeIn(h0_label_overview),
              FadeIn(h0_to_h1_overview),
              FadeIn(x1_label),
              FadeIn(h1_label_with_value), 
              FadeIn(x1_to_h1), 
              FadeIn(word1_vector), 
              FadeIn(x2_label), 
              FadeIn(x2_to_h2), 
              FadeIn(word2_vector))
    

    y = MathTex(r'\begin{bmatrix} 2.1 \\ 0.5 \end{bmatrix}').move_to(h3_label).shift(UP*2)
    
    h3_to_y = Line(start=h3_label.get_top(), end=y.get_bottom(), buff=0.2).add_tip()
    mlp_anno = Text('MLP').scale(0.5).next_to(h3_to_y)

    self.play(Create(h3_to_y), Create(mlp_anno))

    self.wait()

    self.play(Create(y), Create(MathTex(r'y=').next_to(y, LEFT)))

    self.wait()