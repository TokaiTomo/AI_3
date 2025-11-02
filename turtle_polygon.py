import turtle
turtle.Screen().bgcolor("orange")
turtle.Screen().setup(300,400)
turtle.shape("turtle")
polygon=turtle.Turtle()
num_side = 6
length = 70
angle = 360/num_side
for i in range(num_side):
    polygon.forward(length)
    polygon.right(angle)
turtle.done()