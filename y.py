import turtle

t = turtle.Turtle()
turtle.speed(0)
turtle.bgcolor("black")
color1 = ["white", "blue", "yellow", "red", "indigo"]
for i in range(200):
    t.color(color1[i % 5])
    t.pensize(i/10+1)
    t.forward(i)
    t.left(59)
