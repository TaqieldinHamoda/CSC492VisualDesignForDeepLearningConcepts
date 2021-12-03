# original work on colab: https://colab.research.google.com/drive/1_rvoulTl-N61J9YiqtGH8PfWxKTcbKKI?usp=sharing

from manim import *
import itertools

class Autodiff(MovingCameraScene):
  def create_node(self, label, pos=[]):
    if pos:
      node = Circle(radius=0.5, color=BLUE).move_to(pos).scale(0.8)
      anno = MathTex(label).move_to(pos).scale(0.8)
    else:
      node = Circle(radius=0.5, color=BLUE).scale(0.8)
      anno = MathTex(label).scale(0.8)

    return node, anno, Create(node), Write(anno)


  def create_arrows(self, start_nodes, end_nodes, arrow_location="right"):
    if arrow_location == "right":
      edges = list(map(lambda pair: Line(start=pair[0].get_top(), 
                                    end=pair[1].get_bottom()).add_tip(tip_length=0.2),
                      list(itertools.product(start_nodes, end_nodes))))
    else :
      edges = list(map(lambda pair: Line(start=pair[0].get_left(), 
                              end=pair[1].get_right()).add_tip(tip_length=0.2),
                list(itertools.product(start_nodes, end_nodes))))


    self.play(*map(lambda x: Create(x), edges))
    return edges

      
  def construct(self):
    title = Text("Automatic Differentiation", gradient=(BLUE, GREEN))
    self.play(Write(title))
    self.wait(2)
    self.play(FadeOut(title))

    x1_node, x1_anno, x1node_ani, x1anno_ani = self.create_node("h_1", pos=[-5.1, -2.9, 0 ])
    x2_node, x2_anno, x2node_ani, x2anno_ani = self.create_node("h_2", pos=[-3.1, -2.9,  0 ])
    z1_node, z1_anno, z1node_ani, z1anno_ani = self.create_node("z_1", pos=[-5.1, -1.5,  0 ])
    z2_node, z2_anno, z2node_ani, z2anno_ani = self.create_node("z_2", pos=[-3.1, -1.5,  0 ])    
    t_node,  t_anno,  tnode_ani,  tanno_ani  = self.create_node("\mathcal{T}", pos=[-4.1,  0.1,  0 ])
    y_node,  y_anno,  ynode_ani,  yanno_ani  = self.create_node("y", pos=[-6.1,  0.1,  0 ])
    d_node,  d_anno,  dnode_ani,  danno_ani  = self.create_node("\mathcal{D}", pos=[-6.1,  1.5,  0 ])
    l_node,  l_anno,  lnode_ani,  lanno_ani  = self.create_node("\mathcal{L}", pos=[-6.1,  2.9,  0 ])
    target_node, target_anno, targetnode_ani, targetanno_ani = self.create_node("t", pos=[-4.7,  1.5,  0 ])

    # introduce L and y first
    L = MathTex("{{ \mathcal{L} }}=").shift(UP * 3, LEFT*1.5)
    L_func_orig = MathTex(r"{{(t-y)}}^2").next_to(L)

    self.play(Write(L), Write(L_func_orig))
    self.wait()

    # introduce y
    y = MathTex("{{ y }}  =").shift(UP, LEFT*1.5)
    y_func_orig = MathTex(r"{{ e^{h_1} }} \over {{ e^{h_1} }} + {{ e^{h_2} }}").next_to(y)

    self.play(Write(y), Write(y_func_orig))
    
    self.wait()

    self.play(Indicate(L_func_orig.submobjects[0])) # highlight (t-y)

    # introduce D = t-y
    D = MathTex("{{ \mathcal{D} }} =").shift(UP * 2, LEFT*1.5)
    D_replaced = MathTex("{{ \mathcal{D} }}").shift(L_func_orig.submobjects[0].get_center())
    D_func = MathTex(r"{{t}} - {{y}}").next_to(D)

    L_final_right = MathTex(r"{{ \mathcal{D} }} ^2").next_to(L)

    self.play(Write(D), Write(D_func))

    self.wait()
    self.play(Indicate(D_func))
    self.play(Indicate(L_func_orig.submobjects[0]))
    self.wait()
    
    # transform (y-t) to D
    self.play(Transform(L_func_orig.submobjects[0], D_replaced))
    self.play(Transform(L_func_orig, L_final_right))
    self.wait()


    # replace e^h1 + e^h2 with T
    T = MathTex("{{ \mathcal{T} }} =").shift( LEFT*1.5)
    T_func_orig = MathTex("{{ e^{h_1} }} + {{ e^{h_2} }}").next_to(T)
    T_replaced = MathTex("{{ e^{h_1} }} \over {{\mathcal{T}}}").move_to(y_func_orig) # this var is here bc Transform cannot transform a list of objs into 1

    T_final = MathTex("{{ z_1 }} \over {{\mathcal{T}}}").next_to(y)

    self.play(Indicate(y_func_orig.submobjects[2]), 
              Indicate(y_func_orig.submobjects[3]),
              Indicate(y_func_orig.submobjects[4]))
    self.play(Write(T), Write(T_func_orig))
    self.wait()

    self.play(Indicate(T_func_orig))

    self.play(Indicate(y_func_orig.submobjects[2]), 
              Indicate(y_func_orig.submobjects[3]),
              Indicate(y_func_orig.submobjects[4]))
    self.play(Transform(y_func_orig, T_replaced))
    self.wait()

    # highlight e^h1 in y and T
    self.play(Indicate(y_func_orig.submobjects[0]))
    self.play(Indicate(T_func_orig.submobjects[0]))
    self.wait()

    z1 = MathTex("{{ z_1 }} =").shift(DOWN, LEFT*1.5)
    z1_func_orig = MathTex("e^{ {{ h_1 }} }").next_to(z1)
    self.play(Write(z1), Write(z1_func_orig))

    self.play(Indicate(z1_func_orig))
    self.play(Indicate(y_func_orig.submobjects[0])) 
    self.play(Indicate(T_func_orig.submobjects[0]))
              
    
    z1_replaced_1 = MathTex("z_1").move_to(y_func_orig.submobjects[0])
    z1_replaced_2 = MathTex("z_1").move_to(T_func_orig.submobjects[0])

    # replace e^h1 with z1
    self.play(Transform(y_func_orig.submobjects[0], z1_replaced_1), 
              Transform(T_func_orig.submobjects[0], z1_replaced_2))
    self.wait()

    # make the fraction look better for y
    self.play(Transform(y_func_orig, T_final))
    self.wait()
    
    # highlight e^h2 in T
    self.play(Indicate(y_func_orig.submobjects[4]))
    z2 = MathTex("{{ z_2 }} =").shift(DOWN*2, LEFT*1.5)
    z2_func_orig = MathTex("e^{ {{ h_2 }} }").next_to(z2)
    self.play(Write(z2), Write(z2_func_orig))

    z2_replaced = MathTex("z_2").move_to(T_func_orig.submobjects[2])

    self.play(Indicate(z2_func_orig))
    self.play(Indicate(T_func_orig.submobjects[2]))

    # replace e^h2 with z2
    self.play(Transform(T_func_orig.submobjects[2], z2_replaced))
    self.wait()

    # graph all the nodes 
    self.play(Indicate(L.submobjects[0]))
    self.play(lnode_ani, lanno_ani)
    
    self.play(Indicate(D.submobjects[0]))
    self.play(dnode_ani, danno_ani)

    self.play(Indicate(y.submobjects[0]))
    self.play(ynode_ani, yanno_ani)

    self.play(Indicate(T.submobjects[0]))
    self.play(tnode_ani, tanno_ani)

    self.play(Indicate(z1.submobjects[0]))
    self.play(z1node_ani, z1anno_ani)

    self.play(Indicate(z2.submobjects[0]))
    self.play(z2node_ani, z2anno_ani)

    self.play(x1node_ani, x2node_ani, targetnode_ani, 
              x1anno_ani, x2anno_ani, targetanno_ani)

    # graph L and D
    self.play(Indicate(L.submobjects[0]))
    self.play(Circumscribe(L_func_orig))
    self.play(Indicate(L_func_orig.submobjects[0]))

    d_l_edge = self.create_arrows([d_node], [l_node])
    self.wait()

    self.play(Indicate(D.submobjects[0]))
    self.play(Circumscribe(D_func))
    self.play(Indicate(D_func.submobjects[2]))

    # graph target node
    # self.play(Circumscribe(D_func))
    self.play(Indicate(D_func.submobjects[0]))

    y_d_edge = self.create_arrows([y_node], [d_node])
    target_d_edge = self.create_arrows([target_node], [d_node], arrow_location="center")
    self.wait()

    # graph T
    self.play(Indicate(y.submobjects[0]))
    self.play(Circumscribe(y_func_orig))
    self.play(Indicate(y_func_orig.submobjects[3])) 

    # hilight z1 in y
    self.play(Indicate(y_func_orig.submobjects[0]))
    t_y_edge = self.create_arrows([t_node], [y_node], arrow_location="center")
    z1_y_edge = self.create_arrows([z1_node], [y_node])
    self.wait()

    # graph z1
    self.play(Indicate(T.submobjects[0]))
    self.play(Circumscribe(T_func_orig))
    self.play(Indicate(T_func_orig.submobjects[0]))

    # graph z2
    self.play(Indicate(T_func_orig.submobjects[2]))
    z1_t_edge = self.create_arrows([z1_node], [t_node])
    z2_t_edge = self.create_arrows([z2_node], [t_node])
    self.wait()

    # graph h1
    self.play(Indicate(z1.submobjects[0]))
    self.play(Circumscribe(z1_func_orig))
    self.play(Indicate(z1_func_orig.submobjects[1]))
    x1_z1_edge = self.create_arrows([x1_node], [z1_node])
    self.wait()

    # graph h2
    self.play(Indicate(z2.submobjects[0]))
    self.play(Circumscribe(z2_func_orig))
    self.play(Indicate(z2_func_orig.submobjects[1]))
    x2_z2_edge = self.create_arrows([x2_node], [z2_node])
    self.wait()

    # Forward Pass Arrow
    fwd_text = Text("Forward Pass", color=GREEN_C).shift(UP*3, LEFT*4)
    fwd_text.scale(0.5)
    self.play(Write(fwd_text))

    # input/given values substitution
    x1_val = MathTex(r"h_1 = 0").move_to(x1_anno).scale(0.4)
    x2_val = MathTex(r"h_2 = 3").move_to(x2_anno).scale(0.4)
    target_val = MathTex(r"t = 1").move_to(target_anno).scale(0.4)

    self.play(Flash(x1_node, color=GREEN, flash_radius=0.5+SMALL_BUFF))
    self.play((Transform(x1_anno, x1_val)))

    self.play(Flash(x2_node, color=GREEN, flash_radius=0.5+SMALL_BUFF))
    self.play((Transform(x2_anno, x2_val)))

    self.play(Flash(target_node, color=GREEN, flash_radius=0.5+SMALL_BUFF))
    self.play((Transform(target_anno, target_val)))

    # z substitution
    z1_val = MathTex(r"z_1 = 1").move_to(z1_anno).scale(0.4)
    z1_rhs = MathTex(r" = 1 ").next_to(z1_func_orig, RIGHT)
    self.play((Write(z1_rhs)))
    self.play(Flash(z1_node, color=GREEN, flash_radius=0.5+SMALL_BUFF))
    self.play((Indicate(z1_rhs)))
    self.play((Transform(z1_anno, z1_val)))
    self.play((Indicate(z1_anno)))
    self.wait()

    z2_val = MathTex(r"z_2 = 20").move_to(z2_anno).scale(0.4)
    z2_rhs = MathTex(r" = 20").next_to(z2_func_orig, RIGHT)
    self.play((Write(z2_rhs)))
    self.play(Flash(z2_node, color=GREEN, flash_radius=0.5+SMALL_BUFF))
    self.play((Indicate(z2_rhs)))
    self.play((Transform(z2_anno, z2_val)))
    self.play((Indicate(z2_anno)))
    self.wait()

    # T substitution
    T_val = MathTex(r"\mathcal{T} = 21").move_to(t_anno).scale(0.4)
    T_rhs = MathTex(r" = 21").next_to(T_func_orig, RIGHT)
    self.play((Write(T_rhs)))
    self.play(Flash(t_node, color=GREEN, flash_radius=0.5+SMALL_BUFF))
    self.play((Indicate(T_rhs)))
    self.play((Transform(t_anno, T_val)))
    self.play((Indicate(t_anno)))
    self.wait()

    # y substitution
    y_val = MathTex(r"y = 0.05").move_to(y_anno).scale(0.4)
    y_rhs = MathTex(r" = 0.05").next_to(y_func_orig, RIGHT)
    self.play((Write(y_rhs)))
    self.play(Flash(y_node, color=GREEN, flash_radius=0.5+SMALL_BUFF))
    self.play((Indicate(y_rhs)))
    self.play((Transform(y_anno, y_val)))
    self.play((Indicate(y_anno)))
    self.wait()

    #D substitution
    D_val = MathTex(r"\mathcal{D} = 0.95").move_to(d_anno).scale(0.4)
    D_rhs = MathTex(r" = 0.95").next_to(D_func, RIGHT)
    self.play((Write(D_rhs)))
    self.play(Flash(d_node, color=GREEN, flash_radius=0.5+SMALL_BUFF))
    self.play((Indicate(D_rhs)))
    self.play((Transform(d_anno, D_val)))
    self.play((Indicate(d_anno)))
    self.wait()


    # L substitution
    L_val = MathTex(r"\mathcal{L} = 0.90").move_to(l_anno).scale(0.4)
    L_rhs = MathTex(r" = 0.90").next_to(L_func_orig, RIGHT)
    self.play((Write(L_rhs)))
    self.play(Flash(l_node, color=GREEN, flash_radius=0.5+SMALL_BUFF))
    self.play((Indicate(L_rhs)))
    self.play((Transform(l_anno, L_val)))
    self.play((Indicate(l_anno)))
    self.wait()

    # rhs values fade out
    self.play(FadeOut(z1_rhs),
              FadeOut(z2_rhs),
              FadeOut(T_rhs),
              FadeOut(y_rhs),
              FadeOut(D_rhs),
              FadeOut(L_rhs))
    self.wait()

    # BackwardPass Arrow
    bwd_text = Text("Backward Pass", color=RED_A).move_to(fwd_text)
    bwd_text.scale(0.5)
    self.play(Indicate(fwd_text))
    self.play((Transform(fwd_text, bwd_text)))
    self.wait()

    # Divider
    upper_point = Dot().next_to(L, RIGHT*9)
    upper_point.set_color(BLACK)
    lower_point = Dot().next_to(upper_point, DOWN*20)
    lower_point.set_color(BLACK)
    divider = Line(upper_point, lower_point)

    # dLdD formula
    dldD_1 = MathTex(r"{{\frac{\partial \mathcal{L} }{\partial \mathcal{D} }}} = {{\frac{\partial \mathcal{D}^2}{\partial \mathcal{D} }}}").scale(0.75)
    dldD_2 = MathTex(r"{{\frac{\partial \mathcal{L} }{\partial \mathcal{D} }}} = {{2\mathcal{D}}}").scale(0.75)
    dldD_3 = MathTex(r"{{\frac{\partial \mathcal{L} }{\partial \mathcal{D} }}} = 2 \cdot 0.95").scale(0.75)
    dldD_4 = MathTex(r"{{\frac{\partial \mathcal{L} }{\partial \mathcal{D} }}} = 1.9").scale(0.75)
    dldD_1.next_to(upper_point, RIGHT*7)
    dldD_2.move_to(dldD_1)
    dldD_3.move_to(dldD_2)
    dldD_4.move_to(dldD_3)
    # self.play(FadeOut(L), FadeOut(L_func_orig))
    self.play(Write(dldD_1), FadeToColor(d_l_edge[0], RED_A))
    self.wait()
    self.play(ReplacementTransform(dldD_1, dldD_2))
    self.wait()
    self.play(ReplacementTransform(dldD_2, dldD_3))
    self.wait()
    self.play(ReplacementTransform(dldD_3, dldD_4))
    self.wait()
    
    #dldy formula
    dldy_1 = MathTex(r"{{\frac{\partial \mathcal{L} }{\partial y}}} = {{\frac{\partial \mathcal{L} }{\partial \mathcal{D} }}} \cdot {{\frac{\partial \mathcal{D} }{\partial y}}}").scale(0.75)
    dldy_2 = MathTex(r"{{\frac{\partial \mathcal{L} }{\partial y}}} = {{1.9}}{{\frac{\partial \mathcal {D} }{\partial y}}}").scale(0.75)
    dldy_3 = MathTex(r"{{\frac{\partial \mathcal{L} }{\partial y}}} = {{1.9}} \cdot {{\frac{\partial (t-y)}{\partial y}}}").scale(0.75)
    dldy_4 = MathTex(r"{{\frac{\partial \mathcal{L} }{\partial y}}} = {{-1.9}}").scale(0.75)
    dldy_5 = MathTex(r"{{\frac{\partial \mathcal{L} }{\partial y}}} = {{-1.9}}").scale(0.75)
    dldy_1.next_to(dldD_1,DOWN)
    dldy_2.move_to(dldy_1)
    dldy_3.move_to(dldy_1)
    dldy_4.move_to(dldy_1)
    dldy_5.move_to(dldy_1)
    self.play(Write(dldy_1), FadeToColor(y_d_edge[0], RED_A))
    self.wait(0.5)
    self.play(Indicate(dldy_1.submobjects[2]), Indicate(dldD_4))
    self.wait()
    self.play(ReplacementTransform(dldy_1, dldy_2))
    self.wait()
    self.play(ReplacementTransform(dldy_2, dldy_3))
    self.wait()
    self.play(ReplacementTransform(dldy_3, dldy_4))
    self.wait()
    self.play(ReplacementTransform(dldy_4, dldy_5))
    self.wait()

    #dLdT formula
    dldT_1 = MathTex(r"{{\frac{\partial \mathcal{L} }{\partial \mathcal{T} }}} = {{\frac{\partial \mathcal{L} }{\partial y}}} \cdot {{\frac{\partial y}{\partial \mathcal{T} }}}").scale(0.75)
    dldT_2 = MathTex(r"{{\frac{\partial \mathcal{L} }{\partial \mathcal{T} }}} = {{-1.9}} \cdot {{\frac{\partial y}{\partial \mathcal{T} }}}").scale(0.75)
    dldT_3 = MathTex(r"{{\frac{\partial \mathcal{L} }{\partial \mathcal{T} }}} = {{-1.9}} \cdot \frac{\partial \left( \frac{z_1}{\mathcal{T}} \right)}{\partial \mathcal{T}}").scale(0.75)
    dldT_4 = MathTex(r"{{\frac{\partial \mathcal{L} }{\partial \mathcal{T} }}} = {{-1.9}} \cdot {{\frac{z_1}{\mathcal{T}^2}}}").scale(0.75)
    dldT_5 = MathTex(r"{{\frac{\partial \mathcal{L} }{\partial \mathcal{T} }}} = {{-1.9}} \cdot {{\frac{1}{21^2}}}").scale(0.75)
    dldT_6 = MathTex(r"{{\frac{\partial \mathcal{L} }{\partial \mathcal{T} }}} = {{-0.004}}").scale(0.75)
    dldT_1.next_to(dldy_1,DOWN)
    dldT_2.move_to(dldT_1)
    dldT_3.move_to(dldT_1)
    dldT_4.move_to(dldT_1)
    dldT_5.move_to(dldT_1)
    dldT_6.move_to(dldT_1)

    self.play(Write(dldT_1), FadeToColor(t_y_edge[0], RED_A))
    self.wait(0.5)
    self.play(Indicate(dldT_1.submobjects[2]), Indicate(dldy_5))
    self.wait()
    self.play(ReplacementTransform(dldT_1, dldT_2))
    self.wait()
    self.play(ReplacementTransform(dldT_2, dldT_3))
    self.wait()
    self.play(ReplacementTransform(dldT_3, dldT_4))
    self.wait()
    self.play(ReplacementTransform(dldT_4, dldT_5))
    self.wait()
    self.play(ReplacementTransform(dldT_5, dldT_6))
    self.wait()

    #dldz1 formula
    dldz1_1 = MathTex(r"{{\frac{\partial \mathcal{L} }{\partial z_1}}} =" + \
                      r"{{\frac{\partial \mathcal{L} }{\partial y}}} \cdot {{\frac{\partial y}{\partial z_1}}} + {{\frac{\partial \mathcal{L} }{\partial \mathcal{T} }}} \cdot {{\frac{\partial \mathcal{T} }{\partial z_1}}}").scale(0.75)
    dldz1_2 = MathTex(r"{{\frac{\partial \mathcal{L} }{\partial z_1}}} = {{-1.9}} \cdot {{\frac{\partial y}{\partial z_1}}} + {{1.9}} \cdot {{\frac{\partial \mathcal{T} }{\partial z_1}}}").scale(0.75)
    dldz1_3 = MathTex(r"{{\frac{\partial \mathcal{L} }{\partial z_1}}} = {{-1.9}} \cdot \frac{\partial \frac{z_1}{T}}{\partial z_1} + {{1.9}} \cdot {{\frac{z_1}{\mathcal{T}^2}}}{{\frac{\partial (z_1+z_2)}{\partial z_1}}}").scale(0.65)
    dldz1_4 = MathTex(r"\frac{\partial \mathcal{L} }{\partial z_1} = {{-1.9}} \cdot \frac{z_1}{T} +  {{1.9}} \cdot {{\frac{z_1}{\mathcal{T}^2}}}.{{z_1}}").scale(0.75)
    dldz1_5 = MathTex(r"\frac{\partial \mathcal{L} }{\partial z_1} = {{-1.9}} \cdot \frac{1}{21} + {{1.9}} \cdot {{\frac{1}{21^2}}} \cdot {{(1)}}").scale(0.65)
    dldz1_6 = MathTex(r"\frac{\partial \mathcal{L} }{\partial z_1} = {{-0.09}}").scale(0.75)

    dldz1_1.next_to(dldT_1,DOWN)
    dldz1_2.move_to(dldz1_1)
    dldz1_3.move_to(dldz1_1)
    dldz1_4.move_to(dldz1_1)
    dldz1_5.move_to(dldz1_1)
    dldz1_6.move_to(dldz1_1)

    self.play(Write(dldz1_1),
              FadeToColor(z1_t_edge[0], RED_A),
              FadeToColor(z1_y_edge[0], RED_A))
    
    self.wait(0.5)
    self.play(Indicate(dldz1_1.submobjects[2]), Indicate(dldy_5))
    self.wait(0.5)
    self.play(Indicate(dldz1_1.submobjects[6]), Indicate(dldT_6))
    self.wait()
    self.play(ReplacementTransform(dldz1_1, dldz1_2))
    self.wait()
    self.play(ReplacementTransform(dldz1_2, dldz1_3))
    self.wait()
    self.play(ReplacementTransform(dldz1_3, dldz1_4))
    self.wait()
    self.play(ReplacementTransform(dldz1_4, dldz1_5))
    self.wait()
    self.play(ReplacementTransform(dldz1_5, dldz1_6))
    self.wait()


    #dldz2 formula
    dldz2_1 = MathTex(r"{{\frac{\partial \mathcal{L} }{\partial z_2}}} = {{\frac{\partial \mathcal{L} }{\partial \mathcal{T} }}} \cdot {{\frac{\partial \mathcal{T} }{\partial z_2}}}").scale(0.75)
    dldz2_2 = MathTex(r"{{\frac{\partial \mathcal{L} }{\partial z_2}}} =  {{-0.004}}{{\frac{\partial \mathcal{T} }{\partial z_2}}}").scale(0.75)
    dldz2_3 = MathTex(r"{{\frac{\partial \mathcal{L} }{\partial z_2}}} =   {{-0.004}}{{\frac{\partial (z_1+z_2)}{\partial z_2}}}").scale(0.75)
    dldz2_4 = MathTex(r"{{\frac{\partial \mathcal{L} }{\partial z_2}}} =  {{-0.004}}").scale(0.75)
    

    dldz2_1.next_to(dldz1_3, DOWN)
    dldz2_2.move_to(dldz2_1)
    dldz2_3.move_to(dldz2_1)
    dldz2_4.move_to(dldz2_1)

    self.play(Write(dldz2_1), 
              FadeToColor(z2_t_edge[0], RED_A),
              FadeToColor(z1_t_edge[0], WHITE),
              FadeToColor(z1_y_edge[0], WHITE))
    
    self.wait()
    self.play(Indicate(dldz2_1.submobjects[2]), Indicate(dldT_6))
    self.wait()
    self.play(ReplacementTransform(dldz2_1, dldz2_2))
    self.wait()
    self.play(ReplacementTransform(dldz2_2, dldz2_3))
    self.wait()
    self.play(ReplacementTransform(dldz2_3, dldz2_4))
    self.wait()

    #dldh1 formula
    dldh1_1 = MathTex(r"\frac{\partial \mathcal{L} }{\partial h_1} = {{\frac{\partial \mathcal{L} }{\partial z_1}}} \cdot {{\frac{\partial z_1}{\partial h_1}}}").scale(0.75)
    dldh1_2 = MathTex(r"\frac{\partial \mathcal{L} }{\partial h_1} = {{-0.09}} \cdot {{\frac{\partial z_1}{\partial h_1}}}").scale(0.75)
    dldh1_3 = MathTex(r"\frac{\partial \mathcal{L} }{\partial h_1} = {{-0.09}} \cdot \frac{\partial e^{h_1}}{\partial h_1}").scale(0.75)
    dldh1_4 = MathTex(r"\frac{\partial \mathcal{L} }{\partial h_1} = {{-0.09}} \cdot e^{h_1}").scale(0.75)
    dldh1_5 = MathTex(r"\frac{\partial \mathcal{L} }{\partial h_1} = {{-0.09}} \cdot e^{0}").scale(0.75)
    dldh1_6 = MathTex(r"\frac{\partial \mathcal{L} }{\partial h_1} = {{-0.09}}").scale(0.75)

    dldh1_1.next_to(dldz2_1,DOWN)
    dldh1_2.move_to(dldh1_1)
    dldh1_3.move_to(dldh1_1)
    dldh1_4.move_to(dldh1_1)
    dldh1_5.move_to(dldh1_1)
    dldh1_6.move_to(dldh1_1)
    
    self.play(Write(dldh1_1),
              FadeToColor(x1_z1_edge[0], RED_A),
              FadeToColor(z1_y_edge[0], RED_A),
              FadeToColor(z1_t_edge[0], RED_A),
              FadeToColor(z2_t_edge[0], WHITE))
    
    self.wait(0.5)
    self.play(Indicate(dldh1_1.submobjects[1]), Indicate(dldz1_6))
    self.wait()
    self.play(ReplacementTransform(dldh1_1, dldh1_2))
    self.wait()
    self.play(ReplacementTransform(dldh1_2, dldh1_3))
    self.wait()
    self.play(ReplacementTransform(dldh1_3, dldh1_4))
    self.wait()
    self.play(ReplacementTransform(dldh1_4, dldh1_5))
    self.wait()
    self.play(ReplacementTransform(dldh1_5, dldh1_6))
    self.wait()

    #dldh2 formula
    dldh2_1 = MathTex(r"\frac{\partial \mathcal{L} }{\partial h_2} = {{\frac{\partial \mathcal{L} }{\partial z_2}}} \cdot {{\frac{\partial z_2}{\partial h_2}}}").scale(0.75)
    dldh2_2 = MathTex(r"\frac{\partial \mathcal{L} }{\partial h_2} = -0.004 \cdot {{\frac{\partial z_2}{\partial h_2}}}").scale(0.75)
    dldh2_3 = MathTex(r"\frac{\partial \mathcal{L} }{\partial h_2} = -0.004 \cdot \frac{\partial e^{h_2}}{\partial h_2}").scale(0.75)
    dldh2_4 = MathTex(r"\frac{\partial \mathcal{L} }{\partial h_2} = -0.004 \cdot e^{3}}").scale(0.75)
    dldh2_5 = MathTex(r"\frac{\partial \mathcal{L} }{\partial h_2} = -0.08").scale(0.75)
    dldh2_1.next_to(dldh1_1,DOWN)
    dldh2_2.move_to(dldh2_1)
    dldh2_3.move_to(dldh2_1)
    dldh2_4.move_to(dldh2_1)
    dldh2_5.move_to(dldh2_1)
    
    self.wait()
    self.play(Write(dldh2_1),
              FadeToColor(x2_z2_edge[0], RED_A),
              FadeToColor(z2_t_edge[0], RED_A),
              FadeToColor(x1_z1_edge[0], WHITE),
              FadeToColor(z1_y_edge[0], WHITE),
              FadeToColor(z1_t_edge[0], WHITE))
              
    self.wait()
    self.play(Indicate(dldh2_1.submobjects[1]), Indicate(dldz2_4))
    self.wait()
    self.play(ReplacementTransform(dldh2_1, dldh2_2))
    self.wait()
    self.play(ReplacementTransform(dldh2_2, dldh2_3))
    self.wait()
    self.play(ReplacementTransform(dldh2_3, dldh2_4))
    self.wait()
    self.play(ReplacementTransform(dldh2_4, dldh2_5))
    self.wait()

    self.play(FadeToColor(x2_z2_edge[0], WHITE),
              FadeToColor(z2_t_edge[0], WHITE),
              FadeToColor(t_y_edge[0], WHITE),
              FadeToColor(y_d_edge[0], WHITE),
              FadeToColor(d_l_edge[0], WHITE))
    
    self.play(Circumscribe(dldh1_6, run_time=2), Circumscribe(dldh2_5, run_time=2))
    self.wait()