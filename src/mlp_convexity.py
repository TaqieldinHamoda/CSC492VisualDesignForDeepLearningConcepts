# original work on colab: https://colab.research.google.com/drive/1GAqfdyy5p0px6XO6_M9lsUy_37HyQlOc?usp=sharing
from manim import *
import itertools


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
                                stroke_width=4)
                                .add_updater(lambda x: x.put_start_and_end_on(pair[0].get_right(), pair[1].get_left())), 
                   list(itertools.product(start_nodes, end_nodes))))
  return edges

def swap_node(scene, node1, node2, node1_anno, node2_anno):
  scene.play(node2.animate.move_to(node1), node1.animate.move_to(node2), 
             node1_anno.animate.become(node2_anno).move_to(node2_anno),
             node2_anno.animate.become(node1_anno).move_to(node1_anno))

class Convexity(Scene):
  def construct(self):
    # the NN
    x_1_node, x_1_node_anno, x_1_node_ani, x_1_anno_ani = create_node(self, "x_1", [UP, LEFT * 4])
    x_2_node, x_2_node_anno, x_2_node_ani, x_2_anno_ani = create_node(self, "x_2", [DOWN, LEFT * 4])
    h_1_node, h_1_node_anno, h_1_node_ani, h_1_anno_ani = create_node(self, "h_1", [UP*2])
    h_2_node, h_2_node_anno, h_2_node_ani, h_2_anno_ani = create_node(self, "h_2", [(UP*2+DOWN*2)//2])
    h_3_node, x_3_node_anno, h_3_node_ani, h_3_anno_ani = create_node(self, "h_3", [DOWN*2])

    z_node, z_node_anno, z_node_ani, z_anno_ani = create_node(self, "z", [RIGHT*4])

    self.play(x_1_node_ani, x_1_anno_ani, 
              x_2_node_ani, x_2_anno_ani, 
              h_1_node_ani, h_1_anno_ani, 
              h_2_node_ani, h_2_anno_ani, 
              h_3_node_ani, h_3_anno_ani, 
              z_node_ani, z_anno_ani)


    E1 = create_edges(self, [x_1_node, x_2_node], [h_1_node, h_2_node, h_3_node])
    E2 = create_edges(self, [h_1_node, h_2_node, h_3_node], [z_node])
    E1[0].set_color(BLUE)
    E1[3].set_color(BLUE)
    E2[0].set_color(BLUE)
    E1[1].set_color(RED)
    E1[4].set_color(RED)
    E2[1].set_color(RED)
    self.play(*map(lambda x: Create(x), E1), *map(lambda x: Create(x), E2))

    # weight1 matrix dimensions = 2*3
    # weight2 matrix dimensions = 3*1
    W1_1 = ["1", "3", "5"]
    W1_2 = ["2", "4", "6"]
    weight_matrix = Matrix([W1_1, W1_2]).shift(LEFT*3, UP*3)
    weight_matrix.scale(0.75)
    weight_matrix.set_column_colors(BLUE, RED)
    W_text = MathTex("W_1 = ").next_to(weight_matrix, LEFT)
    W_text.scale(0.65)
    col1 = weight_matrix.get_columns()[0]
    col2 = weight_matrix.get_columns()[1]

    weight_matrix2 = Matrix([["1"], ["2"], ["3"]]).shift(RIGHT*3, UP*2.5)
    W2_text = MathTex("W_2 = ").next_to(weight_matrix2, LEFT)
    W2_text.scale(0.65)
    weight_matrix2.scale(0.75)
    weight_matrix2.set_row_colors(BLUE, RED)
    row1 = weight_matrix2.get_rows()[0]
    row2 = weight_matrix2.get_rows()[1]

    self.play(Write(W_text), Create(weight_matrix), Write(W2_text), Create(weight_matrix2))
    # self.play(ReplacementTransform(weight_matrix, modified_weight_matrix))
    self.play(col1.animate.move_to(col2), 
              col2.animate.move_to(col1),
              row1.animate.move_to(row2),
              row2.animate.move_to(row1))
    
    swap_node(self, h_1_node, h_2_node, h_1_node_anno, h_2_node_anno)