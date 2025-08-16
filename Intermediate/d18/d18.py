# install colorgram package and import it
# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r=color.rgb.r
#     g=color.rgb.g
#     b=color.rgb.b
#     rgb_colors.append((r,g,b))
#
# print(rgb_colors)
# remove tuples that have r,g,b values closer to 255 as they represent white like (245, 243, 238), (246, 242, 244), (240, 245, 241)
import random
import turtle as t
t.colormode(255)

colour_list = [ (202, 164, 110),  (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41),
                (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149),
                (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171),
                (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153),
                (176, 192, 208), (168, 99, 102)]

tim=t.Turtle()
tim.penup()
tim.hideturtle()
tim.speed("fastest")
x_cordi=-225
y_cordi=-225
tim.setposition(x_cordi,y_cordi)

def draw_line():
    for j in range(10):

        tim.dot(20, random.choice(colour_list))
        tim.forward(50)
    tim.setposition(x_cordi,tim.ycor()+50)

for i in range(10):
    draw_line()


scr=t.Screen()
scr.exitonclick()