import turtle
turtle.Screen().bgcolor("light blue")
turtle.title("Infinite Spiral")
t=turtle.Turtle()
size=0
while True:
    for i in range(4):
        t.fd(size+1)
        t.left(90)
        size-=1
    size+=1
