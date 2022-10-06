import turtle as t
import random

t.colormode(255)
#Extracted colors from another hirst painting in "rgb" format 
color_list = [(202, 166, 109), (240, 246, 241), (152, 73, 47), (236, 238, 244), (170, 153, 41), (222, 202, 138), (53, 93, 124), (135, 32, 22), (132, 163, 184), (48, 118, 88), (198, 91, 71), (16, 97, 75), (100, 73, 75), (67, 47, 41), (147, 178, 147), (163, 142, 156), (234, 177, 165), (55, 46, 50), (130, 28, 31), (184, 205, 174), (41, 60, 72), (83, 147, 126), (181, 87, 90), (31, 77, 84), (47, 65, 83), (215, 177, 182), (19, 71, 63), (175, 192, 212)]
#Creates the "paintbrush" and its charateristics using the Turtle library
paint_brush = t.Turtle()
paint_brush.hideturtle()
paint_brush.speed('fastest')
paint_brush.penup()
paint_brush.goto(-225,-225)
paint_brush.pendown()
paint_brush.dot(20)
#Function to randomize the colors in the "color_list" list
def random_color():
    rgb = random.choice(color_list)
    return rgb
#Creates the dots in a 10 x 10 format.
for _ in range(10):    
    for _ in range(10):
        paint_brush.color(random_color())
        paint_brush.dot(20)
        paint_brush.penup()
        paint_brush.forward(50)
        paint_brush.pendown()
    paint_brush.penup()
    paint_brush.backward(500)
    paint_brush.left(90)
    paint_brush.forward(50)
    paint_brush.right(90)
    paint_brush.pendown()

screen = t.Screen()
screen.exitonclick()


